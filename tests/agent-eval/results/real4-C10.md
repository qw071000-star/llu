# real4-C10 영상, 일부만 답함 3-3 (3턴) — PASS 2 / 부분 1 / FAIL 0 (real3: PASS 3)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | production-session+video-prompt SKILL+live-action.md+3-3 카드·shot-list·decisions·registry·ok-cuts. 7항목(소리·대사 / 사건 / 끝 상태 / 타이밍 / 연기 양 끝 / 이음새 / 완료 조건) 제안값+이유 한 묶음, 렌즈는 "기본값으로 씀: 50mm≈47°"로 묻지 않음. 감점: 질문 단계인데 `acting/SKILL.md`를 엶(routing.md:23 "영상이면 프롬프트를 쓰는 턴에 연다, 질문 단계는 must-ask로 충분") |
| 2 | PASS | 카드 3-3 [1][3]~[6]을 `(제안값)`으로 기록(git diff 확인). 망원(≈85mm)이 시작 이미지 50mm와 달라 "50mm 유지 / 퍼스트 프레임 다시" 한 번 질문 — 시나리오 2턴 PASS 조건 |
| 3 | PASS | 15블록 전문. OPTICS `Diagonal field of view about 47°`+관찰 3개(mm 없음), 의상(girl)·LIGHT LOCK 글자 그대로, `Nobody looks at the camera`, 손은 `the screen-right hand, nearer the sign`, 타이밍 0:00–0:03–0:04–0:07–0:08 연속, AUDIO 효과음만, 입 잠금, `Exactly one person`. 위험 6줄. 검사 실행, 생성 안 함 |
검사기(`--kind video --refs 2 --seconds 8 --must-include girl+light`): `OK — video 프롬프트 5361자, 걸린 항목 없음`
추가 발견: 3턴 끝 "견적 약 40 크레딧"은 근거 없는 수치(경미). 검사를 절대경로로 돌림(video-prompt/SKILL.md:92 "절대경로 없이"와 다름, 하네스 임시 폴더 때문).
키트 결함: 없음.
총평: 프롬프트·기록은 정확, 1턴에 acting을 연 것만 감점.
