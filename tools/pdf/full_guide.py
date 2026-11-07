#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AI 이미지·영상 제작 키트 — 사용 안내서 (PDF)"""
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
                                PageBreak, KeepTogether, Flowable, CondPageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.pdfgen import canvas as rl_canvas

OUT = sys.argv[1]
FONT_PATH = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
pdfmetrics.registerFont(TTFont("KR", FONT_PATH, subfontIndex=0))
for b in (0, 1):
    for i in (0, 1):
        addMapping("KR", b, i, "KR")

NAVY = colors.HexColor("#1F3A5F")
BLUE = colors.HexColor("#2F6FDE")
LIGHT = colors.HexColor("#EEF3FB")
ZEBRA = colors.HexColor("#F6F8FC")
LINE = colors.HexColor("#D5DCE8")
TEXT = colors.HexColor("#2B3340")
MUTED = colors.HexColor("#6B7280")
AMBER_BG, AMBER = colors.HexColor("#FFF6E0"), colors.HexColor("#E0A100")
GREEN_BG, GREEN = colors.HexColor("#E8F6EE"), colors.HexColor("#2E9E5B")
RED_BG, RED = colors.HexColor("#FDECEC"), colors.HexColor("#D64545")
BLUE_BG = colors.HexColor("#EAF1FD")

W = A4[0] - 36 * mm  # 본문 폭

S = {
    "body": ParagraphStyle("body", fontName="KR", fontSize=10, leading=17, textColor=TEXT, spaceAfter=4),
    "small": ParagraphStyle("small", fontName="KR", fontSize=8.5, leading=13, textColor=MUTED),
    "cell": ParagraphStyle("cell", fontName="KR", fontSize=9, leading=14.5, textColor=TEXT),
    "cellh": ParagraphStyle("cellh", fontName="KR", fontSize=9, leading=13, textColor=colors.white),
    "h1": ParagraphStyle("h1", fontName="KR", fontSize=17, leading=22, textColor=NAVY),
    "h2": ParagraphStyle("h2", fontName="KR", fontSize=12.5, leading=18, textColor=NAVY, spaceBefore=10, spaceAfter=5, keepWithNext=1),
    "h3": ParagraphStyle("h3", fontName="KR", fontSize=10.5, leading=16, textColor=BLUE, spaceBefore=6, spaceAfter=2, keepWithNext=1),
    "bul": ParagraphStyle("bul", fontName="KR", fontSize=10, leading=16.5, textColor=TEXT, leftIndent=13, bulletIndent=1, spaceAfter=2,
                          bulletFontName="KR", bulletFontSize=7, bulletColor=BLUE),
    "mono": ParagraphStyle("mono", fontName="Courier", fontSize=7.6, leading=11, textColor=colors.HexColor("#22303F")),
    "monoh": ParagraphStyle("monoh", fontName="KR", fontSize=8, leading=12, textColor=colors.HexColor("#7A5C00")),
    "title": ParagraphStyle("title", fontName="KR", fontSize=25, leading=33, textColor=colors.white),
    "sub": ParagraphStyle("sub", fontName="KR", fontSize=12.5, leading=20, textColor=colors.HexColor("#CFE0FA")),
    "box": ParagraphStyle("box", fontName="KR", fontSize=9.6, leading=16, textColor=TEXT),
    "boxh": ParagraphStyle("boxh", fontName="KR", fontSize=10.5, leading=16, textColor=NAVY, spaceAfter=2),
    "num": ParagraphStyle("num", fontName="KR", fontSize=14, leading=18, textColor=colors.white, alignment=1),
    "ctr": ParagraphStyle("ctr", fontName="KR", fontSize=9, leading=13, textColor=TEXT, alignment=1),
    "ctrh": ParagraphStyle("ctrh", fontName="KR", fontSize=10, leading=14, textColor=NAVY, alignment=1),
    "arrow": ParagraphStyle("arrow", fontName="KR", fontSize=14, leading=18, textColor=BLUE, alignment=1),
}
ALL_TEXT = []
import json, os
PAGES_FILE = OUT + ".pages.json"
PAGES = json.load(open(PAGES_FILE)) if os.path.exists(PAGES_FILE) else {}
SEEN = {}


class Mark(Flowable):
    def __init__(self, key):
        super().__init__(); self.key = key; self.width = 0; self.height = 0

    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        SEEN[self.key] = self.canv.getPageNumber()


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def P(text, style="body", **kw):
    ALL_TEXT.append(text)
    st = S[style] if not kw else ParagraphStyle("x", parent=S[style], **kw)
    return Paragraph(text, st)


def hl(t, color="#2F6FDE"):
    return f'<font color="{color}">{t}</font>'


def code(t):
    return f'<font name="KR" size="8.8" color="#9A3412">{esc(t)}</font>'


def bullets(items, style="bul"):
    out = []
    for it in items:
        ALL_TEXT.append(it)
        out.append(Paragraph(it, S[style], bulletText="●"))
    return out


def section(num, title, lead=None):
    t = Table([[P(str(num), "num"), P(title, "h1")]], colWidths=[11 * mm, W - 11 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), NAVY), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (1, 0), (1, 0), 9), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, 0), 1.2, NAVY)]))
    out = [CondPageBreak(70 * mm), Mark(str(num)), Spacer(1, 6), t, Spacer(1, 8)]
    if lead:
        out += [P(lead), Spacer(1, 2)]
    return out


def callout(title, body, kind="blue"):
    bg, bd = {"blue": (BLUE_BG, BLUE), "amber": (AMBER_BG, AMBER), "green": (GREEN_BG, GREEN), "red": (RED_BG, RED)}[kind]
    cells = []
    if title:
        cells.append(P(title, "boxh"))
    if isinstance(body, str):
        cells.append(P(body, "box"))
    else:
        cells += body
    t = Table([[cells]], colWidths=[W])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LINEBEFORE", (0, 0), (0, 0), 3.2, bd),
                           ("LEFTPADDING", (0, 0), (-1, -1), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                           ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return KeepTogether([t, Spacer(1, 7)])


def table(header, rows, widths, zebra=True, valign="TOP", first_col_color=None):
    data = [[P(h, "cellh") for h in header]] if header else []
    for r in rows:
        data.append([c if not isinstance(c, str) else P(c, "cell") for c in r])
    t = Table(data, colWidths=[w * W for w in widths], repeatRows=1 if header else 0)
    st = [("VALIGN", (0, 0), (-1, -1), valign), ("GRID", (0, 0), (-1, -1), 0.5, LINE),
          ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
          ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]
    if header:
        st += [("BACKGROUND", (0, 0), (-1, 0), NAVY)]
    if zebra:
        st += [("ROWBACKGROUNDS", (0, 1 if header else 0), (-1, -1), [colors.white, ZEBRA])]
    t.setStyle(TableStyle(st))
    return t


def steps(items, num_bg=NAVY):
    """번호 카드: [(제목, 본문 Flowable/str), ...]"""
    rows = []
    for i, (title, body) in enumerate(items, 1):
        cell = [P(title, "boxh")]
        if isinstance(body, str):
            cell.append(P(body, "cell"))
        else:
            cell += body
        rows.append([P(str(i), "num"), cell])
    t = Table(rows, colWidths=[9 * mm, W - 9 * mm])
    st = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (0, -1), num_bg),
          ("LINEBELOW", (0, 0), (-1, -2), 2.5, colors.white), ("LINEBELOW", (1, 0), (1, -1), 0.4, LINE),
          ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
          ("LEFTPADDING", (1, 0), (1, -1), 10), ("TOPPADDING", (0, 0), (0, -1), 8),
          ("BACKGROUND", (1, 0), (1, -1), colors.white)]
    t.setStyle(TableStyle(st))
    return t


class Arch(Flowable):
    """전체 그림: 나 → Claude 프로젝트(지침·스킬·정본) → Higgsfield"""
    def __init__(self):
        super().__init__()
        self.width, self.height = W, 78 * mm

    def wrap(self, aw, ah):
        return self.width, self.height

    def box(self, x, y, w, h, fill, stroke, lines, r=5, lw=1):
        c = self.canv
        c.setFillColor(fill); c.setStrokeColor(stroke); c.setLineWidth(lw)
        c.roundRect(x, y, w, h, r, fill=1, stroke=1)
        n = len(lines); total = sum(l[1] * 1.35 for l in lines)
        ty = y + h / 2 + total / 2
        for text, size, col in lines:
            ty -= size * 1.2
            c.setFillColor(col); c.setFont("KR", size)
            c.drawCentredString(x + w / 2, ty + size * 0.2, text)
            ty -= size * 0.15

    def arrow(self, x1, y1, x2, y2, label=None, label2=None):
        c = self.canv
        c.setStrokeColor(BLUE); c.setFillColor(BLUE); c.setLineWidth(1.6)
        c.line(x1, y1, x2 - (4 if x2 > x1 else -4), y2)
        d = 5 if x2 > x1 else -5
        p = c.beginPath(); p.moveTo(x2, y2); p.lineTo(x2 - d, y2 + 3); p.lineTo(x2 - d, y2 - 3); p.close()
        c.drawPath(p, fill=1, stroke=0)
        c.setFillColor(NAVY); c.setFont("KR", 7.6)
        if label:
            c.drawCentredString((x1 + x2) / 2, y1 + 5, label)
        if label2:
            c.drawCentredString((x1 + x2) / 2, y1 - 11, label2)

    def draw(self):
        c = self.canv
        m = mm
        self.box(0, 25 * m, 27 * m, 28 * m, colors.white, NAVY, [("나", 14, NAVY), ("(사용자)", 8.5, MUTED)], lw=1.4)
        # Claude 프로젝트
        bx, by, bw, bh = 45 * m, 1 * m, 90 * m, 76 * m
        c.setFillColor(LIGHT); c.setStrokeColor(BLUE); c.setLineWidth(1.4)
        c.roundRect(bx, by, bw, bh, 7, fill=1, stroke=1)
        c.setFillColor(NAVY); c.setFont("KR", 10)
        c.drawCentredString(bx + bw / 2, by + bh - 8 * m, "Claude 프로젝트  (claude.ai 웹)")
        inner = [("지침  ·  항상 읽음", "규칙 11개 · 할 일 목록 23개 · 꼭 물을 것"),
                 ("스킬 7개  ·  그 작업 때만", "프롬프트 쓰기 · 생성 · 세션 운영 · 연기 …"),
                 ("정본  ·  Claude Docs 문서", "확정 사항 · 에셋 · 컷 목록 · OK 대장 · 핸드오프")]
        for i, (a, b) in enumerate(inner):
            y = by + 6 * m + (2 - i) * 20 * m
            fill = colors.HexColor("#FFF6E0") if i == 0 else colors.white
            self.box(bx + 6 * m, y, bw - 12 * m, 16 * m, fill if i == 0 else colors.white, GREEN if i == 0 else BLUE,
                     [(a, 9.2, NAVY), (b, 7.4, MUTED)], r=4, lw=1)
        # Higgsfield
        self.box(150 * m, 18 * m, 24 * m, 42 * m, colors.white, NAVY,
                 [("Higgsfield", 10, NAVY), ("이미지·영상", 7.6, MUTED), ("생성", 7.6, MUTED), ("컷 폴더", 7.6, MUTED), ("승인 / 거절", 7.6, MUTED)], lw=1.4)
        # 화살표
        self.arrow(27 * m, 40 * m, 45 * m, 40 * m, "말로 지시")
        self.arrow(135 * m, 46 * m, 150 * m, 46 * m, "‘만들어’")
        self.arrow(150 * m, 33 * m, 135 * m, 33 * m, None, "결과·OK")


class NumberedCanvas(rl_canvas.Canvas):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self._saved = []

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved)
        for st in self._saved:
            self.__dict__.update(st)
            self.draw_footer(total)
            super().showPage()
        super().save()

    def draw_footer(self, total):
        if self._pageNumber == 1:
            return
        self.setStrokeColor(LINE); self.setLineWidth(0.6)
        self.line(18 * mm, 14 * mm, A4[0] - 18 * mm, 14 * mm)
        self.setFont("KR", 8); self.setFillColor(MUTED)
        self.drawString(18 * mm, 9.5 * mm, "AI 이미지·영상 제작 키트 · 사용 안내서")
        self.drawRightString(A4[0] - 18 * mm, 9.5 * mm, f"{self._pageNumber} / {total}")


story = []

# ───────────────────────── 표지 ─────────────────────────
cover = Table([[[P("AI 이미지·영상<br/>제작 키트", "title"), Spacer(1, 8),
                 P("claude.ai 웹 프로젝트에서 Claude와 Higgsfield로 작품 만들기", "sub"), Spacer(1, 3),
                 P("사용 안내서 — 작업하는 법 · 작성되는 과정과 내용 · 다른 사람에게 알리는 법", "sub")]]], colWidths=[W])
cover.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), NAVY), ("LEFTPADDING", (0, 0), (-1, -1), 16),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 16), ("TOPPADDING", (0, 0), (-1, -1), 20), ("BOTTOMPADDING", (0, 0), (-1, -1), 20)]))
story += [cover, Spacer(1, 8)]

story.append(P("이 문서가 답하는 세 가지", "h2"))
qs = Table([[P("1", "num"), P("작업을 하려면 어떻게 하나", "boxh"), P("설치 → 작업 순서 → 컷 하나의 사이클  (2~4장)", "cell")],
            [P("2", "num"), P("어떤 과정으로, 어떤 내용이 작성되나", "boxh"), P("Claude가 하는 8단계 · 문서 6종 · 프롬프트의 모양  (5~6장)", "cell")],
            [P("3", "num"), P("다른 사람에게 어떻게 알리나", "boxh"), P("전달 전 준비 · 누구에게 무엇을 · 복사해 쓰는 안내 메시지  (7장)", "cell")]],
           colWidths=[10 * mm, 62 * mm, W - 72 * mm])
qs.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, -1), BLUE), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("LINEBELOW", (0, 0), (-1, -2), 2.5, colors.white), ("LINEBELOW", (1, 0), (-1, -1), 0.4, LINE),
                        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6), ("LEFTPADDING", (1, 0), (-1, -1), 10)]))
story += [qs, Spacer(1, 6)]

story.append(callout("30초 요약", bullets([
    "Claude에게 " + hl("말로 시키면") + ", Claude가 그 작업에 맞는 설명서(스킬)를 골라 영어 프롬프트를 쓰고, 검사한 뒤 보여 줍니다.",
    "내가 " + hl("“영상으로 만들어”") + "처럼 말해야만 Higgsfield로 보냅니다. “좋아”, “그대로”는 생성 지시가 아닙니다.",
    "결정한 것은 대화가 아니라 " + hl("정본 문서") + "에 남습니다. 그래서 씬·컷마다 새 대화를 열어도 이어집니다.",
    "Claude는 결과 이미지·영상을 직접 보지 못합니다. 결과는 " + hl("내가 보고") + " “OK” 또는 “거절”을 말합니다.",
]), "blue"))

story.append(P("목차", "h2"))
def pg(k):
    return str(PAGES.get(k, "·"))


toc = table(None, [
    [P("1", "num"), "전체 그림 — 무엇으로 이루어져 있나", pg("1")],
    [P("2", "num"), "처음 시작하기 — claude.ai 웹에서 설치 (10분)", pg("2")],
    [P("3", "num"), "작업하는 순서와 말하는 법 — 컷 하나의 사이클", pg("3")],
    [P("4", "num"), "대화를 나누는 법 — 총괄 · 씬 · 컷 세션", pg("4")],
    [P("5", "num"), "어떤 과정으로 작성되나 — Claude가 하는 8단계", pg("5")],
    [P("6", "num"), "무엇이 작성되나 — 문서 6종과 프롬프트의 모양", pg("6")],
    [P("7", "num"), "다른 사람에게 알리는 법", pg("7")],
    [P("8", "num"), "이상할 때 · 크레딧 · 알아 둘 점", pg("8")],
    [P("+", "num"), "부록 — 자주 쓰는 말 한눈에 · 파일 위치", pg("A")],
], [0.07, 0.83, 0.10], zebra=False, valign="MIDDLE")
toc.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, -1), NAVY), ("GRID", (0, 0), (-1, -1), 0, colors.white),
                         ("LINEBELOW", (1, 0), (-1, -1), 0.4, LINE), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                         ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5), ("LEFTPADDING", (1, 0), (1, -1), 10),
                         ("ALIGN", (2, 0), (2, -1), "RIGHT")]))
story += [toc, PageBreak()]

# ───────────────────────── 1. 전체 그림 ─────────────────────────
story += section(1, "전체 그림 — 무엇으로 이루어져 있나",
                 "이 키트는 " + hl("Claude에게 주는 규칙과 설명서 묶음") + "입니다. 새 작품을 시작할 때 Claude 프로젝트에 한 번 넣어 두면, 그 프로젝트 안의 모든 대화가 같은 규칙으로 움직입니다.")
story += [Arch(), Spacer(1, 8)]
story.append(table(["재료", "무엇이 들어 있나", "어디에 넣나"], [
    [hl("지침"), "항상 지키는 규칙 11개, 사용자 말 → 작업 번호(23개)로 바꾸는 표, 꼭 물어볼 것", "프로젝트의 " + code("지침 칸") + "에 " + code("project-instructions.md") + " 통째로"],
    [hl("스킬 7개"), "작업별 설명서: 새 작품 시작 · 세션 운영 · 생성 · 이미지 프롬프트 · 영상 프롬프트 · 연기 · 컷 나누기. 그 작업을 할 때만 읽힘", "설정 → 스킬 → zip 7개 업로드 (계정마다)"],
    [hl("정본"), "확정 사항, 에셋·폴더 대장, 컷 목록, 컷 카드, OK 대장, 핸드오프. 대화가 아니라 이 문서가 기준", "Claude Docs 문서 1개 (탭 6개)"],
    [hl("Higgsfield"), "실제 이미지·영상을 만드는 서비스. 크레딧이 나감. 컷마다 폴더가 있고 승인/거절 폴더로 나뉨", "설정 → 커넥터에서 연결"],
], [0.14, 0.52, 0.34]))
story.append(Spacer(1, 8))
story.append(callout("핵심 원칙: 대화는 일회용, 기억은 정본에",
                     "Claude는 이전 대화를 기억하지 못합니다. 대신 새 대화가 시작될 때 정본과 핸드오프(인계 메모)를 읽고 이어 갑니다. "
                     "그래서 컷 하나를 끝낼 때마다 " + hl("“핸드오프 써”") + "라고 하면 다음 대화가 막힘 없이 이어집니다.", "green"))

# ───────────────────────── 2. 처음 시작하기 ─────────────────────────
story += section(2, "처음 시작하기 — claude.ai 웹에서 설치 (10분)",
                 "컴퓨터 브라우저에서 합니다(휴대폰에서는 스킬을 올릴 수 없습니다). 준비물: Claude Pro 이상 요금제, Higgsfield 계정(크레딧).")
story.append(steps([
    ("코드 실행 켜기", "설정 → Capabilities → " + hl("코드 실행(파일 만들기)") + ". 스킬과 프롬프트 검사 스크립트가 이 기능으로 돌아서, 꺼져 있으면 동작하지 않습니다."),
    ("스킬 zip 7개 올리기", [P("설정 → 스킬 → Upload a skill. 리포의 " + code("kit/dist/") + "에서 하나씩, 압축은 풀지 않고 올립니다.", "cell"),
                          P(code("project-setup") + "  " + code("production-session") + "  " + code("higgsfield-generation") + "  " + code("image-prompt") + "  " + code("video-prompt") + "  " + code("acting") + "  " + code("shot-design"), "cell")]),
    ("커넥터 연결", "설정 → 커넥터에서 " + hl("Higgsfield") + "와 " + hl("Claude Docs") + "를 연결합니다. 각자 자기 계정으로 로그인합니다."),
    ("프로젝트 만들고 지침 붙이기", "새 프로젝트를 만들고(이름은 작품명), 지침 칸에 " + code("kit/dist/project-instructions.md") + " 내용을 통째로 붙입니다. 프로젝트 지식에는 시나리오·콘티 정도만 넣습니다."),
    ("5분 확인 (생성은 하지 않음)", [P("새 대화에 “키트 설치 확인” 글(" + code("guides/설치-프롬프트.md") + " §2)을 붙입니다. 이렇게 나오면 정상입니다.", "cell")] +
     bullets(["스킬 7개가 보이고, 검사 스크립트(" + code("check_prompt.py") + ")를 한 번 돌려 결과 줄을 보여 줌",
              "“3-2 영상 프롬프트 만들어”라고 하면 바로 쓰지 않고, 확인할 것을 제안값과 함께 먼저 물음",
              "그 뒤 “그대로”라고 해도 프롬프트만 보여 주고 생성은 하지 않음"], "bul")),
    ("첫 마디: “새 작품 시작할게.”", "Claude가 질문 14개를 표 하나로 한 번에 묻습니다(화면비, 길이, 실사/그림체, 모델, 해상도, 시대, 카메라, 금지 요소, 연기 등). "
     "“바꿀 것만 답해 주세요. 나머지는 기본값으로 합니다.” 작품명과 실사/그림체 여부는 필수입니다. 답하면 정본 문서와 Higgsfield 폴더를 만듭니다."),
]))
story.append(Spacer(1, 8))
story.append(callout("웹에서 알아 둘 점", bullets([
    hl("정본은 Claude Docs 문서로 둡니다.") + " 프로젝트 지식은 Claude가 직접 고칠 수 없어서, 바뀐 줄을 매번 “정본 갱신” 블록으로 받아 손으로 옮겨야 합니다.",
    "정본 Doc은 팀원 모두에게 " + hl("편집 권한") + "을 주고, " + hl("제안(Suggesting) 모드를 꺼 둡니다.") + " 켜져 있으면 Claude가 고친 것이 제안으로만 남아 정본에 들어가지 않습니다.",
    "마지막 프레임 뽑기 · 러프컷 · 색 맞추기(21·22번)는 " + hl("Claude Code 전용") + "입니다. 웹에서는 Claude가 한 줄로 알려 줍니다.",
    "프로젝트 공유는 팀 요금제에서만 됩니다. 개인 요금제면 팀원이 같은 방법으로 각자 프로젝트를 만들고, 정본 Doc만 함께 씁니다.",
], "bul"), "amber"))

# ───────────────────────── 3. 작업 순서 ─────────────────────────
story += section(3, "작업하는 순서와 말하는 법",
                 "스킬 이름은 몰라도 됩니다. 하고 싶은 것을 말하면 Claude가 알맞은 작업을 골라, 답의 첫 줄에 " + hl("“13번 실사·인물 영상으로 진행합니다.”") + "처럼 무엇으로 이해했는지 밝힙니다.")
story.append(table(["순서", "단계", "이렇게 말한다", "Claude가 하는 일"], [
    ["1", hl("새 작품 시작"), "“새 작품 시작하자. 실사로 3분짜리”", "질문 14개 → 정본 초안, Higgsfield 폴더"],
    ["2", hl("장면을 컷으로"), "“이 장면 컷 나눠줘”", "카메라 위치, 180도 선, 컷 길이를 제안"],
    ["3", hl("에셋 만들기"), "“할아버지 인물 시트 만들어”<br/>“정류장 만들어” · “왕진 가방 만들어”", "인물 → 장소 → 소품 순서로 이미지 프롬프트"],
    ["4", hl("컷마다 퍼스트 프레임"), "“3-4 퍼스트 프레임 만들어”", "영상의 0:00이 될 이미지 프롬프트"],
    ["5", hl("컷마다 영상"), "“3-2 영상 프롬프트 만들어”<br/>“3-1처럼 3-2 만들어”", "영상 프롬프트(실사 15블록, 배경 4문단)"],
    ["6", hl("만들고·확인·OK"), "“영상으로 만들어” → “됐어” → “OK”", "Higgsfield로 보내고, 결과 확인, OK 기록"],
    ["+", "고해상도", "“1080p로”", "승인된 draft는 7일 안에 같은 테이크를 1080p로"],
], [0.07, 0.19, 0.40, 0.34], valign="MIDDLE"))
story.append(Spacer(1, 10))

story.append(P("컷 하나는 늘 이 순서입니다", "h2"))
cyc = [("프롬프트 보기", "질문에 답하면 프롬프트·위험 목록이 나옴"),
       ("“영상으로 만들어”", "견적 근거와 함께 Higgsfield로 보냄"),
       ("“됐어”", "완성되면 알려 줌. Claude가 결과를 항목별로 보고"),
       ("“OK” 또는 “거절”", "OK면 프롬프트 그대로 기록, 폴더 이동"),
       ("“핸드오프 써”", "다음 대화·총괄을 위한 인계 메모")]
row1, row2 = [], []
for i, (a, b) in enumerate(cyc):
    row1.append([P(f"{i + 1}", "ctrh", textColor=BLUE), P(a, "ctrh"), P(b, "ctr")])
    if i < len(cyc) - 1:
        row1.append(P("→", "arrow"))
cw = []
for i in range(len(cyc)):
    cw.append(28 * mm)
    if i < len(cyc) - 1:
        cw.append((W - 5 * 28 * mm) / 4)
ct = Table([row1], colWidths=cw)
ts = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
      ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3)]
for i in range(0, len(cw), 2):
    ts += [("BACKGROUND", (i, 0), (i, 0), LIGHT), ("BOX", (i, 0), (i, 0), 0.8, BLUE)]
ct.setStyle(TableStyle(ts))
story += [KeepTogether([ct]), Spacer(1, 10)]

story.append(P("말하는 법", "h2"))
story += bullets([
    hl("컷 번호 + 작업 이름") + "이 가장 빠릅니다. “3-2 영상 프롬프트”, “3-4 퍼스트 프레임”, “할아버지 인물 시트”.",
    "막연해도 됩니다. “구름 더 느리게”, “50대처럼”이라고 하면 Claude가 구체적인 값을 제안합니다. 괜찮으면 " + hl("“그대로”") + "(제안 수락)라고 합니다.",
    "질문에는 " + hl("바꿀 것만 답하면") + " 됩니다. 답하지 않은 항목은 제안값으로 가고, “몰라”·“알아서”도 제안값입니다.",
    "방향은 " + hl("화면에 보이는 기준") + "입니다. “왼쪽”은 화면의 왼쪽입니다. 인물 자신의 손이면 “손녀 입장에서 오른손”처럼 말하세요. 동서남북은 쓰지 않습니다.",
    "두 작업을 한꺼번에 말하면 Claude가 순서를 정해 첫 것만 하고, 나머지가 기다리는 이유를 한 줄씩 알려 줍니다.",
])
story.append(Spacer(1, 6))
five_head = P("꼭 기억할 다섯 가지", "h2")
five = [("1", "“만들어”라고 해야 만든다", "프롬프트를 보고 나서 “이미지로 만들어”, “영상으로 만들어”, “보내”라고 말합니다. “좋아”, “그대로”는 만들라는 말이 아닙니다."),
        ("2", "한 번에 한 가지만 바꾼다", "여러 개를 말하면 순서를 나눠 줍니다. 급해도 하나씩이 결국 빠릅니다."),
        ("3", "확인은 싸게 한다", "이미지는 1k, 영상은 480p(draft)로 보고, 확정한 뒤 고해상도로 올립니다. 인물 시트만 처음부터 2k."),
        ("4", "같은 실패가 두 번이면 멈춘다", "Claude가 문장을 더하는 대신 샷 나누기·후반 작업을 제안합니다. 그 제안을 받는 편이 낫습니다."),
        ("5", "결과는 내가 본다", "Claude는 결과를 못 봅니다. 퍼스트 프레임을 OK하기 전에 시선·손·자세를 직접 보고, 다르면 말해 주세요.")]
fv = Table([[P(n, "num"), [P(t, "boxh"), P(b, "cell")]] for n, t, b in five], colWidths=[9 * mm, W - 9 * mm])
fv.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, -1), BLUE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LINEBELOW", (0, 0), (-1, -2), 2.5, colors.white), ("LINEBELOW", (1, 0), (1, -1), 0.4, LINE),
                        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 7), ("LEFTPADDING", (1, 0), (1, -1), 10),
                        ("TOPPADDING", (0, 0), (0, -1), 9)]))
story += [KeepTogether([five_head, fv])]

# ───────────────────────── 4. 세션 나누기 ─────────────────────────
story += section(4, "대화를 나누는 법 — 총괄 · 씬 · 컷 세션",
                 "한 작품 안에서 씬이나 컷마다 새 대화를 엽니다. 대화가 길어지면 앞의 내용이 흐려지고, 다른 컷의 옛 문장이 섞이기 때문입니다. 컷 번호만 말해도 Claude가 알아서 이어 갑니다.")
story.append(table(["세션", "언제", "하는 일", "첫 마디"], [
    [hl("총괄"), "하루 시작, 컷 몇 개가 끝났을 때", "오늘 할 일 정하기, 핸드오프를 정본에 반영, 공용 에셋 확정, 컷 카드 발행", "“총괄 세션이야. 오늘 뭐 하면 돼?”"],
    [hl("씬"), "한 씬을 시작할 때", "컷 나누기(블로킹, 180도 선, 커버리지), 그 씬의 컷 카드 만들기", "“3장면 컷 나눠 줘. 대본은 …”"],
    [hl("컷"), "컷 하나를 만들 때", "퍼스트 프레임 → 영상 → 승인까지. 끝나면 핸드오프", "“3-2”  (또는 “3-2 영상 프롬프트 만들어”)"],
], [0.10, 0.22, 0.38, 0.30]))
story.append(Spacer(1, 8))
story.append(callout("하루 흐름 예시", [
    P("1  새 대화  “총괄 세션이야. 오늘 뭐 하면 돼?” → 오늘 할 컷 3-2, 3-3", "box"),
    P("2  새 대화  “3-2 퍼스트 프레임 만들자.” → OK → “3-2 영상 프롬프트 만들어.” → “영상으로 만들어” → “OK” → “핸드오프 써.”", "box"),
    P("3  새 대화  “3-3” → 이어서 진행 → “핸드오프 써.”", "box"),
    P("4  새 대화  “총괄 세션이야. 받은 핸드오프 정본에 반영해.”", "box"),
], "green"))
story.append(P("컷 세션은 컷 하나만 다룹니다. 다른 컷을 고치고 싶으면 그 컷의 새 대화를 엽니다. 같은 컷에서 생성과 확인을 8번 넘게 주고받으면 Claude가 새 대화로 넘기자고 합니다.", "small"))

# ───────────────────────── 5. 작성 과정 ─────────────────────────
story += section(5, "어떤 과정으로 작성되나 — Claude가 하는 8단계",
                 "요청 하나를 받으면 Claude는 아래 순서로 움직입니다. 이 순서 덕분에 같은 말을 해도 매번 같은 방식으로 프롬프트가 나옵니다.")
story.append(steps([
    ("정본 읽기", "확정 사항 · 컷 목록 · 에셋 대장 3개를 읽습니다. 비어 있으면 “새 작품 시작”으로 갑니다."),
    ("작업 번호 정하기", "할 일 23개 중 하나로 정합니다. 답 첫 줄에 번호와 이름을 밝히고, 두 작업으로 읽히면 “이 작업을 할까요?”라고 먼저 확인합니다."),
    ("설명서(스킬) 열기", "그 작업에 필요한 것만 엽니다. 다른 컷의 카드·핸드오프는 열지 않습니다(옛 문장이 새 프롬프트로 새는 것을 막기 위해)."),
    ("빠진 정보를 한 번에 묻기", [P("항목마다 " + hl("제안값 + 이유") + "를 붙여 한 번에 묻습니다. 정본에 이미 있는 값(모델, 해상도, 화면비, 소리, 저장 폴더)은 묻지 않고 “기본값으로 씀: …” 한 줄로만 알립니다.", "cell"),
                          Spacer(1, 3),
                          P("예)  프롬프트를 쓰기 전에 확인할 것이 3개 있습니다. 제안값이 괜찮으면 “그대로”라고 해 주세요.<br/>"
                            "1. 카메라 전진량: 제안 — 프레임의 약 5%만큼 천천히 (이유: “조금”은 5% 안팎이면 눈에 보임)", "small")]),
    ("프롬프트 쓰기", "영어로, 정해진 틀대로 씁니다. 에셋의 고정 설명문은 정본에서 " + hl("글자 그대로") + " 가져오고, 모든 방향은 화면 기준으로 씁니다. 동작은 한 번에 1~3개로 제한하고 넘으면 샷을 나눕니다."),
    ("위험 목록 + 자동 검사", "실패할 만한 점을 한 줄씩 적고(예: “왼쪽 패널에 머리가 생길 수 있음 → 문장으로 막음”), 검사 스크립트가 빠진 항목·금지 표현·방향 표기를 점검합니다. 걸린 것은 고친 뒤에 보여 줍니다."),
    ("“만들어” 하면 생성", "저장 폴더를 지정하고, 견적은 정본의 비용 메모나 받은 견적일 때만 숫자로 적습니다(없으면 “알 수 없음”). 보낸 뒤에는 기다리지 않고 끝냅니다. 완성되면 내가 “됐어”라고 합니다."),
    ("결과 확인과 기록", "지시한 항목마다 맞음/틀림을 보고하고, 보지 못한 것은 “추정”이라고 씁니다. " + hl("OK") + "면 OK 대장에 보낸 프롬프트를 그대로 기록하고 폴더를 옮깁니다. " + hl("거절") + "이면 이유를 적고, 같은 실패가 두 번이면 멈추고 다른 방법을 제안합니다."),
]))
story.append(Spacer(1, 8))
story.append(callout("정본에 기록되는 방식 (웹)", bullets([
    "정본이 " + hl("Claude Docs") + "이면: Claude가 필요한 탭의 필요한 부분만 읽고, 바뀐 칸만 직접 고칩니다. 사람이 옮길 일이 없습니다.",
    "정본이 " + hl("프로젝트 지식") + "이면: Claude는 읽기만 가능합니다. 바뀐 줄을 파일별로 “정본 갱신” 블록으로 주면 내가 파일을 바꿔 올립니다. 컷 세션을 시작할 때는 그 컷의 카드와 핸드오프를 붙여 달라고 한 번 요청합니다.",
], "bul"), "blue"))

# ───────────────────────── 6. 작성 내용 ─────────────────────────
story += section(6, "무엇이 작성되나 — 문서 6종과 프롬프트의 모양")
story.append(P("6-1  정본 문서 6종", "h2"))
story.append(table(["문서 (Docs 탭)", "담는 내용", "누가 고치나"], [
    [hl("확정 사항"), "화면비·길이, 모델·해상도, 룩·시대, 카메라, 연기 범위, 금지 요소. 줄마다 날짜와 “사용자 답/기본값” 근거. 번복되면 취소선으로 남김", "총괄"],
    [hl("에셋·폴더"), "Higgsfield 폴더 ID 표, 인물·장소·소품의 ID(CH-001, LC-001-V1, PR-001), 고정 설명문(외모·의상·빛 고정), 확정 job, 알려진 실패와 막는 문장", "총괄 (컷 세션은 새 컷 폴더 ID만)"],
    [hl("컷 목록"), "컷마다 한 줄: 시간, 내용, 상태(대기→진행→검토→승인, 보류), 장소 뷰, 확정 첫 프레임·영상, 생성 수와 크레딧. 이웃 컷 이음새·소품 연속성 표", "총괄 (컷 세션은 자기 줄의 상태·확정 job만)"],
    [hl("컷 카드"), "컷 하나를 만드는 데 필요한 정보 한 장(아래 6-2). 컷마다 한 절, 제목은 “3-1”", "총괄이 발행, 컷 세션이 채움"],
    [hl("OK 컷"), "승인한 결과의 번호·종류·job·설정, OK 이유(내 말 그대로), 한계, " + hl("보낸 프롬프트 전문") + ". “3-1처럼”은 여기서 가져옴", "승인한 세션이 그 자리에서"],
    [hl("핸드오프 로그"), "컷 세션이 끝날 때 남기는 인계 메모(아래 6-2). 덧붙이기만 함", "컷 세션"],
], [0.17, 0.60, 0.23]))
story.append(Spacer(1, 6))

story.append(P("6-2  컷 카드와 핸드오프", "h2"))
story.append(table(["컷 카드 (12칸, 3,000자 이하)", "핸드오프 (6칸, 40줄 이하)"], [[
    P("[1] 목표와 완료 조건<br/>[2] 저장 위치(폴더)<br/>[3] 형식: 길이·비율·모델·소리<br/>[4] 카메라: 위치·높이·방향·렌즈(°)<br/>"
      "[5] 인물: 시작·끝 위치, 동선, 시선, 소품<br/>[6] 타이밍: 동작 구간, 이음새<br/>[7] 참조: ID·역할·권한, 가져온 OK<br/>"
      "[8] 고정 설명문(대장 항목 이름)<br/>[9] 적용되는 확정 사항<br/>[10] 난 실패 → 막는 문장<br/>[11] 이전 시도(승인/거절 이유)<br/>[12] 확정 프롬프트(OK 카드 이름)", "cell"),
    P("받는 세션 / 보낸 세션 / 컷 상태<br/>[1] 확정된 것: 종류·job·OK 대장 기록 여부·한계<br/>[2] 이번 세션 생성: 이미지·영상 수, 크레딧, 거절 이유<br/>"
      "[3] 바뀐 결정과 근거<br/>[4] 새로 난 실패 → 막는 문장<br/>[5] 총괄에 올릴 것(이 컷 범위 밖)<br/>[6] 다음 할 일<br/><br/>"
      + hl("역사는 쓰지 않고 결과와 다음 단계만") + " 적습니다. 읽는 사람은 다음 대화의 Claude입니다.", "cell")]],
    [0.5, 0.5], zebra=False))
story.append(Spacer(1, 8))

story.append(P("6-3  이미지 프롬프트", "h2"))
story.append(table(["종류", "모양"], [
    [hl("인물 시트"), "16:9 한 장을 세로 3분할: 왼쪽 목 아래 앞모습(머리 없는 패널) / 가운데 뒷모습 / 오른쪽 얼굴 클로즈업. 얼굴·체형·의상·머리를 객관적 특징부터 적고, 처음부터 2k로 만듦(1k로 확인하고 2k로 다시 뽑으면 다른 사람이 됨)"],
    [hl("장소"), "마스터(기하·팔레트·시대 고정) → 새 시점(반대 방향, 더 가까이) → 상태 변경(불 켜짐, 밤, 시대). 시점마다 “이 뷰의 빛 방향 고정” 문장을 화면 쪽 + 물건으로 적음"],
    [hl("소품 · 그림체"), "소품은 크기·재질·마모 상태를 고정. 그림체는 기준 이미지를 정하고 매체·기법·종이를 지정"],
    [hl("퍼스트 프레임"), "영상 0:00이 될 이미지. 참조가 둘 이상이면 어느 참조가 무엇만 정하는지(장소/얼굴/소품) 권한 블록으로 적음"],
    [hl("고칠 때"), "다시 새로 만들지 않고 결과를 참조로 붙여 " + code("CHANGE") + " / " + code("PRESERVE EXACTLY") + " / " + code("ONLY CHANGE") + " 틀로 바뀌는 것 하나만 지시. 바뀐 값은 “전 → 후”로 따로 보여 줌"],
], [0.17, 0.83]))
story.append(Spacer(1, 8))

story.append(P("6-4  영상 프롬프트", "h2"))
story.append(P("실사·인물 컷은 " + hl("15블록") + ", 배경·풍경 컷은 " + hl("4문단") + "(Camera · Motion · Keep · Silent)으로 씁니다. 프롬프트 본문은 영어, Claude의 설명과 질문은 한국어입니다. 실패한 적이 있는 것(예: 말하지 않는 장면에서 입이 움직임)은 " + hl("그 실패를 막는 문장") + "으로 대장에 남겨 다음 프롬프트에 자동으로 들어갑니다. 15블록은 다음과 같습니다.", "body"))
blocks = [("SCENE_CONTEXT", "이 클립에서 일어나는 일"), ("ACTIVE_REFERENCES", "붙인 참조와 각 참조의 권한"), ("LOCATION_MAP", "화면 왼쪽·가운데·오른쪽에 무엇이 있나"),
          ("FIRST_FRAME_AND_|SPATIAL_BLOCKING", "0:00의 인물 위치·자세"), ("FORMAT_MODE", "길이, 끊김 없는 한 샷"), ("OPTICS", "화각(°)과 눈에 보이는 결과"),
          ("CAMERA", "위치·높이, 고정 또는 한 번의 움직임"), ("ACTION_TIMING", "동작 구간(0:00–0:03)"), ("CHARACTER_ACTING", "연기: 목적과 범위"),
          ("PHYSICS", "움직이는 것은 인물·소품·카메라·환경 중 누구인가"), ("LIGHTING", "주된 빛의 방향"), ("AUDIO", "대사·효과음·음악"),
          ("STYLE", "룩 한 문장"), ("QUALITY", "얼굴·질감"), ("REQUIRED_AND_FORBIDDEN", "지킬 것 + 실제로 났던 실패 막기")]
bt = []
for i in range(0, 15, 3):
    bt.append([P("<br/>".join(code(x) for x in a.split("|")) + "<br/>" + b, "cell") for a, b in blocks[i:i + 3]])
bt = Table(bt, colWidths=[W / 3] * 3)
bt.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.5, LINE), ("BACKGROUND", (0, 0), (-1, -1), ZEBRA), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 6), ("LEFTPADDING", (0, 0), (-1, -1), 6)]))
story += [bt, Spacer(1, 8)]

story.append(P("실제로 만든 영상 프롬프트의 일부 (발췌)", "h3"))
ex = [("[SCENE_CONTEXT]", "Early 1990s. A rural Korean bus shelter at dusk in late autumn. A woman in her late sixties sits alone on the bench waiting for the last bus. ..."),
      ("[CAMERA]", "Across the road at standing eye level, looking at the shelter. Fixed and completely locked from 0:00 to 0:05. No pan, no tilt, no zoom, no push-in, no reframing."),
      ("[ACTION_TIMING]", "0:00-0:02 - she pulls the apron cord tight and finishes the knot; her hands then rest flat on her knees.<br/>0:02-0:05 - her eyes move first toward the timetable-sign side of the road, then her head follows slowly, about 1.5 s. ..."),
      ("[AUDIO]", "No dialogue. She does not say a single word: no attempt to speak, no parted lips, no mouthing. Faint wind in dry grass. No music."),
      ("[REQUIRED_AND_FORBIDDEN_CONSTRAINTS]", "Required: - The camera does not move (ENTIRE_SHOT)<br/>Forbidden: - Subtitles, text, watermarks, logos. (ENTIRE_SHOT)")]
exr = []
for h, b in ex:
    exr.append(Paragraph(h, S["mono"]))
    exr.append(Paragraph(b, S["mono"]))
    exr.append(Spacer(1, 3))
mono_box = Table([[exr]], colWidths=[W])
mono_box.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F4F5F7")), ("BOX", (0, 0), (-1, -1), 0.6, LINE),
                              ("LEFTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
story += [mono_box]

# ───────────────────────── 7. 알리는 법 ─────────────────────────
story += section(7, "다른 사람에게 알리는 법",
                 "문서가 이미 역할별로 나뉘어 있습니다. 링크 하나만 주고 시작하게 하고, 필요할 때 다음 문서를 주면 됩니다.")
story.append(P("7-1  전달 전에 확인할 것", "h2"))
chk = [("TEAM-GUIDE.md 맨 위의 이름 세 칸 채우기", "총괄 · 키트 관리 · Higgsfield 워크스페이스"),
       ("정본용 Claude Docs 문서 1개 만들기", "팀원 모두에게 편집 권한, 제안(Suggesting) 모드는 끄기. 정본은 팀에 하나만"),
       ("Higgsfield 팀 워크스페이스에 팀원 초대", "크레딧은 그 워크스페이스에서 나감. 작업 전에 선택된 워크스페이스가 팀 것인지 확인"),
       ("Claude Docs 「AI 제작 가이드」 공유", "에셋·이미지·영상 만드는 법 요약 문서"),
       ("키트 리포 접근 권한", "리포(qw071000-star/llu)가 비공개면 GitHub 초대, 또는 zip으로 전달")]
ct2 = Table([[P("□", "ctrh", fontSize=13), [P(a, "boxh"), P(b, "cell")]] for a, b in chk], colWidths=[9 * mm, W - 9 * mm])
ct2.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINE),
                         ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
story += [ct2, Spacer(1, 8)]

story.append(P("7-2  누구에게 무엇을 주나", "h2"))
story.append(table(["대상", "주는 문서", "내용"], [
    ["처음 보는 사람", code("guides/한눈에-보기.md"), "스킬, 순서, “이렇게 말하면 된다”가 한 장에"],
    ["설치하는 사람", code("guides/설치-프롬프트.md") + "<br/>" + code("guides/세팅.md"), "웹은 §2의 10분 순서. 자세한 설정과 키트가 바뀌었을 때"],
    ["처음 쓰는 팀원", code("TEAM-GUIDE.md") + "<br/>" + code("guides/알아둘-것.md"), "하루 작업 흐름, Claude가 실제로 움직이는 방식, 결과가 이상할 때"],
    ["컷 작업자", code("guides/세션-시작.md") + "<br/>" + code("guides/작업별-팁.md"), "세션마다 할 말, 작업별 질문·흔한 실패·크레딧 아끼기"],
    ["영상 프롬프트를 읽고 고치는 사람", code("guides/15블록-가이드.md"), "15블록마다 들어가는 것, 예시, 자주 틀리는 것"],
    ["작품 전체를 지시하는 사람", code("guides/할일-목록.md"), "작업 번호로 고르기(23개)"],
], [0.24, 0.34, 0.42]))
story.append(Spacer(1, 6))

story.append(P("7-3  팀원이 각자 해야 하는 것", "h2"))
story += bullets([
    "스킬 zip 7개 업로드 — " + hl("계정마다") + " 따로 올려야 합니다.",
    "Higgsfield와 Claude Docs 커넥터에 자기 계정으로 로그인.",
    "프로젝트 만들고 지침 칸에 " + code("project-instructions.md") + " 붙이기(팀 요금제면 공유받은 프로젝트에 들어가기).",
    "정본 Doc에 편집 권한이 있는지 확인, 5분 확인 글 실행.",
])
story.append(Spacer(1, 6))

story.append(P("7-4  복사해서 쓰는 안내 메시지", "h2"))
msg = ("AI 이미지·영상 제작 키트를 쓰기로 했습니다. 컴퓨터 브라우저(claude.ai)에서 10분이면 설치됩니다.<br/><br/>"
       "1) 먼저 「한눈에 보기」(한 장)를 읽어 주세요: [링크]<br/>"
       "2) 설치는 설치 안내 §2 순서대로 해 주세요. 스킬 7개는 각자 계정에 올려야 합니다.<br/>"
       "3) 정본은 이 Claude Docs 문서 하나만 씁니다: [링크] (편집 권한 있음 / 제안 모드는 꺼 주세요)<br/>"
       "4) 시작은 “새 작품 시작할게.” 이미 작품이 있으면 “3-2”처럼 컷 번호만 말하면 이어집니다.<br/>"
       "5) “이미지로 만들어”, “영상으로 만들어”라고 해야만 생성되고, 크레딧이 나갑니다.<br/>"
       "6) 컷 하나가 끝나면 “핸드오프 써”라고 해 주세요.<br/>"
       "7) 이상하면 그 대화를 [키트 관리자]에게 보내 주세요. 같은 실수가 반복되지 않게 키트에 반영합니다.")
story.append(callout("그대로 복사해 보내세요", msg, "green"))

# ───────────────────────── 8. 이상할 때 ─────────────────────────
story += section(8, "이상할 때 · 크레딧 · 알아 둘 점")
story.append(P("결과가 이상할 때", "h2"))
story.append(table(["증상", "이렇게 말한다", "Claude가 하는 일"], [
    ["“이상해”만 말함", "“0:04쯤 할아버지 입이 움직여”처럼 구간과 인물", "후보 두세 개를 보여 주고 고르게 함. 바로 말해 주면 더 빠름"],
    ["너무 빠르다 / 느리다", "“너무 빨라”, “구름 더 느리게”", "지금 구간의 초를 세어 바꿈. “천천히”는 지금보다 긴 구간이 됨"],
    ["이미지가 가짜 같다", "“너무 매끈해”(피부), “쨍해”(색)", "노출 → 선명함 → 피부 → 색 → 너무 깨끗함 순서로 하나만 고침"],
    ["같은 실패가 두 번", "(Claude가 먼저 멈춤)", "샷 나누기, 직접 편집, 후반 작업을 제안. 받는 편이 낫다"],
    ["승인한 컷을 고치고 싶다", "“새 테이크로 바꿔”", "기존 OK는 새 결과가 승인될 때까지 그대로 두고 먼저 묻는다"],
], [0.24, 0.36, 0.40]))
story.append(Spacer(1, 8))
story.append(callout("크레딧 아끼기", bullets([
    "확인: 이미지 " + hl("1k (품질 medium)") + ", 영상 " + hl("480p draft") + "(Kling 4.0은 480p가 없어 720p). 1080p를 확인용으로 뽑으면 비용도 들고 새 결함도 생깁니다.",
    "Seedance draft는 승인하면 " + hl("7일 안에 같은 테이크를 1080p로") + " 올릴 수 있습니다. 다시 생성하면 다른 테이크가 나오니 “1080p로”라고 말하세요.",
    "크레딧 숫자는 받은 견적이나 정본의 비용 메모가 있을 때만 적습니다. 근거가 없으면 “알 수 없음”입니다.",
    "“크레딧 얼마나 썼어?”에는 컷 목록의 생성/크레딧 칸에 기록된 것만으로 답합니다.",
], "bul"), "green"))

story.append(P("웹에서 안 되는 것 · 알려진 약점", "h2"))
story += bullets([
    "마지막 프레임 뽑기, 이어 붙이기(러프컷), 색 맞추기는 " + hl("Claude Code 전용") + "입니다. 다음 컷 시작 이미지는 Higgsfield에서 받거나 편집 프로그램으로 처리합니다.",
    "도구를 쓰는 사이에 영어 한 줄이 가끔 섞입니다. 답의 본문과 질문은 한국어입니다.",
    "견적 받기 같은 규칙을 가끔 건너뜁니다. 숫자가 근거 없이 나오면 “근거가 뭐야?”라고 물어보세요.",
    "두 사람이 나오는 컷에서 동작 수를 적게 셀 때가 있습니다. 동작이 많아 보이면 “샷 나눠야 하지 않아?”라고 물어보세요.",
])
story.append(Spacer(1, 6))
story.append(callout("아직 확인되지 않은 것 (솔직하게)", bullets([
    "이 키트는 claude.ai 웹 프로젝트와 같은 조건으로 시나리오 81개를 시험했지만, " + hl("실제 claude.ai 화면에서의 설치는 한 번도 확인되지 않았습니다.") + " 설치 후 5분 확인(2장의 5번)을 꼭 해 보세요.",
    "결과물의 품질(모델이 프롬프트를 그대로 그려 주는지)은 첫 작품을 만들면서 쌓입니다. 첫 작품은 컷 3~4개로 짧게 시작하는 것을 권합니다.",
    "이상한 점이 보이면 그 대화를 그대로 알려 주세요. 원인을 찾아 키트에 반영하고, 같은 방식으로 다시 시험합니다.",
], "bul"), "amber"))

# ───────────────────────── 부록 ─────────────────────────
story += [CondPageBreak(90 * mm), Mark("A"), Spacer(1, 6)]
at = Table([[P("+", "num"), P("부록 — 자주 쓰는 말 한눈에 · 파일 위치", "h1")]], colWidths=[11 * mm, W - 11 * mm])
at.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), BLUE), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (1, 0), (1, 0), 9),
                        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5), ("LINEBELOW", (0, 0), (-1, 0), 1.2, BLUE)]))
story += [at, Spacer(1, 8)]
story.append(table(["하고 싶은 일", "이렇게 말한다"], [
    ["새 작품 시작", "“새 작품 시작하자. 실사로 3분짜리”"],
    ["장면을 컷으로 나누기", "“이 장면 컷 나눠줘”"],
    ["인물 만들기 · 고치기", "“할아버지 인물 시트 만들어” · “옷을 겨울 코트로” · “50대처럼”"],
    ["장소 만들기 · 새 시점 · 상태 바꾸기", "“정류장 만들어” · “반대 방향에서 본 것도” · “형광등 켜진 걸로” · “밤으로”"],
    ["소품 만들기 · 고치기", "“왕진 가방 만들어” · “너무 새 거 같아”"],
    ["컷 시작 이미지", "“3-4 퍼스트 프레임 만들어”"],
    ["영상 프롬프트", "“3-2 영상 프롬프트 만들어” · “1-1 배경 영상 만들어”"],
    ["앞 컷처럼", "“3-1처럼 3-2 만들어”"],
    ["결과가 이상할 때", "“입이 움직여” · “너무 빨라” · “구름 더 느리게” · “너무 매끈해”"],
    ["실제로 만들기", "“이미지로 만들어” · “영상으로 만들어” · “보내”"],
    ["결과 확인 · 승인", "“됐어” → “OK” / “거절” / “나중에”(보류)"],
    ["고해상도", "“1080p로”"],
    ["오늘 할 일 · 이어서 하기", "“오늘 뭐 하면 돼?” · “3-2” · “3-2 이어서”"],
    ["끝낼 때", "“핸드오프 써”"],
], [0.36, 0.64], valign="MIDDLE"))
story.append(Spacer(1, 12))
story.append(P("파일은 어디에 있나 (리포 qw071000-star/llu)", "h2"))
story.append(table(["위치", "내용"], [
    [code("kit/dist/"), "웹에 올리는 스킬 zip(7개 + 코드 전용 2개)과 지침 칸에 붙일 " + code("project-instructions.md")],
    [code("kit/project-files/"), "정본 빈 틀(확정 사항, 에셋 대장, 컷 목록, OK 대장)"],
    [code("guides/") + " · " + code("TEAM-GUIDE.md"), "사람이 읽는 안내서 전부(이 문서의 근거)"],
    [code("reference/"), "오류 대장, Higgsfield 사용 기록 분석, 시험 보고서. 근거를 볼 때만 열고, 프로젝트 지식에는 넣지 않음"],
], [0.30, 0.70]))

# ───────────────────────── 빌드 ─────────────────────────
doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=20 * mm,
                      title="AI 이미지·영상 제작 키트 — 사용 안내서", author="llu kit", subject="claude.ai 웹 프로젝트용 사용 안내서")
doc.addPageTemplates([PageTemplate(id="main", frames=[Frame(18 * mm, 20 * mm, W, A4[1] - 36 * mm, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])])
doc.build(story, canvasmaker=NumberedCanvas)
json.dump(SEEN, open(PAGES_FILE, "w"))

# 글리프 점검
from fontTools.ttLib import TTCollection
cm = TTCollection(FONT_PATH).fonts[0].getBestCmap()
import re
chars = set()
for t in ALL_TEXT:
    t = re.sub(r'<font name="Courier"[^>]*>.*?</font>', "", t)
    t = re.sub(r"<[^>]+>", "", t)
    chars |= set(t)
missing = sorted(c for c in chars if ord(c) not in cm and not c.isspace() and ord(c) > 127)
print("missing glyphs:", missing)
