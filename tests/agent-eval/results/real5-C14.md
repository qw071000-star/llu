# real5-C14 "표정은 2-1처럼, 2-2 영상" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real4: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | production-session/ok-reuse.md + 2-1 영상 카드, video-prompt SKILL + live-action.md. "CHARACTER_ACTING 표정·시선 줄과 범위 문장만, 엄지·낙엽은 안 가져옴". 시작 이미지 85mm = 29°. 3항목(동작·횟수·구간 / 끝 상태 / 대사) 제안값+이유. acting 안 엶(OK 연기 줄 그대로 쓰므로 맞음) |
| 2 | PASS | GRANDPA 연기 줄이 `acting_2-1.lines`와 글자 그대로, `He never looks at the camera.`, 입 잠금 강화를 "전 → 후" 알림, 손 `the screen-left hand, nearer the tree`(검사 중 화면 쪽이 빠진 3곳을 고침), `Exactly 1 person`. 블록 밖 모드·참조 3·모델·해상도·길이·소리·폴더. 카드 2-2 v0 `(제안값)`. 검사 4회 실행. 생성 안 함 |

검사기: `--kind video --refs 3 --seconds 8 --must-include grandpa+bag+light+acting_2-1`: `OK — video 프롬프트 4893자, 걸린 항목 없음`

추가 발견: 없음. (real4의 "요소 이름 질문" 군더더기 사라짐)

키트 결함: 없음.

총평: real4와 같은 PASS 2.

G1: 모든 턴 tools가 Bash/Write/Edit/Grep뿐, `mcp__` 호출 없음, `generate_*` 없음.
