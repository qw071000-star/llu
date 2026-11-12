#!/usr/bin/env bash
# kit-midjourney/skills/<이름>/ 폴더마다 Claude 앱 업로드용 zip → kit-midjourney/dist/<이름>.zip
# 프로젝트 지침 칸에 붙일 한 파일 → kit-midjourney/dist/project-instructions.md
# 스킬·지침을 고친 뒤 다시 실행한다.
set -euo pipefail
cd "$(dirname "$0")/skills"
mkdir -p ../dist
for dir in */; do
  name="${dir%/}"
  rm -f "../dist/$name.zip"
  python3 -m zipfile -c "../dist/$name.zip" "$name"
  echo "made kit-midjourney/dist/$name.zip"
done
cd ..
{ cat instructions.md; echo; cat context/tasks.md; echo; cat context/must-ask.md; } > dist/project-instructions.md
echo "made kit-midjourney/dist/project-instructions.md"
