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
check("[지침] instructions.md 4,000자 이하 (README 규칙)", len(inst) <= 4000, f"{len(inst)}자")
for s in re.findall(r"`([a-z-]+)`(?: →|\s*\|)", inst):
    if s in ("decisions", "shot-list", "asset-registry"):
        continue
    check(f"[지침] 스킬 '{s}' 있음", s in skill_dirs)
for line in inst.splitlines():
    m = re.search(r"`([a-z-]+)` → (.+?) \|", line)
    if m:
        for fn in re.findall(r"`([a-z-]+\.md)`", m.group(2)):
            check(f"[지침] {m.group(1)}/{fn} 있음", fn in skill_files.get(m.group(1), []))

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
        for other, ref in re.findall(r"`([a-z-]+)` → `([a-z0-9-]+\.md)`", text):
            cross[ref] = other
            check(f"[참조] {d}/{fn} → {other}/{ref}", ref in skill_files.get(other, []))
        for ref in set(re.findall(r"`([a-z0-9-]+\.(?:md|py))`", text)):
            if ref in external or ref in cross:
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
        spans = []
        for m in re.finditer(r"`([a-z-]+(?:\.md)?)`\s*((?:§\d+[·, ]*)+)", text):
            spans.append(m.span())
            other = m.group(1)
            for num in re.findall(r"§(\d+)", m.group(2)):
                if other in skill_dirs:
                    check(f"[§] {d}/{fn} → {other} §{num}", num in headings(os.path.join(SKILLS, other, "SKILL.md")))
                elif other.endswith(".md") and os.path.exists(os.path.join(KIT, "project-files", other)):
                    check(f"[§] {d}/{fn} → {other} §{num}", re.search(rf"^## §{num}\.", read(os.path.join(KIT, "project-files", other)), re.M) is not None)
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

# 12. 이미지 종류마다: 틀의 항목이 "필요한 정보" 표에 있는가 (사용자에게 물을 칸이 빠지지 않게)
boiler = {"CENTER PANEL", "LEFT PANEL", "RIGHT PANEL", "CONSISTENCY RULES", "ENVIRONMENT", "REALISM", "STRUCTURE",
          "ONLY CHANGE", "PRESERVE EXACTLY", "CONTINUITY", "DO NOT TRANSFER", "PRIORITY", "REFERENCE AUTHORITY"}
img_skill = read(os.path.join(SKILLS, "image-prompt", "SKILL.md"))
for word in ["모델", "해상도", "화면비", "저장 폴더", "붙일 이미지"]:
    check(f"[질문] image-prompt 공통 점검표에 '{word}'", word in img_skill.split("## 0.")[1].split("## 1.")[0])
for kind in ["character", "location", "prop", "style", "first-frame"]:
    t = read(os.path.join(SKILLS, "image-prompt", f"{kind}.md"))
    check(f"[질문] {kind}.md에 '필요한 정보' 표(틀의 자리)", "## 필요한 정보" in t and "틀의 자리" in t)
    intake_i = t.split("## 필요한 정보")[1].split("\n## ")[0]
    labels = set()
    for x in re.findall(r"```text\n(.*?)```", t, re.S):
        labels |= set(re.findall(r"^-?\s*([A-Z][A-Z ]{2,}[A-Z])(?: —[^:\n]*)?:", x, re.M))
        labels |= set(re.findall(r"(?<![A-Z])([A-Z][a-z]+(?: [a-z]+)?):", x))
    for label in sorted(labels - boiler):
        check(f"[질문] {kind}.md 틀의 '{label}'을 채울 정보가 표에 있음", label in intake_i)
bg_intake = intake.split("배경·풍경 영상")[1]
for para in ["Camera", "Motion", "Keep", "Silent"]:
    check(f"[질문] 배경 영상 점검표가 '{para}' 문단을 덮음", f"`{para}`" in bg_intake)
for fn in ["rerender.md", "fixes.md"]:
    check(f"[질문] video-prompt/{fn}에 필요한 정보", "필요한 정보" in read(os.path.join(SKILLS, "video-prompt", fn)))
check("[질문] 지침: 사용자가 말하지 않은 칸도 묻는다", "말하지 않은" in inst)
check("[질문] 지침: 같은 항목을 두 번 묻지 않고, 일부만 답하면 남은 것은 제안값으로", "두 번 묻지 않는다" in inst and "남은 것은 제안값" in inst)
for f, text in [("video-prompt", vskill), ("image-prompt", img_skill)]:
    check(f"[질문] {f}: 묻는 법은 지침 4번을 가리킨다", "묻는 법은 지침 4번" in text)

# 13. OK 기록과 재사용
okt = read(os.path.join(KIT, "project-files", "ok-cuts.md"))
for field in ["번호", "종류", "job", "모델", "참조(붙인 순서)", "OK 이유", "한계", "프롬프트(보낸 그대로)", "가져온 OK"]:
    check(f"[OK] OK 대장 틀에 '{field}'", field in okt)
check("[OK] 생성 운영: 승인하면 OK 기록", "OK 기록" in gen and "ok-cuts.md" in gen)
check("[OK] 생성 운영: 프롬프트는 보낸 그대로, 기억으로 다시 쓰지 않음", "보낸 글자 그대로" in gen and "기억으로 다시 쓰지 않는다" in gen)
check("[OK] 지침: 승인은 그 자리에서 OK 대장에", "그 자리에서 OK 대장에" in inst)
check("[OK] 지침: '3-1처럼'은 OK 카드에서 가져옴", "3-1처럼" in inst and "ok-reuse.md" in inst)
check("[OK] 컷 카드 [12]가 OK 대장을 가리킴", re.search(r"^\[12\].*OK 대장", card, re.M) is not None)
check("[OK] 컷 카드 [7]에 가져온 OK", "가져온 OK" in card)
reuse = read(os.path.join(SKILLS, "production-session", "ok-reuse.md"))
for word in ["모션", "색감", "표정", "카메라", "목소리", "번호만"]:
    check(f"[OK] ok-reuse.md 표에 '{word}'", word in reuse)
check("[OK] 정본 Doc 탭에 OK 컷", "OK 컷" in read(os.path.join(SKILLS, "project-setup", "SKILL.md")))
for f in ["higgsfield-generation/SKILL.md", "production-session/cut-card.md", "production-session/handoff.md"]:
    check(f"[번호] {f}: 옛 번호 형식(C01, C##) 없음", not re.search(r"C\d\d|C##|C\[##\]", read(os.path.join(SKILLS, f))))
for f in ["shot-list.md", "asset-registry.md", "CLAUDE.md"]:
    check(f"[번호] project-files/{f}: 옛 번호 형식 없음", not re.search(r"C\d\d|C##", read(os.path.join(KIT, "project-files", f))))

# 14. 맹검 시험(tests/agent-eval)에서 찾은 결함이 다시 생기지 않는가
claude_md = read(os.path.join(KIT, "project-files", "CLAUDE.md"))
reg = read(os.path.join(KIT, "project-files", "asset-registry.md"))
sess = read(os.path.join(SKILLS, "production-session", "SKILL.md"))
check("[맹검] 컷 카드 수정 권한은 세션 스킬 §1 한 곳", "[3]~[7] [10]~[12]" in sess and "SKILL.md` §1" in card)
check("[맹검] 컷 목록: 컷 세션이 상태·확정 job 칸을 고친다", "상태 칸과 확정 job 칸" in sess and "production-session` §1" in shot)
check("[맹검] 지침: '몰라'도 제안값으로", "몰라" in inst)
nospeak = "does not say a single word: no attempt to speak, no parted lips, no mouthing"
for f in ["video-prompt/fixes.md", "video-prompt/live-action.md", "acting/SKILL.md"]:
    check(f"[맹검] 말하지 않음 문장 통일: {f}", nospeak in read(os.path.join(SKILLS, f)).replace("\n", " "))
check("[맹검] 렌즈 mm → 화각 환산표", "50mm 47°" in vskill and "시작 이미지가 이긴다" in vskill)
check("[맹검] 가져온 OK의 위험도 옮긴다", "위험도 가져온다" in reuse and "위험 → 막는 문장" in okt)
check("[맹검] OK 대장 예시는 지우라고 표시", "예시" in okt and "지운다" in okt)
for word in ["PALETTE", "ERA LOCK", "이 뷰의 LIGHT LOCK", "초안(제안값)", "알려진 실패"]:
    check(f"[맹검] 에셋 대장 틀에 '{word}'", word in reg)
check("[맹검] 자리표시 태그 안내(image-prompt)", "자리표시" in img_skill)
check("[맹검] \"다시 만들어\" 확인 규칙", "그 확인이다" in gen)
check("[맹검] 검토 상태 정의", "`검토`: 완성된 결과" in gen)

# 15. 2차·소넷 맹검에서 찾은 결함
chk = read(CHECKER)
check("[맹검2] 길이 경계 5,500자(검사기·실사 틀)", "> 5500" in chk and "5,500자" in live)
check("[맹검2] OK 카드와 컷 카드 구분", "`ok-cuts.md` 안의 절" in inst and "`ok-cuts.md` 안의 절" in reuse)
check("[맹검2] 다른 컷 카드·핸드오프를 예시로도 열지 않음(읽기 지도)", "다른 컷 카드·핸드오프(형식 예시로도" in inst)
check("[맹검2] 결과 이미지를 볼 수 없을 때 규칙", "볼 수 없어" in inst and "묘사를 사용자에게 묻지 않는다" in inst)
check("[맹검2] 거절하면 진행으로", "거절하면 그 자리에서 `진행`" in gen)
check("[맹검2] OK 제안 전에 카드 열기", "제안하기 전에도" in reuse)
check("[맹검2] 정정 줄이 보냄 형식보다 먼저", "`정정: …`" in gen)
check("[맹검2] 이웃 컷은 연속성 표에서", "연속성 표에서 가져온다" in vskill and "연속성 표의 자기 행" in inst)

# 16. 규칙은 한 곳에만 (같은 규칙이 두 파일에 다르게 적히면 충돌이 생긴다)
#     (이름, 그 규칙을 알아보는 정규식, 그 규칙을 적어도 되는 파일)
docs = {"instructions.md": inst}
for p in glob.glob(os.path.join(KIT, "project-files", "*.md")):
    docs["project-files/" + os.path.basename(p)] = read(p)
for p in glob.glob(os.path.join(SKILLS, "*", "*.md")):
    docs[os.path.relpath(p, SKILLS)] = read(p)
owners = [
    ("묻는 법: '몰라·알아서'면 제안값", r"몰라|알아서", {"instructions.md"}),
    ("묻는 법: 일부만 답하면 남은 것은 제안값으로", r"남은 것은 제안값", {"instructions.md"}),
    ("묻는 법: 추측하지 않는다", r"추측하지 않", {"instructions.md"}),
    ("묻는 법: 말하지 않은 값에 (제안값)", r"직접 말하지 않은 값", {"instructions.md"}),
    ("찾는 순서(사용자 말 → 컷 카드 …)", r"사용자 (말|메시지) → 컷 카드", {"instructions.md"}),
    ("이미지를 볼 수 없을 때", r"볼 수 없", {"instructions.md"}),
    ("읽는 범위: 다른 컷 카드를 열지 않는다", r"다른 컷 카드|이웃 컷 카드|예시로", {"instructions.md", "production-session/cut-card.md", "production-session/SKILL.md"}),  # 카드를 쓰는 그 자리에도 한 줄(맹검 r3: 형식 보려고 다른 카드를 엶)
    ("acting을 여는 때", r"인물이 연기하는 실사 영상", {"instructions.md"}),
    ("방향은 화면 기준(손 포함)", r"모든 방향은 화면", {"instructions.md"}),
    ("반복 실패 한도", r"4회 중 3회", {"instructions.md"}),
    ("고정 설명문은 글자 그대로", r"(대장|설명문)[^\n]{0,15}글자 그대로 (쓴다|옮긴다|복사|붙인다)", {"instructions.md"}),
    ("컷 카드 칸별 수정 권한", r"\[3\]~\[7\]", {"production-session/SKILL.md"}),
    ("컷 목록: 컷 세션이 고치는 칸", r"상태 칸과 확정 job 칸|상태·확정 job 칸", {"production-session/SKILL.md"}),
    ("확정 전 에셋 답은 초안 줄에", r"확정 전[^\n]{0,10}(답|에셋)", {"production-session/SKILL.md"}),
    ("범위 밖 문제는 총괄에 올린다", r"총괄에 올릴", {"production-session/SKILL.md", "production-session/handoff.md"}),
    ("Forbidden에 넣는 것", r"만 Forbidden에|Forbidden[^\n]{0,20}실제", {"video-prompt/SKILL.md"}),
    ("렌즈 환산표", r"24mm 84°", {"video-prompt/SKILL.md"}),
    ("OK 프롬프트 찾는 순서", r"get_project_asset_prompt`?\(그 job\)|결과물 상세", {"higgsfield-generation/SKILL.md"}),
    ("판정 말과 상태(좋아·별로·나중에)", r"\"별로\"|\"나중에\"", {"higgsfield-generation/SKILL.md"}),
    ("가져온 OK의 위험을 옮긴다", r"위험도 가져온다", {"production-session/ok-reuse.md"}),
]
for name, pat, allowed in owners:
    where = sorted(f for f, t in docs.items() if re.search(pat, t))
    extra = [f for f in where if f not in allowed]
    check(f"[한 곳] {name}: {', '.join(sorted(allowed))}에만", not extra and where, "다른 곳: " + ", ".join(extra) if extra else "주인 파일에 없음")
# 같은 상황에 다른 문장을 주지 않는다
turn_fix = re.search(r".*휙 돈다 \|.*", read(os.path.join(SKILLS, "video-prompt", "fixes.md"))).group(0)
turn_act = re.search(r".*휙 돈다 \|.*", read(os.path.join(SKILLS, "acting", "SKILL.md"))).group(0)
check("[한 곳] 휙 도는 동작: 고치기와 연기가 다른 증상을 다룬다(고개·상체 / 몸 전체)", "고개·상체" in read(os.path.join(SKILLS, "video-prompt", "fixes.md")) and "몸 전체" in turn_act, turn_fix + " / " + turn_act)

# 18. r4 맹검에서 찾은 결함
def sk(f):
    return read(os.path.join(SKILLS, f))
ff = sk("image-prompt/first-frame.md")
fixes = sk("video-prompt/fixes.md")
check("[맹검4] 지침 2번: 아직 보지 못한 프롬프트에는 어떤 말도 생성 지시가 아님", "아직 보지 못한" in inst and "직전에 보낼지 물었을 때만" in inst)
check("[맹검4] 지침 6번: 인물 기준이면 향한 쪽으로 화면 쪽, 추정", "인물이 향한 쪽" in inst and "추정" in inst)
check("[맹검4] 지침 4번: 기본값 목록에 소리", "비율·소리·저장 폴더" in inst)
check("[맹검4] 지침 5번: 대장과 OK 줄이 다르면 대장", "둘이 다르면 대장" in inst)
check("[맹검4] 읽기 지도: 이미 쓴 줄 바꾸기도 fixes.md", "이미 쓴 줄" in inst)
check("[맹검4] fixes.md: 사람 동작 속도 줄", "사람 동작이 너무 빠르다" in fixes and "failed take" in fixes.split("사람 동작이 너무 빠르다")[1].split("\n")[0])
check("[맹검4] fixes.md: 승인 컷이면 새 테이크 대체를 먼저 묻는다", "새 테이크로 대체할지" in fixes)
check("[맹검4] fixes.md 별 줄: 생성 전이면 한계와 대안", "생성 전이면 이 한계" in fixes)
check("[맹검4] video-prompt: fixes.md는 결과가 틀렸거나 이미 쓴 줄, acting 먼저", "`fixes.md`는 결과가 틀렸거나" in vskill and "먼저 `acting`" in vskill)
check("[맹검4] background.md: SKILL §0 배경 표(Keep 포함)", "`SKILL.md` §0의 배경 표" in sk("video-prompt/background.md") and "`Keep`" in sk("video-prompt/background.md"))
check("[맹검4] live-action: 덜어내는 순서와 WARN을 남기는 조건", "장소 → 스타일 → 환경" in live and "WARN을 남긴다" in live)
check("[맹검4] acting: 목표 양식 예, 사건 수·비트 수 따로", "[상대]에게/에게서 + 동사" in sk("acting/SKILL.md") and "비트 수" in sk("acting/SKILL.md"))
check("[맹검4] ok-reuse: 강한 입 잠금 문장 인라인", nospeak in reuse)
check("[맹검4] ok-reuse: '카드처럼'은 형식", "카드처럼 써\"는 형식" in reuse)
check("[맹검4] 생성 운영: 크레딧 근거, 재생성이면 '바꾼 것'", "근거(비용 메모 / get_cost / 추정)" in gen and "- 바꾼 것:" in gen)
check("[맹검4] OK 대장 카드에 draft·만료일", "draft_job_id" in okt and "만료일" in okt)
check("[맹검4] 컷 카드 [10]은 난 실패", card_fields.get("10", "").startswith("난 실패"))
check("[맹검4] 컷 목록 생성/크레딧 칸의 주인", "생성/크레딧 칸은 총괄" in sess)
check("[맹검4] 새 컷이어도 이웃 컷 파일은 열지 않음", "새 컷이어도 이웃 컷 카드" in sess and "OK 카드 한 장" in ff)
check("[맹검4] first-frame: 장소 뷰 칸이 비면 모드를 첫 질문으로", "비어 있으면 첫 질문으로" in ff)
check("[맹검4] first-frame: 반대쪽 카메라면 좌우 뒤집기, 틀 2에 In this view 줄", "좌우가 뒤집힌다" in ff and "In this view [landmark]" in ff.split("## 틀 2")[1])
check("[맹검4] first-frame·location: 틀 2를 바로 쓰는 조건", "이 컷만 쓰면 틀 2" in ff and "한 컷만 쓰면 퍼스트 프레임 틀 2" in sk("image-prompt/location.md"))
check("[맹검4] first-frame: 나이만 바꾸는 컷은 character-edit 틀 2", "`character-edit.md` 틀 2" in ff)
check("[맹검4] image-prompt §3 LOCKED EDIT 틀에 WARDROBE 줄", "WARDROBE: [asset registry sentence, verbatim]" in img_skill.split("## 3.")[1].split("## 4.")[0])
check("[맹검4] location-view: 높이는 값으로", "높이는 값으로" in sk("image-prompt/location-view.md"))
check("[맹검4] prop.md: 확정 소품 고치기와 어느 결과인가", "확정 소품 고치기" in sk("image-prompt/prop.md") and "_v2" in sk("image-prompt/prop.md") and "어느 결과" in sk("image-prompt/prop.md"))

# 17. 읽기 지도: 지침의 표에 있는 파일만, 그리고 작업마다 읽는 양
always = len(inst) + sum(len(frontmatter(read(os.path.join(SKILLS, d, "SKILL.md")))["description"]) for d in skill_dirs)
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
}
BUDGET = 22500  # 정본·컷 카드 내용 제외. 늘려야 하면 무엇을 지울지 먼저 본다. (2026-10-28: 원본 문장 복원과 화면 기준 규칙으로 22,000 → 22,500)
for name, files in routes.items():
    n = always + sum(len(read(os.path.join(SKILLS, f))) for f in files)
    check(f"[읽기량] {name}: {n:,}자 ≤ {BUDGET:,}", n <= BUDGET)
for d in skill_dirs:
    for fn in skill_files[d]:
        if fn.endswith(".md") and fn != "SKILL.md":
            check(f"[읽기 지도] {d}/{fn}가 지침의 표에 있다", f"`{fn}`" in inst)

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
bad = [r for r in results if not r[0]]
for ok, name, detail in results:
    if not ok:
        print(f"FAIL  {name}  {detail}")
print(f"\n점검 {len(results)}개 · 통과 {len(results) - len(bad)} · 실패 {len(bad)}")
sys.exit(1 if bad else 0)
