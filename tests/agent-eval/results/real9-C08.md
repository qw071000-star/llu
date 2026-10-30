# real9-C08 퍼스트 프레임, 정보 부족 3-4 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 컷 카드 3-4 없음을 알리고(`3-4는 컷 카드가 없고 컷 목록의 장소 뷰 칸도 비어 있습니다`) 정본(연속성 표 "(미정)")에서 출발. `image-prompt` SKILL + `first-frame.md`. 카메라(LC-001-V1과 같음 → 틀 1) / 할아버지 시작 위치(3-1 OK 카드 BLOCKING 줄을 가져옴, 벤치 감나무 쪽 화면 왼쪽 절반) / 하던 동작·시선 / 손(`화면 왼쪽 손(감나무 쪽)` + 물건) 4항목 제안값+이유 한 묶음. 가방 닫힘·인원 1명·모델·1k·`fld-3-4`는 "기본값으로 씀"으로 보임 |
| 2 | PASS | 틀 1: 첫 줄 `Edit <<<loc_busstop_road_v1>>> WITHOUT reframing …`, `LEFT and RIGHT are SCREEN directions …`, `CHANGE — ADD THE OLD MAN AND THE BAG`, REFERENCE AUTHORITY 3줄, DO NOT TRANSFER, WARDROBE·PROP·LIGHT LOCK 글자 그대로(`must-include` 통과), `Exactly one person is visible.`, 자리표시 태그 없음, 손은 `The screen-left hand, nearer the persimmon tree` 식으로 물건 기준. 컷 카드 `project/cuts/3-4.md` 신규 작성, [4]·[5]에 값과 `(제안값)` 표시. 위험 5개, 생성 안 함 |

검사기: `check_prompt.py --kind image --refs 3 --must-include grandpa+bag+light` → `OK — image 프롬프트 2186자, 걸린 항목 없음`
추가 발견: PROP 줄 크기를 "about the width of his lap"로만 쓰고 cm는 PROP 고정 설명문(40 cm)에 맡김 — 틀의 `[size in cm and body terms]`에는 살짝 못 미치나 고정 설명문에 cm가 있어 허용. 검사 때 `check_prompt.py --help`를 한 번 돌림(불필요, `higgsfield-generation` SKILL은 열지 않음).
키트 결함: 없음.
총평: real8과 같은 PASS 2. G1: mcp__ 없음, 생성 없음.
