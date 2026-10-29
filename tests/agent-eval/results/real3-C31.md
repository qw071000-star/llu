# real3-C31 — 밤 버전 + 형광등
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | reads: image-prompt SKILL·location.md·location-edit.md(+대장·OK 카드). 시간대(1단계)/형광등 켜기(2단계)로 나누고 "1단계 결과는 아직 '형광등 켜진 밤'이 아닙니다" 알림. 새 LIGHT LOCK을 화면 기준으로 다시 씀(`Faint cool moonlight from screen left, the persimmon-tree side …`), 형광등 위치는 대장에 없어 제안값(정류장 안 가운데, 벤치 위)으로 묻고 PALETTE 80% 황토가 밤과 맞지 않음도 짚음. 질문 4개, 생성 없음 |
| 2 (시나리오 밖) | PASS | 1단계 STATE 프롬프트만. 여는 줄 `Edit <<<loc_busstop_road_v1>>> WITHOUT reframing`(꺾쇠 유지 — real2 WARN **해소**), 형광등 `stays OFF`, 달 화면 밖, 노을 광원 문장은 "바뀌기 전" 서술에만. 코드블록 밖 "바뀐 값 (전 → 후)". 생성 없음 |
검사기(채점자, --kind image --refs 1 --must-include 새 LIGHT LOCK 한 줄): `OK — image 프롬프트 2119자, 걸린 항목 없음`
지난 회차 대비: 부분 2 -> PASS 2(**개선**: 태그 WARN 해소, LIGHT LOCK 화면 쪽 명시).
추가 발견: CHANGE 문장에 `the low dusk sun raking in from screen left … is replaced by …`가 남아 해 질 녘 문장이 프롬프트에 한 번 들어감(상태 전환 서술이라 허용으로 봄).
키트 결함: 없음.
총평: PASS 2 / 부분 0 / FAIL 0
