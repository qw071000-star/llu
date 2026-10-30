# real16-C49 막연한 정리 요청 — 대장 정리해줘 (1턴) — PASS 5 / 부분 1 / FAIL 0

> 채점: tests/agent-eval/runs-real16/C49/out/turn*.md·meta.json, git diff. 기준: grader-rules.md, scenarios.md(G1–G9 + C49), kit/.

## 턴별 판정표

| 턴 | 기대 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | PASS | "2번 오늘 할 일·세션 시작·컷 카드·핸드오프로 진행합니다." (tasks.md 2행 "대장 정리") |
| 1 | 정리 후보를 보이고 무엇을 할지 묻기 | PASS | "고칠 후보 1~5 … 확인할 것 1. 정리 범위: 위 1~4 중 어디까지 고칠까요? 제안은 1·2·3입니다." |
| 1 | 후보 내용이 대장과 일치: PR-001 job 빈칸, CH-003 빈 틀, 폐기 1건 | PASS | 대장 확인: PR-001 확정 job 칸 비어 있음, CH-003 `[ ]`, 폐기 목록 `job-ff-3-2-old` 1건 — 일치 |
| 1 | 확정 문장을 고쳐 쓰지 않음(v2로만) | PASS | LIGHT LOCK 중복은 "구조 변경이라 따로 정하는 게 낫습니다"로 보류, 수정 없음(git 변화 없음) |
| 1 | 읽기 순서: 총괄 세션 시작 = decisions → shot-list → registry(production-session §2)(G4/G8) | 부분 | reads: production-session/SKILL.md, asset-registry.md만. decisions·shot-list 안 읽어 3-6 폴더 행 누락도 못 짚고("폴더 표(1-1~3-5)는 … 맞는 것으로 보입니다") 항목 5도 "shot-list에서 확인해야 합니다"로 미룸 |
| 1 | 읽지 않은 것은 "추정" 표시(규칙 10) | PASS | "Higgsfield 저장본과 ok-cuts.md는 열지 않았으니 아래는 모두 "추정"" |

## 검사기 결과

코드블록 없음(질문·보고 턴) — 검사 대상 없음. 인용 한 줄은 코드블록이 아니라 프롬프트가 아님.

## 추가 발견

- 없음

## 키트 결함

- `kit/skills/production-session/SKILL.md:30`(총괄 On start)이 항상 3파일을 읽으라고 하나 tasks.md 2행/지침 4번의 "시작 보고는 프롬프트·생성·정본 작업만"과 범위 연결이 약함 → "대장 정리·오늘 할 일은 3파일 전부 읽는다"를 2행에 명시.

## 총평

후보 발굴은 정확했으나 총괄 세션 시작 읽기(3파일)를 생략했다.
