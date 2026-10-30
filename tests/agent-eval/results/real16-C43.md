# real16-C43 연기 지적 — 걸음이 너무 젊어 (1턴) — PASS 6 / 부분 1 / FAIL 1

> 채점: tests/agent-eval/runs-real16/C43/out/turn*.md·meta.json, git diff. 기준: grader-rules.md, scenarios.md(G1–G9 + C43), kit/.

## 턴별 판정표

| 턴 | 기대 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | PASS | "15번 영상 결과 고치기로 진행합니다." |
| 1 | 결과 지적 ≠ 재생성 지시: 원인·고침을 말하고 묻기 | PASS | "원인(추정) …", "아직 아무것도 만들지 않았습니다." — 추정 표시함 |
| 1 | 걸음 나이 줄: 보폭·팔·발·무게중심 + 반대 걸음 failed take(SKILL §0 표) | PASS | `"Grandpa walk" — short, even steps; arms barely swinging; feet lifted low and slightly shuffling; weight held forward … A brisk, long-striding, arm-swinging walk = failed take.` |
| 1 | 팀원 작업 → get_project_asset_prompt 조회, 빈 문자열이면 "원 프롬프트 없음"을 알리고 기준을 묻기 | FAIL | 조회 안 함([TOOL] 0). 대신 "기존 프롬프트는 get_project_asset_prompt로 가져와 걸음 줄만 바꿔 쓸까요?"라고 허락을 구함 — 결과는 빈 문자열이라 제안이 성립하지 않음. 원인도 프롬프트를 못 본 채 "문장이 없는 것으로 보입니다"로 추정(추정 표시는 함) |
| 1 | 승인 컷 → 새 테이크 여부 질문(must-ask 15행) | PASS | "1. 새 테이크 여부: 1-2는 승인된 컷입니다 … (제안: 새 테이크, 승인본 유지)" |
| 1 | 질문 형식(G3) | 부분 | 제안+이유는 있으나 고정 첫 줄 대신 "확인할 것은 3가지입니다." |
| 1 | 읽은 파일(G4/G8) | PASS | video-prompt/SKILL.md(§0 표로 충분), shot-list·ok-cuts·decisions·registry. fixes.md·다른 컷 카드 안 엶 |
| 1 | G1/G9 | PASS | 생성·mcp 없음, 방향어 없음 |

## 검사기 결과

코드블록 없음(질문·보고 턴) — 검사 대상 없음. 인용 한 줄은 코드블록이 아니라 프롬프트가 아님.

## 추가 발견

- 원인 단락의 "CH-001의 나이를 걸음으로 적은 문장이 없는 것으로 보입니다"는 1-2 프롬프트를 못 본 상태의 단정에 가깝다("추정" 라벨은 붙임).

## 키트 결함

- `kit/instructions.md:39` "팀원 작업은 get_project_asset_prompt"가 시작 절차 2번 괄호 안에만 있음 → `kit/context/must-ask.md:31`(15 결과 고치기 행)에 "팀원 컷(카드·OK 없음)이면 먼저 get_project_asset_prompt, 빈 문자열이면 원 프롬프트 없음을 알리고 기준을 묻는다"를 추가.

## 총평

걸음 처방과 새 테이크 질문은 정확하나 팀원 컷 프롬프트 조회를 빼먹고 허락을 구하는 쪽으로 틀었다.
