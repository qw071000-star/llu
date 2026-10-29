# real8-C13 "3-1의 색감과 질감으로 3-5 퍼스트 프레임" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real7: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | ok-reuse.md + image-prompt SKILL + first-frame.md, 3-1 시작 이미지 카드. "3-1 프롬프트에는 색·질감 문장이 따로 없습니다 … 이미지를 색 참조로 붙이고 권한을 좁힘". 카메라 / 손·동작 / 가방 안쪽 / 프레임 / 0:00·3-4 이음새 / 참조 구성 6항목 제안값+이유 |
| 2 | PASS | 참조 4개 = 태그 4개. `<<<ff_3-1_v2>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.` + DO NOT TRANSFER. WARDROBE·PROP·LIGHT LOCK 글자 그대로, `Except: the bag is open …`, `Exactly 1 person is visible …`. 손은 화면 쪽 + 물건. 뺀 PALETTE 문장을 알림. 카드 3-5 v1 작성. 생성 안 함 |

검사기: `--kind image --refs 4 --must-include grandpa+bag+light` → `OK — image 프롬프트 2639자, 걸린 항목 없음`
추가 발견: 1턴에 `ok-reuse.md`를 `production-session/SKILL.md` 없이 바로 엶(routing.md:29 "SKILL.md를 먼저"; 내용 영향 없음, 경미).
키트 결함: 없음.
총평: PASS 2 유지. G1: tools에 mcp__ 없음, generate_* 없음.
