# real4-C12 "3-1의 모션처럼 3-2 영상" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real3: PASS 2)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | production-session+ok-reuse.md, 3-2 카드·shot-list·ok-cuts·video-prompt SKILL+live-action.md·3-2 핸드오프. "3-1 영상 카드에서 ACTION_TIMING·PHYSICS를 글자 그대로", 카드 [7]에 가져온 OK 기록(git diff). 렌즈 35°→시작 이미지 75mm≈32° 고지. 6항목 제안값+이유(끝·시선·타이밍·연기·렌즈/좌표·이음새) 한 묶음 |
| 2 | PASS | 코드블록 하나, 블록 밖 모드·참조 4·모델·해상도·길이·폴더, 본문에 "3-1"/previous 없음(grep 0), 동서남북 없음. 입 잠금·`Nobody looks at the camera`·`Exactly 2 people` 이월, 3-1에서 바꾼 줄 전→후 목록. 검사 실행 |
검사기(`--kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light+motion_3-1`): `OK — video 프롬프트 5119자, 걸린 항목 없음`
추가 발견: AUDIO 입 잠금 문장을 3-1의 `no lip movement`에서 더 강한 문장으로 올림(전→후로 알림, 허용).
키트 결함: 없음.
총평: 모션 이월·렌즈 충돌 고지·검사 모두 충족.
