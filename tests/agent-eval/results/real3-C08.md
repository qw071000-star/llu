# real3-C08 퍼스트 프레임, 정보 부족 3-4 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real2: PASS 2)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 세 줄 보고, `[TOOL] list_project_assets(fld-3-4)`, 컷 카드 없음 → 정본으로 구성. `image-prompt/SKILL.md`+`first-frame.md`(+production-session·cut-card는 Bash로). 4항목: 카메라(LC-001-V1과 같은가 → 틀 1, 35mm=63°) / 할아버지 자리(3-2 BLOCKING 맞춤, 감나무 쪽 절반) / 시선 / 손(화면 왼쪽 손+감나무). 인원·가방 닫힘은 "기본값으로 씀"으로 제시만(real2 키트 결함 해소). 모델·1k·`fld-3-4` 묻지 않음. |
| 2 | PASS | 틀 1: `Edit <<<loc_busstop_road_v1>>> WITHOUT reframing …`, `LEFT and RIGHT are SCREEN directions …`, 의상·가방·LIGHT LOCK 글자 그대로, `Exactly one person is visible.`, 태그 3=참조 3, 손은 `the screen-left hand, nearer the persimmon tree`. 카드 `project/cuts/3-4.md` v0 작성, 사용자 값 외 `(제안값)`. 블록 밖 모드·참조·모델·해상도·저장. 생성 안 함. |
검사기(`--kind image --refs 3 --must-include grandpa+bag+light`): `OK — image 프롬프트 2052자, 걸린 항목 없음`
추가 발견: 카드 3-4 [1] 완료 조건 `[ ]`, 끝·타이밍 `[미정]` — 카드(프롬프트 아님)라 허용. 3-4 카드 신규 작성은 기대 항목([4],[5] 기록)과 일치.
키트 결함: 없음(`must-ask.md:56-57` 인원 모순은 수정됨 — 현재 "보이는 인원 수(정본에 없을 때만)").
총평: real2와 동일.
