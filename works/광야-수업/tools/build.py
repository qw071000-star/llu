import re, html, sys
import os
W = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..") + "/"
conti = open(W+"project/conti-1.md").read()
script = open(W+"script/01-intro.md").read().splitlines()

# Korean line -> English line (script alternates KO then EN)
ko2en = {}
for i in range(len(script)-1):
    a, b = script[i].strip(), script[i+1].strip()
    if a and b and re.search(r"[가-힣]", a) and not re.search(r"[가-힣]", b) and not a.startswith(("(", "[", "#", ">")):
        ko2en[a] = b
def to_en(ko):
    out = []
    for k, e in ko2en.items():
        if k[:12] in ko:
            out.append((ko.find(k[:12]), e))
    return " ".join(e for _, e in sorted(out))

rows = []
for line in conti.splitlines():
    if re.match(r"^\| 1-\d+ \| \d+초", line):
        c=[x.strip() for x in line.strip().strip("|").split("|")]
        c[1]=c[1].replace("초","")
        rows.append(c[:8])

# sketch specs: (background, [(kind,label,x,size)], extras)
S = {
"1-1":("air",[("crowd","정탐꾼 12",62,"tiny")],[]),
"1-2":("low",[("p","나비",80,"med")],[]),
"1-3":("rock",[("p","갓디",52,"mcu"),("blur","나비",150,"bust")],[]),
"1-4":("sky",[("p","잭",108,"mcu")],["arms"]),
"1-5":("stage",[("p","잭",78,"full"),("crew","",0,"")],["pull"]),
"1-6":("dir",[("p","감독",78,"med")],["monitor"]),
"1-7":("dir",[("p","감독",80,"bust")],[]),
"1-8":("set",[("p","잭",80,"bust")],[]),
"1-9":("dir",[("p","감독",80,"bust")],[]),
"1-10":("set",[("p","잭",80,"bust")],[]),
"1-11":("dir",[("p","감독",80,"bust")],[]),
"1-12":("set",[("p","잭",80,"bust")],[]),
"1-13":("set",[("p","잭",80,"bust")],[]),
"1-14":("dir",[("p","감독",80,"bust")],[]),
"1-15":("dir",[("p","감독",80,"bust")],[]),
"1-16":("dir",[("back","잭",34,"mcu"),("p","감독",108,"med")],[]),
"1-17":("stage",[("p","감독",58,"full"),("crew","",0,"")],["scatter"]),
"1-18":("rest",[("sit","잭",58,"med"),("p","맥스",132,"med")],["walkin"]),
"1-19":("rest",[("sit","잭",56,"med"),("p","맥스",106,"med")],[]),
"1-20":("rest",[("sit","잭",60,"med"),("p","맥스",108,"med")],["script"]),
"1-21":("rest",[("p","맥스",80,"bust")],[]),
"1-22":("rest",[("p","잭",80,"bust")],[]),
"1-23":("rest",[("p","맥스",80,"bust")],[]),
"1-24":("rest",[("p","잭",80,"bust")],[]),
"1-25":("rest",[("p","맥스",80,"bust")],[]),
"1-26":("rest",[("p","잭",86,"bust")],["arm"]),
"1-27":("rest",[("p","잭",86,"bust")],[]),
"1-28":("rest",[("p","맥스",80,"bust")],[]),
"1-29":("rest",[("p","잭",80,"bust")],[]),
"1-30":("rest",[("sit","잭",58,"med"),("p","맥스",118,"med")],["walkout"]),
"1-31":("far",[("p","여호수아",70,"small"),("p","갈렙",92,"small")],[]),
"1-32":("rest",[("p","잭",80,"bust")],[]),
"1-33":("rest",[("p","잭",80,"bust")],["script"]),
"1-34":("rest",[("p","잭",70,"full")],["walkout"]),
"1-35":("dir",[("p","감독",86,"bust")],["monitor"]),
"1-36":("stage",[("p","잭",60,"full")],["flat"]),
"1-37":("stage",[],["mound"]),
}
SIZE = {"tiny":(2.2,6),"small":(3.2,11),"full":(4.5,20),"med":(8,34),"bust":(13,52),"mcu":(17,66)}
BAND = 72  # subtitle band from y=72 to 90 (bottom 1/5)

def bg(kind):
    g = []
    if kind in ("air","low","rock","sky"):
        hz = {"air":30,"low":62,"rock":40,"sky":58}[kind]
        g.append(f'<rect width="160" height="{hz}" class="sky"/>')
        g.append(f'<path d="M0 {hz} Q30 {hz-6} 60 {hz-2} T120 {hz-5} T160 {hz} V90 H0Z" class="hill"/>')
        g.append(f'<rect y="{hz+4}" width="160" height="{90-hz}" class="sand"/>')
        if kind=="air": g.append('<path d="M20 58 Q55 50 95 56 L98 64 Q55 68 18 64Z" class="rock"/><rect x="112" y="40" width="14" height="9" class="tent"/><rect x="128" y="42" width="14" height="8" class="tent"/>')
        if kind=="rock": g.append('<path d="M0 20 Q20 8 46 18 L60 90 H0Z" class="rock"/>')
        if kind=="low": g.append('<path d="M0 74 Q80 62 160 72 V90 H0Z" class="rock"/>')
    elif kind=="stage":
        g.append('<rect width="160" height="90" class="dark"/><path d="M10 14 H150 V44 H10Z" class="drop"/><path d="M0 52 L160 52 L160 74 L0 74Z" class="sand"/><path d="M46 48 Q70 42 96 47 L98 54 Q70 57 44 54Z" class="rock"/>')
        for x in (8,150): g.append(f'<path d="M{x} 74 V30" class="stand"/><rect x="{x-4}" y="26" width="8" height="6" class="lamp"/>')
        g.append('<rect x="118" y="58" width="16" height="10" class="kit"/><path d="M126 68 V76 M120 76 L132 76" class="stand"/>')
    elif kind=="dir":
        g.append('<rect width="160" height="90" class="dark"/><path d="M0 60 H160" class="line"/><rect x="128" y="20" width="10" height="44" class="kit"/><path d="M20 30 V62 M14 26 H26" class="stand"/>')
    elif kind=="set":
        g.append('<rect width="160" height="54" class="drop"/><rect y="54" width="160" height="36" class="sand"/><path d="M0 50 Q40 44 70 52 L74 60 H0Z" class="rock"/>')
    elif kind=="rest":
        g.append('<rect width="160" height="90" class="dark"/><rect x="96" y="18" width="64" height="26" class="drop"/><rect x="96" y="44" width="64" height="8" class="sand"/><path d="M0 56 H160" class="line"/>')
        g.append('<path d="M10 70 h12 v-10 h-12z M140 70 h12 v-10 h-12z" class="chair"/>')
    elif kind=="far":
        g.append('<rect width="160" height="90" class="dark"/><rect x="20" y="16" width="120" height="34" class="drop"/><rect x="20" y="50" width="120" height="12" class="sand"/><path d="M0 62 H160" class="line"/>')
    return "".join(g)

def person(kind,label,x,size):
    out=[]
    if kind=="crowd":
        import random; r=random.Random(1)
        for i in range(12):
            px=36+r.random()*52; py=50+r.random()*10
            out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="1.3" class="fig"/>')
        out.append(f'<text x="62" y="47" class="lbl" text-anchor="middle">{label}</text>')
        return "".join(out)
    if kind=="crew":
        for px in (20,32,136,146): out.append(f'<circle cx="{px}" cy="66" r="1.8" class="fig dim"/><path d="M{px-2.5} 74 Q{px} 67 {px+2.5} 74Z" class="fig dim"/>')
        return "".join(out)
    r,h = SIZE[size]
    head_y = BAND - h if size in ("bust","mcu") else BAND - h - (4 if size!="tiny" else 0)
    if size in ("bust","mcu"): head_y = 22 if size=="mcu" else 26
    if size=="med": head_y = 24
    if size=="full": head_y = 50
    if size=="small": head_y = 44
    cls = "fig" + (" blur" if kind=="blur" else "") + (" back" if kind=="back" else "")
    body_w = r*2.6
    out.append(f'<path d="M{x-body_w:.1f} 90 Q{x-body_w:.1f} {head_y+r*1.6:.1f} {x:.1f} {head_y+r*1.3:.1f} Q{x+body_w:.1f} {head_y+r*1.6:.1f} {x+body_w:.1f} 90Z" class="{cls}"/>' if size in ("bust","mcu","med") or kind=="sit" else
               f'<path d="M{x-r:.1f} {head_y+r+h*0.75:.1f} L{x-r*0.8:.1f} {head_y+r*1.2:.1f} L{x+r*0.8:.1f} {head_y+r*1.2:.1f} L{x+r:.1f} {head_y+r+h*0.75:.1f}Z" class="{cls}"/>')
    out.append(f'<circle cx="{x}" cy="{head_y:.1f}" r="{r:.1f}" class="{cls}"/>')
    ly = max(6, head_y - r - 2)
    out.append(f'<text x="{x}" y="{ly:.1f}" class="lbl" text-anchor="middle">{html.escape(label)}</text>')
    return "".join(out)

def extras(ex, figs):
    g=[]
    if "pull" in ex: g.append('<path d="M60 40 L40 30 M100 40 L120 30 M60 62 L40 70 M100 62 L120 70" class="move"/><text x="80" y="10" class="note" text-anchor="middle">풀백 →</text>')
    if "arms" in ex: g.append('<path d="M86 70 L66 50 M130 70 L150 50" class="move"/><text x="150" y="14" class="note" text-anchor="end">0:03 발연기</text>')
    if "monitor" in ex: g.append('<rect x="34" y="52" width="36" height="20" class="mon"/>')
    if "script" in ex: g.append('<rect x="52" y="60" width="16" height="10" class="paper"/>')
    if "walkin" in ex: g.append('<path d="M156 40 L144 40" class="move"/>')
    if "walkout" in ex: g.append('<path d="M128 40 L152 40" class="move"/>')
    if "scatter" in ex: g.append('<path d="M70 66 L52 60 M90 66 L108 60 M80 66 L80 58" class="move"/>')
    if "arm" in ex: g.append('<path d="M0 64 Q14 60 30 66" class="fig dim" style="stroke-width:6;fill:none"/>')
    if "flat" in ex: g.append('<g transform="rotate(-14 96 72)"><rect x="80" y="20" width="34" height="52" class="flat"/></g><path d="M118 22 L104 30" class="move"/>')
    if "mound" in ex: g.append('<path d="M30 74 Q50 40 80 46 Q110 40 130 74Z" class="flat"/><text x="80" y="38" class="note" text-anchor="middle">천 아래에서 허둥댐</text>')
    return "".join(g)

def svg(cut):
    b, figs, ex = S[cut]
    body = bg(b) + "".join(person(*f) for f in figs) + extras(ex, figs)
    band = f'<rect y="{BAND}" width="160" height="{90-BAND}" class="band"/><text x="4" y="{BAND+6}" class="bandt">자막 띠</text>'
    return f'<svg viewBox="0 0 160 90" role="img" aria-label="{cut} 구도 스케치">{body}{band}<rect width="160" height="90" class="frame"/></svg>'

SECT = [("A","극중극 — 가나안 정탐",1,5),("B","감독과 잭",6,17),("C","휴식 — 잭과 맥스",18,30),("D","혼자 남은 잭",31,33),("E","재촬영과 사고",34,37)]
def fmt(t): return f"{t//60}:{t%60:02d}"
t=0; cards={}
for cut,sec,shot,scr,dia,view,who,risk in rows:
    sec=int(sec)
    m=re.match(r"([^:(]+)(?:\(([^)]*)\))?:\s*(.*)",dia)
    if dia=="없음" or dia.startswith("없음"):
        sp, voice, en, ko = "", "", "", dia
    else:
        sp = m.group(1).strip() if m else ""; voice = (m.group(2) or "") if m else ""
        ko = m.group(3).strip() if m else dia
        en = to_en(ko)
    vtag = view.replace("V","LC-001-V") if view.startswith("V") and "→" not in view else ("LC-001-"+view if view.startswith("V") else view)
    card=f'''<article class="cut" id="c{cut.replace("-","_")}">
<header><span class="no">{cut}</span><span class="tc">{fmt(t)}–{fmt(t+sec)} · {sec}초</span><span class="view">{html.escape(vtag)}</span></header>
{svg(cut)}
<p class="shot">{html.escape(shot)}</p>
<p class="act">{html.escape(scr)}</p>
{f'<div class="line"><span class="who">{html.escape(sp)}{(" · "+html.escape(voice)) if voice else ""}</span><p class="en">{html.escape(en) if en else "(영어 줄 확인 필요)"}</p><p class="ko">{html.escape(ko)}</p></div>' if sp else f'<div class="line quiet"><p class="ko">{html.escape(ko)}</p></div>'}
<p class="meta"><b>인물·소품</b> {html.escape(who)}</p>
{f'<p class="risk">{html.escape(risk)}</p>' if risk else ''}
</article>'''
    cards[int(cut.split("-")[1])]=card; t+=sec
sections="".join(f'<section class="seq"><h2><span>{k}</span>{html.escape(n)}<small>{a}–{b}컷</small></h2><div class="grid">{"".join(cards[i] for i in range(a,b+1))}</div></section>' for k,n,a,b in SECT)
page=open(sys.argv[1]).read().replace("<!--CUTS-->",sections).replace("<!--TOTAL-->",fmt(t))
open(sys.argv[2],"w").write(page)
print(len(rows), fmt(t), sum(1 for c in cards.values() if "영어 줄 확인 필요" in c))
