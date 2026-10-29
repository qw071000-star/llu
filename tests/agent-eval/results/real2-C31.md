# real2-C31 — 밤 버전 + 형광등
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | reads: 대장, decisions, image-prompt SKILL·location.md·location-edit.md. 시간대(1단계)와 형광등 켜기(2단계)를 둘로 나누고 "1단계 결과는 아직 요청하신 '형광등 켜진 밤'이 아닙니다" 알림(지난 회차 결함 **고쳐짐**). 새 LIGHT LOCK을 새로 쓴다고 알림, 이름 `LC-001-V2`. 질문 4개 한 묶음, 생성 없음. 그러나 제안한 새 LIGHT LOCK `Cold fluorescent light from the shelter's single tube, above the bench inside the shelter, is the only key.`에 화면 쪽이 없음(시나리오: "지배광=형광등, 화면 어느 쪽"). 형광등 위치는 대장에 없어 가정이라고 밝힘 |
| 2 (시나리오 밖) | 부분 | 1단계 STATE 프롬프트만. 해 질 녘 문장은 CHANGE의 "바꾸기 전" 서술에만 쓰고 PRESERVE에서 뺌, `tube stays OFF`, 달·별 금지. 생성 없음. 그러나 검사기 WARN 1(`<<<…>>> 태그가 없다`)을 못 고침: 여는 줄이 `Edit loc_busstop_road_v1 WITHOUT…`(꺾쇠 없음). 남길 이유는 적었으나 숫자 없음 |
검사기(채점자, --kind image --refs 1): `WARN  붙일 참조 1개인데 프롬프트에 <<<…>>> 태그가 없다 … — FAIL 0 · WARN 1 · 1411자`
지난 회차 대비: 지난 PASS 2 -> 이번 부분 2(알림 결함은 고쳐졌으나 LIGHT LOCK 화면 쪽 누락, 태그 WARN).
추가 발견: 플레이어가 WARN 원인을 `image-prompt/SKILL.md` §0 문구 탓으로 돌림 — 키트 문구가 모호한 것이 맞음.
키트 결함: `skills/image-prompt/SKILL.md:21` "실제 요소 이름으로 바꾼다"가 꺾쇠까지 지우는 뜻으로 읽힘 -> "`<<< >>>`는 남기고 안의 이름만 바꾼다(`<<<loc_busstop_road_v1>>>`)"로. 또 `location-edit.md:23` 아래에 "상태판의 새 LIGHT LOCK 제안에는 광원의 화면 쪽(위치를 모르면 묻기)을 쓴다" 한 줄.
총평: PASS 0 / 부분 2 / FAIL 0
