# real14-C12 "3-1의 모션처럼 3-2 영상" (2턴) — PASS 1 / 부분 1 / FAIL 0 (real13: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 첫 줄 "[16]번 다른 OK처럼으로 진행합니다." `production-session`→`ok-reuse.md`, 3-1 영상 카드만 열음. `[TOOL] list_project_assets(fld-3-2)`. 렌즈: "카드 35°, 시작 이미지 75mm=32°, 시작 이미지 우선", 같은 쪽이라 좌우 안 뒤집음. 질문 3개(사건 수 / 연기 / 끝 상태)와 "기본값으로 씀" 한 줄. 카드는 안 씀(질문 턴). 감점: 가져온 모션이 4~5사건인데 "쪼개지 않고 3-1 그대로"를 제안. `kit/skills/production-session/ok-reuse.md:41`("the proposal is to split the shot, not to keep it whole")과 `must-ask.md:30`을 읽고도 반대로 제안했다. 플래그·이유 설명은 했다 |
| 2 | PASS | `ACTION_TIMING`·`PHYSICS` 3-1 문장 글자 그대로(검사기 통과). 본문에 "3-1"·"previous shot" 없음(grep). 카메라 32°·위치는 3-2 기준, 입 잠금은 `no parted lips, no mouthing`으로 강화하고 "전 → 후"로 보고. 카드 [4]~[7] 기록, [7] "가져온 OK: 3-1 영상 — 모션(…)"(diff). `acting`·`cut-card.md` 엶. 생성 안 함. "약 40 크레딧(시뮬레이션 견적)"은 sim 결과표에 근거 |

검사기: `python3 kit/skills/higgsfield-generation/check_prompt.py --kind video C12t2_1.txt --refs 4 --seconds 8 --must-include grandpa+girl+bag+light+motion_3-1` → `OK — video 프롬프트 5279자, 걸린 항목 없음`

real13 감점 해소: ① 첫 줄 누락 — 해소. ② 4사건 유지 제안 — 미해소(키트에 ok-reuse.md:41 줄이 새로 생겼지만 플레이어가 따르지 않음).

기대 오류/키트 충돌: `scenarios.md` C12는 4사건 모션을 글자 그대로 옮기는 것을 기대하고, 카드 [1] 완료 조건도 "3-1과 같은 동작·타이밍"이라 키트(분할이 제안)와 서로 부딪친다. 둘 중 하나를 고쳐야 한다.

추가 발견
- 첫 줄에 대괄호를 그대로 씀("[16]번"); 다른 체인은 "2번"처럼 괄호 없이 씀. 표기가 체인마다 다르다.
- 카드 3-2 [6]에 "연기: 3-1과 같은 목표·범위", 사건 4~5개 유지를 `(제안값)`으로 적음.

키트 결함: `kit/skills/production-session/ok-reuse.md:41` — 줄이 번호 목록 위 맨 앞에 떠 있어 §3 단계로 읽히지 않는다 → 번호 단계 0으로 옮기고 굵게, "4+ events: ask 'split into two shots?' with proposal = split"로 쓴다. `scenarios.md` C12 기대도 같이 고친다.

총평: 형식은 고쳐졌고 내용은 정확하나, 키트의 분할 규칙을 넘긴 제안 때문에 1턴 부분.
