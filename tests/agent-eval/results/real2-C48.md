# real2-C48 — 화면 밖으로 나가기

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 질문 내용은 좋음: 나가는 방향 "화면 왼쪽, 정류장 지붕 끝 쪽"+이유, 끝 상태 "몸 절반이 왼쪽 가장자리 밖, 이미 걷는 중", 사건 3개, 카드 [1]이 "돌아선다"에서 끝남을 먼저 짚음, 3-4 이음새. 감점: 질문 턴에 `acting/SKILL.md`를 `cat video-prompt/SKILL.md video-prompt/live-action.md acting/SKILL.md`로 한 번에 열고 "읽은 것"에도 적음. `routing.md:27`이 "질문 단계는 must-ask로 충분"이라 했다. 질문 9개 중 걸음(5)은 §0 표에서 나온 것이라 허용 |
| 2 ("그대로", 프롬프트 턴) | PASS | 15블록, FINAL_FRAME `half out of frame at the LEFT edge, still walking`, 화면 기준만, 위험 7개, 블록 밖 모드·참조 2·모델·해상도·길이·폴더. 검사기 실제 실행(3번). 카드 [1][3]~[6]에 `(제안값)` 기록 |

검사기(`--kind video --refs 2 --seconds 8 --must-include`, 채점자 재실행): `OK — video 프롬프트 5151자, 걸린 항목 없음`

지난 회차 대비: 부분(검사기 미실행) → 고침. 단 1턴에서 `acting`을 일찍 연 새 흠이 생김(지난 회차 1턴은 열지 않았음).

추가 발견: 없음.

키트 결함
- `context/routing.md:27`의 "영상이면 프롬프트를 쓰는 턴에 연다(질문 단계는 must-ask.md로 충분)"가 표 셀 끝 괄호라 묻힌다(`video-prompt/live-action.md` 앞머리에는 같은 말이 없음). → `video-prompt/live-action.md` 맨 위(또는 SKILL.md §2)에 "질문 턴에는 `acting`을 열지 않는다" 한 줄 추가.

총평: PASS 1 / 부분 1 / FAIL 0 (지난 회차 PASS 1 / 부분 1, 부분의 원인은 바뀜).
