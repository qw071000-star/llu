# real12 재채점 (real11에서 부분이던 24체인)

기준: `grader-rules.md` + `scenarios.md`. 키트는 영어(`kit/`), 답은 한국어, 프롬프트는 영어.
턴은 대본 턴 기준으로 센다. 확인 질문("이 작업을 할까요?")과 러너가 넣은 "응, 그 작업 맞아."는 한 대본 턴으로 묶어 최종 결과로 판정한다.
첫 줄 "[N]번 …으로 진행합니다."가 없으면 내용이 맞아도 부분으로 쳤다. 그런 경우는 "형식만"이라고 적었다.
G1: 실제 `mcp__` 도구 호출 없음, RUN 밖 읽기 없음(메타 24체인 전부 확인). C14 t2가 검사용 프롬프트를 임시 폴더로 `cp`한 것은 쓰기라서 G1이 아니다.

## 합계 (대본 턴 46개)

| | real11 (같은 24체인) | real12 |
|---|---|---|
| PASS | 20 | 36 |
| 부분 | 27 | 10 |
| FAIL | 0 | 0 |

real12 부분 10개의 내용:
- 형식만(첫 줄 누락): C04 t1, C10 t1, C22 t1, C58 t1, C60 t1 (5개)
- 불필요한 확인 질문: C27 t1, C51 t1 (2개)
- C41 t1 (질문 항목 안에서 제안이 서로 모순), C47 t2 (길이 WARN), C56 t1 (첫 줄 누락 + 리버스 제안이 A안) (3개)

real11의 핵심 감점 24건은 전부 고쳐졌거나 부분 개선이다(미해결 3건은 아래 목록). 질문 턴에 카드 파일을 만들던 문제(C11·C13·C14·C16·C33·C61)는 모두 사라졌다.

## 체인별 표

| 체인 | real11 문제 | real12 턴별 | 고쳐졌나(근거) | 새 문제 |
|---|---|---|---|---|
| C02 | 렌즈 관찰 결과·심도를 질문에 올림 | t1 PASS | 고침. "카메라는 카드 [4]대로 고정이고 렌즈 화각은 시작 이미지에 맞춥니다"로 질문 5개에서 렌즈 뺌. 첫 줄 "2번 오늘 할 일·세션 시작으로 진행합니다." | 없음 |
| C04 | t2 블록 밖 해상도 비어 있음 | t1 부분(형식만) / t2 PASS | 고침. t2 "GPT Image 2.5 · 2k · 16:9 · 1장". 검사기 `OK — image 프롬프트 2641자, 걸린 항목 없음` | t1 첫 줄이 "**판단:** 5번(옷만…)"이라 "[N]번 …으로 진행합니다."가 없음 |
| C10 | t3에서 `acting` 안 엶 | t1 부분(형식만) / t2 PASS / t3 PASS | 고침. t3 메타 `skills ['acting']`. 검사기 `OK — video 프롬프트 5039자, 걸린 항목 없음`(`--refs 2 --seconds 8 girl+light`). t2에서 망원↔시작 이미지 50mm 충돌을 한 번만 확인 | t1 첫 줄 누락("**판단:** 13번 실사·인물 영상.") |
| C11 | t2 질문 턴에 `cut-card.md` 열고 `1-1.md` 신설 | t1~t6 모두 PASS | 고침. t2 메타 reads/tools 비어 있음. 카드는 t3(프롬프트 턴)에서 생성(`?? project/cuts/1-1.md`). 검사기 `--refs 0 --seconds 10` → `OK — video 프롬프트 986자, 걸린 항목 없음` | 경미: 플레이어가 `--refs 1`로 돌려 태그 WARN이 나옴(배경 영상은 `--refs 0`) |
| C13 | t1 질문 턴에 카드 신설 | t1 PASS / t2 PASS | 고침. t1 "이번 턴에는 카드를 만들지 않고", git diff는 t2에서만 `?? project/cuts/3-5.md`. 색 문장 안 지어냄: "3-1 프롬프트에는 색·질감 문장이 없고… 색 참조로 붙입니다". 검사기 `--refs 4 bag+light` → `OK — image 프롬프트 2836자, 걸린 항목 없음` | 없음 |
| C14 | t1 질문 턴에 `acting` 열고 카드 신설 | t1 PASS / t2 PASS | 고침. t1 reads에 `acting` 없음("`acting`은 프롬프트를 쓰는 턴에"), 카드 없음. t2에서 엶. 검사기 `--refs 3 --seconds 8 grandpa+bag+light+acting_2-1` → `OK — video 프롬프트 5015자, 걸린 항목 없음` | 경미: t2 메타의 Bash `cp`가 RUN 밖 스크래치 폴더로 파일을 복사(규칙 5 정신 위반, 읽기 아님) |
| C16 | t1 질문 턴에 카드 신설 | t1 PASS | 고침. git diff 비어 있음. `[TOOL] get_project_asset_prompt(job-ff-1-2)` → "빈 문자열입니다… 1-2의 색감 문장은 추정해서 쓰지 않습니다" | 없음 |
| C22 | t1 프롬프트를 검사 없이 보임 | t1 부분(형식만) / t2 PASS | 고침. t1에서 검사 실행 후 제시. 검사기 `OK — image 프롬프트 4919자, 걸린 항목 없음`. t2 "그대로"를 생성 지시로 안 읽음 | t1 첫 줄 누락("**판단:** 4번 인물 시트 만들기") |
| C30 | t2 블록 밖 "전 → 후" 없음 | t1 PASS / t2 PASS | 고침. "전 → 후: 나이: 약 열 살 → 약 열두 살". 검사기 `--refs 1 girl+light` → `OK — image 프롬프트 1731자, 걸린 항목 없음` | 없음 |
| C31 | t2 블록 밖 "전 → 후" 없음 | t1 PASS / t2 PASS | 고침. "바꾼 값(전 → 후): 하늘… → …, key 빛… → …". 검사기 `OK — image 프롬프트 1598자, 걸린 항목 없음` | 없음 |
| C33 | t1 질문 턴에 `cut-card.md` 엶 | t1 PASS / t2 PASS | 고침. t1 reads에 cut-card 없음, t2에서만 엶. 틀 2, 감나무 화면 오른쪽, `LIGHT LOCK for this view: Low dusk sun from screen right…`. 검사기 `--refs 3 grandpa+bag` → `OK — image 프롬프트 2702자, 걸린 항목 없음` | 없음 |
| C37 | `[TOOL]` 줄 없이 sim 수치 인용, `get_cost`를 사용자에게 넘김 | t1 PASS | 고침. `[TOOL] get_cost(draft_job_id=job-v-2-1, 해상도=1080p…)` 직접 조회, 1080p 견적은 sim에 없어 "알 수 없음". `draft_job_id`·만료 10-31 안내 | 경미: 이미 조회해 놓고 "견적을 먼저 받을까요?"를 사용자에게 다시 물음. 답에 "시험 환경표"라는 하네스 용어가 샘 |
| C40 | t2 블록 밖 "전 → 후" 없음 | t1 PASS / t2 PASS | 고침. "전 → 후: 낮은 포니테일 → 어깨 아래로 곧게 풀린 머리". 검사기 `--refs 1 girl+light` → `OK — image 프롬프트 1927자, 걸린 항목 없음` | 없음 |
| C51 | 번역을 코드블록에 넣음 | 대본 t1 부분(불필요한 확인) | 코드블록은 고침(번역은 일반 텍스트, 컷 카드 안 엶). 그러나 t1이 "23번 … 이 작업을 할까요?"로 멈춤. "한국어로"는 23번 행의 says 단어라 바로 진행해야 함 | 불필요한 확인 질문. 번역 앞에 "생성은 영어 원문"이라는 말이 없음 |
| C59 | `background.md` 안 열고 기본값 오류, 3-2 안 짚음 | t1 PASS | 고침. 표로 3개 순서화: 1-1은 "시작 이미지만 있고 영상이 없습니다… '좀 느리게'는 구체값도 필요", 3-2는 "영상이 없어 색을 잴 수 없습니다". 3-4만 진행, 질문 3개. 생성 없음 | 없음(순서를 3-4 먼저로 바꿨으나 나머지 둘이 막힌 이유를 적어 허용) |
| C63 | t3에 `[TOOL] generate_video` 줄 없음 | t1 PASS / t2 PASS / t3 PASS | 고침. t3 `[TOOL] generate_video(get_cost=true…) → 약 40 크레딧`과 `[TOOL] generate_video(… folder_id="fld-3-3" … draft=true …) → sim-job-3201`. 카드 [11]·`shot-list.md` 3-3 칸 기록(diff). t2 메타 `acting` 엶, 검사기 `OK — video 프롬프트 5484자, 걸린 항목 없음` | 없음 |
| C27 | t1 불필요한 확인 / 해상도 1k | 대본 t1 부분(불필요한 확인) / t2 PASS | 해상도는 고침: t2 "GPT Image 2.5 · 2k", t3 "2k", 검사기 `OK — image 프롬프트 1768자, 걸린 항목 없음`(`--refs 1 grandpa`). 확인 질문은 못 고침: "'50대 때 모습도'는 5번에 해당합니다. 다만 '시트로'라고 하셔서 4번… 먼저 여쭙습니다"(`kit/context/tasks.md:21` 5번 행에 "50대 때 모습도"가 이미 있음) | 같은 문제가 남음(불필요한 확인) |
| C41 | t2에서 장소 질문을 두 번째 묶음으로 쪼갬 | t1 부분 / t2 PASS | 고침. t2가 "그대로" 뒤 바로 LC-002 방 이미지 프롬프트를 냄. 검사기 `OK — image 프롬프트 2016자, 걸린 항목 없음`(`--refs 0`). 사건 4개를 A/B로 나눔 유지 | t1 항목 4가 모순: "방문은 화면 오른쪽 벽… 방문이 오른쪽이면 방향이 맞지 않으니… 화면 왼쪽 벽으로 바꾸는 쪽을 제안합니다". t2 첫머리 "정정:"으로 고침. t1 끝에 "[TOOL] 호출 없음 (질문 턴이라…)" 같은 내부 메모가 샘 |
| C47 | 사건 수를 묶어 셈, 길이 WARN 이유가 틀림 | 대본 t1 PASS / t2 부분 | 사건 수는 고침: 대사를 빼고 "한 걸음, 손 내밀기, 잡기 3개"로 셈. WARN은 반만 고침: 검사기 `WARN 길이 6655자`, 이유 "인물 2명에 참조 4개라 줄이려면 고정 문장이나 감정 범위를 지워야 해서… 약 250자는 이미 줄였습니다". 승인본 3-1은 5,060자. `his screen-right hand, nearer the timetable sign`류가 반복돼 부풀었고, 줄이는 순서(location→style→environment)를 따르지 않음 | 길이 1,155자 초과 유지. t2에서 `cd project && grep…`를 먼저 써서 "cd 금지"(`kit/instructions.md` Check 줄) 어김(검사 자체는 정상 실행). t1은 확인 질문을 했지만 3-2에 영상이 없어 13/11이 겹치므로 허용 |
| C56 | 리버스를 축 샷으로 바꾸고 좌우 안 뒤집힘이라고 설명 | t1 부분 | 대부분 고침. "리버스: 마스터의 정반대… 화면 좌우가 뒤집힙니다. 손녀는 화면 왼쪽 시간표 앞에, 감나무는 화면 오른쪽", `새 뷰 필요`, "LIGHT LOCK도 새로 써야 합니다… `location-view.md`", LIGHT LOCK 문장은 안 씀 | ① 첫 줄이 "**판단**: 장면 3의 컷 추가로 봤습니다."로 "[N]번 …" 없음. ② 질문 2번의 제안이 A(어깨 너머, "마스터의 정확한 반대는 아님")이고 진짜 리버스 B는 대안으로 내려감. `kit/skills/shot-design/SKILL.md:27`은 "put the camera opposite the master view" |
| C58 | 1-2(팀원 컷, 로컬 파일 없음)를 빠뜨림 | t1 부분(형식만) / t2 PASS | 고침. t1 "확정 영상이 있는 컷은 1-2, 2-1, 3-1인데 media/에는 2-1과 3-1만 있습니다", t2 "1-2는 media/1-2.mp4가 없어서 제외했습니다". 스크립트 4번 모두 단독 호출, ΔU −8.7→+0.4, ΔV −4.2→−4.1 정직하게 보고 | t1 첫 줄이 "판단: 22번 색 맞추기입니다."로 정해진 문장이 아님 |
| C60 | 2-2를 대기로 뒀다는 한 줄 없음 | t1 부분(형식만) / t2 PASS | 고침(문구는 다름). t2 "2-2는 상태를 바꾸지 않고 `진행` 그대로 두며, 거기서 물은 6개는 답을 받지 못한 채 남아 있습니다." 2-2 값을 3-3에 옮기지 않고 카드 빈칸 [3][5][6] 기준으로 새로 5개 질문 | t1 첫 줄 누락("판단: 2-2는 `shot-list.md`에 `진행` 상태…"). `kit/context/tasks.md:8`은 `대기`라고 쓰라는데 2-2는 이미 `진행`이라 문구가 맞지 않음 |
| C61 | 질문 턴에 `cut-card.md` 엶 | t1 PASS | 고침. t1 reads에 cut-card 없음, diff 비어 있음. "자기 왼손"을 화면 오른쪽 손으로 바꾸고 "추정" 표시, 시작 이미지(화면 왼쪽 손이 쓰다듬는 중)와의 충돌을 (a)/(b)로 제시. `his left hand` 안 씀 | 경미: 제안 문구 "화면 오른쪽 손, 가방 쪽 손이 아니라 감나무 반대쪽 손"이 읽기 어려움 |
| C65 | 러프컷→색 순서를 거꾸로 제안 | t1 PASS | 고침. "22번 색 맞추기로 진행합니다… 제안 순서: 22번 색 맞추기, 그다음 21번 러프컷." 3장에서 확정 영상은 3-1뿐이라 맞출 컷·러프컷 불가를 짚음. 스크립트 실행 없음(`ls media`만) | 없음. 경미: 비프롬프트 질문 턴인데 "프롬프트를 쓰기 전에 확인할 것이 2개…" 고정 문장을 씀(`kit/instructions.md:22`) |

## 아직 안 고쳐졌거나 새로 생긴 문제와 키트 고침

| # | 문제 (체인) | 키트 위치 | 한 줄 고침 |
|---|---|---|---|
| 1 | 첫 줄 "[N]번 …으로 진행합니다."를 빼고 "판단:"으로 시작 (C04 t1, C10 t1, C22 t1, C56, C58 t1, C60 t1). 규칙이 `tasks.md` 하나에만 있고 시작 보고 규칙은 `instructions.md`에 따로 있어서 놓침 | `kit/instructions.md:41` (Starting a conversation 4번), `kit/context/tasks.md:8` | `instructions.md:41`에 "Line 1 of every answer that starts a task is `[N]번 [작업명]으로 진행합니다.` (`context/tasks.md` §1); the 판단/읽은 것/할 일 lines follow it." 추가 |
| 2 | 단어 하나가 한 행과 정확히 맞는데도 확인 질문을 함 (C27 "50대 때 모습도 … 시트로", C51 "한국어로") | `kit/context/tasks.md:8` (Go straight on), 행 5(`:21`)·행 23(`:39`) | `tasks.md:8`에 "A message that matches the says column of exactly one row goes straight on, even if another row overlaps loosely (e.g. '시트로', '프롬프트 보여줘'); ask only when no row's says word matches." 추가 |
| 3 | 영상 프롬프트가 5,500자를 1,155자 넘고 줄이는 순서를 안 지킴 (C47 t2) | `kit/skills/video-prompt/live-action.md:29-31` (How to trim) | "With 2 people and 4 refs, first shorten LOCATION_MAP and the overlap in ACTIVE_REFERENCES, and write a repeated hand qualifier in full only in ACTION_TIMING; compare with the approved cut of the same kind (3-1 = 5,060) and state the cut chars" 추가 |
| 4 | 한 질문 항목 안에서 제안과 이유가 서로 모순 (C41 t1 항목 4) | `kit/context/must-ask.md:30` (13번 행, 새 장소) | "For a new room, state the camera position first, then place the door/wardrobe from it; never write a proposal and its reversal in one item." 추가 |
| 5 | 리버스를 물으면서 정반대 뷰(B)를 대안으로 내리고 A를 제안값으로 둠 (C56) | `kit/skills/shot-design/SKILL.md:27` | "The proposed value for '리버스' is the true opposite view (선 넘음(의도: …)); an over-the-shoulder inside the line may only be listed as the alternative." 추가 |
| 6 | 말 바꿀 때 이전 컷에 `대기`를 쓰라는 문구가 상태 값과 안 맞음 (C60). 플레이어는 `진행`을 그대로 둔다고 말해 내용은 맞음 | `kit/context/tasks.md:8` | "say the earlier cut is parked (status unchanged, its questions unanswered)"로 바꿈 |
| 7 | 이미 `[TOOL] get_cost`로 조회하고 sim에 값이 없는데 "견적을 먼저 받을까요?"를 다시 물음 (C37) | `kit/skills/video-prompt/rerender.md:5` | "If the quote is not in the sim, write 알 수 없음 once and ask only 'send anyway?', not whether to quote." 추가 |
| 8 | 배경 영상을 `--refs 1`로 검사해 태그 WARN (C11 t3). 플레이어가 설명했으나 규칙이 모호 | `kit/instructions.md:49`, `kit/skills/video-prompt/background.md` | "Background video: the start image is not an element, use `--refs 0`." 추가 |
| 9 | `cd` 금지 위반 (C47 t2) | `kit/instructions.md:47` (Check) | 플레이어 실수로 보이며 이번에는 검사가 정상 실행됐다. 키트 쪽 고침은 급하지 않음 |
| 10 | 비프롬프트 질문 턴에 "프롬프트를 쓰기 전에 확인할 것이…" 고정 문장 사용 (C65) | `kit/instructions.md:22` | "For non-prompt tasks (color, rough cut) say '확인할 것이 [N]개 있습니다…'" 한 줄 추가(경미) |
