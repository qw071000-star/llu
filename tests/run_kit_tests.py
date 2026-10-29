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
inst_core = read(os.path.join(KIT, "instructions.md"))
check("[지침] instructions.md 4,000자 이하 (README 규칙)", len(inst_core) <= 4000, f"{len(inst_core)}자")
# 항상 읽히는 것 = 지침 + context/ (언제 무엇을, 꼭 물어볼 것)
CTX = ["routing.md", "must-ask.md"]
for f in CTX:
    check(f"[항상] context/{f} 있음", os.path.exists(os.path.join(KIT, "context", f)))
    check(f"[항상] 지침이 context/{f}를 가리킨다", f"context/{f}" in inst_core)
inst = inst_core + "\n" + "\n".join(read(os.path.join(KIT, "context", f)) for f in CTX)
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
check("[맹검] 렌즈 mm → 화각 환산표", "50mm=47°" in vskill and "시작 이미지가 이긴다" in vskill)
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
    ("렌즈 환산표", r"24mm=84°", {"video-prompt/SKILL.md"}),
    ("모호한 말 → 값·문장(속도·별·사람 동작·걸음)", r"taking the full three seconds|2회 실패면 후반|\[centre of weight\]|이동량\(화면 %\)", {"video-prompt/SKILL.md"}),
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
check("[맹검4] 읽기 지도: fixes.md는 결과가 틀렸을 때", "영상 결과 고치기" in inst)
check("[맹검4] 사람 동작 속도 줄(video-prompt 모호한 말 표)", "taking the full three seconds" in vskill and "제안값으로 묻는다" in vskill.split("taking the full three seconds")[1].split("\n")[0])
check("[맹검4] fixes.md: 승인 컷이면 새 테이크 대체를 먼저 묻는다", "새 테이크로 대체할지" in fixes)
check("[맹검4] 별 줄: 생성 전에 한계, 2회 실패면 오버레이", "생성 전에 알린다" in vskill and "2회 실패면 후반 오버레이" in vskill)
check("[맹검4] video-prompt: fixes.md는 결과가 틀렸을 때, acting 먼저", "`fixes.md`는 결과가 틀렸을 때만" in vskill and "먼저 `acting`" in vskill)
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

# 19. r5 맹검에서 찾은 결함
vague = vskill.split("**모호한 말 → 값·문장**")[1].split("**묻는 법")[0] if "**모호한 말 → 값·문장**" in vskill else ""
for word in ["속도", "움직임 추가", "작고 반복되는 요소", "사람 동작 속도", "걸음 나이", "동작 여럿"]:
    check(f"[맹검5] video-prompt §0 모호한 말 표에 '{word}'", word in vague)
check("[맹검5] 모호한 말 표: 움직임 추가면 사건이 늘었다고 알림", "사건이 하나 늘었다" in vague)
check("[맹검5] 모호한 말 표: 걸음 나이(보폭·팔·발·무게중심, 반대 걸음 = failed take)", all(w in vague for w in ["[step size]", "[arm swing]", "[feet lifted or dragged]", "[centre of weight]", "walk = failed take"]))
check("[맹검5] fixes.md: 모호한 말 줄은 옮기고 SKILL 표를 가리킴", "\"모호한 말\" 표" in fixes and not re.search(r"구름이 더|풀도 흔들|별이 더 반짝|taking the full", fixes))
check("[맹검5] 지침 4번: 모호한 말은 video-prompt §0 표", "`video-prompt` §0 \"모호한 말\" 표" in inst)
check("[맹검5] 지침: 시작 보고 세 줄은 프롬프트·생성·정본 작업일 때만, 정보·정리 질문은 생략 가능", "프롬프트·생성·정본 작업일 때만" in inst and "정보·정리 질문은 생략" in inst)
check("[맹검5] 지침: 컷 번호도 job도 없을 때만 묻고 컷 파일을 열지 않음", "컷 번호도 job도 없을 때만 묻고, 컷 파일은 열지 않는다" in inst)
check("[맹검5] 읽기 지도: OK 재표시·번역은 그 카드 하나, 검사 안 함, 번역은 코드블록 밖", "재표시·번역" in inst and "검사 안 함" in inst and "코드블록 밖" in inst)
check("[맹검5] 읽기 지도: 시트 자체 고치기만 character-edit, 퍼스트 프레임 속 인물은 first-frame", "확정 시트 고치기" in inst and "프레임 속 인물 바꾸기" in inst)
check("[맹검5] 읽기 지도: 프롬프트만 쓰면 higgsfield-generation 안 엶, 크레딧 질문", "프롬프트만 쓰면 열지 않는다" in inst and "크레딧" in inst)
check("[맹검5] 읽기 지도: SKILL.md 먼저", "SKILL.md를 먼저" in inst)
check("[맹검5] video-prompt: 사건은 묶어 세지 않고 샷별 사건 목록 먼저", "묶어 세지 않는다" in vskill and "샷별 사건 목록" in vskill and "합치지 말고" in vskill)
check("[맹검5] video-prompt: 나가기 = 마지막 프레임에 몸 절반이 프레임 밖", "몸 절반이 프레임 밖" in vskill)
check("[맹검5] video-prompt: 렌즈 표에 없는 mm는 두 값 사이", "가까운 두 값 사이" in vskill)
check("[맹검5] video-prompt 점검표: 소리 칸이 비면 대사 유무, 문 경첩 쪽", "대사 유무를 묻는다" in vskill and "경첩 쪽" in vskill)
bg = sk("video-prompt/background.md")
check("[맹검5] background: 정본 기본값은 묻지 않음, Keep은 제안값, 매체가 다르면 시작 이미지부터", "묻지 않고" in bg and "`Keep`은 사용자가 말하지 않아도 제안값" in bg and "시작 이미지부터 새로" in bg)
check("[맹검5] ok-reuse: 가져온 줄은 쪼개지 않고 새 문장, 전체를 --must-include", "쪼개거나 사이에 끼우지 않고" in reuse and "`;`·`,`로 잇지 않는다" in reuse and "전체를 `--must-include`" in reuse)
check("[맹검5] live-action: WARN 이유에 줄여 본 항목과 글자 수", "줄여 본 항목과 줄인 글자 수" in live)
check("[맹검5] production-session: [1]이 비거나 다른 방향이면 제안값으로 고치고 확인", "[1]과 다른 방향" in sess and "`(제안값)`으로 고치고" in sess)
check("[맹검5] production-session: 생성/크레딧 칸에 '이미지 N / 영상 N · 약 N 크레딧'", "`이미지 N / 영상 N · 약 N 크레딧`" in sess)
check("[맹검5] 컷 카드 [7]: [1]에 다른 컷과 같게가 있으면 그 OK", "[1]에 \"3-1과 같게\"" in card)
check("[맹검5] first-frame 틀 2: 반대편이면 필수 표시, 하늘·색은 PALETTE·LIGHT LOCK", "반대편 카메라면 필수" in ff.split("## 틀 2")[1] and "PALETTE·LIGHT LOCK과 부딪치는지" in ff)
prop = sk("image-prompt/prop.md")
check("[맹검5] prop.md: 시트가 필요한가, 차량·건물급은 장면 프레임에서", "시트가 필요한가" in prop and "차량·건물급" in prop)
check("[맹검5] 생성 운영: 크레딧 질문은 기록만 합치고 추정은 근거를 밝힘", "크레딧 얼마나 썼어" in gen and "무엇으로 셈했는지 밝힌다" in gen)
check("[맹검5] decisions 틀에 비용 메모 줄", "비용 메모" in read(os.path.join(KIT, "project-files", "decisions.md")))

# 20. 실제 Claude Code 실행(real-C01~C52) 채점에서 찾은 결함
import json
ALLOW_CMD = "python3 .claude/skills/higgsfield-generation/check_prompt.py"
sj_path = os.path.join(KIT, "project-files", "settings.json")
try:
    sj = json.load(open(sj_path, encoding="utf-8"))
except Exception:
    sj = {}
check("[실행] project-files/settings.json: 검사기 하나만 허용", sj == {"permissions": {"allow": [f"Bash({ALLOW_CMD}:*)"]}}, str(sj))
check("[실행] README 설치에 settings.json 복사", "cp kit/project-files/settings.json .claude/settings.json" in read(os.path.join(ROOT, "README.md")))
check("[실행] make_run.sh가 settings.json을 복사", '"$RUN/.claude/settings.json"' in read(os.path.join(ROOT, "tests", "agent-eval", "make_run.sh")))
check("[실행] real_run.py --allowedTools 검사기", f'"--allowedTools", "Bash({ALLOW_CMD}:*)"' in read(os.path.join(ROOT, "tests", "agent-eval", "real_run.py")))
check("[실행] image-prompt §6 명령이 허용 패턴과 같은 글자", f"`{ALLOW_CMD} --kind image" in img_skill)
check("[실행] video-prompt §4 명령이 허용 패턴과 같은 글자", f"`{ALLOW_CMD} --kind video" in vskill)
check("[실행] 검사기: --refs ≥1인데 <<< 태그 0개면 WARN", "태그가 없다" in chk and os.path.exists(os.path.join(FIX, "image__fail__N12_refs_without_tags.txt")))
check("[실행] 검사기: hand nearer/closer에 화면 쪽이 없으면 WARN", "화면 쪽이 없다" in chk and os.path.exists(os.path.join(FIX, "video__fail__N13_hand_without_screen_side.txt")))
ctx_route = read(os.path.join(KIT, "context", "routing.md"))
ctx_ask = read(os.path.join(KIT, "context", "must-ask.md"))
check("[실행] 지침 4번: job처럼 제안값 없는 항목에 '그대로'면 에셋 자체", "job처럼 제안값이 없는 항목" in inst_core)
check("[실행] 지침 4번: 다시 묻는 두 경우(직접 말한 값끼리 / 정본·OK·시작 이미지와 다름)", "다시 묻는 것은 두 경우뿐" in inst_core and "시작 이미지와 다를 때(어느 쪽인지 한 번)" in inst_core)
check("[실행] routing: 카드 [1]이 다른 컷과 같은 동작이면 ok-reuse", "카드 [1]이 \"3-1과 같은 동작\"" in ctx_route)
check("[실행] routing: '쓰고 바로 만들어'·폴더 없음이면 생성 운영 §2", "\"쓰고 바로 만들어\"이거나 컷 폴더가 없으면 §2 폴더 절" in ctx_route)
check("[실행] routing: 소품 지적·고치기 → prop.md", "\"가방이 너무 새 거 같아\" | 소품 만들기·지적·고치기" in ctx_route)
check("[실행] routing: 컷의 '뒤에서 본' 첫 프레임 → first-frame", "컷의 \"뒤에서 본\" 첫 프레임" in ctx_route)
check("[실행] routing: 영상이면 acting은 프롬프트 쓰는 턴에", "프롬프트를 쓰는 턴에 연다" in ctx_route)
check("[실행] routing: 영상 요청이면 video-prompt §0·§2", "`video-prompt` SKILL.md(§0" in ctx_route and "§2 사건 수" in ctx_route)
check("[실행] routing: 그 컷 번호의 핸드오프만, 이웃 OK 카드는 기준이 아니면 안 엶", "그 컷 번호의 마지막 핸드오프" in ctx_route and "기준 OK가 아니면 열지 않는다" in ctx_route)
check("[실행] routing: 총괄 시작은 반영 안 된 핸드오프만", "아직 반영되지 않은 핸드오프만" in ctx_route)
check("[실행] must-ask: '이걸로'인데 이미지 없으면 그것만", "그 이미지 하나만 묻고" in ctx_ask)
check("[실행] must-ask: 컷 폴더 없으면 구성안과 누가 만들지", "제가 만들까요, 직접 만드시겠어요?" in ctx_ask and "`3-6 [대기]`" in ctx_ask)
check("[실행] must-ask 실사 영상: 시작 이미지 없으면 영상 질문 보류", "영상 질문은 보류" in ctx_ask)
check("[실행] must-ask 실사 영상: 새 장소면 장소 마스터 항목을 함께", "\"장소 — 마스터\" 항목을 이 질문과 한 번에" in ctx_ask)
check("[실행] must-ask 실사 영상: 이웃 컷 OK 연기와 반대면 짚기", "이웃 컷 OK의 연기" in ctx_ask)
check("[실행] production-session: 그 컷 번호의 핸드오프", "그 컷 번호의 마지막 핸드오프" in sess)
check("[실행] cut-card: 다른 컷 카드를 형식 예시로 열지 않음", "다른 컷 카드를 형식 예시로 열지 않는다" in card)
check("[실행] 생성 운영 크레딧: 컷 목록 칸, 핸드오프는 빈 칸만", "컷 목록 생성/크레딧 칸으로 답한다" in gen and "그 칸이 빈 컷만" in gen)
check("[실행] project-setup: 11번 동의가 승인, 다시 묻지 않음", "11번 기본값 동의가 곧 승인" in sk("project-setup/SKILL.md") and "승인을 받은 뒤" not in sk("project-setup/SKILL.md"))
check("[실행] project-setup: .claude/ 수정 거절이면 바꿀 줄을 보임", "수정이 거절되면" in sk("project-setup/SKILL.md"))
check("[실행] first-frame: 틀 2 고유 문장은 OK 카드에 없어도", "OK 카드를 고쳐 쓸 때 거기 없어도 넣는다" in ff)
check("[실행] first-frame: 벽에 등을 대면 뒤는 벽 밖 → 어깨 너머", "벽 밖이다" in ff and "어깨 너머" in ff)
check("[실행] live-action: 줄여도 되는 줄과 WARN 이유 예", "겹치는 권한 설명부터 뺀다" in live and "5,788자 유지:" in live)
check("[실행] background: 소리는 정본 소리 줄대로, 묻지 않음", "대사 없는 컷 = 효과음만" in bg)
check("[실행] video-prompt 속도 줄: 전 → 후", "그 줄을 \"전 → 후\"로" in vague)
check("[실행] prop.md: 시트 없으면 카드 [5]에 문장만, 등록은 대장 초안만", "컷 카드 [5] 소품 줄에만" in prop and "코드블록은 내지 않는다" in prop and "에셋 대장 초안 줄만" in prop)
loc_edit = sk("image-prompt/location-edit.md")
check("[실행] location-edit 틀 2: LOCKED EDIT 여는 문장 전문(<<<image_1>>>)", "Edit <<<image_1>>> WITHOUT reframing" in loc_edit.split("## 틀 2")[1].split("## 틀 3")[0])
check("[실행] location-edit: 표지판 판 = IDENTITY AND TEXT, 기둥 = FIXTURES", "표지판 판은 `IDENTITY AND TEXT`, 그 기둥은 `FIXTURES`" in loc_edit)
check("[실행] location-edit: 나누면 1단계는 요청한 상태가 아님을 알림", "아직 요청한 상태" in loc_edit)
loc_view = sk("image-prompt/location-view.md")
check("[실행] location-view: 카메라가 구조물 안이면 Except 한 줄", "Except: [이 뷰에서 보이는 것만]" in loc_view)
check("[실행] location-view: LIGHT LOCK 뒤에 덧붙이지 않음", "LIGHT LOCK 줄은 글자 그대로 끝낸다" in loc_view)
ce = sk("image-prompt/character-edit.md")
check("[실행] character-edit 틀 1: GONE·No trace·no 목록이 [old 1]~[old 3] 세 자리", ce.count("[old 1], [old 2], [old 3]") >= 2 and ce.count("no [old 1], no [old 2], no [old 3]") >= 3)

# 21. 실제 실행 2회차 채점 결함
out_sec = inst_core.split("## 출력")[1]
check("[실행2] 지침 출력: 고치면 전 → 후만, 새로 쓰면 전문, 편집 프롬프트는 둘 다", "**확정 프롬프트를 고칠 때:**" in out_sec and "새로 쓰면 전문" in out_sec and "LOCKED EDIT·나이 수정" in out_sec)
check("[실행2] 지침 출력: 블록 밖 줄은 코드블록에 넣지 않음", "코드블록에 넣지 않는다" in out_sec)
check("[실행2] 지침 3번은 보이는 법을 출력에 맡김", "보이는 법은 \"출력\"" in inst_core)
check("[실행2] 지침 6번: 옆모습도 화면 쪽 + 물건, nearer the camera만은 안 됨", "`the screen-left hand, farther from the sign`" in inst_core and "`nearer the camera`·`road-side hand`처럼 화면 쪽 없이 쓰지 않는다" in inst_core)
check("[실행2] live-action 맨 위: 질문 턴에는 acting을 열지 않음", "질문 턴에는 `acting`을 열지 않는다" in live.split("## 블록")[0])
check("[실행2] 생성 운영 §6: 비용 메모가 비면 get_cost 없이 채우지 않음", "비용 메모가 비어 있으면 단가가 없다" in gen.split("## 6.")[1])
check("[실행2] routing: OK 재표시는 생성용 영어 원문 그대로", "생성용은 영어 원문 그대로" in ctx_route)
check("[실행2] routing: 속도·별·걸음은 §2, fixes.md는 그 밖", "속도·별·걸음 같은 말은 아래 §2" in ctx_route)
check("[실행2] routing: 시트 고치기에 character.md는 안 엶", "`character-edit.md` (`character.md`는 열지 않는다)" in ctx_route)
check("[실행2] location.md 틀 아래: 블록 밖 줄은 지침 출력대로(모드 신규)", "블록 밖 줄은 지침 \"출력\"대로" in sk("image-prompt/location.md") and "`모드: 신규`" in sk("image-prompt/location.md"))
check("[실행2] 생성 운영 §2: 폴더 묻는 문장은 must-ask 한 곳", "제가 만들까요" not in gen and "제가 만들까요" in ctx_ask)
for name, txt in [("video-prompt", vskill), ("image-prompt", img_skill)]:
    check(f"[실행2] {name} 검사 명령: 단독 Bash 호출(cd·&&·파이프·절대경로 없이)", "단독 Bash 호출로(cd·`&&`·파이프·절대경로 없이)" in txt)
check("[실행2] must-ask 장소 수정: 나누면 앞세운 변경 먼저", "사용자가 앞세운 변경을 먼저" in ctx_ask)
check("[실행2] image-prompt 태그: 꺾쇠는 두고 이름만, 여는 줄 예", "꺾쇠는 두고 안의 이름만" in img_skill and "`Edit <<<loc_…_v1>>> WITHOUT reframing`" in img_skill)
check("[실행2] location-view: 부모 카메라가 대상 밖 + 안에서 보면 먼 끝으로 이동", "부모 카메라가 대상 밖이고 사용자가 \"안에서\" 보면 먼 끝으로 이동" in loc_view)
check("[실행2] must-ask 퍼스트 프레임: 인원 수는 정본에 없을 때만", "보이는 인원 수(정본에 없을 때만)" in ctx_ask)
check("[실행2] must-ask 실사 영상: 시작 이미지 없을 때 허용·보류 범위", "사건 수 점검·샷 나누기·끝 프레임 상태 제안" in ctx_ask and "보류: 연기·소리·타이밍·카메라 움직임" in ctx_ask)
check("[실행2] location-edit: 새 LIGHT LOCK에 광원의 화면 쪽, 모르면 묻기", "광원의 화면 쪽 + 물건을 쓰고, 위치를 모르면 묻는다" in loc_edit)
check("[실행2] first-frame 틀 1: PROP 크기는 CHANGE를 가리킴", "its size is as described in CHANGE above." in ff and "its size is as described above." not in ff)
check("[실행2] 검사기: 손을 nearer the camera로만 쓰면 WARN", "손을 카메라 쪽으로만 썼다" in chk and os.path.exists(os.path.join(FIX, "image__fail__N14_hand_nearer_camera_only.txt")))
rr = read(os.path.join(ROOT, "tests", "agent-eval", "real_run.py"))
check("[실행2] real_run.py: 메타에 Bash 명령 문자열(bash)", '"bash": bash' in rr and 'bash.append(i.get("command", ""))' in rr)

# 22. 실제 실행 3회차 채점 결함
check("[실행3] must-ask 폴더 질문에 제안값(제가 만든다)", "직접 만드시겠어요?\"라고 묻는다(제안: 제가 만든다)" in ctx_ask)
check("[실행3] prop.md: 크기는 수치(차량급은 m + 사람), 수락 뒤 카드 줄만 인용·코드블록 없음", "크기(수치로: cm, 차량급은 m + 사람 기준)" in prop and "그 카드 줄만 인용한다. 코드블록은 내지 않는다" in prop)
cred = gen.split("## 6.")[1]
check("[실행3] 생성 운영 §6: '얼마나 썼어'는 기록 칸·알 수 없음만, 추정은 원할 때 get_cost 부른 뒤", "기록된 칸과 \"알 수 없음\"" in cred and "사용자가 원할 때만, `get_cost`를 실제로 부른 뒤" in cred and "단가로 셈하면" not in cred)
check("[실행3] production-session §3: 다음 할 일이 확인이면 확인과 빈 칸 제안값을 한 번에", "그 일이 사용자 확인이면 그 확인과 카드 빈 칸의 제안값을 한 번에 묻는다" in sess)
start2 = inst_core.split("## 대화를 시작할 때")[1].split("\n3.")[0]
check("[실행3] 지침 시작 2번: 컷 번호면 컷 목록 확정 job 먼저(팀원 작업이면 get_project_asset_prompt)", "컷 목록 그 줄의 확정 job을 먼저" in start2 and "get_project_asset_prompt" in start2 and "job이 대화에 없으면 묻고" not in start2)
check("[실행3] must-ask: job 질문은 컷 번호도 job도 없을 때", "컷 번호도 job도 대화에 없을 때" in ctx_ask and "어느 job인지(컷 번호도 job도 없으면)" in ctx_ask)
route3 = ctx_route.split("## 3.")[1]
check("[실행3] routing §3: 카드에 답을 적을 때 cut-card.md, 새 카드도 그 틀 복사", "컷 카드에 답을 적을 때는 `production-session` → `cut-card.md`" in route3 and "`cut-card.md` 틀을 복사해" in route3)
check("[실행3] routing: 총괄 시작 핸드오프는 생성/크레딧 칸이 빈 컷만", "컷 목록 생성/크레딧 칸이 빈 컷의 것만" in ctx_route)
ex = card.split("칸을 채운 예")[1] if "칸을 채운 예" in card else ""
check("[실행3] cut-card: 가상의 값으로 채운 예(칸 번호 형식)", "가상의 값" in ex and len(re.findall(r"^\[\d+\] ", ex, re.M)) >= 4 and len(card) <= 2000, f"{len(card)}자")
check("[실행3] cut-card 예의 손도 화면 쪽", "the screen-left hand" in ex)
check("[실행3] character-edit 틀 2: 젊게 할 때 표지와 no beauty filter", "젊게 할 때" in ce and "no beauty filter" in ce.split("## 틀 2")[1])
check("[실행3] scenarios C10 2턴: 망원이 시작 이미지와 달라 한 번 묻기도 PASS", "한 번 묻는 것도 PASS" in read(os.path.join(ROOT, "tests", "agent-eval", "scenarios.md")).split("## C10")[1].split("## C11")[0])
check("[실행3] 검사기: 단수 hand 앞에 화면 쪽이 없으면 WARN(합성어·복수 제외)", "(?<![-\\w])hand(?![-\\w])" in chk and os.path.exists(os.path.join(FIX, "image__fail__N15_side_hand_without_screen_side.txt")))
for lp in sorted(glob.glob(os.path.join(FIX, "*.lines")) + glob.glob(os.path.join(ROOT, "tests", "agent-eval", "testbed", "grade", "*.lines")) + [os.path.join(ROOT, "tests", "agent-eval", "testbed", "project", "ok-cuts.md")]):
    r = subprocess.run([sys.executable, CHECKER, "--kind", "image", lp], capture_output=True, text=True)
    check(f"[실행3] 손 규칙에 걸리지 않음: {os.path.relpath(lp, ROOT)}", "화면 쪽이 없다" not in r.stdout and "카메라 쪽으로만" not in r.stdout, r.stdout.strip()[:200])

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
ALWAYS_BUDGET = 13000  # 지침 + context/ + 스킬 설명. 모든 대화가 읽는다
check(f"[읽기량] 항상 읽히는 양: {always:,}자 ≤ {ALWAYS_BUDGET:,}", always <= ALWAYS_BUDGET)
BUDGET = 17550  # 단계 파일만(항상 읽히는 양 제외). 2026-10-28: 읽기 지도를 context/로 옮기며 22,500(항상 포함, 그때 항상 몫 약 4,980)에서 분리.
_old_budget_note = 22500  # 정본·컷 카드 내용 제외. 늘려야 하면 무엇을 지울지 먼저 본다. (2026-10-28: 원본 문장 복원과 화면 기준 규칙으로 22,000 → 22,500)
for name, files in routes.items():
    n = sum(len(read(os.path.join(SKILLS, f))) for f in files)
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
