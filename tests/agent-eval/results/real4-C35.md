# real4 C35

**PASS 1 / 부분 1 / FAIL 0** (real3 PASS 2 → 하락(구간 초가 늘지 않음))

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt/SKILL.md`만 열림(`fixes.md` 안 열림). 2-1은 승인 컷 → 새 테이크 질문, 느리게 할 동작·길이 질문, 바뀌는 줄 전 → 후 미리 보임 |
| 2 | 부분 | `job-v-2-1` OK 카드에서 한 줄만 전 → 후, 나머지 글자 그대로, 검사 실행. 그러나 §0 표(`SKILL.md:51`)는 '그 구간 초를 늘린다'인데 원래 구간이 이미 `0:04–0:08`(4초)이라 `taking the full four seconds`는 4초→4초라 느려진 것이 없고 `failed take` 문장만 추가됨. 길이 8초 유지를 '늘릴 필요 없음'으로 처리 |

## 검사기
검사기(내 실행, OK 카드 151–213줄에 같은 치환, `--kind video --refs 3 --seconds 8 --must-include grandpa+bag+light`): `OK — video 프롬프트 4205자, 걸린 항목 없음`

## 추가 발견
추가: 없음.

## 키트 결함
`video-prompt/SKILL.md:51` 속도 줄이 '구간 초를 늘린다'만 말해 구간이 이미 동작 전체(4초)일 때를 못 다룸 → '구간이 이미 길면 시작을 앞당기거나 길이를 늘리는 안을 제안값으로 보이고 `taking the full N seconds`의 N이 원래보다 커야 한다'를 덧붙임.
