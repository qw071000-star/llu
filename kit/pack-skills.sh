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
