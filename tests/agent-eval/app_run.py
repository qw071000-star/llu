#!/usr/bin/env python3
"""Claude 앱 프로젝트를 흉내 내 체인을 돌린다: ./app_run.py <체인ID> [run_root]

real_run.py(Claude Code 설치본)와 다른 점 — 앱에서 달라지는 것만 바꿨다.
- 지침: .claude/·CLAUDE.md 없음. kit/dist/project-instructions.md(앱판)를 지침 칸처럼 시스템 프롬프트에 붙인다.
- 스킬: kit/dist/*.zip(앱에 올리는 그 파일)을 작업 폴더 밖 플러그인 폴더에 풀어 --plugin-dir로 싣는다.
  그래서 검사 스크립트 경로가 .claude/skills/…가 아니다(앱의 업로드 스킬 폴더와 같은 처지).
- 정본: 프로젝트 지식처럼 시스템 프롬프트에 넣는다. 파일로 두지 않으므로 Claude가 고칠 수 없다(앱과 같다).
  컷 카드·핸드오프는 지식에 넣지 않는다(키트 안내대로).
- Higgsfield는 real_run.py와 같은 시뮬레이션.
턴마다 out/turnN.md와 out/turnN.meta.json을 남긴다."""
import json, os, re, shutil, subprocess, sys, time, zipfile
HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.join(HERE, "..", "..", "kit")
APP_SKILLS = ["project-setup", "production-session", "higgsfield-generation", "image-prompt", "video-prompt", "acting", "shot-design", "edit-planning"]
cid = sys.argv[1]
root = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "runs-app")
chains = json.load(open(os.path.join(HERE, "real-chains.json")))
chains.update(json.load(open(os.path.join(HERE, "app-chains.json"))))
spec = chains[cid]
run = os.path.join(root, cid)
plugin = os.path.join(root, f"_plugin_{cid}")
for d in (run, plugin):
    shutil.rmtree(d, ignore_errors=True)
os.makedirs(os.path.join(run, "out")); os.makedirs(os.path.join(run, "sim"))
os.makedirs(os.path.join(plugin, ".claude-plugin")); os.makedirs(os.path.join(plugin, "skills"))
json.dump({"name": "kit", "version": "0.0.0", "description": "llu kit skills (app upload zips)"},
          open(os.path.join(plugin, ".claude-plugin", "plugin.json"), "w"))
for s in APP_SKILLS:
    with zipfile.ZipFile(os.path.join(KIT, "dist", f"{s}.zip")) as z:
        z.extractall(os.path.join(plugin, "skills"))
EMPTY = bool(spec.get("empty"))
if EMPTY:  # 새 작품: 빈 정본 틀, Higgsfield에는 아직 프로젝트 없음
    open(os.path.join(run, "sim", "higgsfield.md"), "w", encoding="utf-8").write(
        "# Higgsfield 시뮬레이션 결과표 (시험용)\n\n실제 Higgsfield를 부르지 않는다. 답에 `[TOOL] 도구이름(인자)`를 적는다.\n\n"
        "- 선택된 워크스페이스: 팀 워크스페이스 `ws-sim-0001`\n- list_projects: 「빈 정류장」 프로젝트는 아직 없다.\n"
        "- create_project, create_folder: 성공. ID는 `prj-new-0001`, 폴더는 `fld-<이름>`.\n")
else:
    shutil.copy(os.path.join(HERE, "testbed", "sim", "higgsfield.md"), os.path.join(run, "sim"))

inst = open(os.path.join(KIT, "dist", "project-instructions.md"), encoding="utf-8").read()
# 사용자가 지침 칸에서 하듯 "This project" 칸의 값만 채운다(그 밖의 줄은 그대로)
for k, v in [("「[작품명]」", "「빈 정류장」"), ("[name] (`[project_id]`)", "빈 정류장 (`prj-sim-0001`)"),
             ("Canon location: [Claude Doc link (recommended) / project knowledge]", "Canon location: project knowledge")]:
    assert k in inst, k
    if not EMPTY or k.startswith("Canon location"):
        inst = inst.replace(k, v, 1)
proj = os.path.join(KIT, "project-files") if EMPTY else os.path.join(HERE, "testbed", "project")
knowledge = "\n\n".join(f'<document name="{f}">\n{open(os.path.join(proj, f), encoding="utf-8").read()}\n</document>'
                        for f in ["decisions.md", "asset-registry.md", "shot-list.md", "ok-cuts.md"])
SIM = ("이 환경에는 Higgsfield MCP가 연결되어 있지 않다(시험 환경). Higgsfield 도구를 부를 때는 실제로 부르지 말고 "
       "답 안에 `[TOOL] 도구이름(인자)` 줄을 쓰고, 그 결과는 sim/higgsfield.md에서 찾는다. 거기 없는 결과는 알 수 없음이다.")
system = ("# Project instructions (Claude app project)\n\n" + inst +
          "\n\n# Project knowledge (read-only; you cannot edit these files)\n\n" + knowledge + "\n\n# Test environment\n\n" + SIM)
open(os.path.join(run, "out", "system.md"), "w", encoding="utf-8").write(system)

session = None
turns = list(spec["turns"])
n = 0
while turns:
    msg = turns.pop(0); n += 1
    cmd = ["claude", "-p", msg, "--model", spec.get("model", "sonnet"), "--output-format", "stream-json", "--verbose",
           "--permission-mode", "acceptEdits", "--disallowedTools", "mcp__*", "--plugin-dir", plugin, "--add-dir", plugin,
           "--allowedTools", "Bash(python3:*)", "Bash(ls:*)", "Bash(find:*)", "Bash(mkdir:*)", "Bash(cat:*)", "Bash(rm:*)",
           "--append-system-prompt", system]
    if session: cmd += ["--resume", session]
    for _ in range(37):
        r = subprocess.run(cmd, cwd=run, capture_output=True, text=True, timeout=900, stdin=subprocess.DEVNULL)
        if not re.search(r"hit your .{0,20}limit|usage limit|rate limit", r.stdout[-3000:] + r.stderr[-3000:], re.I):
            break
        print(f"{cid} turn{n}: 사용량 한도 — 10분 뒤 다시 시도", flush=True)
        time.sleep(600)
    skills, reads, tools, bash, final, texts = [], [], [], [], "", []
    for line in r.stdout.splitlines():
        try: e = json.loads(line)
        except Exception: continue
        if e.get("type") == "system" and e.get("session_id"): session = e["session_id"]
        if e.get("type") == "assistant":
            for c in e["message"].get("content", []):
                if c.get("type") == "text" and c.get("text", "").strip():
                    texts.append(c["text"].strip())
                if c.get("type") == "tool_use":
                    i = c.get("input", {})
                    if c["name"] == "Skill": skills.append(i.get("skill"))
                    elif c["name"] == "Read": reads.append(i.get("file_path", "").replace(plugin, "<plugin>").replace(run + "/", ""))
                    else:
                        tools.append(c["name"])
                        if c["name"] == "Bash": bash.append(i.get("command", "").replace(plugin, "<plugin>"))
        if e.get("type") == "result":
            final = e.get("result", ""); session = e.get("session_id", session)
    shown = "\n\n".join(texts) if texts else final
    if final and final.strip() not in shown: shown += "\n\n" + final
    open(os.path.join(run, "out", f"turn{n}.md"), "w").write(f"<!-- 사용자: {msg} -->\n\n{shown}\n")
    json.dump({"user": msg, "skills": skills, "reads": reads, "tools": tools, "bash": bash, "rc": r.returncode, "stderr": r.stderr[-500:]},
              open(os.path.join(run, "out", f"turn{n}.meta.json"), "w"), ensure_ascii=False, indent=1)
    print(f"{cid} turn{n}: skills={skills} reads={len(reads)} bash={len(bash)} rc={r.returncode}", flush=True)
    if "이 작업을 할까요" in shown and not msg.startswith("응, 그 작업"):
        turns.insert(0, "응, 그 작업 맞아.")
