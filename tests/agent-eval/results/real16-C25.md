# real16-C25 같은 쪽 클로즈업 새 시점 (거울 문장 조건) (2턴) — PASS 9 / 부분 1 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C25/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `7번 장소 새 시점으로 진행합니다.` |
| 1 | 읽기 | PASS | image-prompt SKILL + location.md + location-view.md + 정본 |
| 1 | 질문 한 묶음 | PASS | 3개(표지판 크기·위치, 남길 랜드마크 1~3, 프레임 밖), `"절반"을 높이 기준으로 봤습니다`로 모호한 말을 값으로 |
| 1 | 질문 턴에 제안값을 정본에 쓰지 않기 | 부분 | `받은 값은 asset-registry.md에 LC-001-V2 초안(제안값) 줄로 적어 두었습니다` — diff에 사용자 말 외에 제안값(1.6m, 35mm, 랜드마크 3개, 밖으로 밀 것)까지 기록. tasks.md:48 `write no proposed values to canon` 위반 |
| 2 | 틀 B: Do not inherit·부모·같은 쪽 문장·거울 문장 없음 | PASS | `Do not inherit its camera angle, framing or composition.`, `Move in from the same side and along the same line of sight; no reverse angle and no view from behind.`; `not a horizontal mirror` 없음 |
| 2 | 표지판 글자 안 읽힘, 랜드마크 1~3 | PASS | `text not legible`; 지붕 모서리·기둥·논 |
| 2 | 화면 기준 LIGHT LOCK 글자 그대로 + `In this view …` | PASS | `In this view the shelter is at screen left of the sign and the sign stands at screen right.` + LIGHT LOCK 마지막 줄 그대로(must-include 통과) |
| 2 | MASTER GEOMETRY 등 부모 문장 글자 그대로 | PASS | MASTER GEOMETRY·PALETTE·ERA LOCK·FINISH 대장과 같음 |
| 2 | G7 검사 / G6 블록 밖 / 위험 | PASS | check_prompt --refs 1 --must-include light 통과; 위험 5개 |
| 2 | G1 생성 통제 | PASS | `"이미지로 만들어" 또는 "보내"라고 해 주세요` |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image --refs 1 --must-include light.lines C25_turn2_b1.txt`
  - 결과: `OK — image 프롬프트 2440자, 걸린 항목 없음`

## 추가 발견

- 2턴 첫 줄이 `7번 장소 새 시점으로 진행합니다. ("그대로"는 …)`처럼 괄호가 붙는다. 정확한 한 줄 형식은 새 요청에만 요구되므로 감점하지 않음.

## 키트 결함

- `kit/instructions.md:50`(`Before ending the turn: answers received are on the existing cut card / registry with (제안값)`)와 `kit/context/tasks.md:48`(질문 턴에는 제안값을 정본에 쓰지 않는다)이 서로 부딪힌다 → C25 1턴이 제안값까지 씀. 수정: instructions.md:50에 `On a question-only turn write only the user's own words; proposals are written the turn the user accepts them.`

## 총평

새 시점 문장 조건과 LIGHT LOCK은 정확. 질문 턴에 제안값을 정본에 쓴 점만 흠.
