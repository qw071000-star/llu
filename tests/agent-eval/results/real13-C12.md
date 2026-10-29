# real13-C12 "3-1의 모션처럼 3-2 영상" (2턴) — PASS 1 / 부분 1 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | `production-session`→`ok-reuse.md`, 3-1 영상 카드 하나만. 질문 2개(사건 4개 유지 / 연기 문장 3-1 그대로)와 "알 둘 것": 렌즈 35° vs 시작 이미지 75mm(32°) 시작 이미지 우선, 같은 쪽이라 좌우 안 뒤집음. 카드 [4][5][6][7] 기록(질문 턴이지만 받은 답 아닌 제안값을 기록). 감점: 첫 줄이 "**시작 보고**"라 "[16]번 다른 OK처럼으로 진행합니다."가 없음. 또 사건 4개(>3)를 "쪼개라" 규칙(`must-ask.md` 13번 행)에도 유지를 제안 — 플래그는 했으므로 허용 |
| 2 | PASS | `ACTION_TIMING`·`PHYSICS` 3-1 문장 글자 그대로(`motion_3-1.lines` 통과), 본문에 "3-1"·"previous shot" 없음. 카메라·렌즈 32°·위치는 3-2 기준, 할아버지 입 잠금 `no parted lips, no mouthing`(3-1보다 강화, 전 → 후로 보고). 카드 [7] "가져온 OK: 3-1 영상 — 모션…" 기록(diff). 생성 안 함 |

검사기: `--kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light+motion_3-1` → `OK — video 프롬프트 5236자, 걸린 항목 없음`
추가 발견: 그루터기 없음. CHARACTER_ACTING도 3-1 OK 문장 재사용(`acting` 안 열어도 되는 경우).
키트 결함: 첫 줄 누락(C01과 같은 원인). `must-ask.md` 13번 행 "more than 3 events → split"과 ok-reuse의 "3-1과 같게" 가 부딪쳐 플레이어가 4개 유지를 제안 → `ok-reuse.md`에 "가져온 모션이 4사건이면 제안값은 분할"을 한 줄 추가.
총평: 내용 정확, 첫 줄 누락 1턴 부분.
