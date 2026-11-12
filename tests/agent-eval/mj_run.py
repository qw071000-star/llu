#!/usr/bin/env python3
"""미드저니 전용 키트(kit-midjourney)를 Claude 앱 프로젝트처럼 흉내 내 체인을 돌린다: ./mj_run.py <체인ID> [run_root]
app_run.py와 같은 방식: dist의 지침을 시스템 프롬프트에, zip을 플러그인 폴더에 풀고, 정본 틀을 프로젝트 지식(읽기 전용)으로 넣는다.
미드저니는 연결 도구가 없다. 이미지는 만들지도 붙이지도 않는다(결과 판정 체인은 '이미지 없음' 상황을 시험한다)."""
import json, os, re, shutil, subprocess, sys, time, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.join(HERE, "..", "..", "kit-midjourney")
SKILLS = ["mj-setup", "mj-image", "mj-video", "mj-production", "mj-shots"]
cid = sys.argv[1]
root = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "runs-mj")
spec = json.load(open(os.path.join(HERE, "mj-chains.json")))[cid]
run = os.path.join(root, cid)
plugin = os.path.join(root, f"_plugin_{cid}")
for d in (run, plugin):
    shutil.rmtree(d, ignore_errors=True)
os.makedirs(os.path.join(run, "out")); os.makedirs(os.path.join(plugin, ".claude-plugin")); os.makedirs(os.path.join(plugin, "skills"))
json.dump({"name": "mjkit", "version": "0.0.0", "description": "kit-midjourney skills (app upload zips)"},
          open(os.path.join(plugin, ".claude-plugin", "plugin.json"), "w"))
for s in SKILLS:
    with zipfile.ZipFile(os.path.join(KIT, "dist", f"{s}.zip")) as z:
        z.extractall(os.path.join(plugin, "skills"))
inst = open(os.path.join(KIT, "dist", "project-instructions.md"), encoding="utf-8").read()
EMPTY = bool(spec.get("empty"))
if not EMPTY:
    inst = inst.replace("「[작품명]」", "「빈 정류장」").replace("[V7 / V8.x]", "V7").replace("[있음 / 없음]", "있음", 1)
inst = inst.replace("Canon location: [Claude Doc link (recommended) / project knowledge]", "Canon location: project knowledge")
proj = os.path.join(KIT, "project-files") if EMPTY else os.path.join(HERE, "mj-testbed")
knowledge = "\n\n".join(f'<document name="{f}">\n{open(os.path.join(proj, f), encoding="utf-8").read()}\n</document>'
                        for f in ["decisions.md", "asset-registry.md", "shot-list.md", "ok-cuts.md"])
if spec.get("shared"):
    h = "## §7. 작업 방식 (이 작품에서 정한 것)\n"
    assert h in knowledge
    knowledge = knowledge.replace(h, h + "- 운영 방식: 공용 계정: Claude 1개 · Midjourney 1개를 지수 · 민호 · 서연이 돌아가며 사용 · 총괄: 지수 · 사용량 한도: 없음\n", 1)
system = ("# Project instructions (Claude app project)\n\n" + inst +
          "\n\n# Project knowledge (read-only; you cannot edit these files)\n\n" + knowledge +
          "\n\n# Test environment\n\nMidjourney는 연결되어 있지 않다. 이 환경에서 이미지는 만들어지지도 첨부되지도 않는다.")
open(os.path.join(run, "out", "system.md"), "w", encoding="utf-8").write(system)
session = None
turns = list(spec["turns"]); n = 0
while turns:
    msg = turns.pop(0); n += 1
    cmd = ["claude", "-p", msg, "--model", spec.get("model", "sonnet"), "--output-format", "stream-json", "--verbose",
           "--permission-mode", "acceptEdits", "--disallowedTools", "mcp__*", "--plugin-dir", plugin, "--add-dir", plugin,
           "--allowedTools", "Bash(python3:*)", "Bash(ls:*)", "Bash(cat:*)", "--append-system-prompt", system]
    if session: cmd += ["--resume", session]
    for _ in range(37):
        r = subprocess.run(cmd, cwd=run, capture_output=True, text=True, timeout=900, stdin=subprocess.DEVNULL)
        if not re.search(r"hit your .{0,20}limit|usage limit|rate limit", r.stdout[-3000:] + r.stderr[-3000:], re.I):
            break
        print(f"{cid} turn{n}: 사용량 한도 — 10분 뒤 다시 시도", flush=True); time.sleep(600)
    skills, reads, texts, final = [], [], [], ""
    for line in r.stdout.splitlines():
        try: e = json.loads(line)
        except Exception: continue
        if e.get("type") == "system" and e.get("session_id"): session = e["session_id"]
        if e.get("type") == "assistant":
            for c in e["message"].get("content", []):
                if c.get("type") == "text" and c.get("text", "").strip(): texts.append(c["text"].strip())
                if c.get("type") == "tool_use":
                    i = c.get("input", {})
                    if c["name"] == "Skill": skills.append(i.get("skill"))
                    elif c["name"] == "Read": reads.append(i.get("file_path", "").replace(plugin, "<plugin>"))
        if e.get("type") == "result":
            final = e.get("result", ""); session = e.get("session_id", session)
    shown = "\n\n".join(texts) if texts else final
    if final and final.strip() not in shown: shown += "\n\n" + final
    open(os.path.join(run, "out", f"turn{n}.md"), "w").write(f"<!-- 사용자: {msg} -->\n\n{shown}\n")
    json.dump({"user": msg, "skills": skills, "reads": reads, "rc": r.returncode}, open(os.path.join(run, "out", f"turn{n}.meta.json"), "w"), ensure_ascii=False, indent=1)
    print(f"{cid} turn{n}: skills={skills} reads={len(reads)} rc={r.returncode}", flush=True)
    if "이 작업을 할까요" in shown and not msg.startswith("응, 그 작업"):
        turns.insert(0, "응, 그 작업 맞아.")
