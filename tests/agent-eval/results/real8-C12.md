# real8-C12 "3-1의 모션처럼 3-2 영상" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real7: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | production-session SKILL → ok-reuse.md, 3-1 영상 OK 카드 + 3-2 시작 이미지 카드 + 3-2 핸드오프, live-action.md. 카드 35° vs 시작 이미지 75mm(32°) 충돌을 알리고 시작 이미지를 따름. 가져올 줄: `ACTION_TIMING`·`PHYSICS`·속도 문장, 입 잠금 등 Required·Forbidden. 연기·대사·사건 수·이음새 4항목 제안값+이유 |
| 2 | PASS | `ACTION_TIMING`·`PHYSICS` 글자 그대로(motion_3-1 must 통과), 본문에 "3-1"·"previous shot" 없음(grep 0), 카드 [7] "가져온 OK: 3-1 영상 — 모션(ACTION_TIMING, PHYSICS, 속도 문장) + 연기 (제안값)". 입 잠금을 강한 쪽으로 올림(알림). 위험 5개. 생성 안 함 |

검사기: `--kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light+motion_3-1` → `OK — video 프롬프트 5140자, 걸린 항목 없음`
추가 발견: acting을 안 엶(OK 연기 줄을 그대로 씀, routing.md:25 대로).
키트 결함: 없음.
총평: PASS 2 유지. G1: tools에 mcp__ 없음, generate_* 없음.
