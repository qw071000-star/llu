#!/usr/bin/env bash
# 안내서 PDF를 다시 만든다 → guides/pdf/
#   bash tools/pdf/build.sh            (전부)
#   bash tools/pdf/build.sh install    (설치 안내만) | work | full
# 필요한 것: python3, reportlab, fonttools, 한글 폰트 WenQuanYi Zen Hei(/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc)
# 키트를 고쳐 안내 내용이 바뀌면 tools/pdf/*.py의 본문을 고치고 다시 돌린다.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$HERE/../../guides/pdf"
mkdir -p "$OUT"
TMP="$(mktemp -d)"
trap 'rm -rf "${TMP:?}"' EXIT
what="${1:-all}"

build_short() { # <본문 파일> <출력 이름>
  cat "$HERE/common.py" "$HERE/$1.py" > "$TMP/$1.py"
  python3 "$TMP/$1.py" "$OUT/$2"
  echo "만듦  guides/pdf/$2"
}

[ "$what" = all ] || [ "$what" = install ] && build_short install_guide "AI제작키트_설치안내.pdf"
[ "$what" = all ] || [ "$what" = work ] && build_short work_guide "AI제작키트_작업안내_5쪽.pdf"
if [ "$what" = all ] || [ "$what" = full ]; then
  cp "$HERE/full_guide.py" "$TMP/full_guide.py"
  # 목차의 쪽 번호는 두 번째 실행에서 채워진다(첫 실행이 쪽 번호를 .pages.json에 적어 둔다)
  python3 "$TMP/full_guide.py" "$OUT/AI제작키트_사용안내서.pdf"
  python3 "$TMP/full_guide.py" "$OUT/AI제작키트_사용안내서.pdf"
  rm -f "$OUT/AI제작키트_사용안내서.pdf.pages.json"
  echo "만듦  guides/pdf/AI제작키트_사용안내서.pdf"
fi
