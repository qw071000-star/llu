#!/usr/bin/env bash
# 시험 실행 폴더를 만든다: ./make_run.sh <체인ID> [empty] [run_root]
# 키트(kit/)의 지금 상태 + 시험 작품(testbed/)으로 사용자의 작업 리포를 흉내 낸다.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
KIT="$HERE/../../kit"
ID="$1"; MODE="${2:-full}"; ROOT="${3:-$HERE/runs}"
RUN="$ROOT/$ID"
rm -rf "$RUN"; mkdir -p "$RUN/.claude" "$RUN/out" "$RUN/sim"
cp -r "$KIT/skills" "$RUN/.claude/skills"
cp "$KIT/project-files/CLAUDE.md" "$RUN/CLAUDE.md"
cp -r "$KIT/context" "$RUN/.claude/context"
if [ "$MODE" = "empty" ]; then
  mkdir -p "$RUN/project/cuts" "$RUN/project/log"
  cp "$KIT/project-files/"{decisions,asset-registry,shot-list,ok-cuts}.md "$RUN/project/"
  cp "$KIT/instructions.md" "$RUN/.claude/instructions.md"
  printf '# Higgsfield 시뮬레이션 결과표 (시험용)\n\n실제 Higgsfield를 부르지 않는다. 답에 `[TOOL] 도구이름(인자)`를 적는다.\n\n- 선택된 워크스페이스: 팀 워크스페이스 `ws-sim-0001`\n- list_projects: 「빈 정류장」 프로젝트는 아직 없다.\n- create_project, create_folder: 성공. ID는 `prj-new-0001`, 폴더는 `fld-<이름>`.\n' > "$RUN/sim/higgsfield.md"
else
  cp -r "$HERE/testbed/project" "$RUN/project"
  cp "$HERE/testbed/sim/higgsfield.md" "$RUN/sim/"
  python3 - "$KIT/instructions.md" "$RUN/.claude/instructions.md" <<'PY'
import sys
s = open(sys.argv[1]).read()
a = s.index("## 이 프로젝트"); b = s.index("## 역할")
filled = """## 이 프로젝트

- 작품: 「빈 정류장」 · Higgsfield 프로젝트: 빈 정류장 (`prj-sim-0001`)
- 정본: 확정 사항 `decisions.md` · 에셋·폴더 대장 `asset-registry.md` · 컷 목록 `shot-list.md` · OK 대장 `ok-cuts.md` · 핸드오프 로그
- 컷 번호: 장면-컷(`3-1`). 에셋은 에셋 ID(`CH-001`)
- 정본 위치: 리포 `project/`

"""
open(sys.argv[2], "w").write(s[:a] + filled + s[b:])
PY
fi
cp "$HERE/player-rules.md" "$RUN/PLAYER-RULES.md"
if [ -f "$HERE/testbed/prev/$ID.md" ]; then cp "$HERE/testbed/prev/$ID.md" "$RUN/out/turn0.md"; fi
python3 - "$RUN" <<'PY'
import os, re, sys
run = sys.argv[1]
rows = []
for d in sorted(os.listdir(os.path.join(run, ".claude/skills"))):
    t = open(os.path.join(run, ".claude/skills", d, "SKILL.md")).read()
    m = re.search(r"description: (.*)", t)
    rows.append(f"- **{d}**: {m.group(1)}")
open(os.path.join(run, "SKILLS-INDEX.md"), "w").write("# 이 환경에서 쓸 수 있는 스킬 (이름과 설명만 항상 보인다)\n\n" + "\n".join(rows) + "\n")
PY
( cd "$RUN" && git init -q && git add -A && git -c user.email=t@t -c user.name=t commit -qm base )
echo "$RUN"
