# real5-C04 인물 시트 의상 수정 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real4: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL + character-edit.md(character.md 안 엶) + ok-cuts CH-001 카드. 4항목(새 의상 / 옛 항목·목둘레 / 참조 이미지 없음 / 새 상태 요소 `char_grandpa_winter_v1`, 정본 "늦가을"과 다름)을 제안값+이유로 한 묶음. 신규 재작성 아님 |
| 2 | PASS | `Edit reference image 1: change only the character's outfit…` / CHANGE / REMOVE COMPLETELY / PRESERVE EXACTLY(HEADLESS not an injury, IDENTITY) / ONLY CHANGE. 목둘레 3곳, GONE 목록 = LEFT 줄 `no …` 목록, 얼굴 재묘사 없음. 사용자가 안 정한 토글·후드는 "바꿔 쓴 제안"으로 알림. 위험 5줄, 생성 안 함 |

검사기: `--kind image --refs 1`: `OK — image 프롬프트 2645자, 걸린 항목 없음` (참조 0개로 돌리면 `FAIL 프롬프트 속 참조 태그 1개, 붙일 참조 0개`이므로 --refs 1이 맞음).

추가 발견: 프롬프트 본문에 틀의 안내 괄호 `(by name)`가 그대로 남음: `The faded olive work jacket, … (by name) are GONE in every panel.`

키트 결함: `image-prompt/character-edit.md:45` — `(by name, shoes and small accessories included)`는 사람용 안내인데 코드블록 안에 있어 문장으로 복사됨. 고칠 곳: 괄호를 코드블록 밖 규칙으로 옮기거나 `[…]` 자리표시 안에 넣는다.

총평: 프롬프트 정확. 틀 안내 괄호 누출만 경미.

G1: 모든 턴 tools가 Bash/Write/Edit/Grep뿐, `mcp__` 호출 없음, `generate_*` 없음.
