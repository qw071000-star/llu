# real-C48 — 화면 밖으로 나가기

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | reads: 3-3 카드, shot-list, video-prompt, live-action.md. 질문 6개: 나가는 방향("화면 왼쪽, 벤치·정류장 쪽" + 이유), 끝 상태("몸의 절반이 화면 왼쪽 밖, 이미 걷는 중"), 타이밍, 시선·손, 소리, 이음새(3-4는 손녀 없음). 사건 수 3개 확인 명시. 컷 카드 [1]이 "돌아선다"에서 끝남을 먼저 짚고 `(제안값)`으로 고침 |
| 2 ("그대로", 프롬프트 턴) | 부분 | acting 열고 15블록, FINAL_FRAME에 `body half beyond the left edge, mid-stride`, 화면 기준만 사용, 위험 6개, 블록 밖 정보 완비. 검사기 미실행(밝힘). 시작 이미지 위치는 "추정" 표기. |

검사기(`--kind video --refs 2 --seconds 8 --must-include girl+light`): `OK — video 프롬프트 5253자, 걸린 항목 없음`

키트 결함: 검사기 실행 권한(C44 참조).
총평: PASS 1 / 부분 1 / FAIL 0.
