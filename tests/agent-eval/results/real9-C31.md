# real9-C31 장소 시간대 바꾸기 — "밤으로, 형광등 켜진 걸로" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`location.md`+`location-edit.md` Read(`location-view.md` 안 열림). 변경이 둘로 읽힘을 짚고 나눔(`kit/skills/image-prompt/location-edit.md:17`): "① 노을을 밤으로, ② 그 결과에서 형광등을 켭니다 … 시간대와 광원 켜기는 따로 뗄 수 있어서". `1단계 결과는 아직 "형광등 켜진 밤"이 아니라, 형광등이 꺼진 밤입니다.`(규칙 알림 충족). 새 광원 LIGHT LOCK을 화면 기준으로 제안(`화면 왼쪽, 감나무 쪽에서 약한 푸른 달빛`), 형광등 위치를 물건 기준(`지붕 아래 천장 한가운데, 벤치 바로 위`)으로 제안. 새 판 `LC-001-V2`(STATE). 질문 먼저, 생성 없음 |
| 2 | PASS | 1단계 LOCKED EDIT: `CHANGE — time of day, sky and key light`, `dim, cool blue moonlight from screen left, the persimmon-tree side … fluorescent tube stays off`, PRESERVE의 `fluorescent tube, unlit`, 해 질 녘 LIGHT LOCK 문장을 남기지 않음, 시대 잠금 줄. 블록 밖 모드·참조·모델·1k·`fld-locs`, 바뀐 값 전 → 후, 위험 5개. 대장에 `초안(제안값)`. 생성 안 함 |

## 검사기
내 실행 `--kind image --refs 1`: `OK — image 프롬프트 1632자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음. 첫 검사 호출이 `.claude/skills/image-prompt/../higgsfield-generation/…` 경로였고 한 번 더 정식 경로로 다시 돌림(지침 검사 줄은 단독·상대 경로) — 경미.
- 검사에 `--must-include`로 Era lock만 넣고 새 LIGHT LOCK은 "편집으로 바뀐다"며 뺌 — 적절.

## 키트 결함
없음.

## 총평
시간대와 광원 켜기를 두 생성으로 나누고 1단계가 최종 모습이 아님을 알림 — 규칙 충족.
