# real9-C04 인물 시트 의상 수정 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt` SKILL + `character-edit.md` + OK 대장 CH-001 카드 읽음. "기준 시트 `job-ch001`(참조 1장)". 코트의 색·재질·길이·여밈, 없앨 옛 항목+목둘레, 새 상태 `char_grandpa_winter_v1` 여부, 코트 참조 이미지 유무를 제안값+이유와 함께 한 묶음으로 물음. 신규 제작으로 가지 않음. 정본이 "늦가을"이라 겨울 코트와 어긋남도 짚음 |
| 2 | PASS | 틀 1: `Edit reference image 1 …` / CHANGE — OUTFIT(무릎 길이 남색 울 더플코트, 토글 4개) / REMOVE COMPLETELY(올리브 재킷·크림 조끼·덮개 가슴 주머니) / PRESERVE EXACTLY(HEADLESS `not an injury`, IDENTITY 보존만) / ONLY CHANGE. 목둘레 세 곳 모두 있음, REMOVE 목록 = LEFT 줄 `no …` 목록(3개 일치). 얼굴 재묘사 없음, 참조 1개. 더플코트 후드 때문에 목둘레 제안을 바꾼 이유를 한 줄 알림. 대장 CH-001에 `초안(제안값)` 기록, 생성 안 함 |

검사기: `check_prompt.py --kind image --refs 1` → `OK — image 프롬프트 2567자, 걸린 항목 없음`
추가 발견: 3번 질문(쓸 컷)에 사용자가 답하지 않았는데 "제안값으로 진행"으로 처리하고 정본(늦가을)과 어긋남을 다시 짚음. 규칙 범위 안.
키트 결함: 없음.
총평: real8과 같은 PASS 2. G1: mcp__ 없음, 생성 없음. 읽기도 지도대로.
