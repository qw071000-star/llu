#!/usr/bin/env python3
"""실제 Claude Code로 체인을 돌린다: 키트를 설치한 시험 폴더에서 사용자 말만 넣는다.
./real_run.py <체인ID> [run_root]   — 턴은 real-chains.json에서 읽는다.
턴마다 out/turnN.md(답 전문)와 out/turnN.meta.json(부른 Skill, 연 파일, 도구, Bash 명령)을 남긴다."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
cid = sys.argv[1]
root = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "runs-real")
chains = json.load(open(os.path.join(HERE, "real-chains.json")))
spec = chains[cid]
mode = "empty" if spec.get("empty") else "full"
subprocess.run([os.path.join(HERE, "make_run.sh"), cid, mode, root], check=True, stdout=subprocess.DEVNULL)
run = os.path.join(root, cid)
for f in ("PLAYER-RULES.md", "SKILLS-INDEX.md"):
    p = os.path.join(run, f)
    if os.path.exists(p): os.remove(p)
SIM = ("이 환경에는 Higgsfield MCP가 연결되어 있지 않다(시험 환경). Higgsfield 도구를 부를 때는 실제로 부르지 말고 "
       "답 안에 `[TOOL] 도구이름(인자)` 줄을 쓰고, 그 결과는 sim/higgsfield.md에서 찾는다. 거기 없는 결과는 알 수 없음이다.")
session = None
for n, msg in enumerate(spec["turns"], 1):
    cmd = ["claude", "-p", msg, "--model", spec.get("model", "sonnet"), "--output-format", "stream-json", "--verbose",
           "--permission-mode", "acceptEdits", "--disallowedTools", "mcp__*",
           "--allowedTools", "Bash(python3 .claude/skills/higgsfield-generation/check_prompt.py:*)", "Bash(python3 .claude/skills/assembly/assemble.py:*)", "Bash(python3 .claude/skills/color-continuity/color.py:*)", "--append-system-prompt", SIM]
    if session: cmd += ["--resume", session]
    r = subprocess.run(cmd, cwd=run, capture_output=True, text=True, timeout=900)
    skills, reads, tools, bash, final = [], [], [], [], ""
    for line in r.stdout.splitlines():
        try: e = json.loads(line)
        except Exception: continue
        if e.get("type") == "system" and e.get("session_id"): session = e["session_id"]
        if e.get("type") == "assistant":
            for c in e["message"].get("content", []):
                if c.get("type") == "tool_use":
                    i = c.get("input", {})
                    if c["name"] == "Skill": skills.append(i.get("skill"))
                    elif c["name"] == "Read": reads.append(os.path.relpath(i.get("file_path", ""), run))
                    else:
                        tools.append(c["name"])
                        if c["name"] == "Bash":
                            bash.append(i.get("command", ""))
                            import re as _re
                            for f in _re.findall(r"(\.claude/[\w./-]+\.md|project/[\w./-]+\.md)", i.get("command", "")):
                                reads.append(f + " (bash)")
        if e.get("type") == "result":
            final = e.get("result", ""); session = e.get("session_id", session)
    os.makedirs(os.path.join(run, "out"), exist_ok=True)
    open(os.path.join(run, "out", f"turn{n}.md"), "w").write(f"<!-- 사용자: {msg} -->\n\n{final}\n")
    json.dump({"user": msg, "skills": skills, "reads": reads, "tools": tools, "bash": bash, "rc": r.returncode, "stderr": r.stderr[-500:]},
              open(os.path.join(run, "out", f"turn{n}.meta.json"), "w"), ensure_ascii=False, indent=1)
    print(f"{cid} turn{n}: skills={skills} reads={len(reads)} rc={r.returncode}", flush=True)
