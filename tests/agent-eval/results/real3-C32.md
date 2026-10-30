# real3-C32 — "오른손에 우산"
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | reads: 3-1 카드·핸드오프, image-prompt SKILL·first-frame.md·prop.md(+production-session), ok-cuts. 질문 5개: 승인 컷 새 테이크 대체(#1), 어느 손(#2: 화면 오른쪽 손이 시간표를 짚으므로 우산은 화면 왼쪽·사인에서 먼 손 제안, 인물 기준이면 알려 달라, "추정"), 우산 사양(새 소품, 대장에 없음)·크기, 시트 여부. 사용자 "오른손"을 화면 오른쪽 그대로 쓰지 않고 충돌을 짚어 반대 손 제안 — 근거 있어 허용. 경미: 작은 소품인데 prop.md를 염(routing 표에 없는 열기) |
| 2 | 부분 | 인물 기준 오른손 -> 손녀가 화면 오른쪽 사인을 향하니 길(카메라) 쪽 손으로 풀고 "손 방향 (추정)" 적음. `her right hand` 없음, 동서남북 없음, LOCKED EDIT, 위험 6개, 3-1 영상 재제작·3-2/3-3 이음새 알림, 생성 안 함, 카드 [5] 기록. 그러나 프롬프트가 `the empty road-side hand, the hand toward the foreground road edge and not the hand tracing the printed times`로 `screen-left/right`가 없고, 1턴에서 말한 "화면 왼쪽 손, 사인에서 먼 손"과도 어느 손인지 맞춰지지 않음. 지침 6번은 `the screen-left hand, farther from the sign`처럼 화면 쪽 + 물건을 요구 |
검사기(채점자, --kind image --refs 1 --must-include girl+grandpa+light): `OK — image 프롬프트 1919자, 걸린 항목 없음` (검사기는 `road-side hand` 표현을 못 잡음 — 오탐 아님, 검사기 사각)
지난 회차 대비: PASS1/부분1 -> PASS1/부분1 유지. `nearer the camera`는 사라졌으나 같은 유형(화면 쪽 누락)이 `road-side hand`로 재발.
추가 발견: 없음.
키트 결함: (1) `instructions.md:28`이 옆모습이면 "물건 기준"만 허용해 `road-side hand` 같은 화면 쪽 없는 표현이 통과함 -> "옆모습이어도 `screen-left/right`는 붙이고 물건을 더한다(`the screen-left hand, farther from the sign`)"로. (2) `higgsfield-generation/check_prompt.py:50~58` 손 패턴이 `-side hand`·`hand toward`를 안 잡음 -> `\b\w+-side hand\b`와 `hand (?:toward|facing)`에 화면 쪽 없으면 WARN 추가.
총평: PASS 1 / 부분 1 / FAIL 0
