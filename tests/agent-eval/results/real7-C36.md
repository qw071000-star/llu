# real7-C36 — 레지스터와 부딪치는 연기 ("웃게")

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 맞음: `acting` 안 엶(reads: shot-list·production-session·decisions·asset-registry·ok-cuts·video-prompt SKILL·live-action·cut-card). `decisions.md` §5 절제 인용, "살짝"을 "입술 다문 옅은 미소, 입꼬리·눈가만, 이빨 보이면 실패"로 범위 안에 둠(2), 컷 목록 "같은 얼굴"과 다른 방향 질문(1), 6개 한 묶음, 생성 없음. 미달: (a) 이웃 2-1 OK의 연기(`ok-cuts.md` 목록 줄 "할아버지 표정(기대 안 하는 얼굴)")가 웃음과 반대인데 짚지 않음(must-ask 실사 영상 "먼저 짚는다" 마지막 항목). 2-1은 위치만 이음새로 씀. (b) 양 끝 failed take 중 웃음 쪽(이빨·소리)만 말하고 무표정 쪽 끝은 1턴에 없음(2턴 프롬프트에는 있음) |
| 2 (그대로, 프롬프트 턴) | PASS | `acting/SKILL.md` 엶. 코드블록 1(15블록), 블록 밖 모드·시작 이미지·참조 3·모델·해상도·화면비·길이·소리·폴더, 사건 2·비트 1, 위험 표 5, 양 끝 `teeth showing, a laugh or a broad grin = failed take, and a face that never changes = failed take`, 손 `the screen-left hand, nearer the tree`. `cuts/2-2.md` v0 신규(`(제안값)`) + 6답 기록. "보낼까요?" 생성 없음 |

검사기(내 실행, `--kind video --refs 3 --seconds 8`, must-include grandpa+bag+light): `OK — video 프롬프트 5418자, 걸린 항목 없음`.
추가 발견: 검사용 임시 파일은 scratchpad로 옮김(좋음). 읽기 목록 `_p22.txt`는 RUN 루트에서 지움.
키트 결함: `.claude/context/must-ask.md:67` "이웃 컷 OK의 연기(목록·연속성 표)"가 어느 표인지 모호해 플레이어가 컷 목록·연속성 표(연기 열 없음)만 보고 OK 대장 목록표의 "OK 이유" 칸을 놓침. 고칠 것: "이웃 컷 OK의 연기(OK 대장 목록표 'OK 이유' 칸)"로 쓴다.
6회차 대비: PASS 2 → PASS 1 / 부분 1 (이웃 2-1 연기 미지적, 6회차는 2-1 카드를 열어 지적).
총평: PASS 1 / 부분 1 / FAIL 0.
