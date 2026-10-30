# real16-C21 장소 시대 교체 (한 생성에 한 층) (2턴) — PASS 13 / 부분 0 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C21/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `8번 장소 고치기로 진행합니다.` (tasks.md 8번 = 시대 교체) |
| 1 | 읽기 G4/G8 | PASS | image-prompt SKILL, location.md, location-edit.md + 정본만. 다른 컷 카드·핸드오프 없음 |
| 1 | 질문 한 묶음 G3 | PASS | `프롬프트를 쓰기 전에 확인할 것이 4개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요.` 항목마다 제안+이유 |
| 1 | 한 생성에 한 층·층 순서 제안 | PASS | `4단계로 나눠 한 단계에 한 층씩 바꿉니다. ① 표지판 층(IDENTITY AND TEXT) ② 기둥과 벤치(FURNITURE / VEHICLES / FIXTURES) ③ 조명 ④ 화면 질감`; 구조 면·문 층은 건물 부피를 건드리므로 생략한다고 이유를 적음 |
| 1 | 정본 §3(1990년대 초)과 다른 시대 짚기 | PASS | `요청은 2020년대라서 정본과 다릅니다 … 이 장소의 별도 버전(LC-001-V2)으로만 만들고` |
| 1 | 프롬프트·생성·정본 기록 없음 | PASS | `이번 턴에는 프롬프트 작성, 생성, 정본 기록을 하지 않습니다`; 1턴 도구는 Bash(ls, grep)뿐 |
| 2 | 첫 층만 쓴 프롬프트 | PASS | `this step changes only its IDENTITY AND TEXT`; 다른 층은 `unchanged from the parent image` |
| 2 | 틀 2 구성(대응물·REMOVE·PRESERVE에 다른 층·건물 부피·ONLY CHANGE 같은 층) | PASS | `REMOVE: the hand-painted face…`, `Every building volume and opening position`, `ONLY CHANGE: IDENTITY AND TEXT.` |
| 2 | 원래 시대 이름 없음, 시대 문구는 마지막 층에만 | PASS | 블록에 `1990` 0건. `1단계라 시대 문구는 넣지 않았고, 원래 시대 이름(1990년대)도 쓰지 않았습니다` |
| 2 | LIGHT LOCK·표준 여는 문장 글자 그대로 | PASS | `Edit <<<image_1>>> WITHOUT reframing: …` 표준형, PRESERVE에 `Low dusk sun from screen left, the persimmon-tree side, is the only key; …` (must-include 통과) |
| 2 | G7 검사 후 보임 / G6 블록 밖 설정 / 전→후 / 위험 | PASS | 메타 check_prompt 실행 후 표시. 모드·참조·모델·해상도·저장 폴더·`전 → 후`·위험 4개 |
| 2 | 대장 `(제안값)` 기록 | PASS | diff: `초안(제안값) LC-001-V2 …` 4줄, 확정은 순서만 |
| 2 | G1 생성 통제 | PASS | `보낼까요?` 로 끝, [TOOL] 없음 |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image --refs 1 --must-include light.lines C21_turn2_b1.txt`
  - 결과: `OK — image 프롬프트 1613자, 걸린 항목 없음`

## 추가 발견

- 1턴 출력에 `8번 장소 고치기로 진행합니다.`가 두 번 나온다(첫 줄 + 서술 뒤). 해롭지 않음.
- 1턴 `읽은 것`에 location.md 가 빠져 있으나 메타에는 열려 있음(보고 누락 수준).

## 키트 결함

- 결함 없음.

## 총평

시대 교체를 층 하나로 나눠 첫 층만 정확히 쓴 모범 사례.
