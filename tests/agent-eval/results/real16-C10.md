# real16-C10 영상, 일부만 답함 (3-3) (3턴) — PASS 10 / 부분 1 / FAIL 0

## 턴별 판정

| 턴 | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄 | PASS | "13번 실사·인물 영상으로 진행합니다." |
| 1 | video-prompt + live-action.md 열기, acting은 질문 턴에 열지 않음 (G8, 기능 67) | PASS | T1 reads video-prompt/SKILL.md, live-action.md (skills=[] , acting 없음) |
| 1 | 카드 3-3 빈 칸을 제안값·이유로 한 번에(6개), 렌즈·길이·소리·고정은 "기본값으로 씀" | PASS | "**기본값으로 씀:** Seedance 2.5 · 확인 480p · 8초… 렌즈는 시작 이미지의 50mm(47°)"; 1. 끝 상태 … 6. 이음새 |
| 1 | 카드 [4]와 시작 이미지가 다름을 짚음 | PASS | "카드 [4]는 '정류장 정면을 봄'이라 쓰여 있습니다. 시작 이미지는 시간표 맞은편… 시작 이미지가 이기므로" |
| 2 | 렌즈(망원)·대사만 반영, 나머지 제안값으로 카드 [3]~[6] 기록 + `(제안값)` 표시 | PASS | "'나머지는 몰라'라고 하셨으니 1~6번은 제안값으로 씁니다."; diff 3-3.md [3]~[6] (제안값) |
| 2 | 망원이 시작 이미지(50mm)와 부딪침을 한 번 물음 — 허용(키트 모호 아님) | PASS | "1. 렌즈: 제안 — 시작 이미지 그대로 50mm(47°)… 망원(85mm, 29°)을 꼭 쓰려면 시작 이미지를 망원으로 새로 만들어야" |
| 3 | acting 열고 15블록 전문, 렌즈는 화각° + 관찰 3개(mm 없음) | PASS | meta skills=[acting]; "Diagonal field of view about 47°. GIRL and the timetable sign fill the right half… / straight lines stay straight" |
| 3 | 손녀 의상·LIGHT LOCK 글자 그대로, 소리(대사 없음→효과음만) | PASS | checker girl+light OK; "[AUDIO] No dialogue… Distant wind over the paddies… No music." |
| 3 | 검사 후 표시 (G7), 생성 안 함 (기능 6) | PASS | Bash check_prompt --kind video … --refs 2 --seconds 8 ×2 (첫 회 WARN: PHYSICS 손 표현 → 수정); "'영상으로 만들어'라고 해 주세요." |
| 3 | G2 한국어 | 부분 | "Now I'll update the card's lens line and delete the tmp files." (영어 서술) |
| 전체 | G9 화면 기준 손 | PASS | "the screen-right hand, nearer the sign" |

## 검사기 결과

- C10 t3 코드블록 1: `--kind video --refs 2 --seconds 8 --must-include girl+light`: OK — video 프롬프트 4903자, 걸린 항목 없음

## 추가 발견

- 없음

## 키트 결함

- kit/context/tasks.md:8 — 영어 서술 1건(C04 결함 2와 동일).

## 총평

질문 단계(렌즈 충돌 짚기)와 15블록 모두 기대대로. 영어 서술 1줄만 부분.
