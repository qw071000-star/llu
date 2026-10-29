# real4 C27

**PASS 1 / 부분 1 / FAIL 0** (real3 PASS 2 → 하락(젊게 표지 문구))

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `character-edit.md` 틀 2, 기준 `job-ch001`, 55세 제안·나이 표지(주름 얕게·머리색·자세·손)·의상 유지 제안·`char_grandpa_age50_v1`. 생성 없음 |
| 2 | 부분 | `IDENTITY BONES`, HEADLESS `not an injury`, 얼굴 재묘사 없음, 표지 OK. 그러나 `character-edit.md:103`('젊게 할 때 … 끝 줄에 `no beauty filter`를 더한다')를 놓침: 끝 줄이 `no babyface, no exaggerated old-age makeup, …` 그대로이고 `no beauty filter` 없음 |

## 검사기
검사기(내 실행, `--kind image`): `OK — image 프롬프트 1703자, 걸린 항목 없음` (플레이어는 첫 실행의 좌표 WARN을 문장 추가로 해소)

## 추가 발견
추가: 없음.

## 키트 결함
`image-prompt/character-edit.md:99~103` 틀 끝 줄에 `no exaggerated old-age makeup`이 박혀 있고 젊게 할 때의 `no beauty filter`는 틀 밖 한 줄(103)에만 있음 → 틀 99줄에 `[젊게면 old-age makeup 대신 no beauty filter]`를 넣어 틀 안에 둔다.
