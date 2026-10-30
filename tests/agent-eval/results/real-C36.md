# real-C36 — 레지스터와 부딪치는 연기 ("웃게")
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | production-session·video-prompt·acting 열람. "입을 다문 채 입꼬리만, 이는 보이지 않음", 컷 목록 "같은 얼굴로"와 충돌 짚음, 7항목 한 번에 질문. 2-1 표정 OK와의 관계는 안 물음 → 기대 오류(키트는 이웃 OK를 기준 하나만 읽게 함, 2-1 OK 연기 줄 `a smile = failed take`와의 충돌은 키트가 열라고 하지 않음) |
| 2 ("그대로", 프롬프트 턴) | 부분 | 양 끝 failed take(`visible-teeth grin or a laugh` / `face that never changes`), 화면 기준 손, 고정문 그대로. 검사기 플레이어 미실행. 내가 돌린 결과 아래: WARN 길이 5776자를 이유 없이 남김 |
검사기(내 실행, `--kind video --refs 3 --seconds 8 --must-include grandpa+identity+bag+light`): `WARN  길이 5776자. 5,500자 이하가 안전했다 … — FAIL 0 · WARN 1 · 5776자`
추가 발견: 시작 이미지 태그를 `<<<job-ff-2-2>>>`로 씀(보고에 명시, 요소 ID 부재 때문). PRE_SHOT_CONTINUITY 블록 없음(선택 규칙, 문제 없음).
키트 결함: 검사기 허용 규칙 없음(C35 참조). `must-ask.md` 실사 영상 "먼저 짚는다"에 "이웃 컷 OK의 연기 줄이 이번 요청과 반대일 때" 항목이 없음 → 한 줄 추가하면 2-1 대비를 짚게 됨.
총평: 연기 처리 좋음, 길이 WARN 미공개. PASS 1 / 부분 1 / FAIL 0.
