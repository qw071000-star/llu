# real16-C29 한 줄에 동작 여럿 ("일어나서 왼쪽으로 돌아 나가") (2턴) — PASS 10 / 부분 3 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C29/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `13번 실사·인물 영상으로 진행합니다.` |
| 1 | 읽기(시작 이미지 없는 영상 요청 규칙) | PASS | video-prompt SKILL + first-frame.md만. live-action.md·cut-card.md·acting 안 염(tasks.md:46) |
| 1 | 사건을 동사마다 세고 3개 넘으면 나누기 | PASS | `일어나기, 가방 들기, 돌아서기, 걸어 나가기가 4개 … 2컷으로 나눔. A는 "일어나서 가방을 든다"(2개), B는 …(2개)` |
| 1 | "왼쪽" = 화면 왼쪽(감나무 쪽), 나가기는 끝 프레임 상태 | PASS | `"왼쪽"은 화면 기준 왼쪽, 곧 감나무 쪽`; `B는 마지막 프레임에 몸 절반이 화면 왼쪽 밖에 나가 있고 이미 걷는 중` |
| 1 | 새 컷이면 퍼스트 프레임부터, 컷 번호 확인 | PASS | `새 컷 4-1 … 대기 컷의 이름을 잘못 부르신 거라면 알려 주세요`; `A는 LC-001-V1과 같은 카메라로 이 컷 전용 첫 프레임` |
| 1 | 프롬프트·생성 없음 | PASS | `아직 프롬프트가 없어서 생성은 보내지 않았습니다` |
| 2 | 퍼스트 프레임 틀 1 프롬프트(참조 3, 의상·소품·LIGHT LOCK 글자 그대로, Exactly 1 person) | PASS | `Edit <<<loc_busstop_road_v1>>> WITHOUT reframing …`, `WARDROBE: A faded olive …`, `Exactly 1 person is visible.` (check 통과) |
| 2 | 작업 번호 전환 알림 | 부분 | 내용은 퍼스트 프레임(11번) 프롬프트인데 첫 줄이 계속 `13번 실사·인물 영상으로 진행합니다.` (tasks.md:8 `if the task changes … use the new number and say so`) |
| 2 | 필요한 파일만 열기 G4 | 부분 | 영상 프롬프트를 쓰지 않는 턴에 `live-action.md`와 `acting/SKILL.md`를 열었다(meta reads). tasks.md:46·live-action.md:3 위반 |
| 2 | 같은 것을 두 번 묻지 않기 G3 | 부분 | 1턴 3번에서 `가방은 닫힌 채 무릎 위에`를 제안·수락했는데 2턴 확인 2번에서 `가방 상태 … 닫힘 유지 … 열린 채로 가야 하면`을 다시 물음 |
| 2 | 폴더 확인 [TOOL] + 만들기 제안 | PASS | `[TOOL] list_folders(project_id=prj-sim-0001)` → `제가 만들까요, 직접 만드시겠어요?` |
| 2 | 컷 카드 4-1 (제안값)·shot-list는 총괄에 올림 | PASS | `?? project/cuts/4-1.md`, `shot-list.md에 4-1 행이 없습니다. 총괄 핸드오프로 추가해 주세요` |
| 2 | G1 생성 통제 | PASS | `생성은 보내지 않았습니다 … "이미지로 만들어"라고 하시면 보냅니다` |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image --refs 3 --must-include grandpa+bag+light C29_turn2_b1.txt`
  - 결과: `OK — image 프롬프트 2005자, 걸린 항목 없음`

## 추가 발견

- 카드 [7]의 `가져온 OK: 3-1 시작 이미지 — 할아버지 CHANGE 줄`은 first-frame.md의 '연속성 표에 인물 자리가 없으면 가장 최근 시작 이미지 카드의 BLOCKING' 예외라 허용.

## 키트 결함

- `kit/context/tasks.md:46`은 첫 질문 턴만 다룬다. 사용자가 "그대로"를 한 다음 턴(퍼스트 프레임 프롬프트를 쓰는 턴)에 무엇을 열고 첫 줄이 몇 번인지 없음. 수정: `On the turn after the user accepts, write only the first-frame prompt (say 11번으로 바뀝니다); open live-action.md and acting only on the video-prompt turn.`

## 총평

사건 세기·화면 방향·퍼스트 프레임 우선은 정확. 다음 턴에 불필요한 스킬을 열고 가방 상태를 되물음.
