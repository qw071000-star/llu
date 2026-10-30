# real8-C08 퍼스트 프레임, 정보 부족 3-4 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real7: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 3-4 카드 없음을 알리고 정본으로 구성. image-prompt SKILL + first-frame.md + production-session SKILL, 3-1 시작 이미지 카드(first-frame 인물 자리 예외). 첫 질문이 카메라·모드(LC-001-V1과 같은가), 할아버지 자리/손/시선 4항목 제안값+이유. 가방 닫힘·모델·해상도·`fld-3-4`는 "기본값으로 씀". 이웃 컷 카드 안 엶 |
| 2 | PASS | `Edit <<<loc_busstop_road_v1>>> WITHOUT reframing`(틀 1), `LEFT and RIGHT are SCREEN directions …`, WARDROBE·PROP·LIGHT LOCK 글자 그대로, `Exactly 1 person is visible.`, 자리표시 태그 없음, 손은 `the screen-left hand, nearer the persimmon tree` / `the screen-right hand, nearer the timetable sign`. 참조 3 = 태그 3. 위험 6개. `cut-card.md`를 열고 `cuts/3-4.md` v0 작성([4][5] 카메라·시작, 사용자 답/(제안값) 구분). 생성 안 함 |

검사기: `--kind image --refs 3 --must-include grandpa+bag+light` → `OK — image 프롬프트 2197자, 걸린 항목 없음`
추가 발견: 2턴 답 첫머리에 "정본이 다음과 같이 바뀌었습니다."라는 맥락 없는 문장이 섞임(경미, 오기).
키트 결함: 없음.
총평: PASS 2 유지. G1: tools에 mcp__ 없음, generate_* 없음.
