# real3-C14

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | ok-reuse.md(Bash cat), 2-1 영상 카드·2-2 시작 이미지 카드, video-prompt SKILL·live-action.md. "2-1 CHARACTER_ACTING 할아버지 줄을 가져옴", 시작 이미지 job-ff-2-2(85mm), 2-1 낙엽 한계는 프레이밍상 안 가져온다고 설명. 5문항(사건·타이밍·끝 상태·이음새·소리) |
| 2 | PASS | CHARACTER_ACTING 첫 문장이 `acting_2-1.lines`와 글자 일치(뒤에 새 문장 2개 덧붙임), 입 잠금 강화를 전→후로 알림, `screen-left hand, nearer the tree`. 코드블록 하나+블록 밖 모드·참조3·모델·해상도·길이·폴더 |

검사(내가): `--kind video --refs 3 --seconds 8 --must-include grandpa+bag+light+acting_2-1` → `OK — video 프롬프트 4918자, 걸린 항목 없음` (플레이어 보고와 일치).

**PASS 2 / 부분 0 / FAIL 0** (2회차 PASS 2 유지)

추가 발견(사소): 2턴에 acting/SKILL.md를 엶. 2-1 줄에 새 손 동작 문장을 더해서 경계 사례(routing.md:27). 키트 결함: 없음.
총평: 표정 줄 이월 정확, 검사 통과.
