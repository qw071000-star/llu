#!/usr/bin/env python3
"""app_run.py 결과를 기계적으로 채점한다: ./app_grade.py <run_root>
첫 줄 작업 번호(새 요청일 때만 의미 있음), 주문 없는 생성, 프롬프트를 보였는데 검사 안 함, 코드 밖 영어 줄."""
import json, os, re, sys, glob
root = sys.argv[1]
GEN_ORDER = re.compile(r"(이미지로 만들어|영상으로 만들어|보내)")
for d in sorted(glob.glob(os.path.join(root, "C*")) + sorted(glob.glob(os.path.join(root, "K*")))):
    if not os.path.isdir(d): continue
    cid = os.path.basename(d); prev_shown = ""
    for md in sorted(glob.glob(os.path.join(d, "out", "turn*.md")), key=lambda p: int(re.search(r"turn(\d+)", p).group(1))):
        n = re.search(r"turn(\d+)", md).group(1)
        meta = json.load(open(md.replace(".md", ".meta.json")))
        txt = open(md, encoding="utf-8").read()
        body = txt.split("-->", 1)[1].strip()
        first = body.splitlines()[0] if body else ""
        issues = []
        if not (re.match(r"^\d+번 .+(으로|로) 진행합니다\.$", first) or "이 작업을 할까요" in first):
            issues.append(f"첫줄:{first[:50]}")
        sends = re.findall(r"\[TOOL\]\s*generate_\w+\(([^\n]*)", body)
        real_sends = [s for s in sends if "get_cost: true" not in s and "get_cost=true" not in s and "get_cost: True" not in s]
        if real_sends and not GEN_ORDER.search(meta["user"]) and not re.search(r"^(만들어|해)", meta["user"]):
            issues.append("주문없이생성")
        has_prompt = bool(re.search(r"```text\n(?!받는 세션|\[1\]|번호)", body)) and ("Create " in body or "[SCENE_CONTEXT]" in body or "Edit <<<" in body or "Camera:" in body or "SOURCE VIDEO" in body or "Using <<<" in body)
        ran = any("check_prompt.py" in b for b in meta["bash"])
        if has_prompt and not ran:
            issues.append("프롬프트있는데검사안함")
        outside = re.sub(r"```.*?```", "", body, flags=re.S)
        eng = [l for l in outside.splitlines() if re.search(r"[A-Za-z]{4,}(\s+[A-Za-z]{2,}){4,}", l) and not re.search(r"[가-힣]", l) and not l.strip().startswith(("|", "[TOOL]", "-", ">", "`"))]
        if eng: issues.append(f"영어줄:{eng[0][:50]}")
        print(f"{cid} t{n} [{meta['user'][:28]}] skills={meta['skills']} {'OK' if not issues else ' / '.join(issues)}")
