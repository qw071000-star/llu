# real16-C27 나이 바꾸기 ("50대처럼") (2턴) — PASS 10 / 부분 0 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C27/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `5번 인물 시트 고치기로 진행합니다.` (tasks.md 5번 says에 "50대 때 모습도") |
| 1 | 기준 시트·틀 2 선택, 새 요소 이름 제안 | PASS | `job-ch001을 기준으로 틀 2(나이 변경)로 편집합니다. 결과는 별도 요소 char_grandpa_50s_v1` |
| 1 | 모호한 말 → 값(나이 표지) 제안 | PASS | `about fifty-five` + 나이 표지(머리 짙은 검정·관자놀이만 희끗, 주름 얕게, 턱선, 어깨, 손) |
| 1 | 의상은 그대로·회상용 의상 변경은 한 생성에 하나라고 안내 | PASS | `지금 옷 그대로 (이유: 한 번에 한 가지만 …)` |
| 1 | 질문 턴에 정본 안 씀 / 한 묶음 | PASS | 질문 3개, 도구는 grep 1회 |
| 2 | 틀 2 전문: IDENTITY BONES·HEADLESS not an injury·얼굴 재서술 없음 | PASS | `IDENTITY BONES: the same face shape, bone structure, eye shape …`, `an editorial clothing crop, not an injury` |
| 2 | 젊게 변형: 나이 표지 반대로·[젊게] 마지막 줄 | PASS | `shallower forehead lines and crow's feet, a firmer jawline …`; `ONLY CHANGE: the visible age of the same person. no babyface, no beauty filter, …` |
| 2 | 의상 글자 그대로 | PASS | `OUTFIT: the exact same clothes in every panel: A faded olive work jacket …` (must-include grandpa 통과) |
| 2 | 전→후·위험 목록 먼저·G7·2k | PASS | `나이: about seventy → about fifty-five` 외 4줄, 위험 5개, 2k 16:9, check 통과 |
| 2 | G1 생성 통제 | PASS | `보낼까요? "이미지로 만들어"라고 해 주시면 생성합니다.` |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image --refs 1 --must-include grandpa.lines C27_turn2_b1.txt`
  - 결과: `OK — image 프롬프트 1676자, 걸린 항목 없음`

## 추가 발견

- 2턴 첫 줄이 `"그대로"로 받아 …`로 시작한다(새 요청이 아니라 제안 수락 턴이라 허용).
- 여는 문장을 틀의 `age the same person to`에서 `make the same person younger, about fifty-five`로 바꿔 썼다. 틀 2에 젊게용 여는 문장이 없어서 생긴 일.
- 기능 지도 3번은 C27을 "확인 필요"로 적었지만 tasks.md 5번 says에 "50대 때 모습도"가 있어 바로 진행이 키트상 맞다 → 기대 오류 가능.

## 키트 결함

- `kit/skills/image-prompt/character-edit.md:80` 틀 2 여는 문장이 늙게 전용(`age the same person to [target age]`). 수정: `[젊게] make the same person younger, to [target age] …` 변형 한 줄 추가.
- `kit/context/tasks.md:22` 5번 says에 "50대 때 모습도"가 있어 "시트로"(4번 words)와 겹치지만 바로 진행하게 된다. 기능 지도는 확인을 기대 → 한쪽을 고칠 것(지도 3번 C27을 "바로"로).

## 총평

틀 2를 정확히 적용. 젊게 변형 문장이 틀에 없어 플레이어가 직접 고쳐 썼다.
