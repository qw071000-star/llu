# real3-C11 (C11 1~3턴 + C26 4~6턴)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | video-prompt SKILL·background.md만 엶(+ok-cuts). "기본값으로 씀: Seedance 2.5 · 480p · 8초 · 16:9 · 삼각대 고정 · 소리는 효과음만 · 시작 이미지 job-ff-1-1 · 저장 fld-1-1". 질문은 움직일 것·Keep 2개뿐, 생성 안 함 |
| 2 | PASS | "시작 이미지의 감나무는 잎이 없는 맨가지", "정본은 컷당 8초(decisions §1), 1-2가 0:08 시작" 두 충돌을 한 번에. 푸시인 5% 제안값 |
| 3 | 부분 | 내용 PASS: Camera/Motion/Keep/Silent 4문단, %단위, 끝 상태 없음, 카드 v1 `(제안값)`, 실패 위험 6줄, 검사 실행. 감점: 같은 Bash에서 `cat cut-card.md; cat project/cuts/3-3.md`로 다른 컷 카드를 형식 예시로 엶(cut-card.md:3, routing §3 위반, G4) |
| 4 | PASS | 구름 줄만 "전 3% → 후 1.5%", 다른 문단 그대로, 카드도 고침, 검사 실행. fixes.md 안 엶 |
| 5 | PASS | 풀 추가 시 4개>3 알림, 구름 뺄까 제안을 전→후로, 그루터기 확인. 파일 안 건드림 |
| 6 | PASS | 시작 이미지/승인 프롬프트에 별 없음(추정 표기), 모델 한계, 후반 오버레이, 사건 수 초과, 생성 안 함 |

검사(3턴 프롬프트): `--kind video --refs 0 --seconds 10` → `OK — video 프롬프트 1049자, 걸린 항목 없음`. 4턴 수정본(구름 줄 치환) → `OK — video 프롬프트 1056자, 걸린 항목 없음`.

**PASS 5 / 부분 1 / FAIL 0** (2회차 PASS 6 / 0 / 0 → 3턴 열람 감점으로 한 칸 후퇴)

G1 OK, G9 OK(screen right/left만). 추가 발견: 6턴이 5턴 제안(구름 제외)을 확정처럼 전제(사소, 지난 회차와 같음).
키트 결함: 없음(규칙은 cut-card.md:3·routing §3에 이미 있고 플레이어가 어김). 경미 제안: `video-prompt/SKILL.md:57`에 "카드가 없으면 production-session/cut-card.md 틀로 만들고 다른 컷 카드는 열지 않는다" 한 구절.
총평: 소리 안 묻기·전→후·검사 유지, 새 카드 쓰며 이웃 컷 카드를 연 것만 흠.
