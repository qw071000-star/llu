# real9-C25 같은 쪽 클로즈업 새 시점 — 시간표 표지판 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`location.md`+`location-view.md` Read. 소품 확대 뷰(계보 PROP, 부모 `job-lc001v1`). 5개 제안값(높이 1.6m·경로 3m·랜드마크 3개·렌즈·표지판 면)을 한 묶음 질문. 감나무·벤치는 프레임 밖, 표지판 글자 안 읽히게. 대장 LC-001 `초안(제안값)` 줄에는 사용자 말만 기록. 프롬프트·생성 없음 |
| 2 | PASS | 틀 C 순서 그대로: `Using <<<loc_busstop_road_v1>>> as the exact same bus stop and the exact same timetable sign, generate a CONTEXT CLOSE-UP`, `Do not inherit its camera angle, framing or composition.`, `Move in from the same side and along the same line of sight; no reverse angle and no view from behind.`, `newly observed direction` 문장 없음, `Any lettering on it: text not legible. No legible text anywhere.`, 랜드마크 3개(셸터 오른쪽 끝·표지판 기둥·낮은 언덕). LIGHT LOCK `Low dusk sun from screen left, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off.` 글자 그대로. 블록 밖 모드·참조·모델·1k·16:9·`fld-locs`, 위험 6개 |

## 검사기
내 실행 `--kind image --refs 1 --must-include light.lines`: `OK — image 프롬프트 1909자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인.
- 프롬프트에 `In this view the shelter is at screen LEFT and the sign is at screen RIGHT` 같은 화면 기준 명시는 없고 `screen-right half`, `screen-left edge`로 대신함(기준 위반 아님).
- 위험 5번에서 "크기와 위치 수치는 대략만 지켜진다 … 결과를 본 뒤 재서 보고"라고 추정 표시(규칙 10 충족).

## 키트 결함
없음.

## 총평
같은 쪽 접근 조건 문장·글자 읽힘 방지·LIGHT LOCK 모두 충족.
