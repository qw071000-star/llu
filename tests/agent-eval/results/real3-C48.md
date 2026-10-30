# real3-C48 — 화면 밖으로 나가기

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 연 것: video-prompt SKILL·live-action.md, 정본(OK 대장 3-3 시작 이미지). `acting` 안 엶(2회차 결함 해소). 질문 8개: 나가는 방향 "화면 왼쪽(시간표가 화면 오른쪽이라 오른쪽은 지나침)", 끝 상태 "몸 절반이 프레임 밖, 이미 걷는 중", 사건 3개, 3-4에 손녀 없음 이음새, 걸음(§0 표). 생성 없음 |
| 2 ("그대로", 프롬프트 턴) | PASS | `acting` 열고 15블록, FINAL_FRAME `half of her body past the left edge of the frame, already walking`. 위험 8개, 블록 밖 모드·참조 2·모델·해상도·길이·소리·폴더. 화면 기준만. 카드 [1][3]~[6]에 `(제안값)` 기록. 검사기 2회 실행 |

검사기(`--kind video --refs 2 --seconds 8 --must-include girl,light`, 채점자 재실행): `OK — video 프롬프트 5428자, 걸린 항목 없음`

2회차 대비: PASS 1/부분 1 → PASS 2. `acting` 조기 열기 해소(routing.md:27 괄호 문장 효과 또는 우연).

추가 발견(경미): 컷 목록 3-3 줄("돌아선다")은 컷 세션이 못 고쳐 핸드오프 [5]에 올린다고 알림(맞음).

키트 결함: 없음.

총평: PASS 2 / 부분 0 / FAIL 0 (2회차 PASS 1 / 부분 1).
