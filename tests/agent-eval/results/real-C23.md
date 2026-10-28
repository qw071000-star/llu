# real-C23 — 의상 수정 + 의상 참조
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL·character-edit.md만 열고 질문 4개 한 묶음(범위·입는 상태·주머니·인물 설정/이 컷만), 프롬프트 없음. "기본값으로 씀: … 참조 1 job-ch002, 참조 2 job-ref-coat" |
| 2 | 부분 | 권한 줄 3개·목둘레 3곳 있음. 그러나 REMOVE의 GONE 목록(우비·후드·플랩 주머니)과 LEFT 줄 끝 `no yellow raincoat, no yellow hood`가 어긋남(주머니 빠짐). 틀의 `No trace of [old items]`를 `No trace of yellow`로 바꿈. 검사기는 "실행 승인 안 남"으로 못 돌림(키트가 허용한 보고) |
검사기(채점자 실행): `OK — image 프롬프트 2840자, 걸린 항목 없음` (--kind image --refs 2)
추가 발견: 없음(mcp 호출 없음, [TOOL] job_display는 시뮬레이션 줄).
키트 결함: `character-edit.md` 규칙 "목록을 맞춘다"가 한 줄이라 반복해서 놓친다 -> 틀 1에 GONE 목록 = LEFT `no …` 목록임을 `[old 1], [old 2], [old 3]`처럼 세 자리 예시로 보인다.
총평: PASS 1 / 부분 1 / FAIL 0
