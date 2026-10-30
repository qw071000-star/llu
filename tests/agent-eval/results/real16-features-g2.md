# real16 기능 판정 — G2 (C21 C22 C23 C24 C25 C27 C28 C29 C30 C31 C32 C33 C34 C35 C36 C37 C38 C39 C40)

> 기준: `guides/주요-기능.md` 번호, `tests/agent-eval/feature-map.md`에서 위 체인이 걸린 번호 + 전체 적용(1, 2, 27, 35).
> 판정 규칙: 걸린 체인 모두 충족 = PASS, 한 체인이라도 실제 결함 = 부분, 핵심이 무너짐 = FAIL. 체인별 근거는 `real16-<체인>.md`.
> 정적 번호(28, 33, 34, 36–42, 47–54, 58, 62, 64, 68, 76–90)는 이 묶음 체인이 걸리지 않아 제외했다.

| 기능 # | 판정 | 체인·턴 | 근거 |
|---|---|---|---|
| 1 답 한국어·프롬프트 영어 | 부분 | 전 체인; 결함 C31 t2 | 프롬프트 본문 영어, 정본 카드(C39 `project/cuts/3-4.md`) 한국어. C31 t2에 영어 서술 한 줄: `Check passed. Now I'll record the answers on the registry's draft line and delete the tmp files.` |
| 2 첫 줄 "N번 작업명으로 진행합니다." | 부분 | 19체인 t1; 결함 C36 t1, C34 | 번호·형식 대부분 맞음(예 C37 `17번 고해상도로 진행합니다.`). C36 t1 첫 줄 `2번 …`, 세 줄 뒤 `13번 …(2번에서 바뀜)`으로 정정. C34 `9번 소품 만들기·고치기으로`(조사 오류). C38은 라벨을 줄여 `2번 오늘 할 일·세션 시작으로` |
| 3 두 작업일 때만 확인 / 번호면 바로 | 부분 | C27 t1, C36 t1 | C27은 tasks.md 5번 says(`50대 때 모습도`)에 따라 `5번 인물 시트 고치기로` 바로 진행(기능 지도는 '확인 필요'로 적음 → 지도와 tasks.md 불일치). C36은 확인도 안 하고 2번으로 시작했다 13번으로 정정 |
| 4 여러 작업: 순서 제안·첫 것만·미룬 이유 | PASS | C40 t1 | `한 번에 하나만 바꿀 수 있어서 첫 번째 것만 진행 … 1. 진행 순서: 제안 — 머리 풀기 → 장화 파란색 → 하늘 붉게 (이유: … 하늘은 마지막이 안전)`; t2에 머리만 진행 |
| 5 시작 문구 없이 이어 감 | PASS | C38 t1 | `오늘 뭐 하면 돼?` → 정본 3개를 순서대로 읽고 후보 제시, 시작 문구 요구 없음 |
| 6 "이미지로/영상으로/보내"에만 생성 | PASS | C22 t2 (+ 전 체인 t2) | `"그대로"는 제안을 받아들이는 말이라 생성 지시로 보지 않습니다 … 아직 아무것도 보내지 않았습니다`. C40 t2 `"해"는 보내라는 말이 아니라서 프롬프트까지만`. 19체인 모두 generate 호출 0 |
| 8 확인 1k·480p, 고해상도는 확정 뒤 | PASS | C37 t1 | 사용자 요청 1080p라도 draft 경로+견적(`알 수 없음`)+`지금 보낼까요?` 확인. 나머지 체인은 `1k`/`480p` 기본값(C21·C33·C36) |
| 10 모호한 말 → 구체적 값 | PASS | C27 t1, C30 t1, C35 t1 | `50대` → `about fifty-five`+나이 표지; `열두 살쯤` → `키 약간 큼 … 피부는 그대로`; `천천히` → `0:04–0:08(4초)` → `0:02–0:08(6초)` |
| 11 변환 표 대신 그때그때 묻기 | PASS | C35 t1 | 표 없이 `1. 어느 동작이 빠른가 … 3. 엄지 구간이 이미 4초라 더 늘릴 방법` 개별 질문 |
| 12 한 번에·제안값+이유·두 번 안 묻기 | 부분 | C24 t1 (PASS), C29 t2 (결함) | C24 `확인할 것이 6개 …` 한 묶음, 2턴에 되묻기 없음. C29 t2는 1턴에 수락된 `가방 닫힘`을 `가방 상태 … 열린 채로 가야 하면`으로 다시 물음 |
| 13 묻지 않는 것(모델·해상도·렌즈) | PASS | C24 t1 | `기본값으로 씀: Seedance 2.5 · 확인 480p · 16:9 · 8초 …`; 렌즈는 묻지 않고 `카드에는 35°, 시작 이미지는 75mm(약 32°) … 32°로 씁니다` |
| 14 먼저 짚는 것 | PASS | C21 t1, C28 t1, C36 t1, C40 t1 | C21 `요청은 2020년대라서 정본과 다릅니다`; C28 `"이걸로"가 가리키는 이미지가 이 대화에 없습니다`; C36 `2-1 OK의 이유는 "기대 안 하는 얼굴"이라 웃음과 다릅니다`; C40 `장화: CH-002는 빨간 장화입니다` |
| 16 화면 기준 방향, 손 = 화면 쪽+물건 | PASS | C32 t1·t2 | `She holds it by the handle in the screen-left hand, farther from the sign` ; `her right hand` 없음 |
| 17 인물 기준 → 화면 기준 | PASS | C32 t2 | `화면 기준으로 바꾸면 화면 왼쪽 손, 시간표에서 먼 손입니다(추정)`. 변환 근거(옆모습)는 얇음 → 키트 결함 참고 |
| 18 반대쪽 카메라 좌우·빛 뒤집기 | PASS | C33 t1·t2 | `전 from screen left, the persimmon-tree side → 후 from screen right …`; 프롬프트 `In this view the persimmon tree is at screen right and the timetable sign is at screen left.` |
| 19 사건 동사마다 세기·3개 넘으면 나눔 | PASS | C29 t1 | `일어나기, 가방 들기, 돌아서기, 걸어 나가기가 4개 … 2컷으로 나눔`; 나가기는 `마지막 프레임에 몸 절반이 화면 왼쪽 밖` |
| 20 한 생성에 한 가지 | PASS | C21 t2, C31 t1, C40 t1 | C21 `this step changes only its IDENTITY AND TEXT`; C31 `2단계로 나눕니다`; C40 머리만 |
| 21 컷 사이 이어짐 | PASS | C29 t1·t2 | `2-1 끝 상태와 같이 …`, 카드 [6] `다음 컷 첫 프레임과 맞출 것 — B 첫 프레임 = A 마지막 프레임` |
| 22 이미지 프롬프트 종류별 | 부분 | C21 C22 C23 C25 C27 C31 C33 (PASS), C34 t2 (결함) | 틀 2 시대·틀 1 시트·편집 틀 1·틀 B·나이 틀 2·STATE·first-frame 틀 2 모두 맞음. C34 소품 편집은 `the existing background` 대신 `The plain seamless light grey studio background`, 전 문장 오인용 |
| 23 실사 15블록 | PASS | C24 t2, C36 t2 | 15블록 이름·순서 그대로 `[SCENE_CONTEXT] … [REQUIRED_AND_FORBIDDEN_CONSTRAINTS]`, 검사 통과/WARN 사유 |
| 24 결과 고치기 / 1080p | PASS | C35 t2, C37 t1 | 해당 줄만 `전 → 후`+`finished in under 5 seconds = failed take`; 1080p는 `draft_job_id`로 같은 테이크 |
| 25 "3-1처럼" | PASS | C39 t1 | `3-1 카드는 열지 않았습니다 … 3-1의 내용을 가져오려던 거라면 … "다른 OK처럼"(16번)` — 형식과 OK 기준 구분 |
| 26 고정 문장 글자 그대로 | PASS | C24 t2, C32 t2 | must-include(grandpa·girl·bag·light) 검사기 OK; 목소리·입 잠금 문장도 그대로 |
| 27 검사 스크립트 먼저 | 부분 | 프롬프트 낸 15체인; 결함 C24 t2 | 14체인은 보이기 전 검사 후 같은 본문. C24는 `프롬프트는 점검 뒤에 목소리 파일 문장 하나를 지웠습니다 … 점검을 다시 돌리지 않았고`, WARN 사유 숫자도 6,344(실제 6305) |
| 35 열면 안 되는 파일 | PASS | 전 체인 메타 | 다른 컷 카드·핸드오프 열람 0(자기 컷 카드·핸드오프만: C24 3-2, C32 3-1, C30·C40 3-3). C39 `3-1 카드는 열지 않았습니다`. OK 대장 열람은 first-frame.md 예외(C29·C33)나 자기 카드 |
| 43 고치는 사람 정하기 | PASS | C38 t1 | 총괄 세션으로 읽기만 하고 `대장 문제 2건 … 제가 고칠까요?`로 묻기 |
| 44 총괄 세션 | PASS | C38 t1 | `3-1과 3-2의 생성/크레딧 칸은 이미 채워져 있어서 두 핸드오프는 열지 않았습니다`; 진행 4·대기 4·승인 3 정확 |
| 45 컷 세션 | 해당 없음 | C38 | C38은 총괄 세션만 확인(컷 세션 동작은 이 묶음 체인에서 직접 시험되지 않음) |
| 46 컷 카드(질문 턴엔 안 만듦) | PASS | C39 t1 + 질문 턴들 | 12칸 카드 `project/cuts/3-4.md`(카드 요청 턴). 질문 턴(C23 t1, C27 t1, C28, C35 t1, C36 t1)에는 카드 파일 없음. 단 C25 t1은 제안값을 대장에 씀 → 규칙 대립(키트 결함) |
| 55 이미지 편집 문법·전→후 | PASS | C21 t2 | `CHANGE — IDENTITY AND TEXT … REMOVE … PRESERVE EXACTLY … ONLY CHANGE`, `**전 → 후**` 줄 |
| 56 인물 시트 새로 | PASS | C22 t1 | 틀 1 전부, `fld-chars`, 2k, `No profession-signaling props …` |
| 57 인물 시트 고치기 | PASS | C23 t2, C27 t2, C30 t2 | C23 목둘레 세 곳+권한 세 줄; C27 `IDENTITY BONES`; C30 나이 표지·LOCKED EDIT |
| 59 장소 새 시점 | PASS | C25 t2, C33 t2 | C25 `Move in from the same side … no reverse angle`(거울 문장 없음); C33 `not a horizontal mirror`+새 LIGHT LOCK |
| 60 장소 고치기 | PASS | C21 t1·t2, C31 t1·t2 | C21 층 하나씩; C31 `시간대`와 `점등`을 나눔, `no glow, no halo, no light spilling`. C31 최종 상태 LIGHT LOCK(형광등 쪽)은 미리 안 물음(추가 발견) |
| 61 소품 | 부분 | C34 t1·t2 | t1 에셋 vs 결과 질문·v2/폐기 절차 PASS. t2 `the existing background` 규칙과 전 문장 인용 위반(prop.md:24) |
| 63 퍼스트 프레임 | PASS | C32 t2, C33 t2 | 틀 1(`Exactly 2 people are visible.`)·틀 2(`PRIORITY: the CAMERA block overrides every reference.`) |
| 65 모호한 말 표 | PASS | C35 t1 | §0 속도 줄 그대로: 4초 구간 → 앞당기기 제안 |
| 66 사건 세기 주인 | PASS | C29 t1 | `video-prompt` §2 `Event count`의 예(일어나서·돌아서·나가기 = 4)를 그대로 적용, 나가기는 끝 프레임 상태 |
| 67 15블록·연기 스킬 여는 때 | PASS | C24 t1·t2, C36 t1·t2 | 질문 턴에 acting 안 열고(C24 t1, C36 t1) 프롬프트 턴에 열음(meta skills `['acting']` / reads `acting/SKILL.md`). C29 t2는 프롬프트를 쓰지 않는데 열음(별도 결함, 이 번호에는 안 걸림) |
| 69 결과 고치기 표 | PASS | C35 t1·t2 | 속도 줄 값/문장 적용 |
| 70 고해상도 재렌더 | PASS | C37 t1 | rerender.md: `draft_job_id`, `[TOOL] get_cost`, `알 수 없음`, 기한 `2026-10-31` |
| 71 연기: 목표와 양 끝 | PASS | C24 t2, C36 t2 | `wants her grandfather to hear …`; `a trembling voice or tears = failed take, a flat voice … = failed take` |
| 72 연기: 몸·손·시선 | PASS | C24 t2, C36 t2 | `Weight low and even, tempo slow and economical, breath quiet`, `micro-saccades … live wet catchlights` |
| 73 연기: 프로필·고정 목소리 | PASS | C24 t2 | 목소리 `A ten-year-old girl's clear, slightly hoarse voice, quiet and careful.` 글자 그대로(`ACTING PROFILE` 문단은 쓰지 않았지만 acting §6은 장면용 재작성 허용) |
| 74 연기: 레지스터 넘는 요청 짚기 | PASS | C36 t1 | `decisions.md §5가 절제된 연기를 정했고 … 입을 다문 채 입꼬리만 살짝` |
| 75 연기: 질문 턴엔 안 염 | PASS | C24 t1, C36 t1 | t1 reads에 acting 없음, t2에서 열음 |

## 부분/FAIL 요약

- FAIL: 없음.
- 부분: 1(C31 영어 한 줄), 2(C36·C34 첫 줄), 3(기능 지도와 tasks.md 불일치+C36), 12(C29 가방 되묻기), 22·61(C34 소품 편집 규칙), 27(C24 검사 뒤 수정).
