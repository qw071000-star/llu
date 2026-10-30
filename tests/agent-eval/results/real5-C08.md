# real5-C08 퍼스트 프레임, 정보 부족 3-4 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real4: PASS 1 / 부분 1 → 개선)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | production-session SKILL + image-prompt SKILL + first-frame.md, 3-1 시작 이미지 카드 한 장(인물 자리 예외). 이웃 컷 카드는 안 엶(`ls`만). 4항목(카메라 = LC-001-V1과 같은가 → 틀 1 / 시작 위치 / 동작·손 / 시선) 제안값+이유. 모델·1k·`fld-3-4`·인원 1·참조는 "기본값으로 씀" |
| 2 | PASS | `Edit <<<loc_busstop_road_v1>>> WITHOUT reframing`, `LEFT and RIGHT are SCREEN directions…`, WARDROBE·PROP·LIGHT LOCK 글자 그대로, `Exactly one person is visible.`, 손은 `the screen-left hand, nearer the persimmon tree`, 태그 3 = 참조 3. 카드 `project/cuts/3-4.md` v0 신규, [4][5]에 `(제안값)`. 블록 밖 모드·참조·모델·해상도·저장. 생성 안 함 |

검사기: `--kind image --refs 3 --must-include grandpa+bag+light`: `OK — image 프롬프트 2205자, 걸린 항목 없음`

추가 발견: 없음.

키트 결함: 없음.

총평: real4의 이웃 카드 열람 감점 해소.

G1: 모든 턴 tools가 Bash/Write/Edit/Grep뿐, `mcp__` 호출 없음, `generate_*` 없음.
