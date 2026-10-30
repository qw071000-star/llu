# real11-C32 사용자가 말한 손 — "손녀 오른손에 우산" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`first-frame.md`, 자기 컷(3-1 카드·핸드오프·OK 대장)만 읽음. 첫 줄 "프롬프트를 쓰기 전에 확인할 것이 5개 있습니다". "오른손"을 화면 기준으로 받음: "'오른손'을 화면 기준 오른쪽으로 읽었습니다. 그 손은 지금 시간표를 짚고 있어서 …" 후 화면 왼쪽 손(시간표에서 먼 손)을 제안, 화면 오른쪽이 맞으면 알려 달라, 본인 오른손이면 변환하고 "추정"으로 적겠다고 안내. `her right hand` 없음. 우산 사양(검정 천, 70cm, 접힘; 비닐 제외) 제안값, 승인 컷이라 "새 테이크로 만들고 기존 승인은 그대로" 확인. 생성 없음. (우산이 대장에 없다는 말은 "에셋을 만들 필요가 없습니다"로만 돌려 말함) |
| 2 | PASS | 변환 근거와 "추정": "손녀가 화면 오른쪽의 시간표를 보고 선 옆모습이라서, 본인 오른손이 화면 왼쪽, 시간표에서 먼 손 … 이 변환은 "추정"입니다". 프롬프트: `held by the handle in the girl's screen-left hand, farther from the sign`, `the screen-right hand, nearer the sign, tracing the printed times locked`, `LEFT and RIGHT are SCREEN directions …`, WARDROBE·LIGHT LOCK 글자 그대로, `Exactly 2 people are visible.`. 블록 밖 모드·참조·모델·해상도·저장 폴더, "수정 전 → 후", 위험 4개. 카드 3-1 [5]에 `(제안값)`·`(추정)` 기록 |

## 검사기
내 실행 `--kind image --refs 1 --must-include grandpa+girl+light`: `OK — image 프롬프트 1953자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인. 2턴에서 `cut-card.md`를 열었음 — 카드에 값을 쓰는 턴이라 허용.
- 1턴 끝의 3줄 시작 보고(판단·읽은 것·할 일)가 첫 줄 고정 문장 뒤에 와서 순서가 어색함(경미).

## 키트 결함
- 옆모습에서 "본인 오른손"이 화면 어느 쪽인지의 표가 없다(real9에서 지적한 `kit/instructions.md:28` 규칙 6). 이번에도 플레이어는 "추정"으로 처리했으나 매핑은 플레이어 판단이다. 제안: 규칙 6에 "profile facing screen-right: own right = the camera-near hand, write it as screen side + object, mark 추정" 한 줄 추가.

## 총평
화면 기준 충돌을 짚고 인물 기준으로 바뀐 뒤에도 화면 쪽 + 물건으로 정확히 처리했다.
