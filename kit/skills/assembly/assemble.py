#!/usr/bin/env python3
"""러프컷 조립과 이어 붙이기 프레임. 표준 라이브러리 + ffmpeg/ffprobe만 쓴다.

  python3 .claude/skills/assembly/assemble.py lastframe <영상> <출력.png>
  python3 .claude/skills/assembly/assemble.py frame <영상> <초> <출력.png>
  python3 .claude/skills/assembly/assemble.py concat <출력.mp4> <영상1> <영상2> ...
  python3 .claude/skills/assembly/assemble.py seam <앞영상> <뒷영상> <출력.png>

실행 전에 ffmpeg 명령을 출력한다. 입력 파일과 이미 있는 파일은 덮어쓰지 않는다.
"""
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile


def die(msg):
    print(f"오류: {msg}", file=sys.stderr)
    sys.exit(1)


def need_tools():
    for t in ("ffmpeg", "ffprobe"):
        if not shutil.which(t):
            die(f"{t}가 없다. 설치한 뒤 다시 실행한다.")


def need_input(path):
    if not os.path.isfile(path):
        die(f"파일이 없다: {path}")


def need_output(out, inputs):
    if os.path.abspath(out) in {os.path.abspath(p) for p in inputs}:
        die(f"출력이 입력과 같다. 원본은 덮어쓰지 않는다: {out}")
    if os.path.exists(out):
        die(f"출력 파일이 이미 있다. 다른 이름을 쓴다: {out}")
    d = os.path.dirname(out)
    if d:
        os.makedirs(d, exist_ok=True)


def run(cmd):
    print("$ " + shlex.join(cmd), flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        tail = "\n".join(r.stderr.strip().splitlines()[-5:])
        die(f"ffmpeg 실패(코드 {r.returncode}).\n{tail}")


def probe(path):
    need_input(path)
    r = subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path],
                       capture_output=True, text=True)
    if r.returncode != 0:
        die(f"영상을 읽지 못했다: {path}")
    data = json.loads(r.stdout)
    v = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), None)
    if v is None:
        die(f"영상 스트림이 없다: {path}")
    num, _, den = v.get("r_frame_rate", "0/1").partition("/")
    fps = float(num) / float(den or 1) if float(den or 1) else 0.0
    return {
        "w": int(v["width"]), "h": int(v["height"]), "fps": fps, "rate": v.get("r_frame_rate", ""),
        "codec": v.get("codec_name", ""), "pix": v.get("pix_fmt", ""),
        "audio": any(s.get("codec_type") == "audio" for s in data["streams"]),
        "dur": float(data.get("format", {}).get("duration") or v.get("duration") or 0),
    }


def lastframe(video, out):
    probe(video)
    need_output(out, [video])
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-sseof", "-1", "-i", video,
         "-update", "1", "-an", out])
    print(f"마지막 프레임: {out}")


def frame(video, sec, out):
    try:
        t = float(sec)
    except ValueError:
        die(f"초는 숫자로 쓴다: {sec}")
    info = probe(video)
    if t < 0 or (info["dur"] and t >= info["dur"]):
        die(f"{t}초는 영상 밖이다(길이 {info['dur']:.2f}초).")
    need_output(out, [video])
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f"{t}", "-i", video,
         "-frames:v", "1", "-an", out])
    print(f"{t}초 프레임: {out}")


def concat(out, videos):
    if len(videos) < 2:
        die("영상을 둘 이상 준다.")
    infos = [probe(v) for v in videos]
    need_output(out, videos)
    first = infos[0]
    same = all((i["w"], i["h"], i["rate"], i["codec"], i["pix"], i["audio"]) ==
               (first["w"], first["h"], first["rate"], first["codec"], first["pix"], first["audio"]) for i in infos)
    if same:
        fd, lst = tempfile.mkstemp(suffix=".txt")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            for v in videos:
                f.write("file '" + os.path.abspath(v).replace("'", "'\\''") + "'\n")
        try:
            run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                 "-c", "copy", out])
        finally:
            os.remove(lst)
        print(f"이어 붙임(다시 인코딩 없음): {out}")
        return
    w, h, rate = first["w"], first["h"], first["rate"] or "24"
    with_audio = any(i["audio"] for i in infos)
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error"]
    for v in videos:
        cmd += ["-i", v]
    n = len(videos)
    filt, pairs = [], []
    for k, i in enumerate(infos):
        filt.append(f"[{k}:v]scale={w}:{h}:force_original_aspect_ratio=decrease,"
                    f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={rate},format=yuv420p[v{k}]")
        if with_audio:
            if i["audio"]:
                filt.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo[a{k}]")
            else:
                filt.append(f"anullsrc=r=48000:cl=stereo,atrim=duration={i['dur']:.3f}[a{k}]")
            pairs.append(f"[v{k}][a{k}]")
        else:
            pairs.append(f"[v{k}]")
    filt.append("".join(pairs) + f"concat=n={n}:v=1:a={1 if with_audio else 0}" + ("[v][a]" if with_audio else "[v]"))
    cmd += ["-filter_complex", ";".join(filt), "-map", "[v]"]
    if with_audio:
        cmd += ["-map", "[a]", "-c:a", "aac"]
    cmd += ["-c:v", "libx264", "-crf", "18", "-preset", "veryfast", out]
    diff = [os.path.basename(v) for v, i in zip(videos, infos)
            if (i["w"], i["h"], i["rate"]) != (w, h, first["rate"])]
    if diff:
        print(f"첫 영상({w}x{h}, {rate} fps)에 맞춰 다시 인코딩: {', '.join(diff)}")
    else:
        print("코덱·소리 형식이 달라 다시 인코딩한다.")
    run(cmd)
    print(f"이어 붙임: {out}")


def seam(a, b, out):
    ia, _ = probe(a), probe(b)
    need_output(out, [a, b])
    with tempfile.TemporaryDirectory() as d:
        pa, pb = os.path.join(d, "a_end.png"), os.path.join(d, "b_start.png")
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-sseof", "-1", "-i", a, "-update", "1", "-an", pa])
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", b, "-frames:v", "1", "-an", pb])
        h = ia["h"]
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", pa, "-i", pb, "-filter_complex",
             f"[0:v]pad=iw+8:ih:0:0:white[l];[1:v]scale=-2:{h}[r];[l][r]hstack=inputs=2", "-frames:v", "1", out])
    print(f"경계 비교(왼쪽 = 앞 컷 끝 | 오른쪽 = 다음 컷 시작): {out}")


USAGE = __doc__.split("\n\n")[1]


def main(argv):
    if not argv:
        die("하위 명령이 없다.\n" + USAGE)
    need_tools()
    cmd, args = argv[0], argv[1:]
    if cmd == "lastframe" and len(args) == 2:
        lastframe(*args)
    elif cmd == "frame" and len(args) == 3:
        frame(*args)
    elif cmd == "concat" and len(args) >= 3:
        concat(args[0], args[1:])
    elif cmd == "seam" and len(args) == 3:
        seam(*args)
    else:
        die("명령 형식이 틀렸다.\n" + USAGE)


if __name__ == "__main__":
    main(sys.argv[1:])
