#!/usr/bin/env python3
"""생성 전에 프롬프트를 기계적으로 검사한다. 과거 실수(reference/error-registry.md)를 규칙으로 옮긴 것이다.

사용법:
  python3 check_prompt.py --kind video prompt.txt [--refs 3] [--seconds 8] [--must-include fixed.txt]
  python3 check_prompt.py --kind image prompt.txt [--refs 2] [--must-include fixed.txt]

--refs          실제로 붙일 참조 요소 수. 프롬프트 속 <<<...>>> 태그 수와 비교한다.
--seconds       영상 길이(초). 없으면 프롬프트의 "NN seconds"에서 읽는다.
--must-include  한 줄에 하나씩, 프롬프트에 글자 그대로 들어가야 할 고정 문장(에셋 대장 문장).

결과: FAIL(보내기 전에 반드시 고친다) / WARN(고치거나, 그대로 둘 이유를 한 줄 적는다). FAIL이 있으면 종료 코드 1.
"""
import argparse
import re
import sys

BLOCKS_15 = [
    "SCENE_CONTEXT", "ACTIVE_REFERENCES", "LOCATION_MAP", "FIRST_FRAME_AND_SPATIAL_BLOCKING",
    "FORMAT_MODE", "OPTICS", "CAMERA", "ACTION_TIMING", "CHARACTER_ACTING", "PHYSICS",
    "LIGHTING", "AUDIO", "STYLE", "QUALITY", "REQUIRED_AND_FORBIDDEN_CONSTRAINTS",
]


def find(pattern, text, flags=re.IGNORECASE):
    return re.findall(pattern, text, flags)


def check_common(text, args, out):
    if len(text) > 8000:
        out.append(("WARN", f"길이 {len(text)}자. 뒤쪽 문장이 약해진다(E-29). 반복을 지우고 사건 수를 줄인다"))
    elif len(text) > 5000:
        out.append(("WARN", f"길이 {len(text)}자. 5,000자 안팎이 안전했다(E-29)"))

    placeholders = find(r"\[(?:\s*|N|NN|NAME|PERSON(?: 2)?|OBJECT|PROP|[^\]\n]*[가-힣][^\]\n]*)\]", text, 0)
    if placeholders:
        out.append(("FAIL", f"채우지 않은 빈칸 {len(placeholders)}개: {', '.join(sorted(set(placeholders))[:5])}"))

    stale = find(r"same as (?:before|the previous)|as in the previous (?:shot|clip|cut)|continu(?:e|ing) from the previous|앞과 같|이전과 같|계속해서", text)
    if stale:
        out.append(("WARN", f"이전 샷을 가리키는 말 {stale[:3]}. 새 생성에는 그 내용을 직접 쓴다(E-43)"))

    tags = set(re.findall(r"<<<\s*([^>]+?)\s*>>>", text))
    if args.refs is not None and tags and len(tags) != args.refs:
        out.append(("FAIL", f"프롬프트 속 참조 태그 {len(tags)}개, 붙일 참조 {args.refs}개. 정확히 맞춘다"))

    if args.must_include:
        with open(args.must_include, encoding="utf-8") as f:
            for line in (l.strip() for l in f):
                if line and line not in text:
                    out.append(("FAIL", f"고정 문장이 글자 그대로 들어 있지 않다: {line[:60]}…"))


def check_video(text, args, out):
    if find(r"\b\d{2,3}\s?mm\b|\bf/\d|\bT\d\.\d\b|\b(?:Cooke|Zeiss|ARRI|Alexa|Panavision|Kodak Vision)\b", text):
        out.append(("WARN", "렌즈 mm·조리개·장비명은 영상 모델이 듣지 않는다. 대각 화각(도) + 관찰 결과 3개로 쓴다"))

    has_people = "[SCENE_CONTEXT]" in text or find(r"\b(?:hands?(?!-)|walks?|steps?|turns? (?:to|toward))\b", text)
    if has_people and find(r"\b(?:left|right)\b", text) and "SCREEN direction" not in text:
        out.append(("WARN", "좌우를 썼는데 좌표 문장이 없다: 'LEFT and RIGHT are SCREEN directions.'(E-14)"))
    if find(r"\b(?:left|right) hand\b|오른손|왼손", text):
        out.append(("WARN", "'오른손/왼손'은 인물 기준으로 읽힌다. 화면 속 물건 기준('신발장 쪽 손')으로 쓴다(E-14)"))

    if find(r"about to speak|almost (?:says|speaks)|tries to speak|starts to say|on the verge of speaking|말하려다", text):
        out.append(("WARN", "'말하려다 만다'는 입술을 움직이게 한다. 말하려는 시도 자체를 없애고 숨·손으로 쓴다(E-35)"))

    moves = find(r"(?<!no )(?<!No )(?<!without )\b(orbit(?:s|ing)?|dolly|crane|push(?:es)?[- ]in|tracking shot|arc(?:s|ing)? around)\b", text)
    static = find(r"\b(?:locked|tripod|static camera|fixed camera)\b", text)
    if moves and static:
        out.append(("WARN", f"고정 카메라와 움직임({', '.join(sorted(set(m.lower() for m in moves)))})이 함께 있다. 한 생성에 카메라 동작 하나"))

    seconds = args.seconds
    if seconds is None:
        m = re.search(r"(\d{1,2})\s*seconds?\b", text, re.IGNORECASE)
        seconds = int(m.group(1)) if m else None
    if seconds and seconds > 15:
        out.append(("WARN", f"길이 {seconds}초. 15초를 넘으면 둘로 나눈다(E-25)"))

    if "[SCENE_CONTEXT]" in text:
        pos = [text.find(f"[{b}]") for b in BLOCKS_15]
        missing = [b for b, p in zip(BLOCKS_15, pos) if p < 0]
        if missing:
            out.append(("WARN", f"15블록 중 빠진 제목: {', '.join(missing)} (쓸 게 없어도 제목은 남긴다)"))
        present = [p for p in pos if p >= 0]
        if present != sorted(present):
            out.append(("WARN", "15블록 순서가 바뀌었다"))

    ranges = re.findall(r"(\d+):(\d{2}(?:\.\d)?)\s*[–-]\s*(\d+):(\d{2}(?:\.\d)?)", text)
    spans = sorted((int(a) * 60 + float(b), int(c) * 60 + float(d)) for a, b, c, d in ranges)
    timing = [s for s in spans if s[1] > s[0]]
    for (s1, e1), (s2, e2) in zip(timing, timing[1:]):
        if s2 > e1 + 0.05:
            out.append(("WARN", f"시간 구간 사이가 비었다: {e1:g}초 ~ {s2:g}초. 빈 구간은 모델이 멋대로 채운다"))
            break

    if find(r"\bgradually (?:becomes|turns|changes)|\btransforms? into\b|\bmorphs? into\b|점점", text):
        out.append(("WARN", "전환을 썼다. 시작 상태와 끝 상태를 고정하고, 사이가 길면 생성을 나눈다"))


def check_image(text, args, out):
    if "WITHOUT reframing" in text and find(r"new view|Do not inherit its camera", text):
        out.append(("FAIL", "LOCKED EDIT(WITHOUT reframing)와 DERIVED VIEW(new view)가 섞였다. 둘 중 하나만"))
    has_change = re.search(r"^CHANGE\b", text, re.MULTILINE) is not None
    has_only = "ONLY CHANGE" in text
    if has_change != has_only:
        out.append(("WARN", "CHANGE와 ONLY CHANGE는 함께 쓰고 같은 항목을 적는다"))
    if find(r"--ar\b|--v \d|--style\b|::\d", text):
        out.append(("FAIL", "다른 도구 문법(--ar, ::가중치)이 있다. 지우고 화면비는 설정으로"))
    if find(r"\bmannequin\b", text) and not find(r"ghost[- ]mannequin", text):
        out.append(("WARN", "'mannequin'만 쓰면 플라스틱 마네킹이 나온다. 'hollow ghost-mannequin, invisible person'"))
    if "HEADLESS" in text and "not an injury" not in text:
        out.append(("WARN", "머리 없는 패널에 'not an injury … no wound' 문장이 없다. 목 단면이 상처처럼 나온다"))
    if find(r"composition only|only (?:for )?the composition|구도만", text) and not find(r"reproduce|exact same photograph|\d+\s?%", text):
        out.append(("WARN", "'구도만 참조'로는 구도가 따라오지 않는다. 좌표를 적거나 '그대로 재현 + 바꿀 것 목록'으로(E-20)"))


def main():
    p = argparse.ArgumentParser(description="생성 전 프롬프트 검사")
    p.add_argument("file")
    p.add_argument("--kind", choices=["video", "image"], required=True)
    p.add_argument("--refs", type=int)
    p.add_argument("--seconds", type=int)
    p.add_argument("--must-include")
    args = p.parse_args()

    with open(args.file, encoding="utf-8") as f:
        text = f.read()
    out = []
    check_common(text, args, out)
    (check_video if args.kind == "video" else check_image)(text, args, out)

    if not out:
        print(f"OK — {args.kind} 프롬프트 {len(text)}자, 걸린 항목 없음")
        return 0
    for level, msg in out:
        print(f"{level}  {msg}")
    fails = sum(1 for level, _ in out if level == "FAIL")
    print(f"— FAIL {fails} · WARN {len(out) - fails} · {len(text)}자")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
