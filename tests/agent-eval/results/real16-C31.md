# real16-C31 장소 시간대 바꾸기 ("밤으로") (2턴) — PASS 8 / 부분 3 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C31/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `8번 장소 고치기로 진행합니다.` |
| 1 | 읽기 | PASS | image-prompt, location.md, location-edit.md, 정본 |
| 1 | 둘로 읽히는 변경 → 나누기 제안, 사용자가 먼저 말한 것부터, 1단계 결과는 아직 요청 상태가 아님 | PASS | `2단계로 나눕니다. 1단계는 석양을 밤으로 … 형광등은 꺼 둔 채 … 1단계 결과는 아직 "형광등 켜진 밤"이 아닙니다` |
| 1 | 새 LIGHT LOCK을 화면 기준으로, 해 질 녘 문장 남기지 않기 | 부분 | 1단계 문장은 제안: `Cold moonlight from screen left, the persimmon-tree side, is the only key; …` 하지만 시나리오가 말한 지배광=형광등(화면 어느 쪽)은 묻지 않음. location-edit.md:23 `if the position is unknown, ask` |
| 1 | 시작 보고(판단·읽은 것·할 일) | 부분 | `먼저 정본과 관련 스킬 파일을 확인하겠습니다.` 뒤 곧바로 질문. instructions.md:41 시작 보고 없음 |
| 1 | 질문 한 묶음·생성 없음 | PASS | `확인할 것이 3개 있습니다 …`, 도구는 ls 1회 |
| 2 | STATE 틀 + 표준 여는 문장 + 형광등 번짐 막는 문장 | PASS | `same location with one state change only: late dusk becomes a clear moonlit night`, `no glow, no halo, no light spilling onto any surface` |
| 2 | LIGHT LOCK를 CHANGE에 쓰고 해 질 녘 문장 제거 | PASS | `The low dusk sun is gone …`; PRESERVE에 옛 LIGHT LOCK 없음, `Cold moonlight from screen left, the persimmon-tree side …` |
| 2 | G7 검사 / 전→후 / 위험 / 대장 | PASS | check 통과, `빛 (LIGHT LOCK): … → …`, 초안(제안값) diff |
| 2 | 한국어 답 G2 | 부분 | `Check passed. Now I'll record the answers on the registry's draft line and delete the tmp files.` 영어 한 줄(tasks.md:8 `short lines between tool calls are Korean too`) |
| 2 | G1 생성 통제 | PASS | `이 프롬프트로 1단계를 보낼까요?` |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image --refs 1 C31_turn2_b1.txt`
  - 결과: `OK — image 프롬프트 1805자, 걸린 항목 없음`

## 추가 발견

- 2턴이 1단계(달빛 밤, 형광등 꺼짐)만 보였다. 2단계(점등)의 LIGHT LOCK(형광등의 화면 쪽+물건)은 다음 턴으로 미뤘으나 1턴에서 미리 묻지 않음.

## 키트 결함

- `kit/context/must-ask.md:28` 8번 행: `light changes → that view's LIGHT LOCK`만 있고 "켜지는 광원의 화면 쪽+물건을 지금 물어라"가 없음. 수정: `…and ask the lit source's screen side + object for the final state.`
- `kit/instructions.md:41` '시작 보고는 프롬프트·생성·정본 작업에만'이라 질문 턴(프롬프트 앞 단계)에는 빠져도 되는 것처럼 읽힘(C31·C34 1턴 누락). 수정: `also on the question turn that precedes a prompt`.
- `kit/instructions.md:12` 한국어 규칙이 도구 호출 사이 서술을 직접 말하지 않음(tasks.md:8 괄호에만 있음). 수정: instructions.md Role에 `narration between tool calls too`.

## 총평

분리·표준 STATE 틀은 정확. 최종 상태 LIGHT LOCK 질문, 시작 보고, 한국어 서술에서 흠.
