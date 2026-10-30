# real4 C22

**PASS 2 / 부분 0 / FAIL 0** (real3 PASS 2 유지(단 검사기 새 WARN은 오탐, 아래 결함))

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `character.md` 열림, CH-004·`char_fishmonger_autumn_v1`, 7개 칸을 제안값으로 한 묶음 질문('알아서'인데 한 번만 묻고 이유 붙임) |
| 2 | PASS | 틀 1: `mature adult bone structure`, `no babyface`, `lined forehead and crow's feet … reddened knuckles and short unpainted nails`, HEADLESS + `not an injury`, 앞치마·팔토시만, `No profession-signaling props unless explicitly requested: no fish, no basin …`, 시대 금지 줄, 2k 16:9 `fld-chars`. 생성 안 함. 연기 프로필·목소리는 두 번째 코드블록(약 140단어, 목표 150~220에 못 미침을 스스로 적음) |

## 검사기
검사기(내 실행, `--kind image`): 시트 `WARN  인물이 있는 프롬프트에서 좌우를 썼는데 좌표 문장이 없다 … — FAIL 0 · WARN 1 · 4715자`. 원인은 `character.md:79` 틀 문구 `Keep exactly the same body proportions in the left and center panels`(패널 이름)이라 **검사기 오탐**. 연기 프로필 블록도 `a child is left waiting`에 같은 WARN(이미지 프롬프트 아님, 오탐).

## 추가 발견
추가: 연기 프로필이 150단어 미만(`acting` §6).

## 키트 결함
`higgsfield-generation/check_prompt.py:68` 좌표 문장 WARN이 `character.md:79`·`character-edit.md` 틀의 자기 문구 `left and center panels`에 걸림 → 룩어헤드에 ` and (?:center|centre|right) panels?`를 예외로 추가.
