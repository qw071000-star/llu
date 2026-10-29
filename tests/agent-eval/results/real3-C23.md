# real3-C23 — 의상 수정 + 의상 참조 (실제 Claude Code)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | reads: image-prompt/SKILL.md, character-edit.md만(character.md 안 염). 질문 5개 한 묶음(밑 옷·후드/목둘레·여밈·주머니·범위=인물 설정 자체인지), 프롬프트·생성 없음. "기본값으로 씀: … 모델·2k·16:9·fld-chars". 코트 사진 내용을 답에 썼으나 `[TOOL] job_display` 줄이 없음(플레이어 규칙 4 경미) |
| 2 | PASS | 권한 줄(`Reference image 1 controls…`/`image 2 controls only…`/`Do not transfer the face, body, pose, hanger, background or lighting from reference image 2`). 목둘레 3곳(`At the neckline`/`Its clothes change fully`/`including the neckline of the headless panel`). GONE(raincoat·two flap pockets·glossy yellow fabric) = LEFT 끝 `no …` 3개 일치. 교복·양말·장화 유지. 얼굴 재묘사 없음. 생성 없음 |
검사기(채점자, 채팅 코드블록을 뽑아 --kind image --refs 2 --must-include LEFT/RIGHT 줄): `OK — image 프롬프트 2810자, 걸린 항목 없음`. 플레이어도 2810자 보고(G7 PASS).
지난 회차(real2) 대비: PASS 2 유지.
추가 발견: 검사용 임시 파일을 `out/`에 씀(`out/prompt_ch002_duffle.txt`, `out/must_ch002_duffle.txt`), 플레이어 규칙 5는 `tmp/`. 키트 결함 아님.
키트 결함: 없음.
총평: PASS 2 / 부분 0 / FAIL 0
