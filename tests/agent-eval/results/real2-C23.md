# real2-C23 — 의상 수정 + 의상 참조 (실제 Claude Code)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | reads: image-prompt/SKILL.md, character-edit.md만. 질문 6개 한 묶음(밑 옷·후드·여밈·목둘레·주머니·저장 방식), 프롬프트·생성 없음. "기본값으로 씀: … 참조 1 job-ch002, 참조 2 job-ref-coat". 사진은 `[TOOL] job_display(job-ref-coat)`로 조회(sim에 있음) |
| 2 | PASS | 권한 줄 3개(`Reference image 1 controls…`/`image 2 controls only…`/`Do not transfer the face, body, pose, background or lighting from reference image 2`). 목둘레 3곳(`At the neckline`/`Its clothes change fully`/`including the neckline of the headless panel`). REMOVE `The yellow raincoat, its yellow hood and its yellow flap pockets are GONE` = LEFT `no yellow raincoat, no yellow hood, no yellow flap pockets` 일치. 남색 교복·흰 양말·빨간 장화 유지. 얼굴 재묘사 없음. 생성 안 함, 주머니 `(제안값)` |
검사기(채점자, --kind image --refs 2): `OK — image 프롬프트 2924자, 걸린 항목 없음`. 플레이어도 돌려 "2924자"로 보고(G7 PASS).
지난 회차 대비: 부분(GONE 목록과 LEFT 목록 불일치) -> **고쳐짐**.
추가 발견: 없음(mcp 호출 없음).
키트 결함: 없음.
총평: PASS 2 / 부분 0 / FAIL 0
