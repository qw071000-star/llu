# real-C12

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | production-session/ok-reuse.md → video-prompt live-action 열람, 3-1 영상 카드 사용. ACTION_TIMING·PHYSICS 글자 그대로 나열, 렌즈 "카드의 35°와 시작 이미지 75mm(약 32°)가 다릅니다…시작 이미지를 따라". 질문 5개 한 묶음. acting 스킬 안 염(OK 연기 줄 재사용이라 맞음) |
| 2 | PASS | 프롬프트 코드블록 하나, 블록 밖에 모드·참조4·모델·해상도·길이·폴더. 본문에 "3-1" 없음. 컷 카드 [7] "가져온 OK: 3-1 영상 — 모션(ACTION_TIMING, PHYSICS), 연기 줄…" 기록. 입 잠금·카메라 응시 Forbidden 이월. 검사: 플레이어는 승인 거부로 못 돌림(정직히 고지). 내가 돌림: `OK — video 프롬프트 5169자, 걸린 항목 없음` (--refs 4 --seconds 8 --must-include grandpa+girl+bag+light+motion_3-1) |

**PASS 2 / 부분 0 / FAIL 0**

추가 발견: 답에 "scratchpad의 must32.txt" 같은 내부 파일 언급은 사용자에게 불필요.
키트 결함: 하네스 check_prompt 실행 권한(C11 참고). 키트 문서 결함 없음.
총평: 키트 따라 정확. 모션 줄 글자 일치, 렌즈 충돌 고지, 검사 통과.
