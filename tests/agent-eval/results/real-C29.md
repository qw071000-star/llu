# real-C29 — 한 줄에 동작 여럿
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 사건 4개 세고 샷 A/B 분할, 시작 이미지 없음 -> 퍼스트 프레임부터, "왼쪽"=화면 왼쪽(감나무). 질문만, 생성 없음. 그러나 `video-prompt`를 열지 않음(reads: production-session, ok-cuts + Bash). SKILL.md §2의 "나가기는 끝·첫 프레임 상태로 쓴다"를 놓침: 샷 B를 "돌아서 걸어 나간다"로 둠 |
| 2 (시나리오 밖) | PASS | "그대로"를 수락으로 받아 퍼스트 프레임 프롬프트(틀 1)만 씀, 보낼지 물음. 화면 쪽+물건 사용 |
검사기(채점자, --kind image --refs 3 --must-include bag+light+grandpa): `OK — image 프롬프트 1913자, 걸린 항목 없음`
추가 발견: 임의로 새 컷 `3-7`을 만들고 project/cuts/3-7.md 작성(총괄 확인 필요라고 알림).
키트 결함: routing.md 1행 "컷 번호만 -> production-session"이 먼저 걸려 영상 요청인데 video-prompt를 안 연다 -> routing.md §3에 "영상 요청이면 시작 이미지·컷 번호가 없어도 video-prompt/SKILL.md §0·§2 표는 연다"를 추가.
총평: PASS 1 / 부분 1 / FAIL 0
