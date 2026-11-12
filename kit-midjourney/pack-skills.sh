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
# 이 폴더 전체를 한 파일로: 한 단계 위에 kit-midjourney.zip (받아서 다른 프로젝트에 적용)
cd ..
python3 - <<'PY'
import os, zipfile
here = "kit-midjourney"
with zipfile.ZipFile("kit-midjourney.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for d, dirs, files in os.walk(here):
        dirs[:] = [x for x in dirs if x not in ("__pycache__", "runs-mj")]
        for f in sorted(files):
            if f.endswith(".pyc"):
                continue
            p = os.path.join(d, f)
            z.write(p, p)
print("made kit-midjourney.zip")
PY
