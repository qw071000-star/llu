# real6 C22

**PASS 2 / 부분 0 / FAIL 0** (real5 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `character.md`; CH-004; 6개 항목 제안값+이유 한 묶음; 앞치마·팔토시는 사용자 값; 직업 소품 제외 명시 |
| 2 | PASS | 틀 1 전문: `mature adult bone structure`, `no babyface`, `lined forehead and crow's feet … reddened knuckles and short unpainted nails`, 왼쪽 패널 A(HEADLESS, `not an injury`), `No profession-signaling props …: no fish, no knife, no bucket, no gloves, no bag`, 시대 금지 줄, 2k·16:9·`fld-chars`; 대장에 `초안(제안값)`; 생성 없음 |

## 검사기
내 실행(`--kind image`, `--refs 0` 둘 다): `OK — image 프롬프트 4738자, 걸린 항목 없음`

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 사용자가 '알아서'라 했는데 6개 질문(허용: 한 번에 물음). 프롬프트에 `LEFT and RIGHT are SCREEN directions` 줄 없음(템플릿에 없음).

## 키트 결함
있음(경미): `instructions.md:28`(규칙 6)은 '프롬프트마다' 화면 방향 문장을 넣으라는데 `image-prompt/character.md` 틀 1(55줄~)에 그 줄이 없음 → 틀 1에 그 문장 한 줄 추가하거나 규칙 6에 '인물 시트 제외' 명시.
