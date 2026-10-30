# real16-C36 레지스터와 부딪치는 연기 ("웃게") (2턴) — PASS 10 / 부분 1 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C36/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | 부분 | 첫 줄 `2번 오늘 할 일·세션 시작·컷 카드·핸드오프로 진행합니다.` → 세 줄 뒤 `13번 실사·인물 영상으로 진행합니다. (2번에서 바뀜 …)`. tasks.md:8은 바뀜을 허용하나 첫 줄이 틀린 번호(기능 지도 3번은 이 요청을 '확인 필요'로 봄) |
| 1 | 질문 턴에 acting 안 열기 | PASS | reads: video-prompt SKILL, live-action만. `연기 문서(acting)는 …`는 2턴에서 열림 |
| 1 | §5 절제와 맞는지 짚고 "살짝"은 범위 안 | PASS | `2. 웃음의 크기: … 입을 다문 채 입꼬리만 살짝 올리고, 치아는 보이지 않고 … decisions.md §5가 절제된 연기` |
| 1 | 이웃 컷 2-1 OK 연기와 반대 짚기, OK 카드는 안 열기 | PASS | `2-1 OK의 이유는 "기대 안 하는 얼굴"이라 웃음과 다릅니다` — 목록 줄·2-2 시작 이미지 카드만 |
| 1 | 질문 한 묶음·정본 미기록 | PASS | 4개 항목, `이번 턴은 질문만 하므로 컷 카드와 정본은 건드리지 않았습니다` |
| 2 | acting 열기(프롬프트 쓰는 턴) | PASS | reads `acting/SKILL.md`; 목표·beat·eye life 포함 |
| 2 | 양 끝 failed take(무표정/활짝 웃음) | PASS | `teeth showing or a broad grin = failed take, no change in the mouth at all = failed take` |
| 2 | 15블록·시작 이미지 카드와 일치(미드 스트로크, 85mm) | PASS | `mid-stroke with the screen-left hand, nearer the tree` = 2-2 시작 이미지 카드, `Diagonal field of view about 29°` |
| 2 | 사건 수·타이밍 | PASS | 쓰다듬기+웃기 2개, `0:00–0:03 / 0:03–0:05 / 0:05–0:08` |
| 2 | G7 검사 / 카드 기록 / 추정 표시 | PASS | check 5367자 통과, `project/cuts/2-2.md` 신규, `감나무가 화면 왼쪽이라고 보고 썼습니다. (추정)` |
| 2 | G1 생성 통제 | PASS | `"영상으로 만들어"라고 해 주세요` |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind video --refs 3 --seconds 8 --must-include grandpa+bag+light C36_turn2_b1.txt`
  - 결과: `OK — video 프롬프트 5367자, 걸린 항목 없음`

## 추가 발견

- `[OPTICS]`가 망원 문장 `the camera is physically far away`를 그대로 쓰지만 `[CAMERA]`는 `about 2 m from the old man` — 서로 부딪힌다.
- shot-list 2-2 행의 "같은 얼굴로" 변경을 핸드오프로 올리라고 알림 — 좋음.

## 키트 결함

- `kit/context/tasks.md:30` 13번 says에 "표정·연기 요청 on a cut with only a start image (예: '2-2에서 웃게')"가 없어 플레이어가 2번→13번으로 헤맸다. 수정: 13번 says에 그 예시 추가.
- `kit/skills/video-prompt/live-action.md:125` `[망원]` 문장이 거리와 무관하게 `the camera is physically far away`를 쓰게 한다 → 2 m 클로즈업과 모순. 수정: `(only when the camera is 3 m or more away)`.

## 총평

acting 시점·레지스터 충돌 처리·이웃 컷 충돌은 정확. 첫 줄 번호만 바로잡힘이 늦었다.
