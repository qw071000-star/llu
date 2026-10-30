# real13-C33 반대편 카메라 퍼스트 프레임 — "뒤에서 보는 걸로" 3-4 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real12-recheck: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 내용: 카메라가 V1과 달라 틀 2(새 시점), "뒤"는 벽 바깥이라 정류장 안 할아버지 어깨 너머로 제안, 빛 LIGHT LOCK을 `from screen right, the persimmon-tree side`로 다시 쓰자고 함, 0:00 자세 제안. 질문 턴에 `cut-card.md`를 열지 않았다(reads에 없음). 흠: ① 첫 줄이 `**판단:**`이라 "[N]번 …"이 없다(11번). ② 질문 1번이 카메라를 "화면 오른쪽 어깨 쪽, 시간표 표지판이 있는 쪽"이라 썼는데 3번은 "감나무가 화면 오른쪽으로 넘어간다"여서 서로 모순(표지판은 새 뷰에서 화면 왼쪽). t2 첫머리에서 "정정"함 |
| 2 | PASS | 틀 2 전문. `newly observed direction … not a horizontal mirror`, `Do not inherit its camera angle, framing or composition.`, `PRIORITY: the CAMERA block overrides every reference.`, WARDROBE·PROP 고정 문장 글자 그대로, 손은 `the screen-left hand, nearer the timetable sign` / `the screen-right hand, nearer the persimmon tree`(뒤집힌 방향과 일치). `In this view the timetable sign is at screen left and the persimmon tree is at screen right.` + `LIGHT LOCK for this view: Low dusk sun from screen right, the persimmon-tree side …`. `Exactly one person is visible.` 블록 밖 모드·참조·모델·폴더·위험 5개. 카드 3-4 v0는 값을 쓰는 턴에서 생성(`?? project/cuts/3-4.md`). 생성 없음 |

검사기: `--kind image C33t2_1.txt --refs 3 --must-include grandpa+bag` → `OK — image 프롬프트 2697자, 걸린 항목 없음` (LIGHT LOCK은 뒤집힌 새 문장이라 원 문장은 제외)

추가 발견
- 카메라 위치를 "벤치 옆 정류장 안, 할아버지 어깨 너머"로 골라 기대 제안값과 같다. 좌우·빛 뒤집기 모두 맞음(통합된 `location.md` "Writing directions" 규칙과 `first-frame.md:236`을 찾아 씀).

키트 결함
- `kit/instructions.md:41`: 첫 줄 누락(퍼스트 프레임 질문 턴에서도).
- `kit/skills/image-prompt/first-frame.md:236`: 반대편 카메라 규칙이 "전 → 후"로 다시 쓰라고만 하고, 질문 단계에서 카메라 쪽 landmark(표지판/감나무)가 화면 어느 쪽인지 먼저 적으라는 줄이 없다. 고침: "In the question, name the camera side by an object and state which landmark is now screen left/right before proposing the light".

총평: 프롬프트의 좌우·빛 뒤집기는 정확했고 질문 턴의 첫 줄·좌우 서술 모순이 흠이다.
