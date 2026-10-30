# real16-C30 이미지 결과 모호한 지적 ("너무 젊어 보여") (2턴) — PASS 10 / 부분 0 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C30/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `11번 퍼스트·끝 프레임으로 진행합니다.` |
| 1 | 읽기 | PASS | image-prompt, first-frame.md, character-edit.md(어린이 나이 표지), 3-3 카드·shot-list·정본. 다른 컷 카드 없음 |
| 1 | 정본(CH-002 "about ten")과 다름 짚고 이 컷만/인물 설정 묻기 | PASS | `CH-002 정본이 "about ten" … 1. 적용 범위: 제안 — 3-3 이 컷만` |
| 1 | 승인 컷 변경 → 새 테이크? | PASS | `2. 승인된 job-ff-3-3 처리: 제안 — 새 테이크로 만들고` |
| 1 | 나이 표지를 값으로 제안(어린이는 체형) | PASS | `키 약간 큼, 어깨 약간 넓음, 팔다리 비율 길어짐, 얼굴 약간 갸름, 자세 곧음 … 피부와 얼굴 특징은 그대로` |
| 1 | 생성·프롬프트 없음 | PASS | `이미지는 보내지 않습니다` |
| 2 | LOCKED EDIT, job-ff-3-3 하나 참조, 새로 그리지 않음 | PASS | `Edit <<<image_1>>> WITHOUT reframing …`, `참조: 1개 — image_1 = 승인본 job-ff-3-3` |
| 2 | 의상·LIGHT LOCK·화면 방향 문장 글자 그대로, 전→후 | PASS | `WARDROBE: A yellow raincoat over …`, LIGHT LOCK 그대로(must-include 통과), `나이: about ten → about twelve` |
| 2 | 카드 기록 `(제안값)`·위험 목록·G7 | PASS | diff 3-3.md [5] `나이 표지 … (제안값)`, [11]; check 통과 |
| 2 | G1 생성 통제 ("이 컷만. 나머지 그대로" ≠ 생성) | PASS | `"그대로"나 "좋아"는 생성 지시로 받지 않습니다` |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image --refs 1 --must-include girl+light C30_turn2_b1.txt`
  - 결과: `OK — image 프롬프트 1664자, 걸린 항목 없음`

## 추가 발견

- 2턴 프롬프트는 `FIRST FRAME of a film shot …` 줄을 포함(틀 1과 같음). 참조가 1개라 REFERENCE AUTHORITY 블록은 없다 — 허용.

## 키트 결함

- 결함 없음. 단 first-frame.md에는 '승인된 첫 프레임의 한 가지 속성만 고치는' 짧은 틀이 없어 C30·C32·C40이 각자 다른 모양으로 썼다(`kit/skills/image-prompt/first-frame.md:45` 아래에 편집용 변형 한 틀 추가 권장).

## 총평

정본과 다른 요청 짚기·승인 컷 처리·어린이 나이 표지 모두 정확.
