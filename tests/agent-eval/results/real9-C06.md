# real9-C06 새 소품 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt` SKILL + `prop.md`. PR-002 매김. 시트 여부 / 재질·크기(15×20cm, 할아버지 손바닥 기준)·사용 흔적 / 사진 내용 / 무게 물성 / 나오면 안 되는 것 / 상태·손(`the screen-left hand, nearer the persimmon tree`, "추정") 6항목 제안값+이유. 모델·1k·16:9·`fld-props`는 "기본값으로 씀". 컷 목록·연속성 표는 건드리지 않고 제안만 |
| 2 | PASS | 소품 틀: `Photorealistic product-reference photograph … isolated on a plain seamless light grey studio background, nothing else in frame — no scene, no room, no other objects, no hands, no people … Avoid: …`. 위험 5개+막는 문장, 대장에 PR-002 표+고정 설명문 `초안(제안값)` 기록(diff 확인). 생성 안 함 |

검사기: `check_prompt.py --kind image` → `OK — image 프롬프트 791자, 걸린 항목 없음`
추가 발견: 없음. (`prop.md` "고정 설명문은 재질·모양·크기·사용 흔적만" — 사진 내용이 설명문에 들어갔으나 소품 정체성이라 허용 범위.)
키트 결함: 없음.
총평: real8과 같은 PASS 2. G1: mcp__ 없음, 생성 없음.
