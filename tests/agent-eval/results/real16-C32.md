# real16-C32 사용자가 말한 손 ("오른손에") (2턴) — PASS 10 / 부분 0 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C32/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `11번 퍼스트·끝 프레임으로 진행합니다.` |
| 1 | "오른손"을 화면 기준으로 받고 충돌 짚기, 확인 받기 | PASS | `"오른손"은 화면 기준으로 보면 화면 오른쪽 손인데 … 시간표 쪽 손으로 시간을 짚고 있습니다 … 제안 — 화면 왼쪽 손, 시간표에서 먼 손` |
| 1 | 새 소품(우산)이 대장에 없음 → 설명 제안값 | PASS | `4. 우산 사양: 제안 — 접힌 검정 장우산, 길이 약 80cm … 소품 ID는 등록하지 않고 이 컷에만 말로 씁니다` |
| 1 | 승인 컷 대체 여부 질문 | PASS | `1. 승인된 컷 변경: 제안 — 승인본은 그대로 두고 새 테이크` |
| 1 | 읽기(자기 컷 카드·핸드오프만) | PASS | 3-1 카드, 3-1 핸드오프, 정본, first-frame.md. 다른 컷 없음 |
| 2 | 인물 기준 → 화면 기준 변환 + 근거 + "추정" | PASS | `화면 기준으로 바꾸면 화면 왼쪽 손, 시간표에서 먼 손입니다(추정). 손녀가 시간표를 보고 선 옆모습이라 …`. 근거 문장은 약함(옆모습의 카메라 쪽 손이 왜 화면 왼쪽인지 설명 없음)이나 추정 표기·화면 쪽+물건 표기는 지킴 |
| 2 | 프롬프트에 `her right hand` 없음, 화면 쪽 + 물건 | PASS | `She holds it by the handle in the screen-left hand, farther from the sign`, `the screen-right hand, nearer the sign, tracing the printed times` |
| 2 | 고정 문장 글자 그대로·좌표 문장·Exactly 2 | PASS | WARDROBE/PROP/LIGHT LOCK must-include 통과, `LEFT and RIGHT are SCREEN directions …`, `Exactly 2 people are visible.` |
| 2 | 전→후·위험 목록·G7·카드 `(제안값)` | PASS | `전 → 후 (손녀 소품): 없음 → 접힌 검정 장우산 …`; diff 3-1.md 우산 줄 |
| 2 | G1 생성 통제 | PASS | `이 프롬프트로 보낼까요?` |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image --refs 1 --must-include grandpa+girl+bag+light C32_turn2_b1.txt`
  - 결과: `OK — image 프롬프트 2347자, 걸린 항목 없음`

## 추가 발견

- 2턴 첫 줄에 `N번 …` 없음(제안 수락 턴이라 허용).
- 인물 기준 손 변환 근거: 키트가 '카메라를 보면 반대, 등지면 같음'만 주고 옆모습 처리 규칙이 없다.

## 키트 결함

- `kit/instructions.md:21`(규칙 6)에 옆모습(인물이 화면 옆을 보는 경우)의 변환법이 없다. 수정: `In profile, ask which hand is meant by the object it is nearer (e.g. nearer the sign) rather than deriving it.`

## 총평

화면 기준 손·추정 표기·고정 문장 모두 지킴. 옆모습 변환 근거만 얇다.
