# real11-C08 퍼스트 프레임, 정보 부족 3-4 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt` SKILL + `first-frame.md` + production-session SKILL. 3-4 카드 없음 → 정본에서 구성. 장소 뷰(LC-001-V1과 같은가)·할아버지 자리/자세/시선/손(3-1 OK 카드 자리와 맞춤)·손녀 이어받기를 제안값+이유로 3개. 가방 닫힘·인원은 "기본값으로 씀"에 제시. 모델·해상도·`fld-3-4`는 묻지 않음. 카드 만들지 않음 |
| 2 | PASS | 틀 1: 여는 문장 `Edit <<<loc_busstop_road_v1>>> WITHOUT reframing: …`, DERIVED와 섞이지 않음. WARDROBE·PROP·LIGHT LOCK 글자 그대로, `LEFT and RIGHT are SCREEN directions …`, `Exactly 1 person`, 손은 `the screen-left hand, nearer the persimmon tree` 식(물건 기준). `<<<LOC>>>` 류 자리표시 없음, 참조 3 = 태그 3. 카드 `cuts/3-4.md` 신설(`cut-card.md`만 엶)·연속성 표 3-4 행에 `(제안값)` 기록(diff). 생성 안 함 |

검사기: `--kind image C08_t2 --refs 3 --must-include grandpa+bag+light` → `OK — image 프롬프트 2228자, 걸린 항목 없음`
추가 발견: 1턴에 `sim/higgsfield.md`를 grep했으나 답에 `[TOOL]` 줄로 기록하지 않음(결과를 답에 쓰진 않아 경미).
키트 결함: 없음.
총평: real9와 같은 PASS 2.
