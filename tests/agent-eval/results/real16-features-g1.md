# real16 기능 판정 — 묶음 G1 (C01–C16, C19, C20)

판정 기준: `feature-map.md`에서 이 묶음 체인에 매핑된 기능 번호 + 전 체인 공통 1·2·27·35. 근거는 `real16-<체인>.md` 표와 플레이어 출력/메타에서 인용했다. 해당 체인에서 확인되지 않는 기능은 "해당 없음"으로 적었다.

| 기능 # | 판정 | 체인·턴 | 근거 |
|---|---|---|---|
| 1 답 한국어·프롬프트 영어 | 부분 | 전체; C04 t2, C06 t2, C10 t3, C01 t1, C08 t1, C16 t1 | 프롬프트 본문은 전부 영어(검사기 통과). 그러나 도구 사이 영어 서술 3건 — C04 t2 "Check passed, so I'll delete the tmp files…", C06 t2 "Now the registry `초안(제안값)` line…", C10 t3 "Now I'll update the card's lens line…" — 과 'canon' 음차 오기 3건 "캔온(정본)"(C01 t1)·"캔on"(C08 t1)·"캔런"(C16 t1) |
| 2 첫 줄 "N번 작업명으로 진행합니다." | PASS | 전체 18체인 | 모두 실제 번호: C01 "1번 새 작품 시작으로…", C02 "2번 오늘 할 일·세션 시작·컷 카드·핸드오프로…", C05 "7번 장소 새 시점으로…", C11 "14번 배경 영상으로…", C20 "8번 장소 고치기로…". 경미: C13 t1 첫 줄에 괄호 덧붙임, C06 t1 첫 줄 중복. 16번 vs 11/13/14 첫 줄 번호가 체인마다 다름(C12·C15=16, C13·C16=11, C14=13) — 키트 결함 |
| 5 시작 문구 없이 컷 번호만으로 이어 감 | PASS | C02 t1, C15 t1 | C02 "3-2"만으로 cuts/3-2.md·핸드오프 3-2·OK 카드를 스스로 읽음; C15 "3-1처럼 3-3 영상 만들어줘"에 시작 문구 요구 없음 |
| 6 "이미지로/영상으로 만들어", "보내"에만 생성 | PASS | C10 t1–t3, C19 t1, C09 t1 | C10 t3 "이대로 영상 480p로 보낼까요? '영상으로 만들어'라고 해 주세요."; C19 "'바로 만들어'는 보여드린 프롬프트에 대한 지시가 아니어서"; C09 "'만들어'는 …생성 지시로 보지 않고"; 전 체인 `[TOOL] generate_*` 0건 |
| 8 확인 1k·480p, 고해상도는 확정 뒤 | PASS | C03 t2, C05 t2, C10 t1 | C03 "해상도: 2k (인물 시트는 처음부터 2k)" 예외 규칙대로; C05 "1k 확인"; C10 "확인 480p"; 1080p/2k 재렌더 제안 없음 |
| 10 모호한 말 → 구체적 값 제안 | PASS | C11 t4, t6; C05 t2 | C11 t4 "3% → 1.5%"(속도 절반), t6 별 → 후반 덧입힘 제안; C05 "벤치 높이" → "벤치 앉는 면, 약 0.45m… 1.1m로 읽을 수도, '추정'" |
| 11 변환 표 대신 그때그때 묻기 | PASS | C11 t2, t5 | t2 잎/길이/전진량 3개를 구체 값으로, t5 "뺄 것" 1개만 — 표를 보이지 않음 |
| 12 한 번에·제안값과 이유·두 번 묻지 않음 | 부분 | C10 t1–t2 (PASS), C11 t6 | C10 t1 6개 한 묶음 제안·이유, t2는 충돌 1건만 재질문(허용). 그러나 C11 t6 "2. 이전에 물은 것: 제안 — 감나무 가지·남은 감 흔들림을 빼고 풀 흔들림을 넣음"이 t5와 같은 항목 재질문 |
| 13 묻지 않는 것(모델·해상도·렌즈 등) | PASS | C02 t1, C11 t1, C12 t1, C03 t1 | C02 "렌즈: 카드 [4]는 35°인데… 시작 이미지가 우선이라 32°로 진행"(질문 아님); C11 "기본값으로 씀: Seedance 2.5, 480p…"; C03 "저장 폴더: `fld-chars`" |
| 14 먼저 짚는 것(정본과 다름 등) | PASS | C07 t1 (+C11 t2, C10 t1) | C07 "이 작품의 룩은 실사 필름입니다(`decisions.md` §3). '수채화'는 그 룩과 달라서" + "승인된 `job-ff-3-3`은 그대로 둠" |
| 15 새 작품 질문 14개, 다시 묻지 않음 | PASS | C01 t1–t3 | t1 표 14행 한 번; t2 "작품명(가제)은 필수라…" 하나만; t3 재질문 없음 |
| 16 화면 기준 방향, 손 = 화면 쪽 + 물건 | PASS | C05 t1–t2 (+C08, C10, C13) | C05 "timetable sign is at screen LEFT… persimmon tree is at screen RIGHT"; C08 "the screen-left hand, nearer the persimmon tree"; 동서남북 0건. 경미: C15 t1 한국어 문장 "시간표 쪽 손"(화면 쪽 누락) |
| 18 반대쪽 카메라 좌우·빛 뒤집기 | PASS | C05 t1, t2 | t1 "낮은 저녁 해는 이 뷰에서 화면 오른쪽으로 옵니다"; t2 LIGHT LOCK "from screen left" → "from screen right, the persimmon-tree side", 검사기 OK |
| 19 사건은 동사마다 센다, 승인 동작은 예외 | PASS | C12 t1 | "이벤트 수: 4개입니다(손녀가 돌아섬, 대사, 한 걸음, 할아버지가 시선을 내림). 이미 승인된 모션이라 그대로 씁니다." (ok-reuse §3.0) |
| 20 한 생성에 한 가지 | PASS | C20 t1 | "2단계로 나눕니다. 1단계는 형광등만 켭니다… 2단계는 해 진 직후 하늘과 빛으로" |
| 21 컷 사이 이어짐(연속성 표) | PASS | C08 t1–t2, C13 t1 | C08 "가방은 0:00에 닫힘(`decisions.md` §6, 3-3→3-4 이음새)"; C13 "3-5는 3-4 끝 상태를 잇습니다. 가방은 열린 채…" + 카드 [6] 이음새 "(제안값)" |
| 22 이미지 프롬프트 종류별 | PASS | C03 t2, C04 t2, C05 t2, C06 t2, C08 t2, C20 t2 | 6종 모두 검사기 OK(4648/2578/2913/1071/2235/1634자). 경미: C04 `No profession-signaling props.` 누락 |
| 23 실사 15블록 / 배경 4문단 | PASS | C10 t3, C11 t3 | C10 t3 15블록 전부(검사기 OK 4903자); C11 t3 "Camera: / Motion: / Keep… / Silent:" 4문단 |
| 25 "3-1처럼" | PASS | C12 t1–t2, C13 t1–t2, C14 t1–t2, C15 t1, C16 t1 | 가져올 것 되묻기(C15), 글자 그대로 옮기기(C12 motion_3-1·C14 acting_2-1 검사기 통과), 카드 없을 때 `get_project_asset_prompt`(C16) |
| 26 고정 문장 글자 그대로 | PASS | C04 t2, C10 t3, C12 t2, C14 t2 | `--must-include`(의상·가방·LIGHT LOCK·모션·연기 줄) 모두 통과 |
| 27 검사 스크립트를 보이기 전에 | PASS | C03/C04/C05/C06/C08/C10/C11/C12/C13/C14/C20 | 각 프롬프트 턴 meta bash에 `check_prompt.py --kind … tmp/…` 실행 기록, 단독 호출 형식. C03 첫 회 FAIL → 수정 후 통과 |
| 28 정본 우선, 정본 초안 | PASS | C01 t3 | diff: decisions 줄마다 "(2026-10-30, 기본값)/(사용자 답)", registry ID만 배정, ok-cuts 예시 삭제 |
| 29 폴더·승인·거절·크레딧 기록 | PASS (폴더 부분만 검증) | C19 t1 | "`3-6 [대기]` 아래에 `승인`과 `거절`… 제가 만들까요, 직접 만드시겠어요?" — 승인·거절·크레딧 기록은 이 체인에서 발생하지 않아 미검증 |
| 33 항상 읽힘 / 필요할 때만 | PASS (참고) | 전체 meta | 각 체인이 작업 행의 SKILL.md와 단계 파일만 열었음. 예외 C12 t1 acting(기능 75) |
| 35 열면 안 되는 파일 | PASS | 전체 18체인 meta | cuts/·log/ 읽기는 자기 컷만(C02 3-2, C07·C10·C15 3-3, C12 3-2); 이웃 컷 카드·핸드오프 0건, RUN 밖 읽기·mcp 호출 0건 |
| 38 질문 14개를 표 하나로 | PASS | C01 t1 | 14행 표 + "바꿀 것만 답해 주세요. 나머지는 기본값으로 합니다." |
| 39 대본·콘티 한 번만 | PASS | C01 t1–t3 | t1 "대본이나 스토리보드가 있나요? 답이 없으면 없는 것으로 보고 다시 묻지 않습니다." t2·t3 재질문 없음 |
| 40 정본 4개 초안 | PASS | C01 t3 | diff 4개 파일(decisions·shot-list 장면 1~3 `대기`·asset-registry·ok-cuts) |
| 41 Higgsfield 프로젝트·폴더 만들고 ID 기록 | 부분 | C01 t3 | registry `prj-new-0001`·`fld-00 에셋`·`fld-99 시험·보관` 기록, 그러나 `[TOOL] create_project/create_folder` 줄 0개. 키트에 `create_project`가 어디에도 없음(project-setup/SKILL.md:52) |
| 42 다음 순서 안내 | PASS | C01 t3 | "1. 인물 시트(할아버지, 손녀) 2. 장소 마스터 3. 소품 4. 컷 나누기와 컷 카드 발행" |
| 43 고치는 사람 | PASS | C02 t1, C12–C14 | C02 파일 무변경; 컷 세션 C12·C13·C14는 자기 컷 카드만 쓰고 shot-list 불변("`shot-list.md`는 건드리지 않았습니다.") |
| 44 총괄 세션 | 해당 없음 | — | C02는 컷 세션("3-2"); 총괄은 C38·C49·C60에서 확인 |
| 45 컷 세션 읽기 범위 | PASS | C02 t1 | 자기 카드 + shot-list + 마지막 핸드오프 + 3-2 시작 이미지 카드 + 3-1 영상 카드(참조) — 3-1·3-3 카드·핸드오프 없음 |
| 46 컷 카드(질문 턴엔 안 만듦) | PASS | C08 t1–t2, C10 t1–t2, C11 t1–t3 | C08 t1 "카드와 정본에는 아무것도 쓰지 않았습니다", t2 새 project/cuts/3-4.md; C11 t1·t2 카드 없음, t3 project/cuts/1-1.md |
| 48 ok-reuse | PASS | C12–C16 | C12 카드 [7] "가져온 OK: 3-1 영상 — 모션(…)"; C13 색 참조 권한 문장; C14 표정 줄 글자 그대로 + 입 잠금 상향; C16 `get_project_asset_prompt` 빈 결과 → 참조로만 제안 |
| 55 이미지 편집 문법·전 → 후 | PASS | C04 t2, C20 t2 | C04 CHANGE/REMOVE COMPLETELY/PRESERVE EXACTLY/ONLY CHANGE + "겉옷: … → 남색 울 더플코트"; C20 "LIGHT LOCK 전 → 후" |
| 56 인물 시트 새로 | PASS | C03 t1–t2 | HEADLESS `not an injury`, 성숙한 골격, 2k, 직업 소품 금지 문장, 검사기 OK |
| 57 인물 시트 고치기 | PASS | C04 t1–t2 | job-ch001 기준 편집, 목선 문장 "At the neckline, only the navy duffle coat's collar opening is visible" + 헤드리스 패널 "no trace… including in the headless LEFT panel" |
| 58 장소 마스터(좌우 뒤집기 규칙) | PASS | C05 t2 | location.md "Writing directions"대로 새 `In this view…` 줄 (마스터 신규 생성은 이 묶음에서 미검증) |
| 59 장소 새 시점 | PASS | C05 t1–t2 | DERIVED VIEW `Do not inherit its camera angle…`, `not a horizontal mirror`, 부모 job-lc001v1 |
| 60 장소 고치기 | PASS | C20 t1–t2 | STATE 공식 "the tube is off and becomes lit", "lit but does NOT glow… no light spilling onto" |
| 61 소품 | PASS | C06 t1–t2 | "13×18cm, 할아버지 손바닥 한 뼘", 회색 무배경·`Avoid:` 줄, 시트 필요 여부부터 질문 |
| 63 퍼스트 프레임 | PASS | C08 t2, C13 t2 | C08 틀 1 `WITHOUT reframing`·`Exactly one person is visible.`; C13 틀 2 + 색 참조 권한 문장 |
| 64 영상 점검표(렌즈·대사) | PASS | C02 t1, C10 t1–t3 | C02 렌즈 묻지 않고 시작 이미지 32° 우선; C10 렌즈 47° + 관찰 결과 3개(mm 없음), 대사 없음 → 효과음만 |
| 65 모호한 말 표 (참고, 지도엔 없음) | PASS | C11 t4–t6 | 속도 절반 "전 → 후", 움직임 추가 한도 초과 알림, 별 → 오버레이 |
| 67 15블록·연기 스킬 여는 때 | PASS | C10 t1–t3 | t1·t2 acting 안 엶, t3 meta skills=[acting] |
| 68 배경 4문단 | PASS | C11 t1–t3 | background.md를 질문 전에 열고 4문단, 15블록 아님 |
| 71 연기: 목표·감정 범위 양 끝 | PASS | C14 t2 | "stillness and quiet resignation; a sigh or a frown = failed take, a smile = failed take" |
| 72 연기: 몸·손·시선을 구체 행동으로 | PASS | C14 t2 | "His eyes stay on the empty road… slow, heavy blinks"; "the screen-left hand… when it stops it does not startle, it simply stops" |
| 73 반복 인물 프로필·고정 목소리 | 해당 없음 | — | C14는 대사 없는 컷, 프로필 작성 턴 아님 |
| 74 연기 범위 넘는 요청 먼저 짚기 | PASS | C14 t1–t2 | 요청 자체가 절제 범위 안(표정 유지); 범위 이탈 없음 — 선제 경고가 필요한 입력은 아님 |
| 75 질문 턴엔 acting 안 열고 쓰는 턴에 연다 | 부분 | C14 t1–t2 (PASS), C12 t1 | C14는 t1 미개봉·t2 개봉. 그러나 C12 t1이 질문 턴에 `acting/SKILL.md`를 읽음(live-action.md:3 "Do not open `acting` in a question turn" 위반; 연기 줄은 3-1에서 글자 그대로 가져와 새 연기 문장이 없었음) |
| 76 보내기 전 점검 | PASS | C19 t1 | 생성 지시 없음 + 폴더 미결정 → "생성은 보내기 전에 다시 여쭙겠습니다" |
| 77 저장 위치(폴더 구조) | PASS | C19 t1 | "`3-6 [대기]` 아래에 `승인`과 `거절`을 둡니다" |
| 78 보낸 뒤 형식·기록 | 해당 없음 | — | 이 묶음에서 생성이 발생하지 않음 |
| 79 판정(됐어→✔/✘) | 해당 없음 | — | 이 묶음에 판정 턴 없음 |
| 80 크레딧 질문 | 해당 없음 | — | 이 묶음에 크레딧 질문 없음 |
