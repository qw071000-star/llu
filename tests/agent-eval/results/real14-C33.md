# real14-C33 반대편 카메라 퍼스트 프레임 — "뒤에서 보는 걸로" 3-4 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real13: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "[11]번 퍼스트·끝 프레임으로 진행합니다." 카메라가 V1과 달라 틀 2(DERIVED VIEW). "정말 뒤쪽은 벽 밖이라 찍을 수 없다"며 카메라를 "정류장 안쪽, 벤치의 시간표 쪽 끝에서 할아버지 어깨 너머로 길 쪽을 봄"으로 제안(기대 제안값과 같음). 3번 질문이 좌우를 일관되게 서술: "이 시점에서는 감나무가 화면 오른쪽, 시간표가 화면 왼쪽. LIGHT LOCK은 새로 `the light comes from screen right, the persimmon-tree side`". 0:00 자세는 연속성 표 3-4가 미정이라 3-2 배치로 제안. 질문 턴에 카드 안 엶·안 씀 |
| 2 | PASS | 틀 2 전문, 템플릿 순서대로. `Do not inherit its camera angle, framing or composition.`, `This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.`, `PRIORITY: the CAMERA block overrides every reference.`, WARDROBE·PROP·PALETTE·ERA 글자 그대로, `In this view the persimmon tree is at screen right and the timetable sign is at screen left.` + `LIGHT LOCK for this view: the light comes from screen right, the persimmon-tree side.` `Exactly 1 person is visible.` 블록 밖에 모드·참조 3개·모델·해상도·폴더·위험 3줄("추정" 표시). 카드 `cuts/3-4.md` v0 신설(값을 쓰는 턴). 생성 안 함, "이미지로 보낼까요?" |

검사기: `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image C33t2_1.txt --refs 3 --must-include grandpa+bag` → `OK — image 프롬프트 2485자, 걸린 항목 없음` (LIGHT LOCK은 뒤집힌 새 문장이라 원문은 제외)

real13 감점 해소: ① 질문 턴 첫 줄 누락 — 해소. ② 질문 1번(시간표 쪽)과 3번(감나무 화면 오른쪽)의 서술 모순 — 해소(카메라를 "시간표 쪽 끝"으로, 화면 쪽은 감나무 오른쪽·시간표 왼쪽으로 일관).

추가 발견: 2턴 첫 줄이 도구 호출 전후로 두 번 출력됨.

키트 결함: 없음.

총평: 두 감점이 모두 해소되고 좌우·빛 뒤집기가 정확해 PASS 2.
