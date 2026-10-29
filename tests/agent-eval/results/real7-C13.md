# real7-C13 "3-1의 색감과 질감으로 3-5 퍼스트 프레임" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real6: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | ok-reuse.md + first-frame.md, 3-1 시작 이미지 카드. "3-1 프롬프트에는 색·질감 문장이 없다 … 문장을 새로 쓰지 않고 이미지를 색 참조로 붙이고 권한을 색·그레이드·대비·질감으로 좁힘". 모드(틀 2) / 카메라 / 인원 / 0:00 손·가방(열림) / 3-4 이음 5항목 제안값 |
| 2 | PASS | 참조 4개 = 태그 4개. `<<<ff_3-1_v2>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.` + DO NOT TRANSFER. WARDROBE·PROP·LIGHT LOCK 글자 그대로, `Exactly 1 person is visible.`, 손은 `the screen-left hand, nearer the bag's brass clasp`. "그대로"인데 카메라 높이를 무릎 높이 → 가슴 높이 30°로 바꾼 것을 첫 줄에 알림(허용 범위). 카드 3-5 v0 작성. 생성 안 함 |

검사기: `--kind image --refs 4 --must-include bag+light` 및 `grandpa+bag+light` (답 코드블록) → 둘 다 `OK — image 프롬프트 2691자, 걸린 항목 없음`
추가 발견: 없음.
키트 결함: 없음.
총평: PASS 2 유지. G1: tools에 mcp__ 없음, generate_* 없음.
