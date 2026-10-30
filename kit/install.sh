#!/usr/bin/env bash
# 키트를 작품 폴더(Claude Code)에 설치하거나 새 버전으로 바꾼다.
#   bash kit/install.sh [작품 폴더] [--title 작품명] [--higgsfield "이름 (ID)"] [--canon 정본 위치]
#   (폴더 기본: 지금 폴더. --옵션은 "This project" 칸이 아직 비어 있을 때만 채운다)
# 정본(project/)과 사용자가 채운 "This project" 칸은 덮어쓰지 않는다.
set -euo pipefail
KIT="$(cd "$(dirname "$0")" && pwd)"
DIR="."; TITLE=""; HIGGS=""; CANON=""
while [ $# -gt 0 ]; do
  case "$1" in
    --title) TITLE="$2"; shift 2 ;;
    --higgsfield) HIGGS="$2"; shift 2 ;;
    --canon) CANON="$2"; shift 2 ;;
    *) DIR="$1"; shift ;;
  esac
done
DEST="$(cd "$DIR" && pwd)"
if [ "$DEST" = "$(dirname "$KIT")" ]; then echo "키트 리포 자체에는 설치하지 않는다. 작품 폴더를 지정한다." >&2; exit 1; fi
cd "$DEST"
mkdir -p .claude project/cuts project/log media

# 지침: 새 버전으로 바꾸되, 이미 채운 "## This project" 칸은 그대로 둔다
if [ -f .claude/instructions.md ]; then
  python3 - "$KIT/instructions.md" .claude/instructions.md <<'PY'
import sys
new = open(sys.argv[1], encoding="utf-8").read()
old = open(sys.argv[2], encoding="utf-8").read()
def block(s):
    a = s.find("## This project"); b = s.find("## Role")
    return (a, b) if 0 <= a < b else None
n, o = block(new), block(old)
if n and o:
    new = new[:n[0]] + old[o[0]:o[1]] + new[n[1]:]
open(sys.argv[2], "w", encoding="utf-8").write(new)
PY
  echo "바꿈  .claude/instructions.md (This project 칸은 유지)"
else
  cp "$KIT/instructions.md" .claude/instructions.md
  echo "추가  .claude/instructions.md (This project 칸을 채운다)"
fi

# 항상 읽는 context와 스킬: 통째로 새 버전
for d in context skills; do
  state="추가"; [ -d ".claude/$d" ] && state="바꿈"
  rm -rf ".claude/$d"; cp -r "$KIT/$d" ".claude/$d"
  echo "$state  .claude/$d/"
done

# 권한: 다르면 옛 파일을 .bak으로 남기고 바꾼다
if [ -f .claude/settings.json ] && ! cmp -s "$KIT/project-files/settings.json" .claude/settings.json; then
  cp .claude/settings.json .claude/settings.json.bak
  echo "바꿈  .claude/settings.json (옛 파일: .claude/settings.json.bak, 따로 넣은 권한이 있으면 옮긴다)"
fi
[ -f .claude/settings.json ] || { cp "$KIT/project-files/settings.json" .claude/settings.json; echo "추가  .claude/settings.json"; }

# CLAUDE.md: 없을 때만. 있으면 세 줄 불러오기가 있는지만 본다
if [ ! -f CLAUDE.md ]; then
  cp "$KIT/project-files/CLAUDE.md" CLAUDE.md; echo "추가  CLAUDE.md"
else
  for f in instructions.md context/tasks.md context/must-ask.md; do
    grep -qF "@.claude/$f" CLAUDE.md || echo "확인  CLAUDE.md에 '@.claude/$f' 줄이 없다. 맨 위에 넣는다"
  done
  echo "유지  CLAUDE.md"
fi

# 정본 틀: 없는 파일만
for f in decisions asset-registry shot-list ok-cuts; do
  if [ -f "project/$f.md" ]; then echo "유지  project/$f.md"; else cp "$KIT/project-files/$f.md" project/; echo "추가  project/$f.md"; fi
done

touch .gitignore
for line in tmp/ media/; do grep -qxF "$line" .gitignore || echo "$line" >> .gitignore; done

# "This project" 칸: 비어 있는(자리표시) 줄만 채운다
python3 - "$TITLE" "$HIGGS" "$CANON" <<'PY'
import re, sys
title, higgs, canon = sys.argv[1:4]
p = ".claude/instructions.md"
s = open(p, encoding="utf-8").read()
done = []
if title and "「[작품명]」" in s:
    s = s.replace("「[작품명]」", f"「{title}」", 1); done.append("작품명")
if higgs and "[name] (`[project_id]`)" in s:
    m = re.match(r"(.*?)\s*\((.*)\)\s*$", higgs)
    val = f"{m.group(1)} (`{m.group(2)}`)" if m else higgs
    s = s.replace("[name] (`[project_id]`)", val, 1); done.append("Higgsfield")
if canon and "Canon location: [" in s:
    s = re.sub(r"Canon location: \[[^\n]*", lambda _: f"Canon location: {canon}", s, count=1); done.append("정본 위치")
open(p, "w", encoding="utf-8").write(s)
if title:
    c = open("CLAUDE.md", encoding="utf-8").read()
    if "[작품명]" in c:
        open("CLAUDE.md", "w", encoding="utf-8").write(c.replace("[작품명]", title, 1))
left = [n for n, k in (("작품명", "「[작품명]」"), ("Higgsfield", "[project_id]"), ("정본 위치", "Canon location: [")) if k in s]
print("채움  This project: " + (", ".join(done) if done else "없음") + (" · 비어 있음: " + ", ".join(left) if left else ""))
PY

# 검사 스크립트가 도는지
mkdir -p tmp
printf 'A quiet bus stop at dusk, photorealistic, no people.\n' > tmp/install_check.txt
if python3 .claude/skills/higgsfield-generation/check_prompt.py --kind image tmp/install_check.txt >/dev/null; then
  echo "확인  검사 스크립트 동작"
else
  echo "확인  검사 스크립트가 돌지 않았다(python3 확인)"
fi
rm -f tmp/install_check.txt
command -v ffmpeg >/dev/null || echo "확인  ffmpeg 없음: 마지막 프레임·러프컷(21번)·색 맞추기(22번)만 안 된다"
echo "끝. 이 폴더에서 claude를 다시 열고 '이 폴더를 믿는가'를 승인한다."
