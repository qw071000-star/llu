FOOTER_TEXT = "AI 이미지·영상 제작 키트 · 설치 안내"

# 셀 크기의 불릿(●) 한 줄
S["cbul"] = ParagraphStyle("cbul", fontName="KR", fontSize=8.9, leading=13.2, textColor=TEXT, leftIndent=11, bulletIndent=1,
                           bulletFontName="KR", bulletFontSize=6.5, bulletColor=BLUE, spaceAfter=1.5)
S["promptbox"] = ParagraphStyle("promptbox", fontName="KR", fontSize=8.8, leading=13.2, textColor=colors.HexColor("#22303F"))


def blist(items):
    out = []
    for it in items:
        ALL_TEXT.append(it)
        out.append(Paragraph(it, S["cbul"], bulletText="●"))
    return out


def steps_from(start, items, num_bg=NAVY):
    rows = []
    for i, (title, body) in enumerate(items, start):
        cell = [P(title, "boxh")]
        cell += [P(body, "cell")] if isinstance(body, str) else body
        rows.append([P(str(i), "num"), cell])
    t = Table(rows, colWidths=[9 * mm, W - 9 * mm])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (0, -1), num_bg),
                           ("LINEBELOW", (0, 0), (-1, -2), 2.5, colors.white), ("LINEBELOW", (1, 0), (1, -1), 0.4, LINE),
                           ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                           ("LEFTPADDING", (1, 0), (1, -1), 10), ("TOPPADDING", (0, 0), (0, -1), 8)]))
    return t


story = []

band = Table([[[P("AI 이미지·영상 제작 키트 — 설치 안내", "tband"),
                P("claude.ai 웹 · 컴퓨터 브라우저 · 약 10분 · 팀원은 각자 1~6단계를 한다", "sband")]]], colWidths=[W])
band.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY), ("LEFTPADDING", (0, 0), (-1, -1), 13), ("TOPPADDING", (0, 0), (-1, -1), 11), ("BOTTOMPADDING", (0, 0), (-1, -1), 11)]))
story += [band, Spacer(1, 7)]

story.append(tbl(["준비물", "내용"], [
    [hl("Claude 요금제"), "Pro 이상 (스킬은 Pro 이상에서 쓸 수 있다)"],
    [hl("Higgsfield"), "계정 + 크레딧. 팀으로 쓰면 팀 워크스페이스 초대를 먼저 받는다 (크레딧이 그 워크스페이스에서 나간다)"],
    [hl("키트 파일"), "GitHub 리포 " + code("qw071000-star/llu") + " 접근 권한. 비공개면 리포 주인에게 초대를 요청하거나 zip으로 받는다"],
    [hl("기기"), "컴퓨터 브라우저(claude.ai). 휴대폰에서는 스킬을 올릴 수 없다"],
], [0.18, 0.82], valign="MIDDLE"))

story += sec(1, "설치 6단계")
story.append(steps([
    ("키트 파일 받기", blist([
        "GitHub 리포 → 초록색 " + hl("Code") + " 버튼 → " + hl("Download ZIP") + " → 압축 풀기 (git을 쓰면 clone, 이후 pull로 최신 유지)",
        "쓰는 폴더는 " + code("kit/dist/") + " 하나: 스킬 zip 10개 + " + code("project-instructions.md"),
    ])),
    ("코드 실행 켜기", blist([
        "설정에서 " + hl("코드 실행(파일 만들기)") + "을 켠다",
        "꺼져 있으면 스킬을 올릴 수 없고, 올려도 프롬프트 검사 스크립트가 돌지 않는다",
    ])),
    ("스킬 zip 8개 올리기", blist([
        "설정 → 스킬 메뉴(Customize → Skills 또는 Settings → Capabilities) → + → " + hl("Upload a skill"),
        hl("압축을 풀지 말고") + " zip 그대로 하나씩 올린다: " + code("project-setup") + " " + code("production-session") + " " + code("higgsfield-generation") + " " + code("image-prompt") + " " + code("video-prompt") + " " + code("acting") + " " + code("shot-design"),
        "올리지 않는 2개: " + code("assembly.zip") + " · " + code("color-continuity.zip") + " (마지막 프레임·러프컷·색 맞추기, Claude Code 전용)",
        "스킬은 " + hl("계정마다") + " 올린다. 올린 뒤 목록에 8개가 보이는지 확인",
    ])),
    ("커넥터 연결", blist([
        "설정 → 커넥터에서 " + hl("Higgsfield") + "와 " + hl("Claude Docs") + "를 연결하고, 각자 자기 계정으로 로그인",
        "Higgsfield가 목록에 없으면 커스텀 커넥터로 추가한다. 주소는 Higgsfield의 MCP 안내 페이지(" + code("higgsfield.ai/mcp") + ")에 있다",
        "로그인 뒤 " + hl("선택된 워크스페이스가 팀 것인지") + " 확인한다 (개인 크레딧이 나가지 않게)",
    ])),
    ("프로젝트 만들고 지침 붙이기", blist([
        "새 프로젝트를 만든다 (이름 = 작품명)",
        "지침(Instructions) 칸에 " + code("kit/dist/project-instructions.md") + " 내용을 " + hl("통째로") + " 복사해 붙인다 (영어 문서가 정상이다)",
        "맨 위 “This project” 칸(작품명, Higgsfield 프로젝트 이름·ID, 정본 위치)은 모르면 비워 둔다. 첫 대화에서 Claude가 채울 줄을 알려 주면 그 줄을 직접 붙여 넣는다",
        "프로젝트 지식에는 시나리오·콘티만 넣는다. " + code("guides/") + " " + code("reference/") + " " + code("tests/") + "는 넣지 않는다 (옛 문장이 프롬프트로 새는 것을 막는다)",
        "팀 요금제면 프로젝트를 팀에 공유한다. 아니면 팀원이 같은 방법으로 각자 만든다",
    ])),
]))
story.append(Spacer(1, 3))

prompt_lines = [
    "키트 설치 확인만 해 줘. 생성은 하지 마.",
    "1. 올라온 스킬 중 project-setup, production-session, higgsfield-generation, image-prompt, video-prompt, acting, shot-design이 보이는지 하나씩 적어 줘.",
    "2. 지침의 \"This project\" 칸에서 비어 있는 줄을 알려 주고, 채울 값을 나에게 한 번에 물어봐. 답하면 고친 줄만 보여 줘(지침 칸은 내가 직접 고친다).",
    "3. Higgsfield 커넥터가 연결돼 있는지 확인해 줘(목록 조회만).",
    "4. 정본이 어디 있는지, 비어 있으면 \"새 작품\"으로 시작하면 된다고 알려 줘.",
    "5. higgsfield-generation 스킬 폴더의 check_prompt.py를 찾아 그 폴더 경로를 알려 주고, \"A quiet bus stop at dusk, photorealistic, no people.\" 한 줄로 --kind image 검사를 한 번 돌려 결과 줄을 그대로 보여 줘.",
]
pb = Table([[[P(esc(l), "promptbox") for l in prompt_lines]]], colWidths=[W])
pb.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F4F5F7")), ("BOX", (0, 0), (-1, -1), 0.7, BLUE),
                        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
step6 = steps_from(6, [("5분 확인 (생성은 하지 않음)", "프로젝트에서 " + hl("새 대화") + "를 열고 아래 글을 붙여 넣는다.")])
story += [KeepTogether([step6, Spacer(1, 4), pb]), Spacer(1, 6)]

story.append(tbl(["이렇게 나오면 정상", "안 나오면"], [[
    P("\n".join([]) or "스킬 8개가 하나씩 보임 · “This project”의 빈 줄을 물어봄 · Higgsfield 연결을 확인함 · 정본이 비어 있으면 “새 작품”으로 시작하라고 함 · " + code("check_prompt.py") + " 경로와 검사 결과 한 줄을 보여 줌", "cell"),
    P("5번이 안 되면 코드 실행이 꺼져 있거나 스크립트를 못 찾은 것이다. 코드 실행을 켜고 " + code("higgsfield-generation.zip") + "을 다시 올린다. 그래도 안 되면 Claude는 손 점검을 하고 “검사 통과”라고 말하지 않는다", "cell")]],
    [0.5, 0.5], zebra=False))
story.append(Spacer(1, 4))
story.append(tbl(["이어서 해 보기", "정상 반응"], [
    ["“오늘 뭐 하면 돼?”", "정본이 비어 있으면 새 작품 질문 14개를 표 하나로 묻는다"],
    ["“3-2 영상 프롬프트 만들어”", "바로 쓰지 않고, 확인할 것을 제안값과 함께 먼저 묻는다"],
    ["“그대로”", "프롬프트와 위험 목록만 보여 주고 " + hl("생성은 하지 않는다") + " (생성은 “영상으로 만들어”라고 해야만 한다)"],
], [0.30, 0.70], valign="MIDDLE"))

story += sec(2, "첫 작품 시작 (설치 직후)")
story.append(steps([
    ("“새 작품 시작할게.”", "Claude가 질문 14개를 표 하나로 묻는다. 바꿀 것만 답한다. " + hl("작품명") + "과 " + hl("실사/그림체") + "는 기본값이 없어 꼭 답한다. 시나리오·콘티가 있으면 같이 준다"),
    ("정본과 폴더 만들기", "기본값(새 Higgsfield 프로젝트, Claude가 만듦)에 동의하면 그것이 승인이다. Claude가 정본 Claude Doc(탭 6개)과 Higgsfield 프로젝트·폴더를 만든다"),
    ("지침 맨 위 줄 채우기", "Claude가 알려 주는 “This project” 줄(작품명, Higgsfield 프로젝트 ID, 정본 Doc 링크)을 지침 칸 맨 위에 직접 붙여 넣는다. 다음 대화부터 바로 이어 간다"),
    ("정본 Doc 공유", "정본 Doc은 팀원 모두에게 " + hl("편집 권한") + "을 주고, " + hl("제안(Suggesting) 모드를 끈다") + " (켜면 Claude의 수정이 제안으로만 남아 정본에 들어가지 않는다)"),
]))

story += sec(3, "팀원이 합류할 때 — 각자 체크")
chk = Table([[P("□", "ctrh"), P(a, "cell"), P("□", "ctrh"), P(b, "cell")] for a, b in [
    ("Higgsfield 팀 워크스페이스 초대 수락, 선택된 워크스페이스 확인", "스킬 zip 8개 업로드 (계정마다)"),
    ("Higgsfield · Claude Docs 커넥터 로그인", "공유받은 프로젝트에 들어가기 (공유가 안 되면 4단계처럼 직접 만들고 지침 붙이기)"),
    ("정본 Doc 편집 권한 확인", "5분 확인 글 실행")]],
    colWidths=[6 * mm, W / 2 - 6 * mm, 6 * mm, W / 2 - 6 * mm])
chk.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("BOX", (0, 0), (-1, -1), 0.5, LINE)]))
story += [chk]

story += [CondPageBreak(95 * mm)]
story += sec(4, "문제가 생기면")
story.append(tbl(["증상", "원인과 해결"], [
    [hl("스킬 업로드가 안 된다"), "Pro 이상 요금제인지, 코드 실행이 켜져 있는지 확인한다. 화면의 메뉴 이름은 업데이트로 바뀔 수 있다. 못 찾으면 키트 관리자에게 묻는다"],
    [hl("스킬이 안 열리거나 검사 스크립트가 안 돈다"), "코드 실행을 켜고, 압축을 풀지 않은 " + code("higgsfield-generation.zip") + "을 다시 올린다"],
    [hl("Higgsfield가 커넥터 목록에 없다"), "커스텀 커넥터로 추가한다. 주소는 " + code("higgsfield.ai/mcp") + " 안내 페이지에 있다"],
    [hl("크레딧이 개인 쪽에서 나간다"), "선택된 워크스페이스를 팀 것으로 바꾼다"],
    [hl("Claude가 정본을 못 고친다"), "정본이 프로젝트 지식이면 읽기 전용이다. Claude Docs로 옮기거나, Claude가 주는 “정본 갱신” 블록을 직접 붙여 넣는다. Docs면 편집 권한과 제안 모드를 확인한다"],
    [hl("마지막 프레임·러프컷·색 맞추기가 안 된다"), "21·22번은 Claude Code 전용이다. 다음 컷 시작 이미지는 Higgsfield에서 받거나 편집 프로그램으로 처리한다"],
    [hl("“This project” 값을 모르겠다"), "비워도 된다. 첫 대화에서 Claude가 알려 주는 줄을 붙여 넣는다"],
], [0.30, 0.70], valign="MIDDLE"))
story.append(Spacer(1, 5))
story.append(tbl(["키트가 바뀌었을 때", "방법"], [
    ["1  최신 받기", "리포를 다시 받는다 (Download ZIP 또는 " + code("git pull") + ")"],
    ["2  스킬 다시 올리기", "바뀐 zip만 다시 올린다. 무엇이 바뀌었는지는 리포의 " + code("git log") + "에 있다"],
    ["3  지침 바꾸기", code("project-instructions.md") + "가 바뀌었으면 지침 칸을 통째로 바꾸고 “This project” 칸을 다시 채운다"],
    ["4  팀에 알리기", "바뀐 내용을 팀원에게 알리고, 각자 2~3을 한다"],
], [0.30, 0.70], valign="MIDDLE"))
story.append(P("Claude Code(터미널)에 설치하려면 프롬프트 하나를 붙이면 된다: " + code("guides/설치-프롬프트.md") + " §1.", "small"))

# ── 빌드 ──
doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=MARG, rightMargin=MARG, topMargin=13 * mm, bottomMargin=17 * mm,
                      title="AI 이미지·영상 제작 키트 — 설치 안내", author="llu kit", subject="claude.ai 웹 프로젝트 설치 안내")
doc.addPageTemplates([PageTemplate(id="main", frames=[Frame(MARG, 17 * mm, W, A4[1] - 30 * mm, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])])
doc.build(story, canvasmaker=NumberedCanvas)

from fontTools.ttLib import TTCollection
import re
cm = TTCollection(FONT_PATH).fonts[0].getBestCmap()
chars = set()
for t in ALL_TEXT:
    t = re.sub(r"<[^>]+>", "", t)
    chars |= set(t)
print("missing glyphs:", sorted(c for c in chars if ord(c) not in cm and not c.isspace() and ord(c) > 127))
