# real7-C08 퍼스트 프레임, 정보 부족 3-4 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real6: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 컷 카드 없음을 알리고 정본으로 구성. image-prompt SKILL + first-frame.md. 첫 질문이 "카메라·틀: 확정 장소 뷰 LC-001-V1과 같은가"(제안 같음, 틀 1). 할아버지 자리·0:00 손·시선·인원 5항목 제안값+이유. 가방 닫힘·모델·해상도·`fld-3-4`는 "기본값으로 씀" |
| 2 | PASS | `Edit <<<loc_busstop_road_v1>>> WITHOUT reframing`(틀 1), `LEFT and RIGHT are SCREEN directions …`, WARDROBE·PROP·LIGHT LOCK 글자 그대로, `Exactly one person is visible.`, 자리표시 태그 없음, 손은 `the screen-right hand, nearer the timetable sign … brass clasp`. 참조 3 = 태그 3. 위험 6개. 3-4 카드 v0 작성(사용자 답/제안값 구분). 생성 안 함 |

검사기: `--kind image --refs 3 --must-include grandpa+bag+light` → `OK — image 프롬프트 2151자, 걸린 항목 없음`
추가 발견: (1) 1턴에 `cut-card.md`를 엶: 카드를 쓰지 않는 질문 턴이라 불필요(real6엔 없었음). routing.md:30 "카드에 답을 적을 때 연다". (2) 프롬프트·must 파일을 `project/log/`에 둠(경미, 정본 폴더 오염).
키트 결함: 없음.
총평: PASS 2 유지. G1: tools에 mcp__ 없음, generate_* 없음.
