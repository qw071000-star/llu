#!/usr/bin/env python3
"""키트 점검 — 스킬 묶음, 참조, 용어, 빈 틀, 프롬프트 검사기를 기계적으로 확인한다.

실행: python3 tests/run_kit_tests.py   (리포 루트에서)
키트를 고칠 때마다 돌린다. 실패가 있으면 종료 코드 1.

AI가 읽는 키트(지침·context/·스킬)는 영어다. 한국어는 사용자에게 보이는 말, 인용한 사용자 말,
정본 칸 이름에만 남는다. 그래서 문장 점검은 영어 문장을, 그 세 가지는 한국어를 찾는다.
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


def tok(text):
    """추정 토큰 수: 한글 글자 × 1.0 + 그 밖의 글자 / 4."""
    hangul = sum(1 for c in text if "\uac00" <= c <= "\ud7a3" or "\u1100" <= c <= "\u11ff" or "\u3130" <= c <= "\u318f")
    return hangul + (len(text) - hangul) / 4


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

# 3. 항상 읽히는 것 = CLAUDE.md가 불러오는 파일(지침 + context/). 할 일 목록에 적힌 스킬·파일이 실제로 있는가
inst_core = read(os.path.join(KIT, "instructions.md"))
claude_md = read(os.path.join(KIT, "project-files", "CLAUDE.md"))
imports = re.findall(r"^@\.claude/(\S+)\s*$", claude_md, re.M)
check("[항상] CLAUDE.md가 instructions.md를 불러온다", "instructions.md" in imports, ", ".join(imports))
CTX = [p[len("context/"):] for p in imports if p.startswith("context/")]
check("[항상] CLAUDE.md가 context/ 파일을 불러온다", len(CTX) >= 1, ", ".join(imports))
check("[항상] routing.md는 없어졌다(tasks.md가 대신함)", not os.path.exists(os.path.join(KIT, "context", "routing.md")) and "tasks.md" in CTX)
check("[항상] CLAUDE.md: 불러오기가 안 될 때 읽을 파일도 같은 목록", all(f"`.claude/{p}`" in claude_md for p in imports))
check("[항상] context/ 파일은 CLAUDE.md가 불러오는 것뿐", sorted(os.listdir(os.path.join(KIT, "context"))) == sorted(CTX))
for f in CTX:
    check(f"[항상] context/{f} 있음", os.path.exists(os.path.join(KIT, "context", f)))
    check(f"[항상] 지침이 context/{f}를 가리킨다", f"context/{f}" in inst_core)
inst = inst_core + "\n" + "\n".join(read(os.path.join(KIT, "context", f)) for f in CTX if os.path.exists(os.path.join(KIT, "context", f)))
INST_BUDGET = 1750  # 추정 토큰. 영어로 옮긴 뒤 4,000자(한국어 기준)는 맞지 않아 토큰으로 바꿈(2026-10-29 약 1,716)
check(f"[지침] instructions.md 추정 {tok(inst_core):,.0f}토큰 ≤ {INST_BUDGET:,}", tok(inst_core) <= INST_BUDGET, f"{len(inst_core):,}자")
for s in re.findall(r"`([a-z-]+)`(?: →|\s*\|)", inst):
    if s in ("decisions", "shot-list", "asset-registry"):
        continue
    check(f"[지침] 스킬 '{s}' 있음", s in skill_dirs)
for line in inst.splitlines():
    m = re.search(r"`([a-z-]+)` → (.+?) \|", line)
    if m:
        for fn in re.findall(r"`([a-z-]+\.md)`", m.group(2)):
            check(f"[지침] {m.group(1)}/{fn} 있음", fn in skill_files.get(m.group(1), []))
ctx_route = read(os.path.join(KIT, "context", "tasks.md"))
ctx_ask = read(os.path.join(KIT, "context", "must-ask.md"))
_task_rows = {int(m.group(1)): m.group(0) for m in re.finditer(r"^\| (\d+) \|.*$", ctx_route.split("## 2.")[1].split("## 3.")[0], re.M)}
check("[할 일] tasks.md 표 번호가 1부터 빠짐없이", sorted(_task_rows) == list(range(1, len(_task_rows) + 1)) and len(_task_rows) >= 20, str(sorted(_task_rows)))
_guide = read(os.path.join(ROOT, "guides", "할일-목록.md"))
_guide_rows = sorted(int(n) for n in re.findall(r"^\| (\d+) \|", _guide, re.M))
check("[할 일] 사람용 할일-목록.md와 번호가 같다", _guide_rows == sorted(_task_rows), str(_guide_rows))
_r1 = ctx_route.split("## 1.")[1].split("## 2.")[0]
check("[할 일] tasks §1: 한 작업만 맞으면 바로 진행하고 첫 줄에 번호를 밝힌다", "**Go straight on** when only one task fits" in _r1 and "\"[N]번 [작업명]으로 진행합니다.\"" in _r1)
check("[할 일] tasks §1: 둘 이상 맞을 때만 한 줄로 묻고 아무것도 열지 않는다", "**Ask first only when two or more tasks fit**" in _r1 and "open nothing yet" in _r1 and "이 작업을 할까요? 아니면 할 일 목록에서 번호로 골라 주세요." in _r1)
for n, row in _task_rows.items():
    check(f"[할 일] {n}번 줄이 여는 스킬이 있다", any(f"`{s}`" in row for s in skill_dirs) or "OK card" in row, row[:80])

# 4. 스킬 안에서 가리키는 파일이 있는가 (같은 스킬 폴더, 또는 "`다른스킬` → `파일`"이면 그 스킬)
external = {"decisions.md", "asset-registry.md", "shot-list.md", "ok-cuts.md", "instructions.md", "SKILL.md"}
for name in external - {"instructions.md", "SKILL.md"}:
    check(f"[정본 틀] project-files/{name} 있음", os.path.exists(os.path.join(KIT, "project-files", name)))
for d in skill_dirs:
    for fn in skill_files[d]:
        if not fn.endswith(".md"):
            continue
        text = read(os.path.join(SKILLS, d, fn))
        cross = {}
        for other, ref in re.findall(r"`([a-z-]+)` (?:→|->) `([a-z0-9-]+\.md)`", text):
            cross[ref] = other
            check(f"[참조] {d}/{fn} → {other}/{ref}", ref in skill_files.get(other, []))
        for ref in set(re.findall(r"`([a-z0-9-]+\.(?:md|py))`", text)):
            if ref in external or ref in cross:
                continue
            check(f"[참조] {d}/{fn} → {ref}", ref in skill_files[d])
        for ref in set(re.findall(r"`context/([a-z0-9-]+\.md)`", text)):
            check(f"[참조] {d}/{fn} → context/{ref}", ref in CTX)
        # routing.md는 없어졌다. 이름만 남은 참조("routing §3")도 잡는다
        check(f"[참조] {d}/{fn}: 없어진 routing 참조 없음", not re.search(r"routing", text), ", ".join(re.findall(r".{0,30}routing.{0,10}", text)))
for f in CTX:
    check(f"[참조] context/{f}: 없어진 routing 참조 없음", "routing" not in read(os.path.join(KIT, "context", f)))
check("[참조] instructions.md: 없어진 routing 참조 없음", "routing" not in inst_core)

# 5. § 참조가 실제 절을 가리키는가
def headings(path):
    return set(re.findall(r"^## (\d+)\.", read(path), re.M))

for d in skill_dirs:
    for fn in skill_files[d]:
        if not fn.endswith(".md"):
            continue
        text = read(os.path.join(SKILLS, d, fn))
        spans = []
        for m in re.finditer(r"`([a-z-]+(?:\.md)?)`\s*((?:§\d+[·, ]*)+)", text):
            spans.append(m.span())
            other = m.group(1)
            for num in re.findall(r"§(\d+)", m.group(2)):
                if other in skill_dirs:
                    check(f"[§] {d}/{fn} → {other} §{num}", num in headings(os.path.join(SKILLS, other, "SKILL.md")))
                elif other.endswith(".md") and os.path.exists(os.path.join(KIT, "project-files", other)):
                    check(f"[§] {d}/{fn} → {other} §{num}", re.search(rf"^## §{num}\.", read(os.path.join(KIT, "project-files", other)), re.M) is not None)
        for m in re.finditer(r"`context/([a-z-]+\.md)`\s*§(\d+)", text):
            spans.append(m.span())
            check(f"[§] {d}/{fn} → context/{m.group(1)} §{m.group(2)}", m.group(2) in headings(os.path.join(KIT, "context", m.group(1))) if m.group(1) in CTX else False)
        for m in re.finditer(r"(?<![`\w])§(\d+)", text):
            if any(a <= m.start() < b for a, b in spans):
                continue
            num = m.group(1)
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

# 7. 상태 용어가 파일마다 같은가 (상태·폴더 이름은 정본 용어라 한국어)
gen = read(os.path.join(SKILLS, "higgsfield-generation", "SKILL.md"))
shot = read(os.path.join(KIT, "project-files", "shot-list.md"))
for word in ["대기", "진행", "검토", "승인", "보류"]:
    check(f"[용어] 컷 상태 '{word}': 생성 운영·컷 목록·핸드오프에 모두 있음", word in gen and word in shot and (word in handoff or word == "대기"))
for word in ["승인", "거절", "보류", "Superseded"]:  # 대체됨은 정본에 쓰이지 않아 영어로 옮김
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

# 9. 배포 파일에 특정 작품·사이트 표현이 없는가 (영어로 옮긴 뒤에는 영어 이름도 본다)
banned = re.compile(r"고등어|어머니|나부코|히브리|합창|Prompter|lucian|conti\.|콘티 사이트|신발장|식탁|봉지|아내|현관|우편|수양버들|헤롯|생선|1980|South Korea|E-\d{2}|error-registry")
banned_en = re.compile(r"\b(mackerel|nabucco|hebrew|herod|chorus|weeping willow|shoe cabinet|dining table|plastic bag)\b", re.I)
shipped = [os.path.join(KIT, "instructions.md")] + glob.glob(os.path.join(KIT, "context", "*.md")) + glob.glob(os.path.join(KIT, "project-files", "*.md")) + glob.glob(os.path.join(SKILLS, "*", "*"))
for p in shipped:
    hits = sorted(set(banned.findall(read(p))) | set(m.lower() for m in banned_en.findall(read(p))))
    check(f"[일반화] {os.path.relpath(p, ROOT)}에 작품 고유 표현 없음", not hits, ", ".join(hits))

# 10. 빈 틀: 15블록 순서, 빈칸이 잡히는가
live = read(os.path.join(SKILLS, "video-prompt", "live-action.md"))
tmpl = re.search(r"## Empty template.*?```text\n(.*?)```", live, re.S).group(1)
order = [tmpl.find(f"[{b}]") for b in ["SCENE_CONTEXT", "ACTIVE_REFERENCES", "LOCATION_MAP", "FIRST_FRAME_AND_SPATIAL_BLOCKING", "FORMAT_MODE", "OPTICS", "CAMERA", "ACTION_TIMING", "CHARACTER_ACTING", "PHYSICS", "LIGHTING", "AUDIO", "STYLE", "QUALITY", "REQUIRED_AND_FORBIDDEN_CONSTRAINTS"]]
check("[빈 틀] 15블록 틀에 블록이 모두 있고 순서대로", all(o >= 0 for o in order) and order == sorted(order))

# 12. 이미지 종류마다: 틀의 항목이 "Required information" 표에 있는가 (사용자에게 물을 칸이 빠지지 않게)
boiler = {"CENTER PANEL", "LEFT PANEL", "RIGHT PANEL", "CONSISTENCY RULES", "ENVIRONMENT", "REALISM", "STRUCTURE",
          "ONLY CHANGE", "PRESERVE EXACTLY", "CONTINUITY", "DO NOT TRANSFER", "PRIORITY", "REFERENCE AUTHORITY"}
img_skill = read(os.path.join(SKILLS, "image-prompt", "SKILL.md"))
for word in ["model", "resolution", "aspect ratio", "save folder", "image jobs to attach"]:
    check(f"[질문] image-prompt 공통 점검표에 '{word}'", word in img_skill.split("## 0.")[1].split("## 1.")[0])
INTAKE_HEAD = "## Required information"
for kind in ["character", "location", "prop", "style", "first-frame"]:
    t = read(os.path.join(SKILLS, "image-prompt", f"{kind}.md"))
    check(f"[질문] {kind}.md에 'Required information' 표(Template slot)", INTAKE_HEAD in t and "Template slot" in t)
    intake_i = t.split(INTAKE_HEAD)[1].split("\n## ")[0] if INTAKE_HEAD in t else ""
    labels = set()
    for x in re.findall(r"```text\n(.*?)```", t, re.S):
        labels |= set(re.findall(r"^-?\s*([A-Z][A-Z ]{2,}[A-Z])(?: —[^:\n]*)?:", x, re.M))
        labels |= set(re.findall(r"(?<![A-Z])([A-Z][a-z]+(?: [a-z]+)?):", x))
    for label in sorted(labels - boiler):
        check(f"[질문] {kind}.md 틀의 '{label}'을 채울 정보가 표에 있음", label in intake_i)
bg_intake = intake.split("background/landscape video (4 paragraphs)")[1]
for para in ["Camera", "Motion", "Keep", "Silent"]:
    check(f"[질문] 배경 영상 점검표가 '{para}' 문단을 덮음", f"`{para}`" in bg_intake)
for fn in ["rerender.md", "fixes.md"]:
    check(f"[질문] video-prompt/{fn}에 필요한 정보(Information needed)", "Information needed" in read(os.path.join(SKILLS, "video-prompt", fn)))
# must-ask가 가리키는 표 이름이 단계 파일의 실제 표 이름과 같은가
_ma_table = re.search(r"that skill's \"([^\"]+)\" table", ctx_ask)
check("[질문] must-ask가 가리키는 \"…\" 표 이름이 단계 파일 표 머리와 같음", bool(_ma_table) and all(_ma_table.group(1) in read(os.path.join(SKILLS, "image-prompt", f"{k}.md")) for k in ["character", "location", "prop", "style", "first-frame"]), _ma_table.group(1) if _ma_table else "")
check("[질문] 지침: 사용자가 말하지 않은 칸도 묻는다", "Ask everything missing in one go" in inst)
check("[질문] 지침: 같은 항목을 두 번 묻지 않고, 일부만 답하면 남은 것은 제안값으로", "Never ask the same item twice" in inst and "take the proposals for the rest" in inst)
for f, text in [("video-prompt", vskill), ("image-prompt", img_skill)]:
    check(f"[질문] {f}: 묻는 법은 지침 4번을 가리킨다", re.search(r"[Hh]ow to ask is (in )?instructions rule 4", text) is not None)

# 13. OK 기록과 재사용
okt = read(os.path.join(KIT, "project-files", "ok-cuts.md"))
for field in ["번호", "종류", "job", "모델", "참조(붙인 순서)", "OK 이유", "한계", "프롬프트(보낸 그대로)", "가져온 OK"]:
    check(f"[OK] OK 대장 틀에 '{field}'", field in okt)
check("[OK] 생성 운영: 승인하면 OK 기록", "OK record" in gen and "ok-cuts.md" in gen)
check("[OK] 생성 운영: 프롬프트는 보낸 그대로, 기억으로 다시 쓰지 않음", "Copy the prompt exactly as sent, character for character" in gen and "Never rewrite it from memory" in gen)
check("[OK] 지침: 승인은 그 자리에서 OK 대장에", "Record an approval (OK) in the OK ledger at once" in inst)
check("[OK] 지침: '3-1처럼'은 OK 카드에서 가져옴", "3-1처럼" in inst and "ok-reuse.md" in inst)
check("[OK] 컷 카드 [12]가 OK 대장을 가리킴", re.search(r"^\[12\].*OK 대장", card, re.M) is not None)
check("[OK] 컷 카드 [7]에 가져온 OK", "가져온 OK" in card)
reuse = read(os.path.join(SKILLS, "production-session", "ok-reuse.md"))
for word in ["모션", "색감", "표정", "카메라", "목소리", "number only"]:
    check(f"[OK] ok-reuse.md 표에 '{word}'", word in reuse)
check("[OK] 정본 Doc 탭에 OK 컷", "OK 컷" in read(os.path.join(SKILLS, "project-setup", "SKILL.md")))
for f in ["higgsfield-generation/SKILL.md", "production-session/cut-card.md", "production-session/handoff.md"]:
    check(f"[번호] {f}: 옛 번호 형식(C01, C##) 없음", not re.search(r"C\d\d|C##|C\[##\]", read(os.path.join(SKILLS, f))))
for f in ["shot-list.md", "asset-registry.md", "CLAUDE.md"]:
    check(f"[번호] project-files/{f}: 옛 번호 형식 없음", not re.search(r"C\d\d|C##", read(os.path.join(KIT, "project-files", f))))

# 14. 맹검 시험(tests/agent-eval)에서 찾은 결함이 다시 생기지 않는가
reg = read(os.path.join(KIT, "project-files", "asset-registry.md"))
sess = read(os.path.join(SKILLS, "production-session", "SKILL.md"))
_r3 = ctx_route.split("## 3.")[1]
CUT_LIST_FIELDS = r"status and confirmed[- ]job (cells|fields|columns)|status and `확정 job`|`상태` and `확정 job`|상태·확정 job"
check("[맹검] 컷 카드 수정 권한은 세션 스킬 §1 한 곳", "[3]~[7] [10]~[12]" in sess and "SKILL.md` §1" in card)
check("[맹검] 컷 목록: 컷 세션이 상태·확정 job 칸을 고친다(tasks §3이 주인, production-session §1은 가리킴)", re.search(CUT_LIST_FIELDS, _r3) is not None and "`context/tasks.md` §3" in sess and "production-session` §1" in shot)
check("[맹검] 지침: '몰라'도 제안값으로", "몰라" in inst)
nospeak = "does not say a single word: no attempt to speak, no parted lips, no mouthing"
for f in ["video-prompt/fixes.md", "video-prompt/live-action.md", "acting/SKILL.md"]:
    check(f"[맹검] 말하지 않음 문장 통일: {f}", nospeak in read(os.path.join(SKILLS, f)).replace("\n", " "))
check("[맹검] 렌즈 mm → 화각 환산표", "50mm=47°" in vskill and "the start image wins" in vskill)
check("[맹검] 가져온 OK의 위험도 옮긴다", "Bring the risks tied to the brought element too" in reuse and "위험 → 막는 문장" in okt)
check("[맹검] OK 대장 예시는 지우라고 표시", "예시" in okt and "지운다" in okt)
for word in ["PALETTE", "ERA LOCK", "이 뷰의 LIGHT LOCK", "초안(제안값)", "알려진 실패"]:
    check(f"[맹검] 에셋 대장 틀에 '{word}'", word in reg)
check("[맹검] 자리표시 태그 안내(image-prompt)", "are placeholders" in img_skill)
check("[맹검] \"다시 만들어\" 확인 규칙", "\"다시 만들어\" is that confirmation" in gen)
check("[맹검] 검토 상태 정의", "`검토`: a finished result" in gen)

# 15. 2차·소넷 맹검에서 찾은 결함
chk = read(CHECKER)
check("[맹검2] 길이 경계 5,500자(검사기·실사 틀)", "> 5500" in chk and "5,500 characters" in live)
check("[맹검2] OK 카드와 컷 카드 구분(OK 카드는 ok-cuts.md 안의 절)", re.search(r"section (inside|in|of) `ok-cuts\.md`", inst) is not None and "An OK card is a section inside `ok-cuts.md`" in reuse)
check("[맹검2] 다른 컷 카드·핸드오프를 예시로도 열지 않음(읽기 지도)", "**Never open another cut's card or handoff**, not even with `head`/`grep` to see the format" in inst)
check("[맹검2] 결과 이미지를 볼 수 없을 때 규칙", "cannot see the result" in inst and "do not ask the user to describe it" in inst)
check("[맹검2] 거절하면 진행으로", "If rejected, revert to `진행` on the spot" in gen)
check("[맹검2] OK 제안 전에 카드 열기", "**before proposing**" in reuse)
check("[맹검2] 정정 줄이 보냄 형식보다 먼저", "`정정: …`" in gen)
check("[맹검2] 이웃 컷은 연속성 표에서", "Take the previous cut's end state from the continuity table" in vskill and "its own continuity row" in inst)

# 16. 규칙은 한 곳에만 (같은 규칙이 두 파일에 다르게 적히면 충돌이 생긴다)
#     (이름, 그 규칙을 알아보는 정규식, 그 규칙을 적어도 되는 파일)
docs = {"instructions.md": inst}
for p in glob.glob(os.path.join(KIT, "project-files", "*.md")):
    docs["project-files/" + os.path.basename(p)] = read(p)
for p in glob.glob(os.path.join(SKILLS, "*", "*.md")):
    docs[os.path.relpath(p, SKILLS)] = read(p)
owners = [
    ("묻는 법: '몰라·알아서'면 제안값", r"몰라|알아서", {"instructions.md"}),
    ("묻는 법: 일부만 답하면 남은 것은 제안값으로", r"take the proposals for the rest", {"instructions.md"}),
    ("묻는 법: 추측하지 않는다", r"do not guess(?! and rewrite)", {"instructions.md"}),
    ("묻는 법: 말하지 않은 값에 (제안값)", r"[Vv]alues the user did not state", {"instructions.md"}),
    ("찾는 순서(사용자 말 → 컷 카드 …)", r"user's words → cut card", {"instructions.md"}),
    ("이미지를 볼 수 없을 때", r"cannot see the result", {"instructions.md"}),
    ("읽는 범위: 다른 컷 카드를 열지 않는다", r"another cut's card|other cut cards|neighbou?ring cut cards|format examples?", {"instructions.md", "production-session/cut-card.md", "production-session/SKILL.md"}),  # 카드를 쓰는 그 자리에도 한 줄(맹검 r3: 형식 보려고 다른 카드를 엶)
    ("acting을 여는 때", r"open `acting` only on the turn that writes the prompt", {"instructions.md"}),
    ("방향은 화면 기준(손 포함)", r"Every direction is a screen", {"instructions.md"}),
    ("반복 실패 한도", r"3 of the last 4", {"instructions.md"}),
    ("고정 설명문은 글자 그대로", r"[Cc]opy fixed descriptions", {"instructions.md"}),
    ("컷 카드 칸별 수정 권한", r"\[3\]~\[7\]", {"production-session/SKILL.md"}),
    ("컷 목록: 컷 세션이 고치는 칸", CUT_LIST_FIELDS, {"instructions.md"}),  # 실제8 C48: 항상 읽히는 tasks §3(옛 routing §3)
    ("확정 전 에셋 답은 초안 줄에", r"[Aa]nswers before confirmation", {"production-session/SKILL.md"}),
    ("범위 밖 문제는 총괄에 올린다", r"총괄에 올릴", {"production-session/SKILL.md", "production-session/handoff.md"}),
    ("Forbidden에 넣는 것", r"Put in Forbidden[^\n]{0,30}only failures", {"video-prompt/SKILL.md"}),
    ("렌즈 환산표", r"24mm=84°", {"video-prompt/SKILL.md"}),
    ("모호한 말 → 값·문장(속도·별·사람 동작·걸음)", r"taking the full \[N\] seconds|after 2 failures add it as a post|\[centre of weight\]|travel \(% of frame\)", {"video-prompt/SKILL.md"}),
    ("OK 프롬프트 찾는 순서", r"`get_project_asset_prompt` \(that job\)|result detail on the Higgsfield web", {"higgsfield-generation/SKILL.md"}),
    ("판정 말과 상태(좋아·별로·나중에)", r"\"별로\"|\"나중에\"", {"higgsfield-generation/SKILL.md"}),
    ("가져온 OK의 위험을 옮긴다", r"Bring the risks tied to the brought element", {"production-session/ok-reuse.md"}),
    ("검사 절차: 임시 파일은 tmp/, 끝나면 지운다", r"Delete the `tmp/` files|delete (it|them) after the check", {"instructions.md"}),
    ("검사 절차: 단독 Bash 호출, WARN은 숫자와 함께", r"single standalone Bash call|give the reason with a number", {"instructions.md"}),
]
for name, pat, allowed in owners:
    where = sorted(f for f, t in docs.items() if re.search(pat, t))
    extra = [f for f in where if f not in allowed]
    check(f"[한 곳] {name}: {', '.join(sorted(allowed))}에만", not extra and where, "다른 곳: " + ", ".join(extra) if extra else "주인 파일에 없음")
# 같은 상황에 다른 문장을 주지 않는다
turn_fix = re.search(r".*whips around \|.*", read(os.path.join(SKILLS, "video-prompt", "fixes.md"))).group(0)
turn_act = re.search(r".*whips around \|.*", read(os.path.join(SKILLS, "acting", "SKILL.md"))).group(0)
check("[한 곳] 휙 도는 동작: 고치기와 연기가 다른 증상을 다룬다(고개·상체 / 몸 전체)", "Head/upper body" in turn_fix and "whole body" in turn_act, turn_fix + " / " + turn_act)

# 18. r4 맹검에서 찾은 결함
def sk(f):
    return read(os.path.join(SKILLS, f))
ff = sk("image-prompt/first-frame.md")
fixes = sk("video-prompt/fixes.md")
ff_t2 = ff.split("## Template 2")[1]
check("[맹검4] 지침 2번: 아직 보지 못한 프롬프트에는 어떤 말도 생성 지시가 아님", "Nothing is a generation order for a prompt the user has not seen" in inst and "count only right after you asked whether to send" in inst)
check("[맹검4] 지침 6번: 인물 기준이면 향한 쪽으로 화면 쪽, 추정", "convert it from the way the character faces" in inst and "추정" in inst)
check("[맹검4] 지침 4번: 기본값 목록에 소리", "aspect, sound, save folder" in inst)
check("[맹검4] 지침 5번: 대장과 OK 줄이 다르면 대장", "If they differ, the registry wins" in inst)
check("[맹검4] 할 일 목록: fixes.md는 결과가 틀렸을 때", "영상 결과 고치기" in inst)
_spd_line = vskill.split("taking the full [N] seconds")[1].split("\n")[0] if "taking the full [N] seconds" in vskill else ""
check("[맹검4] 사람 동작 속도 줄(video-prompt 모호한 말 표)", "taking the full [N] seconds" in vskill and "as a proposal (제안값)" in _spd_line)
check("[맹검4] fixes.md: 승인 컷이면 새 테이크 대체를 먼저 묻는다", "first ask whether to replace it with a new take" in fixes)
check("[맹검4] 별 줄: 생성 전에 한계, 2회 실패면 오버레이", "Before generating, say the model does not hold these well" in vskill and "after 2 failures add it as a post-production overlay" in vskill)
check("[맹검4] video-prompt: fixes.md는 결과가 틀렸을 때, acting 먼저", "Open `fixes.md` only when the result came out wrong" in vskill and "open `acting` first" in vskill)
check("[맹검4] background.md: SKILL §0 배경 표(Keep 포함)", "the background table in `SKILL.md` §0" in sk("video-prompt/background.md") and "`Keep`" in sk("video-prompt/background.md"))
check("[맹검4] live-action: 덜어내는 순서와 WARN을 남기는 조건", "location -> style -> environment" in live and "leave a WARN" in live)
check("[맹검4] acting: 목표 양식 예, 사건 수·비트 수 따로", "[상대]에게/에게서 + 동사" in sk("acting/SKILL.md") and "beat count" in sk("acting/SKILL.md"))
check("[맹검4] ok-reuse: 강한 입 잠금 문장 인라인", nospeak in reuse)
check("[맹검4] ok-reuse: '카드처럼'은 형식", "\"3-1 카드처럼 써\" is about format" in reuse)
check("[맹검4] 생성 운영: 크레딧 근거, 재생성이면 '바꾼 것'", "attach the basis (cost memo / get_cost)" in gen and "- 바꾼 것:" in gen)
check("[맹검4] OK 대장 카드에 draft·만료일", "draft_job_id" in okt and "만료일" in okt)
check("[맹검4] 컷 카드 [10]은 난 실패", card_fields.get("10", "").startswith("난 실패"))
check("[맹검4] 컷 목록 생성/크레딧 칸의 주인", "The lead edits the `생성/크레딧` field" in sess)
check("[맹검4] 새 컷이어도 이웃 컷 파일은 열지 않음", "Even for a new cut, do not open neighboring cut cards" in sess and "one OK card of the most recent approved start image" in ff)
check("[맹검4] first-frame: 장소 뷰 칸이 비면 모드를 첫 질문으로", "is blank, ask it as the first question" in ff)
check("[맹검4] first-frame: 반대쪽 카메라면 좌우 뒤집기, 틀 2에 In this view 줄", "screen left/right flip" in ff and "In this view [landmark]" in ff_t2)
check("[맹검4] first-frame·location: 틀 2를 바로 쓰는 조건", "If only this cut uses that viewpoint, write Template 2 directly" in ff and "if that axis is used in only one cut, first-frame Template 2" in sk("image-prompt/location.md"))
check("[맹검4] first-frame: 나이만 바꾸는 컷은 character-edit 틀 2", "`character-edit.md` Template 2" in ff)
check("[맹검4] image-prompt §3 LOCKED EDIT 틀에 WARDROBE 줄", "WARDROBE: [asset registry sentence, verbatim]" in img_skill.split("## 3.")[1].split("## 4.")[0])
check("[맹검4] location-view: 높이는 값으로", "Write height as a value" in sk("image-prompt/location-view.md"))
check("[맹검4] prop.md: 확정 소품 고치기와 어느 결과인가", "Editing a confirmed prop" in sk("image-prompt/prop.md") and "_v2" in sk("image-prompt/prop.md") and "which result is meant" in sk("image-prompt/prop.md"))

# 19. r5 맹검에서 찾은 결함
VAGUE_HEAD = "**Vague phrases -> values/sentences**"
vague = vskill.split(VAGUE_HEAD)[1].split("How to ask is instructions rule 4")[0] if VAGUE_HEAD in vskill else ""
for word in ["Speed (", "Add motion", "Small repeating elements", "Speed of a person's action", "Age of the walk", "Several actions"]:
    check(f"[맹검5] video-prompt §0 모호한 말 표에 '{word}'", word in vague)
check("[맹검5] 모호한 말 표: 움직임 추가면 사건이 늘었다고 알림", "\"one more event was added\"" in vague)
check("[맹검5] 모호한 말 표: 걸음 나이(보폭·팔·발·무게중심, 반대 걸음 = failed take)", all(w in vague for w in ["[step size]", "[arm swing]", "[feet lifted or dragged]", "[centre of weight]", "walk = failed take"]))
check("[맹검5] fixes.md: 모호한 말 줄은 옮기고 SKILL 표를 가리킴", "§0 \"vague phrases\" table" in fixes and not re.search(r"구름|풀도 흔들|별이 더 반짝|taking the full|Halve/double", fixes))
check("[맹검5] tasks §1: 모호한 말은 스킬 자기 표로 값을 제안(영상 고치기 줄은 §0 표)", "Propose concrete values from the skill's own tables and ask" in inst and "§0 only for speed·stars·gait" in inst)  # 옛 routing §2 표는 일부러 뺌
check("[맹검5] 지침: 시작 보고 세 줄은 프롬프트·생성·정본 작업일 때만, 정보·정리 질문은 생략 가능", "only for prompt, generation or canon work" in inst and "skip it for information questions" in inst)
check("[맹검5] 지침: 컷 번호도 job도 없을 때만 묻고 컷 파일을 열지 않음", "Ask only when there is neither cut number nor job, and then open no cut files" in inst)
check("[맹검5] 할 일 목록: OK 재표시·번역은 그 카드 하나, 검사 안 함, 번역은 코드블록 밖", "다시 보기·번역" in inst and "(no check)" in inst and "never in a code block" in inst)
check("[맹검5] 할 일 목록: 시트 자체 고치기만 character-edit, 퍼스트 프레임 속 인물은 first-frame", "on the sheet itself" in _task_rows.get(5, "") and re.search(r"person|character|인물", _task_rows.get(11, "")) is not None, _task_rows.get(11, ""))
check("[맹검5] 할 일 목록: 프롬프트만 쓰면 higgsfield-generation 안 엶, 크레딧 질문", "(prompt already shown)" in _task_rows.get(18, "") and "크레딧" in inst)
check("[맹검5] 할 일 목록: SKILL.md 먼저", "Open the SKILL.md first" in inst)
check("[맹검5] video-prompt: 사건은 묶어 세지 않고 샷별 사건 목록 먼저", "Do not count them in groups" in vskill and "per-shot event list" in vskill and "do not merge" in vskill)
check("[맹검5] video-prompt: 나가기 = 마지막 프레임에 몸 절반이 프레임 밖", "half the body is outside the frame" in vskill)
check("[맹검5] video-prompt: 렌즈 표에 없는 mm는 두 값 사이", "interpolate between the two nearest" in vskill)
check("[맹검5] 소리 칸이 비면 대사 유무, 문 경첩 쪽(둘 다 video-prompt §0 점검표로 옮김)", "if cut card [3] sound is empty, ask whether there is dialogue" in intake and "hinge side" in intake)
bg = sk("video-prompt/background.md")
check("[맹검5] background: 정본 기본값은 묻지 않음, Keep은 제안값, 매체가 다르면 시작 이미지부터", "Do not ask for camera/length/sound canon values" in bg and "Show `Keep` as a proposal (제안값) even if the user did not mention it" in bg and "Propose making the start image anew" in bg)
check("[맹검5] ok-reuse: 가져온 줄은 쪼개지 않고 새 문장, 전체를 --must-include", "do not split that line or insert into the middle" in reuse and "do not join with `;` or `,`" in reuse and "Put the whole brought line in the `--must-include` file" in reuse)
check("[맹검5] live-action: WARN 이유에 줄여 본 항목과 글자 수", "write what you tried to trim and the characters cut" in live)
check("[맹검5] production-session: [1]이 비거나 다른 방향이면 제안값으로 고치고 확인", "a direction different from [1]" in sess and "edit it that turn as `(제안값)`" in sess)
check("[맹검5] production-session: 생성/크레딧 칸에 '이미지 N / 영상 N · 약 N 크레딧'", "`이미지 N / 영상 N · 약 N 크레딧`" in sess)
check("[맹검5] 컷 카드 [7]: [1]에 다른 컷과 같게가 있으면 그 OK", "[1]에 \"3-1과 같게\"" in card)
check("[맹검5] first-frame 틀 2: 반대편이면 필수 표시, 하늘·색은 PALETTE·LIGHT LOCK", "반대편 카메라면 필수" in ff_t2 and "conflicts with the asset registry's PALETTE·LIGHT LOCK" in ff)
prop = sk("image-prompt/prop.md")
check("[맹검5] prop.md: 시트가 필요한가, 차량·건물급은 장면 프레임에서", "Is a sheet needed?" in prop and "For vehicle/building class" in prop)
check("[맹검5] 생성 운영: 크레딧 질문은 기록만 합치고 추정은 근거를 밝힘", "크레딧 얼마나 썼어" in gen and "write `알 수 없음` instead of a number" in gen)
check("[맹검5] decisions 틀에 비용 메모 줄", "비용 메모" in read(os.path.join(KIT, "project-files", "decisions.md")))

# 20. 실제 Claude Code 실행(real-C01~C52) 채점에서 찾은 결함
import json
ALLOW_CMD = "python3 .claude/skills/higgsfield-generation/check_prompt.py"
sj_path = os.path.join(KIT, "project-files", "settings.json")
try:
    sj = json.load(open(sj_path, encoding="utf-8"))
except Exception:
    sj = {}
ASM_CMD = "python3 .claude/skills/assembly/assemble.py"
COLOR_CMD = "python3 .claude/skills/color-continuity/color.py"
check("[실행] project-files/settings.json: 검사기·조립·색 스크립트와 tmp/ 지우기만 허용", sj == {"permissions": {"allow": [f"Bash({ALLOW_CMD}:*)", f"Bash({ASM_CMD}:*)", f"Bash({COLOR_CMD}:*)", "Bash(rm tmp/*)"]}}, str(sj))
check("[실행] README 설치에 settings.json 복사", "cp kit/project-files/settings.json .claude/settings.json" in read(os.path.join(ROOT, "README.md")))
check("[실행] make_run.sh가 settings.json을 복사", '"$RUN/.claude/settings.json"' in read(os.path.join(ROOT, "tests", "agent-eval", "make_run.sh")))
check("[실행] real_run.py --allowedTools 검사기", f'"--allowedTools", "Bash({ALLOW_CMD}:*)"' in read(os.path.join(ROOT, "tests", "agent-eval", "real_run.py")))
check("[실행] 지침 \"검사\" 이미지 명령이 허용 패턴과 같은 글자", f"`{ALLOW_CMD} --kind image tmp/파일" in inst_core)
check("[실행] 지침 \"검사\" 영상 명령이 허용 패턴과 같은 글자", f"`{ALLOW_CMD} --kind video tmp/파일" in inst_core)
check("[실행] 검사기: --refs ≥1인데 <<< 태그 0개면 WARN", "태그가 없다" in chk and os.path.exists(os.path.join(FIX, "image__fail__N12_refs_without_tags.txt")))
check("[실행] 검사기: hand nearer/closer에 화면 쪽이 없으면 WARN", "화면 쪽이 없다" in chk and os.path.exists(os.path.join(FIX, "video__fail__N13_hand_without_screen_side.txt")))
check("[실행] 지침 4번: job처럼 제안값 없는 항목에 '그대로'면 에셋 자체", "\"그대로\" on an item with no proposal (e.g. a job)" in inst_core)
check("[실행] 지침 4번: 다시 묻는 두 경우(직접 말한 값끼리 / 정본·OK·시작 이미지와 다름)", "Ask again only when the user's own values conflict" in inst_core and "differs from canon/OK/start image (once)" in inst_core)
check("[실행] 컷 카드 [1]이 다른 컷과 같은 동작이면 그 OK(cut-card [7])", "[1]에 \"3-1과 같게\"처럼 다른 컷이 있으면 그 OK" in card)  # tasks 16번 줄은 사용자 말만 적는다. 카드 쪽 규칙은 cut-card.md [7]
check("[실행] 할 일 목록: 폴더를 실제로 만드는 턴에만 생성 운영 §2, 질문 턴 구성안은 must-ask", "open its §2 folder part only on the turn that creates folders" in _task_rows.get(20, ""))
check("[실행] 할 일 목록: 소품 지적·고치기 → prop.md", "소품 만들기·고치기" in _task_rows.get(9, "") and "너무 새 거 같아" in _task_rows.get(9, "") and "`prop.md`" in _task_rows.get(9, ""))
check("[실행] 할 일 목록: 컷의 '뒤에서 본' 첫 프레임 → first-frame", re.search(r"뒤에서 본[^|]*첫 프레임|첫 프레임[^|]*뒤에서", _task_rows.get(11, "")) is not None, _task_rows.get(11, ""))
check("[실행] 할 일 목록: 영상이면 acting은 프롬프트 쓰는 턴에", "open `acting` only on the turn that writes the prompt" in _task_rows.get(13, ""))
check("[실행] 할 일 목록: 영상 요청이면 video-prompt §0·§2", "open `video-prompt` SKILL.md (§0, §2)" in _r3)
check("[실행] 할 일 목록: 그 컷 번호의 핸드오프만, 이웃 OK 카드는 기준이 아니면 안 엶", "its last handoff" in _r3 and "Do not open neighbour OK cards unless one is the reference" in _r3)
check("[실행] production-session §2: 총괄 시작도 칸이 채워진 컷의 핸드오프는 열지 않음", "Do not open the handoff of a cut whose `생성/크레딧` field is already filled" in sess)  # 옛 routing §3에서 세션 스킬로 옮김
check("[실행] must-ask: '이걸로'인데 이미지 없으면 그것만", "ask for that image only" in ctx_ask)
check("[실행] must-ask: 컷 폴더 없으면 구성안과 누가 만들지", "제가 만들까요, 직접 만드시겠어요?" in ctx_ask and "`3-6 [대기]`" in ctx_ask)
check("[실행] must-ask 실사 영상: 시작 이미지 없으면 영상 질문 보류", "hold video questions" in ctx_ask)
check("[실행] must-ask 실사 영상: 새 장소면 장소 마스터 항목을 함께", "ask the location-master items in the same batch" in ctx_ask)
check("[실행] must-ask 실사 영상: 이웃 컷 OK 연기와 반대면 짚기", "opposite to a neighbour cut's acting" in ctx_ask)
check("[실행] production-session: 그 컷 번호의 핸드오프", "If that cut number has a last handoff" in sess)
check("[실행] cut-card: 다른 컷 카드를 형식 예시로 열지 않음", "Do not open other cut cards as format examples" in card)
check("[실행] 생성 운영 크레딧: 컷 목록 칸, 핸드오프는 빈 칸만", "answer from the cut list 생성/크레딧 cell" in gen and "opens only cuts whose cell is empty" in gen)
ps = sk("project-setup/SKILL.md")
check("[실행] project-setup: 11번 동의가 승인, 다시 묻지 않음", "agreeing to the §1 item 11 default is itself the approval" in ps and not re.search(r"after (getting |receiving )?(the )?approval", ps))
check("[실행] project-setup: .claude/ 수정 거절이면 바꿀 줄을 보임", "If the edit is rejected" in ps)
check("[실행] first-frame: 틀 2 고유 문장은 OK 카드에 없어도", "go in even when rewriting an OK card that lacks them" in ff)
check("[실행] first-frame: 벽에 등을 대면 뒤는 벽 밖 → 어깨 너머", "what is behind is outside the wall" in ff and "over the character's shoulder" in ff)
check("[실행] live-action: 줄여도 되는 줄과 WARN 이유 예", "starting with removing authority explanations in `ACTIVE_REFERENCES`" in live and "5,788자 유지:" in live)
check("[실행] background: 소리는 정본 소리 줄대로, 묻지 않음", "cut without dialogue = sound effects only" in bg)
check("[실행] video-prompt 속도 줄: 전 → 후", "Show that line as \"전 → 후\"" in vague)
check("[실행] prop.md: 시트 없으면 카드 [5]에 문장만, 등록은 대장 초안만", "write that sentence only on the `[5] 소품` line of the cut card" in prop and "Do not output a code block" in prop and "write only the asset registry `초안` line" in prop)
loc_edit = sk("image-prompt/location-edit.md")
check("[실행] location-edit 틀 2: LOCKED EDIT 여는 문장 전문(<<<image_1>>>)", "Edit <<<image_1>>> WITHOUT reframing" in loc_edit.split("## Template 2")[1].split("## Template 3")[0])
check("[실행] location-edit: 표지판 판 = IDENTITY AND TEXT, 기둥 = FIXTURES", "the sign board in `IDENTITY AND TEXT`, its pole in `FIXTURES`" in loc_edit)
check("[실행] location-edit: 나누면 1단계는 요청한 상태가 아님을 알림", "is not yet the requested state" in loc_edit)
loc_view = sk("image-prompt/location-view.md")
check("[실행] location-view: 카메라가 구조물 안이면 Except 한 줄", "`Except: [only what is visible in this view].`" in loc_view)
check("[실행] location-view: LIGHT LOCK 뒤에 덧붙이지 않음", "End the LIGHT LOCK line exactly as written" in loc_view)
ce = sk("image-prompt/character-edit.md")
check("[실행] character-edit 틀 1: GONE·No trace·no 목록이 [old 1]~[old 3] 세 자리", ce.count("[old 1], [old 2], [old 3]") >= 2 and ce.count("no [old 1], no [old 2], no [old 3]") >= 3)

# 21. 실제 실행 2회차 채점 결함
out_sec = inst_core.split("## Output")[1]
rule3 = [l for l in inst_core.splitlines() if l.startswith("3. ")][0]
check("[실행2] 지침 출력: 고치면 전 → 후만, 새로 쓰면 전문, 편집 프롬프트는 둘 다", "**Editing a confirmed prompt:**" in out_sec and "A rewrite is a new prompt" in out_sec and "Edit prompts (LOCKED EDIT, age edit)" in out_sec)
check("[실행2] 지침 출력: 블록 밖 줄은 코드블록에 넣지 않음", "Outside the block, one plain line each" in out_sec)
check("[실행2] 지침 3번은 보이는 법을 적지 않는다(출력에만)", "전 → 후" not in rule3 and "full text" not in rule3, rule3)  # 옛 "보이는 법은 출력" 포인터 대신: 3번에 보이는 법이 없으면 충돌도 없다
check("[실행2] 지침 6번: 옆모습도 화면 쪽 + 물건, nearer the camera만은 안 됨", "`the screen-left hand, farther from the sign`" in inst_core and "Never a hand without a screen side (`nearer the camera`, `road-side hand`)" in inst_core)
check("[실행2] live-action 맨 위: 질문 턴에는 acting을 열지 않음", "Do not open `acting` in a question turn" in live.split("## Blocks")[0])
check("[실행2] 생성 운영 §6: 비용 메모가 비면 get_cost 없이 채우지 않음", "If the cost memo is empty, say there is no unit price" in gen.split("## 6.")[1])
check("[실행2] 할 일 목록: OK 재표시는 생성용 영어 원문 그대로", "English original as is" in _task_rows.get(23, ""))
check("[실행2] 할 일 목록: 속도·별·걸음은 video-prompt §0 표, fixes.md는 그 밖", "§0 only for speed·stars·gait; `fixes.md` only for other symptoms" in _task_rows.get(15, ""))
check("[실행2] 시트 고치기에 character.md는 안 엶(character-edit.md 머리로 옮김)", "`image-prompt` → `character-edit.md`" in _task_rows.get(5, "") and "Open only this file for editing (`character.md` is for new sheets)" in ce)
check("[실행2] location.md 틀 아래: 블록 밖 줄은 지침 출력대로(모드 신규)", "Write the lines outside the block as in instructions \"Output\"" in sk("image-prompt/location.md") and "`모드: 신규`" in sk("image-prompt/location.md"))
check("[실행2] 생성 운영 §2: 폴더 묻는 문장은 must-ask 한 곳", "제가 만들까요" not in gen and "제가 만들까요" in ctx_ask)
check("[실행2] image-prompt 검사 명령: 단독 Bash 호출(cd·&&·파이프·절대경로 없이)", "as a single standalone Bash call (no `cd`, `&&`, pipes or absolute paths)" in inst)
check("[실행2] must-ask 장소 수정: 나누면 앞세운 변경 먼저", "(do the one the user said first)" in ctx_ask and "the change the user named first" in loc_edit)
check("[실행2] image-prompt 태그: 꺾쇠는 두고 이름만, 여는 줄 예", "Keep the angle brackets and replace only the name inside" in img_skill and "`Edit <<<loc_…_v1>>> WITHOUT reframing`" in img_skill)
check("[실행2] location-view: 부모 카메라가 대상 밖 + 안에서 보면 먼 끝으로 이동", "if the parent camera is outside the subject and the user says to look \"안에서\" (from inside), move to the far end" in loc_view)
check("[실행2] first-frame 표: 보이는 인원 수(must-ask에서 단계 파일 표로 옮김)", "Number of visible people" in ff.split(INTAKE_HEAD)[1].split("\n## ")[0])
check("[실행2] must-ask 실사 영상: 시작 이미지 없을 때 허용 범위", "allowed now: count events, split shots, propose the end state" in ctx_ask and "hold video questions" in ctx_ask)
check("[실행2] location-edit: 새 LIGHT LOCK에 광원의 화면 쪽, 모르면 묻기", "A new LIGHT LOCK proposal uses the light source's screen side + object; if the position is unknown, ask." in loc_edit)
check("[실행2] first-frame 틀 1: PROP 크기는 CHANGE를 가리킴", "its size is as described in CHANGE above." in ff and "its size is as described above." not in ff)
check("[실행2] 검사기: 손을 nearer the camera로만 쓰면 WARN", "손을 카메라 쪽으로만 썼다" in chk and os.path.exists(os.path.join(FIX, "image__fail__N14_hand_nearer_camera_only.txt")))
rr = read(os.path.join(ROOT, "tests", "agent-eval", "real_run.py"))
check("[실행2] real_run.py: 메타에 Bash 명령 문자열(bash)", '"bash": bash' in rr and 'bash.append(i.get("command", ""))' in rr)

# 22. 실제 실행 3회차 채점 결함
check("[실행3] must-ask 폴더 질문에 제안값(제가 만든다)", "직접 만드시겠어요?\" (proposal: I make it)" in ctx_ask)
check("[실행3] prop.md: 크기는 수치(차량급은 m + 사람), 수락 뒤 카드 줄만 인용·코드블록 없음", "size (numerically: cm; for vehicle class, m + person reference)" in prop and "quote only that card line in the reply. Do not output a code block" in prop)
cred = gen.split("## 6.")[1]
check("[실행3] 생성 운영 §6: '얼마나 썼어'는 기록 칸·알 수 없음만, 추정은 원할 때 get_cost 부른 뒤", "Answer only recorded cells and `알 수 없음`" in cred and "only when the user wants them, after actually calling `get_cost`" in cred and not re.search(r"(calculate|multiply|compute)[^.\n]*unit price", cred))
check("[실행3] production-session §3: 다음 할 일이 확인이면 확인과 빈 칸 제안값을 한 번에", "If that step is a user confirmation, ask that confirmation together with the proposed values for the card's empty fields, in one go" in sess)
start2 = inst_core.split("## Starting a conversation")[1].split("\n3.")[0]
check("[실행3] 지침 시작 2번: 컷 번호면 컷 목록 확정 job 먼저(팀원 작업이면 get_project_asset_prompt)", "use the confirmed job on that `shot-list.md` row first" in start2 and "get_project_asset_prompt" in start2 and not re.search(r"job is not in the conversation", start2))
check("[실행3] must-ask: job 질문은 컷 번호도 job도 없을 때", "neither cut number nor job" in inst_core and "Which job (if neither cut nor job is given)" in ctx_ask)
check("[실행3] 할 일 목록: 카드에 답을 적을 때 cut-card.md, 새 카드도 그 틀 복사", "(+ `cut-card.md` / `handoff.md` only when writing them)" in _task_rows.get(2, "") and "using the `cut-card.md` template" in sess)
ex = card.split("Example of filled fields")[1] if "Example of filled fields" in card else ""
check("[실행3] cut-card: 가상의 값으로 채운 예(칸 번호 형식)", "made-up values" in ex and len(re.findall(r"^\[\d+\] ", ex, re.M)) >= 4 and len(card) <= 2000, f"{len(card)}자")
check("[실행3] cut-card 예의 손도 화면 쪽", "the screen-left hand" in ex)
check("[실행3] character-edit 틀 2: 젊게 할 때 표지와 no beauty filter", "When making younger" in ce and "no beauty filter" in ce.split("## Template 2")[1])
check("[실행3] scenarios C10 2턴: 망원이 시작 이미지와 달라 한 번 묻기도 PASS", "한 번 묻는 것도 PASS" in read(os.path.join(ROOT, "tests", "agent-eval", "scenarios.md")).split("## C10")[1].split("## C11")[0])
check("[실행3] 검사기: 단수 hand 앞에 화면 쪽이 없으면 WARN(합성어·복수 제외)", "(?<![-\\w])hand(?![-\\w])" in chk and os.path.exists(os.path.join(FIX, "image__fail__N15_side_hand_without_screen_side.txt")))
for lp in sorted(glob.glob(os.path.join(FIX, "*.lines")) + glob.glob(os.path.join(ROOT, "tests", "agent-eval", "testbed", "grade", "*.lines")) + [os.path.join(ROOT, "tests", "agent-eval", "testbed", "project", "ok-cuts.md")]):
    r = subprocess.run([sys.executable, CHECKER, "--kind", "image", lp], capture_output=True, text=True)
    check(f"[실행3] 손 규칙에 걸리지 않음: {os.path.relpath(lp, ROOT)}", "화면 쪽이 없다" not in r.stdout and "카메라 쪽으로만" not in r.stdout, r.stdout.strip()[:200])

# 22b. 실제 4회차 결함
first_b = [l for l in _r3.splitlines() if l.startswith("- ")][0]
check("[실행4] tasks §3 첫 줄: 다른 컷 카드·핸드오프 금지(굵게, head·grep으로도, 칸 형식은 cut-card.md로만)", first_b.startswith("- **Never open another cut's card or handoff**") and "`head`/`grep`" in first_b and "comes only from `cut-card.md`" in first_b)
check("[실행4] tasks §3: 컷 세션은 자기 컷 번호의 핸드오프만", "A cut session opens only its own cut's handoff" in first_b and "Do not open other cards" not in _r3)  # 옛 판은 굵게였다. 영어 판은 굵게가 없다
check("[실행4] 할 일 목록 영상 줄: 질문 턴에는 acting을 열지 않는다", "open `acting` only on the turn that writes the prompt" in _task_rows.get(13, ""))
check("[실행4] video §0 모호한 말 표 머리: 전 → 후만 보여도 전문 저장·검사", "If only \"before -> after\" is shown, save the fixed full prompt and run the check on it" in vskill)
star = [l for l in vskill.splitlines() if l.startswith("| Small repeating elements")][0]
check("[실행4] video 별 줄: 시작 이미지에 없으면 시도하지 않고 오버레이·새 시작 이미지", "If it is not in the start image, do not try; use a post overlay or a new start image" in star)
speed = [l for l in vskill.splitlines() if l.startswith("| Speed of a person's action")][0]
check("[실행4] video 속도 줄: 후 구간이 더 길다, 구간이 이미 전체면 앞당기기·길이 늘리기 제안", "The new interval must be longer" in speed and "whether to start earlier or lengthen the video" in speed)
check("[실행4] must-ask 모든 작업: 정본과 다르면 범위(이 컷만/작품 전체)", "this cut only, or the whole work?" in ctx_ask.split("## All tasks")[1].split("\n## ")[0])
check("[실행4] first-frame: 다른 OK 색감이면 질감 문장(Real material truth)을 새로 쓰지 않음", "Do not write new texture sentences (`Real material truth` etc.)" in ff)
check("[실행4] 지침 10번: 견적·크레딧 숫자는 근거가 있을 때만, 생성 운영은 추정 숫자 없음", "Credit numbers only with a basis (cost memo, `get_cost`)" in inst_core and not re.search(r"`추정`[^.\n]*(what|how) (you|it was) (calculated|computed)", gen))
t2 = ce.split("## Template 2")[1].split("```")[1]
_t2_old = [l for l in t2.splitlines() if l.startswith("ONLY CHANGE") and "old-age makeup" in l]
_t2_young = [l for l in t2.splitlines() if l.startswith("ONLY CHANGE") and "no beauty filter" in l]
check("[실행4·실제7] character-edit 틀 2 끝 줄: 늙게·젊게 두 줄로 따로(한 줄에 둘이 섞이지 않음)", "[늙게]\nONLY CHANGE" in t2 and "[젊게]\nONLY CHANGE" in t2 and len(_t2_old) == 1 and len(_t2_young) == 1 and "beauty filter" not in _t2_old[0] and "old-age" not in _t2_young[0] and "젊게면 이 구절" not in t2)
check("[실행4] 지침 4번: 짚은 충돌에 방향만 답하면 더 작은 변경안으로 프롬프트까지, 전 → 후", "If the user answers a flagged conflict with only a direction, pick the smaller change, show the prompt" in inst_core)
check("[실행4] 검사기: '… left and center panels'는 좌우가 아니다(pass 예시 있음)", os.path.exists(os.path.join(FIX, "image__pass__S18_sheet_left_and_center_panels.txt")))
for tp in ["image-prompt/character.md", "image-prompt/character-edit.md"]:
    tmpl = "\n".join(b for i, b in enumerate(sk(tp).split("```")) if i % 2 == 1)
    r = subprocess.run([sys.executable, CHECKER, "--kind", "image", "/dev/stdin"], input=tmpl, capture_output=True, text=True)
    check(f"[실행4] 좌표 WARN이 틀의 패널 문구에 걸리지 않음: {tp}", "좌표 문장이 없다" not in r.stdout, r.stdout.strip()[:200])
sc = read(os.path.join(ROOT, "tests", "agent-eval", "scenarios.md")).split("## C24")[1].split("## C25")[0]
check("[실행4] scenarios C24: acting은 프롬프트 턴(2턴)에 연다", "`acting`은 프롬프트를 쓰는 2턴에 연다" in sc)

# 16b. 실제 Claude Code 시험 5회차(real5)에서 찾은 결함
check("[실제5] 지침 4번: 에셋 질문의 답은 에셋 대장 초안 줄, 컷 질문의 답만 컷 카드", "Write cut answers on the cut card, asset answers on that asset's `초안(제안값)` line in the registry" in inst_core)
check("[실제5] 지침 출력: 파일로 저장해도 답에 전문", "(also when saved to a file)" in out_sec)
check("[실제5] tasks §3: 시작 이미지가 없으면 live-action·cut-card를 열지 않음", "Video request without a start image" in _r3 and "no `live-action.md`, no `cut-card.md`" in _r3)
check("[실제5] must-ask 배경: 카메라는 사용자가 움직임을 말했을 때만 묻는다", "Background video: no camera move question unless the user mentioned movement" in ctx_ask)
_ce_blocks = "\n".join(b for i, b in enumerate(sk("image-prompt/character-edit.md").split("```")) if i % 2 == 1)
check("[실제5] character-edit: 사람용 안내 괄호 (by name …)가 코드블록 안에 없음", "(by name" not in _ce_blocks and "(by name, down to shoes" in sk("image-prompt/character-edit.md"))
check("[실제5] ok-reuse: 권한 문장의 태그는 OK 카드의 요소 이름", "use the OK card's element name as is" in sk("production-session/ok-reuse.md"))
_lv_c = sk("image-prompt/location-view.md").split("## Template C")[1]
check("[실제5] location-view 틀 C: 같은 쪽 접근 고정 문장(틀 B와 같은 글자)", "Move in from the same side and along the same line of sight; no reverse angle and no view from behind." in _lv_c)
check("[실제5] cut-card: 사건 수가 바뀌면 [1] 완료 조건도 고친다", "fix the [1] completion condition in the same turn" in sk("production-session/cut-card.md"))
_sc = read(os.path.join(ROOT, "tests", "agent-eval", "scenarios.md"))
check("[실제5] scenarios C02: 렌즈 관찰 결과를 묻는다고 기대하지 않음", "렌즈 관찰 결과" not in _sc.split("## C02")[1].split("## C03")[0])
check("[실제5] scenarios C25: 표지판 확대는 틀 C", "틀 C" in _sc.split("## C25")[1].split("## C26")[0])
check("[실제5] grader-rules: 영상 must-include에 identity_grandpa.lines를 넣지 않음", "영상 프롬프트에는 `identity_grandpa.lines`를 넣지 않는다" in read(os.path.join(ROOT, "tests", "agent-eval", "grader-rules.md")))

# 16c. 실제 Claude Code 시험 7회차(real7)에서 찾은 결함
_speed = speed
check("[실제7] video 속도 줄: 먼저 기존 구간 초를 세고 후 구간은 더 길다(예시보다 앞)", "First count the seconds of the existing interval" in _speed and "The new interval must be longer" in _speed and _speed.index("First count") < _speed.index("taking the full"))
check("[실제7] video 속도 줄: 예시에 고정 숫자 구간 없음([기존보다 긴 구간])", "[기존보다 긴 구간]" in _speed and not re.search(r"\d:\d\d[–-]\d:\d\d", _speed) and "three seconds" not in _speed)
check("[실제7] video 속도 줄: 이미 4초 이상이면 앞당기기·길이 늘리기 제안", "4+ seconds" in _speed and "whether to start earlier or lengthen the video" in _speed)
_v0 = [l for l in vskill.split("## 0.")[1].splitlines()[1:] if l.strip()][0]
check("[실제7] video §0 맨 위 줄: 15블록 전문 턴에 CHARACTER_ACTING을 새로 쓰면 acting", "full 15-block prompt" in _v0 and "`CHARACTER_ACTING`" in _v0 and "open `acting` first" in _v0)
_img_run = [l for l in img_skill.splitlines() if "Did you run the check script" in l][0]
_vid_run = [l for l in vskill.splitlines() if "Did you run the check script" in l][0]
check("[실제7] 검사 임시 파일: tmp/ 저장·검사 뒤 지우기(지침 \"검사\")", "save it under `tmp/`" in inst and "--kind image tmp/파일" in inst_core and "Delete the `tmp/` files afterwards" in inst)
check("[실제8] 검사 명령·절차는 지침에만, 이미지·영상 SKILL 검사 줄은 지침을 가리키고 --must-include 대상만", all("instructions \"Check\"" in r and "--must-include" in r and "check_prompt.py" not in r and "elete" not in r and "standalone" not in r for r in (_img_run, _vid_run)))
check("[실제8] 생성 운영 §1: 검사 명령·절차는 지침 \"검사\"", "command and procedure: see instructions \"Check\"" in gen.split("## 2.")[0])
check("[실제7] README 설치: tmp/를 .gitignore에", 'echo "tmp/" >> .gitignore' in read(os.path.join(ROOT, "README.md")).split("## 설치")[1].split("## ")[0])
check("[실제7] must-ask: 이웃 OK 연기는 OK 대장 목록표의 'OK 이유' 칸", "opposite to a neighbour cut's acting (`OK 이유` in the `ok-cuts.md` list)" in ctx_ask)
_okt = read(os.path.join(KIT, "project-files", "ok-cuts.md"))
check("[실제7] OK 대장 목록 '모델 · 설정'에 draft 표기", "draft 예(만료일)/아니오" in [l for l in _okt.splitlines() if l.startswith("| (예시")][0])
check("[실제7] 생성 운영 §4 OK 기록: draft 표기 한 줄", "`draft 예 · 만료일`" in gen.split("**OK record")[1].split("## 5.")[0])
check("[실제7] rerender: --refs는 <<<>>> 태그 수, 원본 영상 제외", "the number of `<<<>>>` tags" in sk("video-prompt/rerender.md") and "The attached source video is not counted" in sk("video-prompt/rerender.md"))
check("[실제7] tasks §3: 묻기만 하는 턴에는 cut-card.md를 열지 않음", "On question-only turns do not open `cut-card.md`" in _r3)
check("[실제7] 검사기: 'no people'·'no other people'은 인물로 세지 않음(pass 예시 있음)", "no (?:other )?(?:people|persons?)" in chk and os.path.exists(os.path.join(FIX, "image__pass__S19_location_no_people_left_right.txt")))

# 16e. 실제 Claude Code 시험 8회차(real8)에서 찾은 결함
# removed: "에셋 작업도 같다(등장 컷은 컷 목록 줄로만)" — tasks §3 첫 줄이 예외 없는 "Never open another cut's card"라 에셋 작업도 덮는다
check("[실제8] tasks §3 컷 세션 정본: 컷 목록 내용 칸은 핸드오프 [5]로", re.search(r"handoff \[5\]", _r3) is not None and re.search(CUT_LIST_FIELDS, _r3) is not None)
# removed: 지침 시작 3번 "(routing §1 표가 가리킬 때만)" — tasks §1(스킬을 열기 전에 작업을 확인)이 모든 스킬 열기를 막는다
_start3 = [l for l in inst_core.split("## Starting a conversation")[1].splitlines() if l.startswith("3. ")][0]
_start3_name = re.search(r"\"([^\"]+)\" in `production-session`", _start3)
check("[실제8] 지침 시작 3번: 가리키는 production-session 절 이름이 그 스킬에 있다", bool(_start3_name) and _start3_name.group(1) in sess, _start3)
check("[실제8] first-frame: 나이만 바꾸는 컷은 character-edit 틀 2의 CHANGE — AGE 목록에서", "`CHANGE — AGE` list of `character-edit.md` Template 2" in ff)  # 옛 routing §2 '50대처럼' 줄(모호한 말 표)은 일부러 뺌
check("[실제8] video 시작 이미지 없음 → first-frame.md", "(`image-prompt` -> `first-frame.md`)" in [l for l in vskill.splitlines() if l.startswith("| Start image |")][0])
check("[실제8] prop.md: 원본 job 없으면 요소 ID로 프롬프트까지, job 미기재 알림", "If the original job is not in the registry, do not ask; write the element ID" in prop and "tell the user in one line that the job is unrecorded" in prop)
check("[실제8] 에셋 대장 소품 표에 확정 job 열(틀·시험 작품)", all("| 요소 ID | 확정 job | 출처 |" in read(f) for f in [os.path.join(KIT, "project-files", "asset-registry.md"), os.path.join(ROOT, "tests", "agent-eval", "testbed", "project", "asset-registry.md")]))
check("[실제8] location-edit: 층 순서와 계획의 한 단계에 층 하나", "The order of changes is also the order of this list" in sk("image-prompt/location-edit.md") and "One layer per step of the plan" in sk("image-prompt/location-edit.md"))
_tbok = read(os.path.join(ROOT, "tests", "agent-eval", "testbed", "project", "ok-cuts.md"))
check("[실제8] 시험 작품 OK 대장: 2-1 영상 draft 예·만료일(목록·카드)", "draft 예(2026-10-31)" in [l for l in _tbok.splitlines() if l.startswith("| 2-1 | 영상")][0] and "draft_job_id `job-v-2-1` · 만료일 2026-10-31" in _tbok)
_media = os.path.join(ROOT, "tests", "agent-eval", "testbed", "media")
check("[실제8] 시험 작품 media/: 2-1·3-1 시험 영상(각 100KB 이하), make_run.sh가 복사", all(os.path.exists(os.path.join(_media, f)) and os.path.getsize(os.path.join(_media, f)) <= 100_000 for f in ["2-1.mp4", "3-1.mp4"]) and '"$HERE/testbed/media" "$RUN/media"' in read(os.path.join(ROOT, "tests", "agent-eval", "make_run.sh")))
_chains = json.load(open(os.path.join(ROOT, "tests", "agent-eval", "real-chains.json"), encoding="utf-8"))
check("[실제8] 새 스킬 시나리오 C53~C56: scenarios.md와 real-chains.json", all(f"## {c} " in read(os.path.join(ROOT, "tests", "agent-eval", "scenarios.md")) and c in _chains for c in ["C53", "C54", "C55", "C56", "C57", "C58"]))

# 16d. 새 스킬: assembly(러프컷·프레임), shot-design(장면 컷 설계)
import shutil
import tempfile
EXPECT_SKILLS = ["acting", "assembly", "color-continuity", "higgsfield-generation", "image-prompt", "production-session", "project-setup", "shot-design", "video-prompt"]
check("[스킬 수] 스킬 9개", skill_dirs == EXPECT_SKILLS, ", ".join(skill_dirs))
check("[스킬 수] zip 9개", sorted(os.path.basename(p)[:-4] for p in glob.glob(os.path.join(KIT, "dist", "*.zip"))) == EXPECT_SKILLS)
_tg = read(os.path.join(ROOT, "TEAM-GUIDE.md"))
check("[스킬 수] README·TEAM-GUIDE가 9개로 적음", "스킬 9개" in read(os.path.join(ROOT, "README.md")) and "스킬 9개" in _tg and all(f"{s}.zip" in _tg for s in EXPECT_SKILLS))
for s, word, n in [("assembly", "마지막 프레임", 21), ("shot-design", "컷 나눠", 3), ("color-continuity", "더 노래", 22)]:
    check(f"[새 스킬] 할 일 목록 {n}번 줄에 `{s}`", f"`{s}`" in _task_rows.get(n, "") and word in _task_rows.get(n, ""))
    check(f"[새 스킬] must-ask 작업별 표에 {n}번 줄", re.search(rf"^\| {n} ", ctx_ask, re.M) is not None)
asm = sk("assembly/SKILL.md")
ASM = os.path.join(SKILLS, "assembly", "assemble.py")
for sub in ["lastframe", "frame", "concat", "seam"]:
    check(f"[assembly] SKILL 명령 '{sub}'가 허용 패턴과 같은 글자", f"`{ASM_CMD} {sub} " in asm)
check("[assembly] 원본 덮어쓰지 않음·시작 이미지는 확인 뒤·생성 안 함·shot-list 순서", all(w in asm for w in ["Never overwrite originals", "only after user confirmation", "Do not generate", "the `shot-list.md` order"]))
r = subprocess.run([sys.executable, ASM], capture_output=True, text=True)
check("[assembly] assemble.py 인자 없이: 종료 1, 한국어 사용법", r.returncode == 1 and "하위 명령이 없다" in r.stderr, r.stderr[:200])
if shutil.which("ffmpeg") and shutil.which("ffprobe"):
    with tempfile.TemporaryDirectory() as td:
        a, b = os.path.join(td, "a.mp4"), os.path.join(td, "b.mp4")
        for src, size, rate, out in [("testsrc", "160x90", 24, a), ("testsrc2", "128x96", 30, b)]:
            subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "lavfi", "-i", f"{src}=size={size}:rate={rate}:duration=1",
                            "-pix_fmt", "yuv420p", out], check=True)
        runs = [["lastframe", a, os.path.join(td, "f", "a_last.png")], ["frame", a, "0.5", os.path.join(td, "f", "a_05.png")],
                ["concat", os.path.join(td, "r", "rough.mp4"), a, b], ["seam", a, b, os.path.join(td, "f", "seam.png")]]
        for args in runs:
            r = subprocess.run([sys.executable, ASM] + args, capture_output=True, text=True)
            out = args[1] if args[0] == "concat" else args[-1]
            check(f"[assembly] {args[0]}: 실행되고 ffmpeg 명령을 출력, 결과 파일 생김", r.returncode == 0 and "$ ffmpeg" in r.stdout and os.path.getsize(out) > 0 if os.path.exists(out) else False, (r.stdout + r.stderr)[-300:])
        r = subprocess.run([sys.executable, ASM, "lastframe", a, a], capture_output=True, text=True)
        check("[assembly] 입력을 출력으로 주면 거절", r.returncode == 1 and "덮어쓰지 않는다" in r.stderr and os.path.getsize(a) > 0)
        r = subprocess.run([sys.executable, ASM, "frame", a, "9", os.path.join(td, "x.png")], capture_output=True, text=True)
        check("[assembly] 영상 밖 시각이면 거절", r.returncode == 1 and "영상 밖" in r.stderr)
# 16f. 새 스킬: color-continuity(컷 간 색 맞추기)
col = sk("color-continuity/SKILL.md")
COL = os.path.join(SKILLS, "color-continuity", "color.py")
for sub_ in ["measure", "match", "compare"]:
    check(f"[color] SKILL 명령 '{sub_}'가 허용 패턴과 같은 글자", f"`{COLOR_CMD} {sub_} " in col)
check("[color] 출력은 media/color/, 원본 덮어쓰지 않음, 승인 전 제안만, 크면 다시 만들기(LIGHT LOCK·PALETTE)", all(w in col for w in ["`media/color/`", "Never overwrite originals", "Before approval, only propose", "LIGHT LOCK and PALETTE", "`decisions.md` §3"]))
check("[color] description에 사용자 말", all(w in frontmatter(col)["description"] for w in ["색이 컷마다 달라", "3-2가 더 노래", "3-1이랑 색 맞춰", "밝기 맞춰", "톤 통일", "LUT"]))
# removed: "routing §2: 확정 파일끼리 색 맞추기와 ok-reuse(생성 색감)를 가름" — 옛 routing §2 모호한 말 표는 일부러 뺐고, tasks §1이 22번/16번을 스킬을 열기 전에 확인한다
_ca = [l for l in ctx_ask.splitlines() if l.startswith("| 22 ")]
_ca = _ca[0] if _ca else ""
check("[color] must-ask 22번 줄: 기준 컷·맞출 컷, 차이가 크면 다시 만들기", "Reference cut" in _ca and "target cut" in _ca and "regenerate" in _ca, _ca)  # 작업별 "묻지 않는다(측정값)"는 ablation B에서 일부러 뺌
check("[color] decisions 틀 §3에 기준 색 컷 줄", "기준 색 컷" in read(os.path.join(KIT, "project-files", "decisions.md")).split("## §3")[1].split("## §4")[0])
check("[color] real_run.py --allowedTools에 color.py", f'"Bash({COLOR_CMD}:*)"' in read(os.path.join(ROOT, "tests", "agent-eval", "real_run.py")))
r = subprocess.run([sys.executable, COL], capture_output=True, text=True)
check("[color] color.py 인자 없이: 종료 1, 한국어 사용법", r.returncode == 1 and "하위 명령이 없다" in r.stderr, r.stderr[:200])
if shutil.which("ffmpeg") and shutil.which("ffprobe"):
    def _rows(out):
        return {l.split("|")[1].strip(): [float(x) for x in l.split("|")[3:6]] for l in out.splitlines() if l.startswith("| ") and ".mp4" in l}
    with tempfile.TemporaryDirectory() as td:
        ref, off = os.path.join(td, "ref.mp4"), os.path.join(td, "off.mp4")
        for vf, out in [("null", ref), ("eq=brightness=0.1,colorbalance=rs=0.2,colorchannelmixer=bb=0.85", off)]:
            subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "lavfi", "-i", "testsrc=size=160x90:rate=24:duration=1",
                            "-vf", vf, "-pix_fmt", "yuv420p", out], check=True)
        fixed, cmp_ = os.path.join(td, "color", "off_m.mp4"), os.path.join(td, "color", "cmp.png")
        r = subprocess.run([sys.executable, COL, "match", ref, off, fixed], capture_output=True, text=True)
        check("[color] match: ffmpeg 명령과 쓴 필터(colorchannelmixer·eq)를 출력, 결과 파일 생김", r.returncode == 0 and "$ ffmpeg" in r.stdout and "쓴 필터: colorchannelmixer=" in r.stdout and ",eq=contrast=" in r.stdout and os.path.exists(fixed), (r.stdout + r.stderr)[-300:])
        r = subprocess.run([sys.executable, COL, "measure", ref, off, fixed], capture_output=True, text=True)
        rows = _rows(r.stdout)
        if r.returncode == 0 and len(rows) == 3:
            d0 = sum(abs(a - b) for a, b in zip(rows["off.mp4"], rows["ref.mp4"]))
            d1 = sum(abs(a - b) for a, b in zip(rows["off_m.mp4"], rows["ref.mp4"]))
            check(f"[color] measure → match → measure: Y·U·V 차이 합이 줄어듦({d0:.1f} → {d1:.1f})", d1 < d0 / 2)
        else:
            check("[color] measure: 표를 출력", False, (r.stdout + r.stderr)[-300:])
        r = subprocess.run([sys.executable, COL, "compare", ref, off, fixed, cmp_], capture_output=True, text=True)
        check("[color] compare: 비교 이미지 생김", r.returncode == 0 and os.path.exists(cmp_) and os.path.getsize(cmp_) > 0, (r.stdout + r.stderr)[-300:])
        r = subprocess.run([sys.executable, COL, "match", ref, off, off], capture_output=True, text=True)
        check("[color] 입력을 출력으로 주면 거절", r.returncode == 1 and "덮어쓰지 않는다" in r.stderr and os.path.getsize(off) > 0)
        r = subprocess.run([sys.executable, COL, "measure", os.path.join(td, "없음.mp4")], capture_output=True, text=True)
        check("[color] 없는 파일이면 한국어 오류", r.returncode == 1 and "파일이 없다" in r.stderr)
sd = sk("shot-design/SKILL.md")
check("[shot-design] 블로킹은 지침 6번, 정본 수정은 production-session §1을 가리킴", "instructions rule 6" in sd and "`production-session` §1" in sd)
check("[shot-design] 리버스는 location-view.md를 가리키고 LIGHT LOCK 문장을 쓰지 않음", "`image-prompt` → `location-view.md`" in sd and "light comes from" not in sd)
check("[shot-design] 180도 선 넘음 표시·컷 길이 기준·새 뷰 필요", all(w in sd for w in ["선 넘음(의도", "at most 15 seconds per cut", "2–4 seconds per dialogue line", "새 뷰 필요"]))
check("[shot-design] 틀은 코드블록 하나(블로킹 메모·커버리지)", sd.count("```") == 2 and "블로킹 메모" in sd.split("```")[1] and "커버리지" in sd.split("```")[1])

# 16g. 실제 Claude Code 시험 9회차(real9)에서 찾은 결함
_must = ctx_ask
_asm = sk("assembly/assemble.py"); _col = sk("color-continuity/color.py")
check("[실제9] 지침 검사 줄에 --must-include", inst_core.count("--must-include tmp/문장파일") == 2)
check("[실제9] 지침 6번: 카메라를 보면 자기 왼손 = 화면 오른쪽", "facing camera: own left = screen right" in inst_core)
check("[실제9] tasks §3: 이웃 컷 연기는 OK 대장 목록 줄로만, 질문 턴에 카드 파일 안 만듦", "Neighbour cuts' acting comes only from the `OK 이유` column" in _r3 and "do not create card files" in _r3)
check("[실제9] must-ask: 폴더는 list_folders로 확인 / shot-design: 컷 길이·유지/교체", "(check with `list_folders`)" in _must and "Cut length allocation" in sd and "ask whether to keep or replace it" in sd)  # 작업별 묻는 항목은 ablation B에서 단계 파일로
check("[실제9] assemble.py: lastframe 길이, concat 입력별 해상도·길이·총 길이", "영상 길이" in _asm and "총 {" in _asm)
check("[실제9] color.py: 맞춘 뒤 재서 밝기 보정, 전후 숫자, 벌어지면 경고", "한 번 더 보정" in _col and "맞추기 전" in _col and "차이가 더 벌어졌다" in _col)
check("[실제9] shot-design: 대본 없으면 제안 설계까지, 기존 job 유지·교체", "in the same reply as the questions" in sd and "ask whether to keep or replace it" in sd)
check("[실제9] video §0 동작 여럿: 나가기는 끝 프레임 상태", "Propose writing the exit as an end-frame state" in vskill)
check("[실제9] prop.md: 글자 읽히지 않게, 시트 없으면 대장 초안 안 씀, 못 본 배경은 existing background", "lettering and destinations are not legible" in prop and "do not use the asset registry `초안` line (instructions rule 4)" in prop and "the existing background" in prop)
check("[실제9] location-edit: 중간 단계는 원 시대 이름을 되풀이하지 않음", "do not repeat the source era's name" in sk("image-prompt/location-edit.md"))
check("[실제9] first-frame: 같은 카메라 그림체 변경은 LOCKED EDIT", "Changing only art style/texture from the same camera is a `LOCKED EDIT`" in sk("image-prompt/first-frame.md"))

check("[실제9] must-ask: 없는 컷 번호는 내용만, 작업 여럿은 순서 제안 후 첫 것만", "The cut number is not in `shot-list.md`" in _must and "propose an order (task numbers) and ask only about the first" in _must)
check("[실제9] higgsfield: 보낼 때 컷 목록 생성/크레딧 칸도 올림", "cut list 생성/크레딧 cell" in gen)

# 17. 읽기 지도: 할 일 목록에 있는 파일만, 그리고 작업마다 읽는 양 (추정 토큰: 한글 × 1.0 + 그 밖 / 4)
_descs = sum(tok(frontmatter(read(os.path.join(SKILLS, d, "SKILL.md")))["description"]) for d in skill_dirs)
always = tok(claude_md) + tok(inst) + _descs  # Claude Code: CLAUDE.md + 불러오는 파일 + 스킬 설명. 모든 대화가 읽는다
routes = {
    "인물 시트": ["image-prompt/SKILL.md", "image-prompt/character.md"],
    "장소": ["image-prompt/SKILL.md", "image-prompt/location.md"],
    "장소 새 시점": ["image-prompt/SKILL.md", "image-prompt/location.md", "image-prompt/location-view.md"],
    "장소 편집": ["image-prompt/SKILL.md", "image-prompt/location.md", "image-prompt/location-edit.md"],
    "인물 + 대사": ["image-prompt/SKILL.md", "image-prompt/character.md", "acting/SKILL.md"],
    "퍼스트 프레임": ["image-prompt/SKILL.md", "image-prompt/first-frame.md"],
    "실사 영상": ["video-prompt/SKILL.md", "video-prompt/live-action.md"],
    "실사 영상 + 연기 새로": ["video-prompt/SKILL.md", "video-prompt/live-action.md", "acting/SKILL.md"],
    "\"3-1처럼\" 영상": ["video-prompt/SKILL.md", "video-prompt/live-action.md", "production-session/SKILL.md", "production-session/ok-reuse.md"],
    "생성·판정·OK 기록": ["higgsfield-generation/SKILL.md"],
    "컷 세션 시작": ["production-session/SKILL.md", "production-session/cut-card.md"],
    "장면 컷 설계": ["shot-design/SKILL.md"],
    "프레임·러프컷": ["assembly/SKILL.md"],
    "색 맞추기": ["color-continuity/SKILL.md"],
}
# 2026-10-29: 영어 키트로 바꾸며 글자 수(항상 13,000자, 단계 17,550자) 대신 추정 토큰. 값 = 그때 추정을 250 단위로 올림.
ALWAYS_BUDGET = 5000  # 그때 약 4,937 (CLAUDE.md + 지침 + tasks + must-ask + 스킬 설명 9개)
check(f"[읽기량] 항상 읽히는 양: 추정 {always:,.0f}토큰 ≤ {ALWAYS_BUDGET:,}", always <= ALWAYS_BUDGET)
BUDGET = 7500  # 단계 파일만(항상 읽히는 양 제외). 그때 가장 큰 작업 약 7,386("3-1처럼" 영상). 늘려야 하면 무엇을 지울지 먼저 본다
_route_tok = {}
for name, files in routes.items():
    n = sum(tok(read(os.path.join(SKILLS, f))) for f in files)
    _route_tok[name] = n
    check(f"[읽기량] {name}: 추정 {n:,.0f}토큰 ≤ {BUDGET:,}", n <= BUDGET)
for d in skill_dirs:
    for fn in skill_files[d]:
        if fn.endswith(".md") and fn != "SKILL.md":
            check(f"[읽기 지도] {d}/{fn}가 할 일 목록에 있다", f"`{fn}`" in inst)

# 11. 프롬프트 검사기: 픽스처마다 기대 결과와 같은가
#     파일 이름: <kind>__<pass|fail>__<설명>.txt
#     맨 위 주석 줄: "# args: --refs 3" (검사기 옵션), "# expect: 문구" (fail이면 결과에 이 문구가 있어야 함)
for path in sorted(glob.glob(os.path.join(FIX, "*.txt"))):
    base = os.path.basename(path)
    kind, expect, _ = base.split("__", 2)
    lines = read(path).splitlines()
    args, expects = [], []
    while lines and lines[0].startswith("# "):
        head = lines.pop(0)
        if head.startswith("# args:"):
            args = head[len("# args:"):].split()
        elif head.startswith("# expect:"):
            expects.append(head[len("# expect:"):].strip())
    tmp = os.path.join(FIX, ".tmp_" + base)
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    target = tmp
    args = [a.replace("{FIX}", FIX) for a in args]
    r = subprocess.run([sys.executable, CHECKER, "--kind", kind, target] + args, capture_output=True, text=True)
    os.remove(target)
    fails = [l for l in r.stdout.splitlines() if l.startswith("FAIL")]
    warns = [l for l in r.stdout.splitlines() if l.startswith("WARN")]
    if expect == "pass":
        check(f"[검사기] {base}: FAIL·WARN 없음", not fails and not warns, " / ".join(fails + warns)[:300])
    else:
        check(f"[검사기] {base}: 문제를 잡음", bool(fails or warns), r.stdout.strip()[:300])
        for e in expects:
            check(f"[검사기] {base}: '{e}'를 잡음", e in r.stdout, r.stdout.strip()[:300])

# 결과
print(f"추정 토큰: 항상 읽힘 {always:,.0f} (예산 {ALWAYS_BUDGET:,}) · instructions.md {tok(inst_core):,.0f} (예산 {INST_BUDGET:,}) · "
      f"단계 최대 {max(_route_tok.values()):,.0f} '{max(_route_tok, key=_route_tok.get)}' (예산 {BUDGET:,})")
bad = [r for r in results if not r[0]]
for ok, name, detail in results:
    if not ok:
        print(f"FAIL  {name}  {detail}")
print(f"\n점검 {len(results)}개 · 통과 {len(results) - len(bad)} · 실패 {len(bad)}")
sys.exit(1 if bad else 0)
