# real16-C12 "3-1의 모션처럼 3-2 영상" (2턴) — PASS 11 / 부분 1 / FAIL 0

## 턴별 판정

| 턴 | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | PASS | "16번 다른 OK처럼으로 진행합니다." (시작 보고에서 13번과 함께 진행 명시; 16 vs 13 첫 줄 선택은 키트 결함 1) |
| 1 | ok-reuse.md + OK 대장의 3-1 영상 카드 하나, 3-2 시작 이미지 카드 (G8) | PASS | reads production-session/SKILL.md, ok-reuse.md, ok-cuts.md; "OK 대장의 3-1 영상 카드와 3-2 시작 이미지 카드" |
| 1 | Higgsfield 3-2 폴더를 [TOOL]로 조회 | PASS | [TOOL] list_folders(project_id=prj-sim-0001) / [TOOL] list_project_assets(folder_id=fld-3-2) |
| 1 | 카드 렌즈(35°) vs 시작 이미지(75mm≈32°) — 시작 이미지가 이긴다고 알림 | PASS | "렌즈는 카드에 35°로 적혀 있지만 시작 이미지가 75mm(약 32°)입니다… 시작 이미지가 우선이라 32°로 씁니다." |
| 1 | 가져온 줄의 사건 수(4)를 한 줄로 알림(ok-reuse §3.0), 위험(Required/Forbidden) 함께 가져옴 | PASS | "이벤트 수: 4개입니다… 이미 승인된 모션이라 그대로 씁니다."; "3-1 카드에 '위험' 줄이 없어 프롬프트의 Required/Forbidden을 가져옵니다." |
| 1 | 입 잠금 문장이 약하면 올림 + 전→후 (ok-reuse §3.1 예외) | PASS | "'no attempt to speak, no lip movement' → 'no attempt to speak, no parted lips, no mouthing'" |
| 1 | 질문 턴에 acting을 열지 않음 (live-action.md:3, 기능 75) | 부분 | T1 reads .claude/skills/acting/SKILL.md, "읽은 것: …연기 스킬" — 연기 줄은 3-1에서 글자 그대로 가져와 새 연기 문장이 없는데도 질문 턴에 열었음 |
| 1 | 빈 칸만 제안값으로 한 묶음(3개), 이음새 불일치는 핸드오프 [5]로 | PASS | "3-3의 확정 첫 프레임은 손녀가 시간표 앞… 핸드오프 [5] '총괄에 올릴 것'에 적겠습니다." |
| 2 | `ACTION_TIMING`·`PHYSICS` 글자 그대로, 본문에 "3-1"·"previous" 없음 | PASS | checker --must-include motion_3-1 OK, 컷 번호 WARN 없음 |
| 2 | 카드 3-2 [7] "가져온 OK: 3-1 영상 — 모션…", 렌즈 관찰 결과 기록 | PASS | diff: "가져온 OK: 3-1 영상 — 모션(ACTION_TIMING, PHYSICS, 돌아서는 속도), 연기(CHARACTER_ACTING), 대사(AUDIO) (제안값)" — 사용자는 "모션"만 말했는데 연기·대사도 가져옴(제안 수락 후라 허용) |
| 2 | 검사 후 표시 (G7) | PASS | Bash check_prompt --kind video tmp/3-2_video.txt --refs 4 --seconds 8 --must-include tmp/3-2_must.txt |
| 2 | G2·G9·G1 | PASS | 한국어, "the screen-right hand, nearer the sign", 생성 없음 ("480p 확인용으로 영상을 보낼까요?") |

## 검사기 결과

- C12 t2 코드블록 1: `--kind video --refs 4 --seconds 8 --must-include grandpa+girl+bag+light+motion_3-1`: OK — video 프롬프트 5147자, 걸린 항목 없음

## 추가 발견

- `The persimmon tree is at screen LEFT.` 문장이 3-1에서 그대로 남았으나 3-2 시작 이미지(75mm)에 감나무가 들어오는지 불명 — 플레이어가 "미측정"으로 알림.

## 키트 결함

- kit/context/tasks.md:8·29 — "3-1처럼 3-2 영상"은 16번 행과 13번 행의 says가 모두 맞아 첫 줄 번호가 체인마다 다름(C12·C15=16번, C13·C16=11번, C14=13번). 고침: 행 16에 "첫 줄은 함께 여는 작업(11/13/14)의 번호를 쓰고 16번은 ok-reuse를 여는 신호로만" 쓰거나 반대로 못박는다.

## 총평

ok-reuse 절차(가져오기·위험 동반·입 잠금 상향·카드 [7])를 정확히 이행. 질문 턴 acting 개봉 1건만 부분.
