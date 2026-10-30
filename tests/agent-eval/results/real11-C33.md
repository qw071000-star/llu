# real11-C33 반대편 카메라 퍼스트 프레임 — "뒤에서 보는 걸로" 3-4 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 내용은 PASS: "3-4 퍼스트 프레임(11번)으로 진행합니다". `list_folders`·`list_project_assets` [TOOL]. 카메라가 V1과 다름 → 틀 2(`DERIVED`). "정말 등 뒤는 벽 바깥" → 카메라를 벤치 시간표 쪽 절반, 어깨 너머로 제안. "카메라 방향이 반대라 화면 좌우가 뒤집힙니다. 감나무가 화면 오른쪽, 시간표가 화면 왼쪽 … 새 LIGHT LOCK은 "낮은 석양이 화면 오른쪽, 감나무 쪽""(기대 일치). 기본값 줄에 모델·비율·폴더·렌즈. **감점:** 질문만 하는 턴에 `production-session/cut-card.md`를 열음(`context/tasks.md` §3 마지막 줄 "On question-only turns do not open cut-card.md"). 파일은 만들지 않음. 아래 키트 결함 1과 맞물림. 첫 줄 앞에 한 줄이 먼저 오고, 항목 5번(손·가방)은 정본에 있는 값이라 묻지 않고 "기본값으로 씀"에 넣어도 됨 |
| 2 | PASS | 틀 2: `Using <<<loc_busstop_road_v1>>> as the exact same location, generate a new view. Do not inherit its camera angle, framing or composition.`, `not a horizontal mirror of the reference`, `In this view the persimmon tree is at screen RIGHT and the timetable sign is at screen LEFT.`, `LIGHT LOCK for this view: Low dusk sun from screen right, the persimmon-tree side …`, WARDROBE·PROP·팔레트·시대 글자 그대로, `the screen-left hand, nearer the timetable sign`, `Exactly one person is visible.`, 좌표 문장 있음. 블록 밖 모드·참조·모델·해상도·폴더, 위험 5개, 추정 표기, 카드 3-4 v0를 `(제안값)`으로 신규 작성(`?? project/cuts/3-4.md`). 생성 안 함 |

## 검사기
내 실행 `--kind image --refs 3 --must-include grandpa+bag+light(화면 오른쪽 사본)`: `OK — image 프롬프트 2624자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인.
- 2턴이 "전 → 후"를 따로 보이지 않음. 새 프롬프트이므로 해당 없음.

## 키트 결함
1. `kit/skills/production-session/SKILL.md:37`("If none, build a draft … (`cut-card.md`)")이 `kit/context/tasks.md:47`("question-only turns do not open cut-card.md")과 부딪힌다. 컷 카드가 없는 컷의 첫 질문 턴에 플레이어가 cut-card.md를 연다. 제안: SKILL.md:37에 "(질문 턴에는 열지 않는다. 카드는 값을 받아 쓰는 턴에 `cut-card.md`로 만든다)"를 덧붙인다.

## 총평
카메라 위치·좌우 반전·LIGHT LOCK 모두 맞게 다뤘고, 질문 턴에 cut-card.md를 연 것만 감점.
