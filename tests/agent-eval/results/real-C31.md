# real-C31 — 밤 버전 + 형광등
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | location.md+location-edit.md. 시간대와 광원 켜기를 두 생성(V2 형광등, V3 밤)으로 나눠 제안(location-edit 규칙 1줄과 일치), 새 LIGHT LOCK을 새로 쓴다고 알림, 질문 먼저 |
| 2 (시나리오 밖) | PASS | 1단계 STATE 프롬프트: `switched off becomes switched on`, `lit but does NOT glow`, 해 질 녘 해는 PRESERVE에 유지(바뀌지 않는 광원), 생성 안 함 |
검사기(채점자): `OK — image 프롬프트 1587자, 걸린 항목 없음`
추가 발견: 형광등 위치(지붕 아래, 벤치·바닥만 비춤)를 이미지 없이 지어냄 — "추정"이라 적음. 밤 LIGHT LOCK의 화면 쪽(형광등이 화면 어느 쪽)은 2단계로 미룸.
키트 결함: location-edit.md에 "형광등 켜기+밤"처럼 나눈 뒤 첫 단계의 최종 결과가 사용자가 요청한 '밤'이 아님을 알리는 문장이 없다 -> 규칙 1줄에 "나누면 1단계 결과는 요청한 상태가 아님을 사용자에게 한 줄 알린다" 추가.
총평: PASS 2 / 부분 0 / FAIL 0
