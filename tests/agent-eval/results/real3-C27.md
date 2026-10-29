# real3-C27 — 할아버지 50대 시트
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | reads: image-prompt SKILL·character-edit.md. `character.md` 안 염(real2 후퇴 **복구**). `job-ch001` 기준 틀 2, 목표 55세, 나이 표지 제안(주름·머리색·턱선·자세·손), 의상 그대로(한 생성에 하나), 파생 `char_grandpa_50s_v1`, 2k. 질문 4개 한 묶음. 경미: 시트 수정인데 shot-list.md도 cat |
| 2 | PASS | 틀 2 전문, `IDENTITY BONES` 줄 틀 그대로, HEADLESS `not an injury`, 얼굴 새 묘사 없음. 코드블록 밖에 "바꾼 값 (전 → 후)". 생성 없음, 위험 4개. 틀의 노화 표지를 반대로 쓴 것을 스스로 밝힘 |
검사기(채점자, --kind image --refs 1): `OK — image 프롬프트 1741자, 걸린 항목 없음`. 플레이어도 1741자 보고.
지난 회차 대비: 부분 1 -> PASS 2(**개선**).
추가 발견: ONLY CHANGE 끝의 `no exaggerated old-age makeup`을 `no beauty filter, no digital smoothing`으로 바꿈(젊어지는 방향이라 타당).
키트 결함: `image-prompt/character-edit.md:76~101` 틀 2가 "나이 들게" 예시만 있다(sagging·thinner lips·greying·old-age makeup). 젊게(50대, 12살) 표지 줄이 없어 플레이어가 즉석으로 반대 문구를 지음 -> 틀 아래에 "젊게 할 때 표지(주름 얕게·검은 머리에 흰머리 조금·곧은 어깨·손 탄탄) / `no beauty filter`" 한 줄 추가.
총평: PASS 2 / 부분 0 / FAIL 0
