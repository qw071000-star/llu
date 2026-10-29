# real2-C32 — "오른손에 우산"
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | reads: 3-1 카드, image-prompt SKILL·first-frame.md, ok-cuts. 질문 4개: 승인 컷 새 테이크 대체(Q1), 손(Q2), 우산 사양(검은 천·나무 손잡이·70cm, 대장에 없어 새 소품이라 밝힘), 든 방식. Q2는 화면 오른쪽 손이 시간을 짚고 있어 우산은 반대 손(화면 왼쪽)이 맞다고 제안하고 "인물 기준이면 추정"이라 적음 — 사용자 말(오른손)과 다른 제안이나 근거를 달아 확인을 구함(결과적으로 사용자 답이 인물 기준이었음). 생성 없음 |
| 2 | 부분 | 인물 기준 오른손 -> 시간표를 보고 서 있는 옆모습이라 카메라 쪽 손으로 풀고 "손 해석 (추정)" 적음. `her right hand` 없음, 동서남북 없음, LOCKED EDIT, 위험 6개, 3-1 영상 재제작·3-2 맞춤 알림, 생성 안 함. 그러나 프롬프트가 `the umbrella is in her hand nearer the camera`로 화면 쪽(screen-left/right) 없이 씀(지침 6번 "손은 화면 쪽 + 화면 속 물건") |
검사기(채점자, --kind image --refs 1 --must-include girl+grandpa+light): `WARN  'her hand nearer the camera,'에 화면 쪽이 없다. 'the screen-left hand, nearer the …'처럼 화면 쪽 + 물건으로 쓴다 — FAIL 0 · WARN 1 · 1759자`. 플레이어는 "옆모습이라 화면 좌우로 가를 수 없다"며 유지(숫자 1759자 적음) — 오탐 아님: 옆모습이어도 카메라 쪽 손은 화면 쪽+물건(예: 시간표에서 먼 손 `the hand farther from the sign`)으로 쓸 수 있음.
지난 회차 대비: 지난 PASS 2 -> 이번 PASS 1 / 부분 1(2턴 손 표기 **후퇴**).
추가 발견: 프롬프트 첫 인자 `<<<job-ff-3-1>>>`(job ID를 태그로) — 검사기는 통과.
키트 결함: `instructions.md:28`(규칙 6)에 옆모습·정면/등 구분이 없어 "카메라에 가까운 손"이 허용 표현처럼 보임 -> "옆모습이면 `the hand nearer the [화면 속 물건]` / `the hand farther from the sign`처럼 화면 속 물건 기준으로 쓴다. `nearer the camera`만은 안 된다" 추가.
총평: PASS 1 / 부분 1 / FAIL 0
