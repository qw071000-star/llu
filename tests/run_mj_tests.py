#!/usr/bin/env python3
"""미드저니 전용 키트(kit-midjourney/)의 자동 점검. 실행: python3 tests/run_mj_tests.py
Higgsfield 키트(kit/)와 섞이지 않았는지, 읽기 지도·참조·zip이 맞는지 본다."""
import glob, os, re, sys, zipfile

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KIT = os.path.join(ROOT, "kit-midjourney")
SKILLS = os.path.join(KIT, "skills")
results = []


def check(name, ok, detail=""):
    results.append((bool(ok), name, detail))


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def tok(text):
    hangul = sum(1 for c in text if "가" <= c <= "힣" or "ᄀ" <= c <= "ᇿ" or "㄰" <= c <= "㆏")
    return hangul + (len(text) - hangul) / 4


EXPECT = ["mj-image", "mj-production", "mj-setup", "mj-shots", "mj-video"]
skill_dirs = sorted(d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d)))
check("[스킬] 스킬 5개", skill_dirs == EXPECT, ", ".join(skill_dirs))

# 1. 파일과 머리말
for f in ["README.md", "instructions.md", "context/tasks.md", "context/must-ask.md", "pack-skills.sh",
          "project-files/decisions.md", "project-files/asset-registry.md", "project-files/shot-list.md", "project-files/ok-cuts.md"]:
    check(f"[파일] {f} 있음", os.path.exists(os.path.join(KIT, f)))
descs = {}
for d in skill_dirs:
    t = read(os.path.join(SKILLS, d, "SKILL.md"))
    m = re.match(r"---\nname: (.+)\ndescription: (.+)\n---\n", t)
    check(f"[머리말] {d}/SKILL.md name = 폴더 이름", bool(m) and m.group(1) == d)
    if m:
        descs[d] = m.group(2)

# 2. Higgsfield 전용 말이 섞이지 않았다 (README의 "별개" 설명은 예외)
FORBIDDEN = ["Higgsfield", "check_prompt", "folder_id", "get_cost", "jobs_wait", "models_explore", "UUID", "generate_image",
             "generate_video", "element", "요소 UUID", "크레딧", "draft_job", "seedance", "Seedance", "Kling", "GPT Image"]
files = [p for p in glob.glob(os.path.join(KIT, "**", "*"), recursive=True)
         if os.path.isfile(p) and p.endswith((".md", ".sh")) and "/dist/" not in p and not p.endswith("README.md")]
bad = []
for p in files:
    t = read(p)
    for w in FORBIDDEN:
        if w in t:
            bad.append(f"{os.path.relpath(p, KIT)}:{w}")
check("[분리] Higgsfield 전용 말이 키트에 없다", not bad, ", ".join(bad[:8]))
readme = read(os.path.join(KIT, "README.md"))
check("[분리] README가 Higgsfield 키트와 별개라고 밝힌다", "완전히 별개" in readme)

# 3. 읽기 지도: 할 일 → 스킬·파일
tasks = read(os.path.join(KIT, "context", "tasks.md"))
rows = {}
for line in tasks.splitlines():
    m = re.match(r"\|\s*(\d+)\s*\|(.+)\|(.+)\|(.+)\|\s*$", line)
    if m:
        rows[int(m.group(1))] = m.group(4)
check("[할 일] 번호 1~15가 이어진다", sorted(rows) == list(range(1, 16)), str(sorted(rows)))
used = set()
for n, cell in rows.items():
    for sk in re.findall(r"`(mj-[a-z]+)`", cell):
        used.add(sk)
        check(f"[할 일] {n}번의 스킬 {sk}가 있다", sk in skill_dirs)
    for fn in re.findall(r"`([a-z\-]+\.md)`", cell):
        found = any(os.path.exists(os.path.join(SKILLS, d, fn)) for d in skill_dirs)
        check(f"[할 일] {n}번의 파일 {fn}가 있다", found)
check("[할 일] 모든 스킬이 한 번 이상 가리켜진다", used == set(skill_dirs), str(set(skill_dirs) - used))

# 4. 참조: 스킬 안에서 쓰는 `mj-…`, `*.md` 이름이 실제로 있다
known_md = {"decisions.md", "asset-registry.md", "shot-list.md", "ok-cuts.md", "tasks.md", "must-ask.md", "instructions.md"}
for d in skill_dirs:
    for p in glob.glob(os.path.join(SKILLS, d, "*.md")):
        t = read(p)
        for sk in set(re.findall(r"`(mj-[a-z]+)`", t)):
            check(f"[참조] {d}/{os.path.basename(p)} → {sk}", sk in skill_dirs)
        for fn in set(re.findall(r"`([A-Za-z\-]+\.md)`", t)):
            ok = fn in known_md or any(os.path.exists(os.path.join(SKILLS, x, fn)) for x in skill_dirs)
            check(f"[참조] {d}/{os.path.basename(p)} → {fn}", ok)

# 5. 지침의 규칙 수와 핵심 문장
inst = read(os.path.join(KIT, "instructions.md"))
nrules = len(re.findall(r"^\d+\. \*\*", inst, re.M))
check("[지침] 규칙 10개", nrules == 10, str(nrules))
check("[지침] 미드저니는 연결되지 않았고 만들었다고 말하지 않는다", "Midjourney is not connected here" in inst and "Never say or imply that you made" in inst)
check("[지침] 파라미터는 목록에 있는 것만, 모르면 확인 필요", "never invent one" in inst and "확인 필요" in inst)
check("[지침] 말로 한 불만은 이미지 없이 받아 프롬프트를 고친다, 이미지 없이 판정·승인은 안 한다", "A complaint in words is accepted as the finding" in inst and "never judge or approve anything yourself" in inst)
check("[지침] 승인하면 프롬프트 전문(파라미터 줄 포함)을 OK 대장에", "parameter line" in inst and "OK ledger" in inst)

# 6. 핵심 규칙이 스킬에 있다
img = read(os.path.join(SKILLS, "mj-image", "SKILL.md"))
check("[이미지] 25~60단어, 파라미터는 맨 끝, 호감 단어는 구조로", "25–60 words" in img and "Parameters go last" in img and "Appeal words" in img)
check("[이미지] 파라미터 표에 버전 확인 문구", "verify in the user's current Midjourney docs" in img and "--oref" in img and "--sref" in img)
check("[이미지] 고치기 순환: 한 가지만 전 → 후로", "the revise loop" in img and "전 → 후" in img)
check("[이미지] 인물은 한 장 시트가 아니라 따로", "separate images" in read(os.path.join(SKILLS, "mj-image", "character.md")))
check("[이미지] 인물과 장소를 합칠 때 두 단계", "two steps" in read(os.path.join(SKILLS, "mj-image", "first-frame.md")))
vid = read(os.path.join(SKILLS, "mj-video", "SKILL.md"))
check("[영상] 미검증 표시, 시작 이미지 첫 행 확인", "not verified by generation" in vid and "equals the start image" in vid)
prod = read(os.path.join(SKILLS, "mj-production", "SKILL.md"))
check("[운영] OK 기록: 승인 카드 수정 금지, 쌍 저장", "never edited" in prod and "Start image and clip are a pair" in prod)
sa = read(os.path.join(SKILLS, "mj-production", "shared-account.md"))
check("[운영] 공용 계정 8개 규칙", all(f"\n{i}. **" in sa for i in range(1, 9)))
must = read(os.path.join(KIT, "context", "must-ask.md"))
check("[질문] OK 카드 직접 수정 금지와 총괄 규칙이 항상 읽는 곳에 있다", "never edited in place" in must and "not `총괄:`" in must)
okc = read(os.path.join(KIT, "project-files", "ok-cuts.md"))
check("[정본] OK 대장: 스틸·영상 쌍, 정정 줄", "### 3-1 스틸" in okc and "### 3-1 영상" in okc and "정정(날짜 · 이름)" in okc)
check("[정본] 컷 목록에 담당 칸", "| 상태 | 담당 |" in read(os.path.join(KIT, "project-files", "shot-list.md")))
check("[정본] 확정 사항 §7에 운영 방식·총괄", "운영 방식:" in read(os.path.join(KIT, "project-files", "decisions.md")) and "총괄:" in read(os.path.join(KIT, "project-files", "decisions.md")))

# 7. 읽기량
always = tok(inst) + tok(tasks) + tok(must) + sum(tok(v) for v in descs.values())
check(f"[읽기량] 항상 읽히는 양 추정 {always:,.0f}토큰 ≤ 4,200", always <= 4200)
inst_tok = tok(inst)
check(f"[읽기량] instructions.md 추정 {inst_tok:,.0f}토큰 ≤ 1,500", inst_tok <= 1500)
for d in skill_dirs:
    big = max(tok(read(p)) for p in glob.glob(os.path.join(SKILLS, d, "*.md")))
    check(f"[읽기량] {d}의 가장 큰 파일 추정 {big:,.0f}토큰 ≤ 2,200", big <= 2200)

# 8. dist가 소스와 같다
for d in skill_dirs:
    zp = os.path.join(KIT, "dist", f"{d}.zip")
    ok = os.path.exists(zp)
    if ok:
        with zipfile.ZipFile(zp) as z:
            for name in z.namelist():
                if name.endswith("/"):
                    continue
                src = os.path.join(SKILLS, name)
                ok = ok and os.path.exists(src) and z.read(name).decode("utf-8") == read(src)
            srcs = {os.path.relpath(p, SKILLS) for p in glob.glob(os.path.join(SKILLS, d, "**", "*"), recursive=True) if os.path.isfile(p)}
            ok = ok and srcs == {n for n in z.namelist() if not n.endswith("/")}
    check(f"[zip] {d}.zip이 소스와 같다", ok)
pi = os.path.join(KIT, "dist", "project-instructions.md")
want = read(os.path.join(KIT, "instructions.md")) + "\n" + read(os.path.join(KIT, "context", "tasks.md")) + "\n" + read(os.path.join(KIT, "context", "must-ask.md"))
check("[zip] project-instructions.md가 지침+할 일+질문과 같다", os.path.exists(pi) and read(pi) == want)

# 9. README가 스킬을 모두 적는다
check("[문서] README가 스킬 5개와 설치·작업 흐름을 적는다", all(f"`{s}`" in readme or s in readme for s in EXPECT) and "설치" in readme and "작업 흐름" in readme)

bad = [r for r in results if not r[0]]
for ok, name, detail in results:
    if not ok:
        print(f"FAIL  {name}  {detail}")
print(f"추정 토큰: 항상 읽힘 {always:,.0f} · instructions.md {inst_tok:,.0f}")
print(f"\n점검 {len(results)}개 · 통과 {len(results) - len(bad)} · 실패 {len(bad)}")
sys.exit(1 if bad else 0)
