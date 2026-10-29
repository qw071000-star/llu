# real13-C25 같은 쪽 클로즈업 새 시점 — 시간표 표지판 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | `image-prompt` SKILL·`location.md`·`location-view.md`만 열고 질문 4개를 한 묶음으로 냈다. 같은 쪽 접근이라 "방향은 바꾸지 않습니다", 빛은 "V1처럼 화면 왼쪽, 감나무 쪽"을 질문 4번에 미리 적었다. 모델·해상도·저장 폴더·렌즈는 "기본값으로 씀"으로 처리. 대장 `LC-001-V2` 초안에 `(제안값)` 기록(diff). 첫 줄 "[N]번 …으로 진행합니다."가 없다(7번 해당) → 형식만 부분 |
| 2 | PASS | 첫 줄 "7번 장소 새 시점으로 진행합니다." 틀 B. `Do not inherit its camera angle, framing or composition.`, `Move in from the same side and along the same line of sight; no reverse angle and no view from behind.` 있음, `newly observed direction … not a horizontal mirror`는 안 씀. `text not legible`, 랜드마크 2개(지붕 모서리·벽 모서리). `In this view the timetable sign is at screen RIGHT and the shelter's roof edge and wall corner are at screen LEFT.` 뒤에 LIGHT LOCK 글자 그대로. 블록 밖에 모드·참조·모델·해상도·폴더·위험 목록. 임시 파일 삭제 |

검사기: `--kind image C25t2_1.txt --refs 1 --must-include light` → `OK — image 프롬프트 2451자, 걸린 항목 없음`

추가 발견
- 프롬프트에 `Use <<<image_1>>> as the sole geometry and design authority; do not inherit from discarded variants.`가 없다(`kit/skills/image-prompt/location-view.md:22`의 "After the first line add …"). 검사기는 못 잡는다. 같은 줄에 `Hand-lettered timetable lettering`처럼 지어낸 표현도 있으나 읽히지 않게 막아 두어 문제 없음.
- 요소 이름을 `<<<loc_busstop_road_v1>>>`로 썼다(대장 요소 이름과 일치).

키트 결함
- `kit/skills/image-prompt/location-view.md:22`: "sole geometry" 문장이 "Common" 불릿 한가운데에 있고 틀 A/B/C 코드블록에는 없다. 플레이어가 놓침. 고침: 틀 A·B·C 첫 문단 바로 뒤에 `Use <<<image_1>>> as the sole geometry and design authority; do not inherit from discarded variants.` 줄을 코드블록에 넣는다.
- `kit/instructions.md:41`: 질문 턴 첫 줄 누락(C24와 같음).

총평: 같은 쪽 접근의 거울 문장 조건과 LIGHT LOCK은 맞았다. 질문 턴 첫 줄과 "sole geometry" 문장이 빠졌다.
