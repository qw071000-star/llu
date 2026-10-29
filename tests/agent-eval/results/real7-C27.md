# real7 C27

**PASS 2 / 부분 0 / FAIL 0** (real6 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `character-edit.md` 틀 2; 기준 `job-ch001`; 55세·나이 표지 제안값; 의상은 그대로(회상 의상은 시트 확정 뒤 따로); `char_grandpa_50s_v1` 제안; 2k; 생성 없음 |
| 2 | PASS | `IDENTITY BONES` 줄, HEADLESS `not an injury`, 얼굴 새로 묘사 없음, `OUTFIT: the exact same clothes`, 위험 목록, 바뀐 값 전 → 후, 대장 `초안(제안값)` |

## 검사기
내 실행 `--kind image --refs 1`: `OK — image 프롬프트 1656자, 걸린 항목 없음`.

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 70대 → 55세는 '젊게'인데 끝 줄이 `no babyface, no exaggerated old-age makeup` 그대로(틀의 `[젊게면 이 구절 대신 no beauty filter]` 미적용, 경미).

## 키트 결함
있음(경미): `image-prompt/character-edit.md:99-100`의 `[젊게면 이 구절 대신 no beauty filter]`가 어느 구절을 바꾸는지 모호(`no babyface`? `no exaggerated old-age makeup`?) → 늙게/젊게 끝 줄을 두 줄로 따로 적는다.

## 총평
나이 수정 틀 2 충실.
