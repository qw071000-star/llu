# real16-C33 반대편 카메라 퍼스트 프레임 ("뒤에서 보는 걸로") (2턴) — PASS 10 / 부분 0 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C33/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `11번 퍼스트·끝 프레임으로 진행합니다.` |
| 1 | 카메라가 V1과 다름 → 틀 2(DERIVED), LOCKED와 섞지 않음 | PASS | `장소 뷰 LC-001-V1은 길 건너편 정면이라 "뒤쪽에서"는 다른 시점입니다. 그래서 틀 2(DERIVED VIEW)` |
| 1 | "뒤쪽" = 벽 바깥 → 카메라 위치 먼저 정하기 | PASS | `할아버지가 등을 벽에 대고 앉아서 진짜 뒤는 벽 바깥입니다 … 정류장 안쪽, 벤치의 시간표 쪽에서 할아버지 어깨 너머` |
| 1 | 좌우·빛 뒤집힘 짚고 LIGHT LOCK 전→후 | PASS | `감나무는 화면 오른쪽, 시간표는 화면 왼쪽 … 전 from screen left, the persimmon-tree side → 후 from screen right, the persimmon-tree side` |
| 1 | 질문 한 묶음·읽기 | PASS | 4개 항목; first-frame.md, 정본. 3-4 카드·핸드오프 없음을 밝힘 |
| 2 | 틀 2 문장(Do not inherit, not a horizontal mirror, PRIORITY) | PASS | `Do not inherit its camera angle…`, `This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.` |
| 2 | `In this view …` + 새 LIGHT LOCK를 화면 기준으로 | PASS | `In this view the persimmon tree is at screen right and the timetable sign is at screen left.` `LIGHT LOCK for this view: Low dusk sun from screen right, the persimmon-tree side, is the only key; …` |
| 2 | 손 표기 화면 쪽 + 물건, 의상·소품 글자 그대로 | PASS | `the screen-left hand, nearer the timetable sign … the screen-right hand, nearer the persimmon tree`; must-include grandpa+bag 통과 |
| 2 | G7 검사·참조 3·위험·카드 `(제안값)` | PASS | check 통과(2568자), `3-4 카드가 없어서 project/cuts/3-4.md를 새로 만들고 … (제안값)` |
| 2 | G1 생성 통제 | PASS | `"좋아"만으로는 보내지 않습니다` |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image --refs 3 --must-include grandpa+bag C33_turn2_b1.txt`
  - 결과: `OK — image 프롬프트 2568자, 걸린 항목 없음`

## 추가 발견

- must-ask.md 11번 행 `does it continue the previous cut's end state?`를 따로 묻지 않고 3-1 위치로 이었다(연속성 표 3-4 자리 `(미정)`이라 제안한 것). 이유를 밝힘 → 감점 안 함.
- 2턴 첫 줄 뒤에 같은 줄로 `네 가지 제안값을 …`가 이어진다(정확한 한 줄 아님, 제안 수락 턴이라 허용).

## 키트 결함

- 결함 없음.

## 총평

벽 뒤 카메라 문제·좌우/빛 뒤집기를 정확히 처리한 모범 사례.
