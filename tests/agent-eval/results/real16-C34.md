# real16-C34 소품 지적 ("가방이 너무 새 거 같아") (2턴) — PASS 7 / 부분 3 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C34/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `9번 소품 만들기·고치기으로 진행합니다.` — 번호·이름은 맞고 조사만 `고치기으로`(→ `로`) |
| 1 | 결과(job)인지 에셋 자체인지 묻기, 결과 지적은 재생성 지시가 아님 | PASS | `1. 고칠 대상: 제안 — 가방 에셋 자체(prop_doctor_bag_v1) … 이미 승인된 컷은 그대로 두고` |
| 1 | 고정 설명문 변경 → v2·폐기 목록 절차, 사용 흔적 제안값 | PASS | `prop_doctor_bag_v2로 확정하고 v1은 폐기 목록으로 옮깁니다`, 흔적 문장 제안 |
| 1 | 시작 보고(판단·읽은 것·할 일) | 부분 | `작업 스킬과 소품 파일, 가방 정보가 있는 정본을 먼저 확인하겠습니다.` 뒤 곧바로 질문(instructions.md:41) |
| 2 | LOCKED EDIT, 원본 job 없음 → 요소 ID 편집 원본·한 줄 알림 | PASS | `Edit <<<prop_doctor_bag_v1>>> WITHOUT reframing …`, `대장에 확정 job이 없어서 요소 ID를 편집 원본으로 썼습니다` |
| 2 | 본 적 없는 원본: PRESERVE 배경은 `the existing background` | 부분 | `The plain seamless light grey studio background, with nothing else in frame` (prop.md:24 위반; 원본 배경을 본 적 없음) |
| 2 | 전 → 후는 대장 문장 그대로 인용 | 부분 | `bright-looking worn leather, brass clasp → …` 라고 쓰고 `이전 문장은 "worn" 표현뿐`이라 했으나 대장 문장은 `…scuffed and its corners worn dull.`로 이미 흔적이 있음(전 값이 실제 문장이 아님) |
| 2 | v2 고정 설명문·폐기 목록 알림·Avoid 줄 | PASS | `A worn brown leather doctor's bag with a dull tarnished brass clasp, …`, `확정되면 prop_doctor_bag_v2로 … v1은 폐기 목록`, `Avoid: tears, holes, mould, text, logos, metal corner fittings.` |
| 2 | G7 검사·G6·위험 목록·보이지 않는 상태 "추정" | PASS | check 통과, `원본의 현재 낡은 정도와 걸쇠 모양은 "추정"입니다` |
| 2 | G1 생성 통제 | PASS | `"이미지로 만들어" 또는 "보내"라고 해 주세요` |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image --refs 1 C34_turn2_b1.txt`
  - 결과: `OK — image 프롬프트 1339자, 걸린 항목 없음`

## 추가 발견

- 체크 스크립트는 `the existing background` 같은 배경 서술 규칙을 검사하지 못함(수동 점검 항목).

## 키트 결함

- `kit/instructions.md:12`·`kit/context/tasks.md:8`: `[작업명]으로` 고정 → 받침 없는 이름(`소품 만들기·고치기`)에서 `고치기으로`. 수정: `[작업명](으)로 — 받침 없으면 로` 한 줄, 또는 9번 라벨을 받침 있는 말로.
- `kit/skills/image-prompt/prop.md:24` 편집 규칙이 본문 한 줄에 몰려 있고 틀이 없다 → 플레이어가 `Template`(신규 제품 사진)의 배경 문장을 그대로 씀. 수정: 소품 LOCKED EDIT 짧은 틀(`the existing background`, 전 문장 인용)을 `## Template` 아래에 추가.

## 총평

에셋/결과 구분·v2 절차는 정확. 소품 편집 틀이 없어 배경과 "전" 인용에서 흠.
