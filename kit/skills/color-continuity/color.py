#!/usr/bin/env python3
"""컷 간 색·노출 재기와 1차 맞춤. 표준 라이브러리 + ffmpeg/ffprobe만 쓴다.

  python3 .claude/skills/color-continuity/color.py measure <파일> [<파일> ...]
  python3 .claude/skills/color-continuity/color.py match <기준> <대상> <출력>
  python3 .claude/skills/color-continuity/color.py compare <기준> <원본> <맞춘것> <출력.png>

영상·이미지 모두 받는다. 실행 전에 ffmpeg 명령을 출력한다. 입력 파일과 이미 있는 파일은 덮어쓰지 않는다.
"""
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile

SAMPLES = 5            # 영상에서 고르게 뽑는 프레임 수
SMALL = "160:-2"       # R·G·B·표준편차를 잴 때 줄이는 크기
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}
# 안전 범위: 1차 맞춤만 한다. 넘으면 잘라 쓰고 알린다(그 컷은 다시 만들기 검토)
GAIN = (0.75, 1.33)    # colorchannelmixer rr·gg·bb
CONTRAST = (0.7, 1.4)  # eq contrast
BRIGHT = (-0.15, 0.15) # eq brightness
BIG_UV = 12            # 평균 U·V 차이(0~255)가 이보다 크면 다시 만들기 제안
BIG_Y = 30             # 평균 Y 차이


def die(msg):
    print(f"오류: {msg}", file=sys.stderr)
    sys.exit(1)


def need_tools():
    for t in ("ffmpeg", "ffprobe"):
        if not shutil.which(t):
            die(f"{t}가 없다. 설치한 뒤 다시 실행한다.")


def need_output(out, inputs):
    if os.path.abspath(out) in {os.path.abspath(p) for p in inputs}:
        die(f"출력이 입력과 같다. 원본은 덮어쓰지 않는다: {out}")
    if os.path.exists(out):
        die(f"출력 파일이 이미 있다. 다른 이름을 쓴다: {out}")
    d = os.path.dirname(out)
    if d:
        os.makedirs(d, exist_ok=True)


def run(cmd, capture=False):
    print("$ " + shlex.join(cmd), flush=True)
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode != 0:
        tail = "\n".join(r.stderr.decode("utf-8", "replace").strip().splitlines()[-5:])
        die(f"ffmpeg 실패(코드 {r.returncode}).\n{tail}")
    return r.stdout if capture else None


def is_image(path):
    return os.path.splitext(path)[1].lower() in IMAGE_EXT


def probe(path):
    if not os.path.isfile(path):
        die(f"파일이 없다: {path}")
    r = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path],
                       capture_output=True, text=True)
    if r.returncode != 0:
        die(f"파일을 읽지 못했다: {path}")
    data = json.loads(r.stdout)
    v = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), None)
    if v is None:
        die(f"영상·이미지 스트림이 없다: {path}")
    num, _, den = v.get("r_frame_rate", "0/1").partition("/")
    fps = float(num) / float(den) if float(den or 0) else 0.0
    dur = float(data.get("format", {}).get("duration") or v.get("duration") or 0)
    frames = int(v.get("nb_frames") or 0) or int(round(dur * fps))
    return {"w": int(v["width"]), "h": int(v["height"]), "dur": dur,
            "frames": 1 if is_image(path) else max(frames, 1),
            "audio": any(s.get("codec_type") == "audio" for s in data["streams"])}


def measure_one(path):
    info = probe(path)
    step = max(1, info["frames"] // SAMPLES)
    sel = f"select='not(mod(n-{step // 2},{step}))'"
    with tempfile.TemporaryDirectory() as d:
        meta = os.path.join(d, "stats.txt")
        graph = (f"[0:v]{sel},split[a][b];[a]signalstats,metadata=mode=print:file={meta}[s];"
                 f"[b]scale={SMALL},format=rgb24[r]")
        raw = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", path, "-filter_complex", graph,
                   "-map", "[s]", "-fps_mode", "passthrough", "-f", "null", "-",
                   "-map", "[r]", "-fps_mode", "passthrough", "-f", "rawvideo", "pipe:1"], capture=True)
        yuv = {"YAVG": [], "UAVG": [], "VAVG": []}
        with open(meta, encoding="utf-8") as f:
            for line in f:
                k, _, v = line.strip().partition("=")
                k = k.rsplit(".", 1)[-1]
                if k in yuv:
                    yuv[k].append(float(v))
    if not yuv["YAVG"] or not raw:
        die(f"프레임을 뽑지 못했다: {path}")
    n = len(raw) // 3
    s = [0.0, 0.0, 0.0]
    for c in range(3):
        s[c] = sum(raw[c::3]) / n
    ys = [0.299 * raw[i] + 0.587 * raw[i + 1] + 0.114 * raw[i + 2] for i in range(0, n * 3, 3)]
    ym = sum(ys) / n
    ystd = (sum((y - ym) ** 2 for y in ys) / n) ** 0.5
    avg = lambda xs: sum(xs) / len(xs)
    return {"file": path, "frames": len(yuv["YAVG"]), "Y": avg(yuv["YAVG"]), "U": avg(yuv["UAVG"]),
            "V": avg(yuv["VAVG"]), "R": s[0], "G": s[1], "B": s[2], "Yrgb": ym, "Ystd": ystd}


def measure(paths):
    rows = [measure_one(p) for p in paths]
    print("\n| 파일 | 프레임 | Y | U | V | R | G | B | Y 표준편차(대비) | 첫 파일 대비 ΔY · ΔU · ΔV |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    ref = rows[0]
    for r in rows:
        dlt = "기준" if r is ref else f"{r['Y'] - ref['Y']:+.1f} · {r['U'] - ref['U']:+.1f} · {r['V'] - ref['V']:+.1f}"
        print(f"| {os.path.basename(r['file'])} | {r['frames']} | {r['Y']:.1f} | {r['U']:.1f} | {r['V']:.1f} | "
              f"{r['R']:.1f} | {r['G']:.1f} | {r['B']:.1f} | {r['Ystd']:.1f} | {dlt} |")
    print("(0~255. U가 높으면 파랑, 낮으면 노랑 쪽. V가 높으면 빨강, 낮으면 초록 쪽)")
    for r in rows[1:]:
        if abs(r["U"] - ref["U"]) > BIG_UV or abs(r["V"] - ref["V"]) > BIG_UV or abs(r["Y"] - ref["Y"]) > BIG_Y:
            print(f"차이가 크다: {os.path.basename(r['file'])}. 후반 보정보다 그 컷을 다시 만드는 것을 검토한다.")
    return rows


def clamp(v, lo_hi, name, cut):
    lo, hi = lo_hi
    if v < lo or v > hi:
        cut.append(name)
    return min(max(v, lo), hi)


def match(ref, tgt, out):
    if is_image(out) != is_image(tgt):
        die("출력 확장자가 대상과 맞지 않는다(영상이면 .mp4, 이미지면 .png).")
    need_output(out, [ref, tgt])
    a, b = measure_one(ref), measure_one(tgt)
    cut = []
    gains = {c: clamp(a[c] / max(b[c], 1.0), GAIN, f"{c} 이득", cut) for c in "RGB"}
    # 이득을 건 뒤의 휘도·대비를 어림해 eq로 대비를 맞추고, 평균 휘도는 기준에 둔다
    y_after = 0.299 * b["R"] * gains["R"] + 0.587 * b["G"] * gains["G"] + 0.114 * b["B"] * gains["B"]
    std_after = b["Ystd"] * y_after / max(b["Yrgb"], 1.0)
    contrast = clamp(a["Ystd"] / max(std_after, 1.0), CONTRAST, "대비", cut)
    bright = clamp((a["Yrgb"] - contrast * (y_after - 127.5) - 127.5) / 255.0, BRIGHT, "밝기", cut)
    filt = (f"colorchannelmixer=rr={gains['R']:.3f}:gg={gains['G']:.3f}:bb={gains['B']:.3f},"
            f"eq=contrast={contrast:.3f}:brightness={bright:.3f}")
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", tgt, "-vf", filt]
    if is_image(out):
        cmd += ["-frames:v", "1", "-update", "1", out]
    else:
        cmd += ["-map", "0:v", "-map", "0:a?", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
                "-pix_fmt", "yuv420p", "-c:a", "copy", out]
    run(cmd)
    print(f"\n쓴 필터: {filt}")
    if cut:
        print(f"안전 범위로 잘랐다: {', '.join(cut)}. 차이가 커서 1차 맞춤으로 다 줄지 않는다. 다시 만들기를 검토한다.")
    print(f"맞춘 파일: {out} (원본은 그대로)")


def middle(path, png):
    info = probe(path)
    if is_image(path) or not info["dur"]:
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", path, "-frames:v", "1", "-update", "1", png])
    else:
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f"{info['dur'] / 2:.3f}", "-i", path,
             "-frames:v", "1", "-update", "1", "-an", png])
    return info["h"]


def compare(ref, src, fixed, out):
    need_output(out, [ref, src, fixed])
    with tempfile.TemporaryDirectory() as d:
        ps = [os.path.join(d, f"{k}.png") for k in ("ref", "src", "fix")]
        h = middle(ref, ps[0])
        middle(src, ps[1])
        middle(fixed, ps[2])
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", ps[0], "-i", ps[1], "-i", ps[2],
             "-filter_complex",
             f"[0:v]scale=-2:{h},pad=iw+8:ih:0:0:white[a];[1:v]scale=-2:{h},pad=iw+8:ih:0:0:white[b];"
             f"[2:v]scale=-2:{h}[c];[a][b][c]hstack=inputs=3", "-frames:v", "1", "-update", "1", out])
    print(f"비교(왼쪽 = 기준 | 가운데 = 원본 | 오른쪽 = 맞춘 것, 가운데 프레임): {out}")


USAGE = __doc__.split("\n\n")[1]


def main(argv):
    if not argv:
        die("하위 명령이 없다.\n" + USAGE)
    need_tools()
    cmd, args = argv[0], argv[1:]
    if cmd == "measure" and args:
        measure(args)
    elif cmd == "match" and len(args) == 3:
        match(*args)
    elif cmd == "compare" and len(args) == 4:
        compare(*args)
    else:
        die("명령 형식이 틀렸다.\n" + USAGE)


if __name__ == "__main__":
    main(sys.argv[1:])
