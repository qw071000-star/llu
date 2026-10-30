# real17 기능 재점검 B — 46 51 54 55 61 62 66 75 76 81 82

> 기준: real16-feature-check.md의 '부분' 원인이 real17(runs-real17)에서 없어졌는가. 출력 `out/turn*.md`·메타·`git diff`로 확인. C12·C14는 재실행 안 해 건너뜀. 생성·정본 수정 없음(이 파일만 씀).
> 한계: 출력 파일에는 [TOOL] 줄이 턴마다 들어 있거나 빠져 있다. 호출 줄이 없는 것은 "호출했다는 증거 없음"으로 본다.

| 기능 # | real16 | real17 | 근거 |
|---|---|---|---|
| 46 컷 카드 12칸 | 부분 | PASS | 원인(카드 [7] 가져온 OK 미기록) 해소. C67 t1 `production-session/ok-reuse.md` 열람 + t2 diff `-가져온 OK: 없음` → `+가져온 OK: 3-1 영상 — 모션(ACTION_TIMING, PHYSICS), 연기(CHARACTER_ACTING), 대사(AUDIO)`. 질문 턴엔 카드 안 만듦: C63 t1·C67 t1 쓰기 0건, t2에서 [1][3]~[6] `(제안값)`로 채움. 새 문제: C45 t2 카드 `3-6.md`가 [1][5][9] 3칸뿐이고 [5]를 `소품`으로 씀(틀의 [5]는 인물). C63은 3-1의 "눈→머리→어깨 1.5초"를 가져오면서 [7]을 `가져온 OK: 없음`으로 둠(카드에 "같은 동작" 문구가 없어 규칙 밖) |
| 51 컷마다 카메라·화각·뷰·job·사건·길이 | 부분 | PASS | 원인(길이 미기재) 해소. C55 t1 표 길이 열 전부 `8초`, C56 t1 `3-7 … 8초`. 확정 job도 채움(`job-ff-3-1`/`job-v-3-1`…). 사소한 어긋남: C55 3-2 사건 칸이 숫자 아닌 `3-1과 같은 동작`, 3-2·3-3 화각을 `75mm (OK 카드, 약 32° 추정)`으로 써 규칙의 `NN° (OK 카드)` 형식과 다름 |
| 54 확정 전 정본 불변, 옮길 줄 | 부분 | 부분 | 원인 절반 해소. C55 t1은 3-1~3-3 기존 줄 + 새 3-4 + 밀린 3-5~3-7까지 장면 전체 줄을 보임, git 변화 0, 유지/교체 질문 3개. 그러나 C56 t1은 새 줄 `3-7` 하나만 보이고 "3-4~3-6은 번호 그대로 시간만 8초씩 뒤로"를 말로 때움 → 장면 전체 줄 규칙(SKILL.md:22) 미이행. 또 C55는 기존 컷 상태를 `승인`·`진행` 그대로 복사했는데 같은 규칙은 상태 `대기`라고 함(규칙 안 모순) |
| 55 이미지 편집 공통(전→후, CHANGE 문법) | 부분 | 부분 (검증 불가, 키트 문제 아님) | 원인은 시나리오 기대. C70 t2는 키트(must-ask.md:14 승인 컷 → 새 테이크?)대로 질문 3개만 하고 프롬프트 없음("2. 승인 컷 처리: 제안 — 새 테이크로 만들고 `job-ff-3-2`는 승인 상태로 둠"). 그러나 `scenarios.md` C70은 아직 한 턴에 LOCKED EDIT·검사기까지 기대 → 정리 안 됨. 편집 문법 자체는 C34 t2에서 확인: `Edit <<<prop_doctor_bag_v1>>> WITHOUT reframing`, `CHANGE`, `PRESERVE EXACTLY`, `ONLY CHANGE`, 블록 밖 `변경값(전 → 후)`, 검사 1312자 통과. 새 문제: C70 t2에 `[TOOL] get_project_asset_prompt(job-ff-3-2)`를 "실제 손 상태 확인"이라며 불렀으나 프롬프트 글만 오고 이미지는 못 봄(답에서 "추정"이라 밝힘) |
| 61 소품 | 부분 | PASS | 원인 2개 모두 해소. 크기를 사람 기준으로: C45 t1 `길이 약 9m, 높이 약 3m … 선 어른 키의 약 두 배 높이`, t2 카드 문장에도 `about twice the height of a standing adult`. 편집 배경 문장: C34 t2 `The existing background` / PRESERVE `The existing background` (이전엔 "plain seamless grey studio background"). 첫 줄 조사도 `9번 소품 만들기·고치기로`(고쳐짐). 시트 불필요 판단·카드 줄 인용도 유지 |
| 62 그림체 | 부분 | PASS | 원인(수채화 시작 이미지 안내 막연) 해소. C46 t1 `2. 시작 이미지: 제안 — 수채화 시작 이미지를 새로 만든 뒤 영상 (이유: 지금 job-ff-1-1은 실사라 영상만으로는 매체가 바뀌지 않습니다 … 새 이미지는 10번 그림체 → 11번 퍼스트 프레임 순서입니다.)` 번호가 tasks.md 표(10 그림체, 11 퍼스트)와 맞음. `1. 수채화 적용 범위: 제안 — 이 컷만`도 기대대로. 이 체인은 안내만 확인(style.md의 해 방향 문장은 안 나옴) |
| 66 사건 세기 | 부분 | 부분 | C41 t1 PASS: `옷장 열기, 돌아서기, 방문 열기, 나가기로 4개라 한 번에 3개를 넘음` → `2. 이벤트 분할: 제안 — 2샷으로 나눔`, 샷 A/B 목록. C47은 원인 일부 남음: t2 `사건은 "돌아섬 → 한 걸음 → 손 잡음" 3개`라 했지만 t3 프롬프트에 `the screen-right hand … drops from the times`(손 내림), `GRANDPA lowers his eyes to the bag`, `his fingers tighten very slightly once`가 있어 SKILL.md:83 규칙으로 세면 3개 초과. 샷 나누기 제안 없음. (C29는 맡은 범위 밖) |
| 75 질문 턴엔 연기 스킬 안 열기 | 부분 | PASS | 원인 해소. 질문 턴: C63 t1 reads에 acting 없음, C67 t1 reads에 `ok-reuse.md`만(승인 연기 줄을 가져오는데도 acting 안 엶), C47 t2 reads에 acting 없음. 프롬프트 쓰는 턴: C63 t2·C67 t2·C47 t3 reads에 `acting/SKILL.md` |
| 76 보내기 전 점검 | 부분 | 부분 | 원인 그대로. 지시·폴더·480p draft·검사 통과는 충족(C63 t3 `저장 … fld-3-3`, `480p·8초(draft)`). 그러나 견적을 부른 흔적 없이 "근거"를 인용: C63 t3 `약 40 크레딧 (근거: get_cost 견적)`, C67 t3 같은 문구, C68 t3 `(근거: get_cost 견적)`, C68 t6 `근거: 앞서 받은 get_cost 견적` — 세 체인 어디에도 `[TOOL] get_cost` 줄이 없고 `decisions.md`에 비용 메모도 없음. 카드 [11]에도 `(get_cost 견적)`이 그대로 기록됨(C67·C68). 새 문제: job 번호가 틀림 — C63 t3 `job job-3201`, C67 t3 `job 3201(sim-job-3201)`(표는 `sim-job-3201`; 카드엔 맞게 적음) |
| 81 숫자 분석 | 부분 | PASS | 원인(측정 명령 몰라 막힘) 해소. C72 meta bash `python3 .claude/skills/color-continuity/color.py measure media/3-1.mp4`, 답 `밝기 Y 125.2 / 255 … 대비 71.2`, 표 아래 `✔ 측정됨 / ✘ 비교 못 함 / 추정 / 한계`로 잰 것과 추정을 나눔. 새 문제: `media/3-1.mp4`가 1초짜리 컬러바 시험 파일인데(C73이 같은 파일에서 밝힘) C72는 말 안 하고 "해질녘 저조도(카드 [8])에 비해 중간 밝기"라고 해석 |
| 82 특정 초 프레임 | 부분 | PASS | 원인(해상도·길이 없음) 해소. C73 t2 `media/frames/3-1_0.5s.png (320x180)` + `영상 길이가 1.00초입니다`. 명령도 글자 그대로 `assemble.py frame media/3-1.mp4 0.5 media/frames/3-1_0.5s.png`, seam은 `assemble.py seam media/2-1.mp4 media/3-1.mp4 media/frames/seam_2-1_3-1.png` 단독 호출. 새 문제(경미): 컷 목록 `영상 4`(생성 횟수)를 "영상 비용이 4"로 잘못 읽고 길이와 어긋난다고 추정 |

## 합계

PASS 7 (46 51 61 62 75 81 82) · 부분 4 (54 55 66 76) · FAIL 0. 55는 키트 문제가 아니라 시나리오 기대 문제.

## 열린 키트 결함 (키트 파일:줄 → 한 줄 수정)

1. `kit/skills/higgsfield-generation/SKILL.md:61`(+ 형식 템플릿 `:54`) — 견적 근거를 호출 없이 인용(76). 수정: 템플릿 크레딧 줄에 `(근거: 비용 메모 / 이번 대화 [TOOL] get_cost / 앞선 [job] 기록)` 칸을 넣고, "`get_cost 견적`은 이번 대화에 `[TOOL] get_cost` 줄이 있을 때만 쓴다. 없고 비용 메모도 없으면 처음 쓰는 설정이므로 §1-4대로 먼저 견적을 받는다"를 명시.
2. `kit/skills/higgsfield-generation/SKILL.md:54` — 템플릿 `job `[뒤 8자리]``가 `job-3201`·`3201` 같은 잘린 표기를 부른다. 수정: `job `[전체 job ID]``로.
3. `kit/skills/shot-design/SKILL.md:22`(§2-5) — "모든 컷 줄"을 컷 하나만 추가할 때(C56)도 적용하는지 불명, 그리고 "기존 칸 복사"와 "상태 `대기`"가 충돌(C55는 `승인`·`진행` 복사). 수정: "컷 하나만 넣어도 장면 전체 줄(밀리는 번호·시간 포함)을 보인다. 상태는 기존 컷은 기존 값, 새 컷만 `대기`"로 한 줄.
4. `kit/skills/image-prompt/prop.md:18` — 시트 없이 문장으로 쓸 때 어느 카드 칸에 적는지 없음. C45가 틀의 [5](인물)를 소품 칸으로 쓰고 3칸짜리 카드를 만듦(46). 수정: "카드 [5]의 `소품:` 줄에 적고, 새 카드는 `cut-card.md` 12칸 틀로 만든다".
5. `kit/skills/video-prompt/SKILL.md:83`(Event count) — 문구는 고쳐졌으나 C47에서 제안 단계의 개수(3)가 프롬프트의 손 내림·시선 내림·손가락 움직임을 안 세고 지나감. 수정: "개수는 최종 프롬프트의 ACTION_TIMING·CHARACTER_ACTING에 있는 모든 인물의 동사를 나열해 센다. 예: 읽다 멈춤·손 내림·돌아섬·한 걸음·손 잡음 = 5 → 샷 나누기 제안".
6. `kit/skills/shot-design/SKILL.md:48`(템플릿 `새 뷰 필요` 행) — C56이 새 뷰를 이미지로 먼저 만들라고만 하고 `image-prompt → location-view.md` 틀 A를 안 가리킴(규칙은 :25에 있으나 표 행에는 없음). 수정: 템플릿 행 주석에 "새 뷰 필요 → image-prompt/location-view.md 틀 A" 추가.
7. (키트 밖) `tests/agent-eval/scenarios.md` C70 — 승인 이미지 편집은 질문 턴 + "그대로" 뒤 프롬프트의 2턴으로 기대를 고치거나 `그대로` 턴을 추가해야 55를 확인할 수 있음.
