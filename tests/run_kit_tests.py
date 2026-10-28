#!/usr/bin/env python3
"""키트 점검 — 스킬 묶음, 참조, 용어, 빈 틀, 프롬프트 검사기를 기계적으로 확인한다.

실행: python3 tests/run_kit_tests.py   (리포 루트에서)
키트를 고칠 때마다 돌린다. 실패가 있으면 종료 코드 1.
"""
import glob
import os
import re
import subprocess
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.path.join(ROOT, "kit")
SKILLS = os.path.join(KIT, "skills")
CHECKER = os.path.join(SKILLS, "higgsfield-generation", "check_prompt.py")
FIX = os.path.join(ROOT, "tests", "fixtures")

results = []


def check(name, ok, detail=""):
    results.append((ok, name, detail))


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        data[k.strip()] = v.strip()
    return data


skill_dirs = sorted(d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d)))
skill_files = {d: sorted(os.listdir(os.path.join(SKILLS, d))) for d in skill_dirs}

# 1. 스킬 frontmatter
for d in skill_dirs:
    fm = frontmatter(read(os.path.join(SKILLS, d, "SKILL.md")))
    check(f"[스킬] {d}: frontmatter 있음", fm is not None)
    if fm:
        check(f"[스킬] {d}: name이 폴더 이름과 같음", fm.get("name") == d, fm.get("name", ""))
        check(f"[스킬] {d}: name 형식(소문자·숫자·하이픈, 64자 이하)", re.fullmatch(r"[a-z0-9-]{1,64}", fm.get("name", "")) is not None)
        desc = fm.get("description", "")
        check(f"[스킬] {d}: description 1~1024자", 0 < len(desc) <= 1024, f"{len(desc)}자")
        check(f"[스킬] {d}: description에 꺾쇠(<, >) 없음", "<" not in desc and ">" not in desc)

# 2. 배포 zip이 소스와 같은가
for d in skill_dirs:
    zp = os.path.join(KIT, "dist", f"{d}.zip")
    if not os.path.exists(zp):
        check(f"[zip] {d}.zip 있음", False)
        continue
    z = zipfile.ZipFile(zp)
    tops = {n.split("/")[0] for n in z.namelist()}
    check(f"[zip] {d}.zip 최상위가 폴더 하나", tops == {d}, str(tops))
    same = True
    for fn in skill_files[d]:
        src = os.path.join(SKILLS, d, fn)
        if os.path.isdir(src):
            continue
        try:
            same &= z.read(f"{d}/{fn}") == open(src, "rb").read()
        except KeyError:
            same = False
    check(f"[zip] {d}.zip 내용이 소스와 같음 (다르면 pack-skills.sh 실행)", same)

# 3. 지침의 스킬 지도에 적힌 스킬·파일이 실제로 있는가
inst = read(os.path.join(KIT, "instructions.md"))
for s in re.findall(r"`([a-z-]+)`(?: →|\s*\|)", inst):
    if s in ("decisions", "shot-list", "asset-registry"):
        continue
    check(f"[지침] 스킬 '{s}' 있음", s in skill_dirs)
for line in inst.splitlines():
    m = re.search(r"`([a-z-]+)` → (.+?) \|", line)
    if m:
        for fn in re.findall(r"`([a-z-]+\.md)`", m.group(2)):
            check(f"[지침] {m.group(1)}/{fn} 있음", fn in skill_files.get(m.group(1), []))

# 4. 스킬 안에서 가리키는 파일이 같은 스킬 폴더에 있는가
external = {"decisions.md", "asset-registry.md", "shot-list.md", "instructions.md", "SKILL.md"}
for d in skill_dirs:
    for fn in skill_files[d]:
        if not fn.endswith(".md"):
            continue
        for ref in set(re.findall(r"`([a-z0-9-]+\.(?:md|py))`", read(os.path.join(SKILLS, d, fn)))):
            if ref in external:
                continue
            check(f"[참조] {d}/{fn} → {ref}", ref in skill_files[d])

# 5. § 참조가 실제 절을 가리키는가
def headings(path):
    return set(re.findall(r"^## (\d+)\.", read(path), re.M))

for d in skill_dirs:
    for fn in skill_files[d]:
        if not fn.endswith(".md"):
            continue
        text = read(os.path.join(SKILLS, d, fn))
        for other, num in re.findall(r"`([a-z-]+)`\s*§(\d+)", text):
            if other in skill_dirs:
                check(f"[§] {d}/{fn} → {other} §{num}", num in headings(os.path.join(SKILLS, other, "SKILL.md")))
        for num in re.findall(r"(?<![`\w])§(\d+)", text):
            if re.search(rf"`[a-z-]+`\s*§{num}", text) and num not in headings(os.path.join(SKILLS, d, fn)):
                continue
            check(f"[§] {d}/{fn} 안의 §{num}", num in headings(os.path.join(SKILLS, d, fn)) or num in headings(os.path.join(SKILLS, d, "SKILL.md")))

# 6. 컷 카드·핸드오프 칸 번호 참조
card = read(os.path.join(SKILLS, "production-session", "cut-card.md"))
handoff = read(os.path.join(SKILLS, "production-session", "handoff.md"))
card_fields = dict(re.findall(r"^\[(\d+)\] ([^:：\n]+)", card, re.M))
check("[컷카드] [2] 저장 위치", card_fields.get("2", "").startswith("저장 위치"))
check("[컷카드] [4] 카메라", card_fields.get("4", "").startswith("카메라"))
check("[컷카드] [5] 인물", card_fields.get("5", "").startswith("인물"))
check("[컷카드] [6] 타이밍", card_fields.get("6", "").startswith("타이밍"))
check("[컷카드] [11] 이전 시도", card_fields.get("11", "").startswith("이전 시도"))
check("[컷카드] [12] 확정 프롬프트", card_fields.get("12", "").startswith("확정 프롬프트"))
check("[핸드오프] [6] 다음 할 일", re.search(r"^\[6\] 다음 할 일", handoff, re.M) is not None)

# 7. 상태 용어가 파일마다 같은가
gen = read(os.path.join(SKILLS, "higgsfield-generation", "SKILL.md"))
shot = read(os.path.join(KIT, "project-files", "shot-list.md"))
for word in ["대기", "진행", "검토", "승인", "보류"]:
    check(f"[용어] 컷 상태 '{word}': 생성 운영·컷 목록·핸드오프에 모두 있음", word in gen and word in shot and (word in handoff or word == "대기"))
for word in ["승인", "거절", "보류", "대체됨"]:
    check(f"[용어] 결과물 상태 '{word}': 생성 운영 스킬에 있음", word in gen)
for word in ["00 에셋", "99 시험·보관"]:
    check(f"[용어] 폴더 이름 '{word}': 생성 운영·에셋 대장에 모두 있음", word in gen and word in read(os.path.join(KIT, "project-files", "asset-registry.md")))

# 8. 영상 정보 점검표가 15블록을 모두 덮는가
vskill = read(os.path.join(SKILLS, "video-prompt", "SKILL.md"))
intake = vskill.split("## 0.")[1].split("## 1.")[0]
for block in ["PRE_SHOT_CONTINUITY", "SCENE_CONTEXT", "ACTIVE_REFERENCES", "LOCATION_MAP", "FIRST_FRAME_AND_SPATIAL_BLOCKING",
              "FORMAT_MODE", "OPTICS", "CAMERA", "ACTION_TIMING", "CHARACTER_ACTING", "PHYSICS", "LIGHTING", "AUDIO",
              "STYLE", "REQUIRED_AND_FORBIDDEN_CONSTRAINTS"]:
    check(f"[점검표] 15블록 '{block}'에 들어갈 정보가 점검표에 있음", block in intake)

# 9. 배포 파일에 특정 작품·사이트 표현이 없는가
banned = re.compile(r"고등어|어머니|나부코|히브리|합창|Prompter|lucian|conti\.|콘티 사이트|신발장|식탁|봉지|아내|현관|우편|수양버들|헤롯|생선|1980|South Korea|E-\d{2}|error-registry")
shipped = [os.path.join(KIT, "instructions.md")] + glob.glob(os.path.join(KIT, "project-files", "*.md")) + glob.glob(os.path.join(SKILLS, "*", "*"))
for p in shipped:
    hits = sorted(set(banned.findall(read(p))))
    check(f"[일반화] {os.path.relpath(p, ROOT)}에 작품 고유 표현 없음", not hits, ", ".join(hits))

# 10. 빈 틀: 15블록 순서, 빈칸이 잡히는가
live = read(os.path.join(SKILLS, "video-prompt", "live-action.md"))
tmpl = re.search(r"## 빈 틀.*?```text\n(.*?)```", live, re.S).group(1)
order = [tmpl.find(f"[{b}]") for b in ["SCENE_CONTEXT", "ACTIVE_REFERENCES", "LOCATION_MAP", "FIRST_FRAME_AND_SPATIAL_BLOCKING", "FORMAT_MODE", "OPTICS", "CAMERA", "ACTION_TIMING", "CHARACTER_ACTING", "PHYSICS", "LIGHTING", "AUDIO", "STYLE", "QUALITY", "REQUIRED_AND_FORBIDDEN_CONSTRAINTS"]]
check("[빈 틀] 15블록 틀에 블록이 모두 있고 순서대로", all(o >= 0 for o in order) and order == sorted(order))

# 11. 프롬프트 검사기: 픽스처마다 기대 결과와 같은가
#     파일 이름: <kind>__<pass|fail>__<설명>.txt, 옵션은 첫 줄 주석 "# args: --refs 3"
for path in sorted(glob.glob(os.path.join(FIX, "*.txt"))):
    base = os.path.basename(path)
    kind, expect, _ = base.split("__", 2)
    text = read(path)
    args = []
    first = text.splitlines()[0] if text else ""
    if first.startswith("# args:"):
        args = first[len("# args:"):].split()
        body = "\n".join(text.splitlines()[1:])
        tmp = os.path.join(FIX, ".tmp_" + base)
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(body)
        target = tmp
    else:
        target = path
    args = [a.replace("{FIX}", FIX) for a in args]
    r = subprocess.run([sys.executable, CHECKER, "--kind", kind, target] + args, capture_output=True, text=True)
    if target != path:
        os.remove(target)
    fails = [l for l in r.stdout.splitlines() if l.startswith("FAIL")]
    warns = [l for l in r.stdout.splitlines() if l.startswith("WARN")]
    if expect == "pass":
        check(f"[검사기] {base}: FAIL·WARN 없음", not fails and not warns, " / ".join(fails + warns)[:300])
    else:
        check(f"[검사기] {base}: 문제를 잡음", bool(fails or warns), r.stdout.strip()[:300])

# 결과
bad = [r for r in results if not r[0]]
for ok, name, detail in results:
    if not ok:
        print(f"FAIL  {name}  {detail}")
print(f"\n점검 {len(results)}개 · 통과 {len(results) - len(bad)} · 실패 {len(bad)}")
sys.exit(1 if bad else 0)
