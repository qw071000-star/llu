# real6-C12 "3-1의 모션처럼 3-2 영상" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real5: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | production-session SKILL → ok-reuse.md, OK 대장 3-1 영상 카드 + 3-2 시작 이미지 카드. 카드 35°와 시작 이미지 75mm(32°) 차이 알림(시작 이미지가 이김). 카메라 방향 같아서 좌우·손 안 뒤집음. 끝 상태·타이밍·연기·사건 수·이음새 5항목 제안값. 프롬프트 없음 |
| 2 | PASS | `ACTION_TIMING` 세 줄·`PHYSICS` 네 줄 글자 그대로(motion_3-1.lines 포함). OPTICS 32°. 프롬프트 본문에 "3-1"·"previous shot" 없음. 카드 [7]에 "가져온 OK: 3-1 영상 — 모션(ACTION_TIMING, PHYSICS) …". 할아버지 입 잠금을 ok-reuse §3대로 올림(알림). 위험 목록. 생성 안 함 |

검사기: `check_prompt --kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light+motion_3-1` → `OK — video 프롬프트 5174자, 걸린 항목 없음`
추가 발견: 2턴에 acting/SKILL.md를 엶(연기 줄은 3-1에서 옮긴 것이라 routing.md:25 "OK의 연기 줄을 그대로 쓸 때만 뺀다"에 따르면 불필요). 프롬프트·고정 문장 파일을 `project/log/`에 만듦(시킨 적 없는 파일, 경미).
키트 결함: 없음.
총평: PASS 2 유지, 불필요한 acting 열기만 감점 없이 기록.
