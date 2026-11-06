#!/usr/bin/env bash
# kit/skills/<이름>/ 폴더마다 Claude 앱 업로드용 zip을 만든다 → kit/dist/<이름>.zip
# 스킬 파일을 고친 뒤 다시 실행한다.
set -euo pipefail
cd "$(dirname "$0")/skills"
mkdir -p ../dist
for dir in */; do
  name="${dir%/}"
  rm -f "../dist/$name.zip"
  python3 -m zipfile -c "../dist/$name.zip" "$name"
  echo "made kit/dist/$name.zip"
done
# Claude 앱 프로젝트 지침 칸에 붙일 한 파일: 지침 + 언제 무엇을 + 꼭 물어볼 것
cd ..
{ cat instructions.md; echo; cat context/tasks.md; echo; cat context/must-ask.md; } > dist/project-instructions.md
# 앱판: 검사 줄의 Claude Code 경로(.claude/skills/…)와 Code 허용 목록용 제한을 앱 코드 실행에 맞게 바꾼다
python3 - dist/project-instructions.md <<'PY'
import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
old_rule = ("run the line below exactly, as a single standalone Bash call (no `cd`, `&&`, pipes or absolute paths). "
            "No `cd` in earlier calls either.")
new_rule = ("run the line below with code execution, one call. In the Claude app the script is in the uploaded "
            "`higgsfield-generation` skill folder, the folder its SKILL.md was read from: put that absolute path "
            "where the line says `<skill folder>`. If code execution is off or the script is not there, say so in "
            "one line, go through the pre-send checklist (`image-prompt` §6 / `video-prompt` §4) by hand, and never "
            "report the check as passed.")
old_cmd = "python3 .claude/skills/higgsfield-generation/check_prompt.py"
new_cmd = "python3 <skill folder>/check_prompt.py"
assert s.count(old_rule) == 1 and s.count(old_cmd) == 2, "instructions.md Check 줄이 바뀌었다: pack-skills.sh 앱판 치환을 고친다"
s = s.replace(old_rule, new_rule).replace(old_cmd, new_cmd)
open(p, "w", encoding="utf-8").write(s)
PY
echo "made kit/dist/project-instructions.md (Claude 앱판 검사 줄)"
