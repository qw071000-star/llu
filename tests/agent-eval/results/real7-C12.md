# real7-C12 "3-1의 모션처럼 3-2 영상" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real6: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | production-session SKILL → ok-reuse.md, 3-1 영상 OK 카드 + 3-2 시작 이미지 카드 + 3-2 핸드오프. 카드 35°와 시작 이미지 75mm(≈32°) 충돌을 알리고 시작 이미지를 따름. 가져올 것: `ACTION_TIMING`·`PHYSICS` 그대로, 카메라는 안 가져옴. 타이밍·끝 상태·동선·시선·대사·연기·렌즈·이음새 8항목 제안값+이유(렌즈는 알림 성격) |
| 2 | PASS | `ACTION_TIMING` 3줄·`PHYSICS` 4줄 글자 그대로(motion_3-1 일치, 검사 통과). 3-1 Required·Forbidden의 두 사람·대사 1회·가방 닫힘·할아버지 무발화 이동. 본문에 "3-1"·"previous shot" 없음. 카드 [7] "가져온 OK: 3-1 영상 — 모션 …". 입 잠금을 ok-reuse §3 예외대로 올림(알림). 전 → 후 목록, 위험 목록. 생성 안 함 |

검사기: `--kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light+motion_3-1` (답 코드블록) → `OK — video 프롬프트 5389자, 걸린 항목 없음`
추가 발견: acting을 안 엶(OK 연기 줄을 그대로 쓰므로 routing.md:25 대로, real6의 불필요 열기 해소). 검사용 임시 파일은 스크래치로 옮김.
키트 결함: 없음.
총평: PASS 2 유지. G1: tools에 mcp__ 없음, generate_* 없음.
