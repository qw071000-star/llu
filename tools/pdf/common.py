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

MARG = 15 * mm
W = A4[0] - 2 * MARG  # 본문 폭

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
FOOTER_TEXT = "AI 이미지·영상 제작 키트"
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
        self.line(MARG, 14 * mm, A4[0] - MARG, 14 * mm)
        self.setFont("KR", 8); self.setFillColor(MUTED)
        self.drawString(MARG, 9.5 * mm, FOOTER_TEXT)
        self.drawRightString(A4[0] - MARG, 9.5 * mm, f"{self._pageNumber} / {total}")



# ───────── 요약판 본문 (short_head.py 뒤에 이어 붙여 실행) ─────────
# 촘촘한 스타일
S["cell"] = ParagraphStyle("cell", fontName="KR", fontSize=8.9, leading=12.9, textColor=TEXT)
S["cellh"] = ParagraphStyle("cellh", fontName="KR", fontSize=9.2, leading=13, textColor=colors.white)
S["h2"] = ParagraphStyle("h2", fontName="KR", fontSize=11.5, leading=16, textColor=NAVY, spaceBefore=7, spaceAfter=3, keepWithNext=1)
S["box"] = ParagraphStyle("box", fontName="KR", fontSize=9.0, leading=13.2, textColor=TEXT)
S["boxh"] = ParagraphStyle("boxh", fontName="KR", fontSize=10, leading=14, textColor=NAVY, spaceAfter=2)
S["h1"] = ParagraphStyle("h1", fontName="KR", fontSize=15.5, leading=20, textColor=NAVY)
S["num"] = ParagraphStyle("num", fontName="KR", fontSize=12, leading=15, textColor=colors.white, alignment=1)
S["ctr"] = ParagraphStyle("ctr", fontName="KR", fontSize=8.6, leading=12.4, textColor=TEXT, alignment=1)
S["tband"] = ParagraphStyle("tband", parent=S["title"], fontSize=19, leading=25)
S["sband"] = ParagraphStyle("sband", parent=S["sub"], fontSize=9.5, leading=14)
S["ctrh"] = ParagraphStyle("ctrh", fontName="KR", fontSize=9.4, leading=13, textColor=NAVY, alignment=1)


def tbl(header, rows, widths, zebra=True, valign="TOP", pad=3.2):
    data = [[P(h, "cellh") for h in header]] if header else []
    for r in rows:
        data.append([c if not isinstance(c, str) else P(c, "cell") for c in r])
    t = Table(data, colWidths=[w * W for w in widths], repeatRows=1 if header else 0)
    st = [("VALIGN", (0, 0), (-1, -1), valign), ("GRID", (0, 0), (-1, -1), 0.5, LINE),
          ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
          ("TOPPADDING", (0, 0), (-1, -1), pad), ("BOTTOMPADDING", (0, 0), (-1, -1), pad)]
    if header:
        st += [("BACKGROUND", (0, 0), (-1, 0), NAVY)]
    if zebra:
        st += [("ROWBACKGROUNDS", (0, 1 if header else 0), (-1, -1), [colors.white, ZEBRA])]
    t.setStyle(TableStyle(st))
    return KeepTogether([t])


def sec(n, title):
    t = Table([[P(str(n), "num"), P(title, "h1")]], colWidths=[9 * mm, W - 9 * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), NAVY), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (1, 0), (1, 0), 8),
                           ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3), ("LINEBELOW", (0, 0), (-1, 0), 1.1, NAVY)]))
    return [Spacer(1, 7), t, Spacer(1, 5)]


def note(items, kind="amber", title=None):
    body = [P("● " + i, "box") for i in items]
    return callout(title, body, kind)


def code(t):
    return f'<font name="KR" size="8.8" color="#9A3412">{esc(t)}</font>'


