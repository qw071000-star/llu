# real4-C08 퍼스트 프레임, 정보 부족 3-4 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real3: PASS 2)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | image-prompt SKILL+first-frame.md, 3-1 시작 이미지 OK 카드(first-frame.md:32 인물 자리 예외). 4항목(카메라=LC-001-V1과 같은가→틀 1 / 자리 / 동작·손 / 시선) 제안값+이유, 모델·1k·`fld-3-4`·가방 닫힘·인원 1은 "기본값으로 씀". 감점: Bash에서 `cat cuts/3-3.md; ls cuts; ls log`로 이웃 컷 카드(3-3)를 엶(routing §3 "다른 컷 카드 열지 않는다"). 답의 "읽은 것"에는 3-3 카드가 빠져 있음 |
| 2 | PASS | 틀 1: `Edit <<<loc_busstop_road_v1>>> WITHOUT reframing …`, `LEFT and RIGHT are SCREEN directions …`, 의상·가방·LIGHT LOCK 글자 그대로, `Exactly one person is visible.`, 손은 `the screen-left hand, nearer the persimmon tree`, 태그 3=참조 3, 자리표시 태그 없음. 카드 `project/cuts/3-4.md` 신규(cut-card.md 열람), [4][5]에 `(제안값)`. 블록 밖 모드·참조·모델·해상도·저장. 생성 안 함 |
검사기(`--kind image --refs 3 --must-include grandpa+bag+light`): `OK — image 프롬프트 2211자, 걸린 항목 없음`
추가 발견: 카드 [4]에 틀의 `[고정/움직임]` 자리표시가 남음(카드라 허용).
키트 결함: 없음(routing.md:34가 "새 카드도 cut-card.md 틀을 복사"를 이미 말함. 플레이어가 지시를 어김).
총평: 프롬프트는 정확, 질문 턴에서 이웃 카드를 연 것만 흠.
