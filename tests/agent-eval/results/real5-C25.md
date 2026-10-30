# real5 C25

**PASS 2 / 부분 0 / FAIL 0** (real4 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `location.md`+`location-view.md`. 부모 V1, 같은 쪽 다가가기, 거리 2m(가정 명시)·높이 1.6m·랜드마크 3개·표지판 상태·LIGHT LOCK 글자 그대로. 프롬프트 없음 |
| 2 | PASS | `Do not inherit …`, `Use <<<…>>> as the sole geometry and design authority`, `Move in from the same side; no reverse angle and no view from behind.`, `newly observed direction` 없음, `text is not legible`, 랜드마크(지붕 모서리·기둥·산등성이), `In this view the shelter corner is at screen left and the timetable sign is at screen right.`, LIGHT LOCK 글자 그대로 마지막 줄. 단 틀 B가 아니라 틀 C(소품 확대)를 써서 시나리오의 정확한 문장(`… and along the same line of sight; …`)은 CAMERA에 `along the same line of sight`로 흩어져 있음. 키트 표('소품 확대 = 틀 C')를 따른 것이라 PASS |

## 검사기
내 실행(`--kind image --refs 1 --must-include light`): `OK — image 프롬프트 2137자, 걸린 항목 없음`

## 추가 발견
없음.

## 키트 결함
`image-prompt/location-view.md:80~` 틀 C에는 같은 쪽 접근 고정 문장(`Move in from the same side and along the same line of sight; no reverse angle …`)이 없어 표지판 확대에서 문장이 제각각 → 틀 C CAMERA 아래에 그 줄(69줄과 같은 문장)을 넣거나 시나리오를 틀 C로 고친다(기대 오류 가능).
