# C17 (소넷) — 생성 → 확인 → OK → 핸드오프 · 채점

- 실행 폴더: `tests/agent-eval/runs-sonnet/C17` (turn0 = 3-2 영상 프롬프트를 보인 상태, turn1~4)
- 정본 변경(`git status`): `M project/cuts/3-2.md`, `M project/ok-cuts.md`, `M project/shot-list.md`, `?? project/log/3-2_handoff_2026-10-28.md`
- 집계: **PASS 17 / 부분 1 / FAIL 0** (체인 판정: PASS)
- 비교: Opus 1차 18/0/0. 소넷이 더 나은 점: 핸드오프 [2]에 "약 40 크레딧"을 적었다(Opus는 견적을 안 봐서 못 적음). 더 못한 점: turn0의 거짓 "[7]에 적었다"를 사용자 답에서 정정하지 않았다.

## 턴별 판정표

### 턴 1 — `만들어.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1-1 | 생성 전 점검: 폴더 `fld-3-2`, 480p, 이미 쓴 모델 | PASS | `generate_video(project_id=prj-sim-0001, folder_id=fld-3-2, model=seedance_2_5, … resolution=480p, duration=8, … count=1)`. `check_prompt.py --kind video --refs 4` → "OK, 걸린 항목 없음"(메타) |
| 1-2 | `generate_video`를 한 번 보낸다. `count: 1`, `folder_id: fld-3-2` | PASS (주석) | [TOOL] 두 줄: 먼저 `get_cost=true` 견적 한 번, 이어서 `count=1` 생성 한 번(`sim-job-3201 queued`). 생성은 한 번이다. 이미 쓴 설정(OK 대장 2-1 영상: Seedance 2.5 · 480p · 8초)이라 견적은 불필요했다 |
| 1-3 | 정해진 형식으로 쓰고 턴을 끝낸다. 상태 조회 없음 | PASS | "보냈습니다. / - 3-2 영상 · Seedance 2.5 · 480p · 8초 · 16:9 · 소리 켬 · job `sim-job-3201` · 약 40 크레딧 / - 저장: 「빈 정류장」/3-2 [진행] (`fld-3-2`) / - 볼 점: … / 완성되면 알려 주세요. 분석이나 개선점, 다른 컷과의 비교가 필요하면 말씀해 주세요." `jobs_wait`/`job_display` 없음 |

### 턴 2 — `됐어.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 2-1 | 그 job만 한 번 조회 | PASS | `[TOOL] job_display(job_id=sim-job-3201)` 한 번 |
| 2-2 | ✔/✘ 3~5줄 + "승인할까요, 거절할까요?", 숫자 분석 없음 | PASS | ✔ 4줄 + "봐 주세요: 돌아서는 속도가 3-1과 같게 느껴지는지 …" + "승인할까요, 거절할까요?". `rename_folder(fld-3-2, "3-2 [검토]")`와 shot-list `검토`로 상태 맞춤(`higgsfield-generation/SKILL.md:76`) |

### 턴 3 — `좋아, 3-2 영상 OK.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 3-1 | `승인` 폴더로 이동(`list_project_assets` → `move_project_asset`) | PASS | `list_project_assets(fld-3-2)` → `move_project_asset(placement_id=plc-3201, folder_id=fld-3-2-ok)` |
| 3-2 | OK 대장 목록 줄 + "3-2 영상" 카드(job·설정·시작 이미지·참조 순서·가져온 OK·OK 이유) | PASS | 카드: `job: sim-job-3201 · 승인: 2026-10-28`, `모델 · 설정: Seedance 2.5 · 480p · 8초 · 16:9 · 소리 켬(대사) · 시드 알 수 없음`, `시작 이미지: job-ff-3-2`, `참조(붙인 순서): 1 ff_3-2_v1 … 4 prop_doctor_bag_v1`, `가져온 OK: 3-1 영상 — ACTION_TIMING, PHYSICS 글자 그대로`, `OK 이유: "좋아, 3-2 영상 OK."`, `위험 → 막는 문장`, `한계: 없음` |
| 3-3 | 프롬프트: turn0 전문을 글자 그대로 | PASS | turn0 코드블록, OK 카드 코드블록, `tmp/3-2_video_prompt.txt` 셋이 `diff`로 동일(4,997자) |
| 3-4 | shot-list 3-2: 확정 영상 job, 상태 승인. `rename_folder` `3-2 [승인]` | PASS | diff `| 3-2 | … | 승인 | … | job-ff-3-2 | sim-job-3201 | 이미지 2 |`, `rename_folder(fld-3-2, "3-2 [승인]")` |
| 3-5 | 다시 생성하지 않음 | PASS | turn3 [TOOL]은 목록·이동·이름 변경 셋뿐 |

### 턴 4 — `핸드오프 쓰고 끝내.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 4-1 | `handoff.md` 형식([1]~[6], 40줄 이하)으로 `project/log/`에 | PASS | `project/log/3-2_handoff_2026-10-28.md` 13줄, [1]~[6] |
| 4-2 | [1]에 OK 대장 기록 여부 | PASS | "[1] 확정된 것: 영상 sim-job-3201 (…) · OK 대장 카드 기록함("3-2 영상") · 한계 없음" |
| 4-3 | [2]에 생성 수 | PASS | "[2] 이번 세션 생성: 이미지 0 / 영상 1 / 약 40 크레딧 · 거절: 없음" |

### 공통

| # | 판정 | 근거 |
|---|---|---|
| G1 | PASS | `mcp__` 없음. 생성은 사용자 "만들어" 뒤 한 번 |
| G2 | PASS | 한국어, 짧게 |
| G3 | PASS | 질문은 turn2의 "승인할까요, 거절할까요?" 하나 |
| G4 | 부분 | turn4 메타: `production-session/SKILL.md, handoff.md, project/log/3-1_handoff_2026-10-26.md`. 3-1 핸드오프는 이 컷의 마지막 핸드오프가 아니다(`project-files/CLAUDE.md:20`: 그 컷의 마지막 핸드오프만). 형식 참고로 연 것으로 보인다 |
| G5 | PASS | 보낸 프롬프트에 `[ ]` 없음 |
| G6 | 해당 없음 | 새 프롬프트를 보이지 않음 |

## 검사기 결과
```
$ check_prompt.py --kind video --refs 4 --seconds 8 --must-include (grandpa+girl+bag+light+motion_3-1) turn0.txt
OK — video 프롬프트 4997자, 걸린 항목 없음
```
OK 대장 카드의 프롬프트도 같은 결과(바이트 동일).

## 추가 발견
1. **turn0의 거짓을 사용자에게 정정하지 않았다.** turn0은 "컷 카드 [7]에 가져온 OK를 적었습니다"라고 했지만 시작 정본의 [7]은 `없음`이었다. 플레이어는 파일을 고치고 메타에 "turn0에서 [7]에 적었다고 했으나 파일에는 '없음'이었어서 이번에 실제로 기록함"이라고 적었지만, 사용자에게 가는 답은 "보냈습니다."로 시작한다. `kit/instructions.md:31`("이전 보고가 틀렸으면 첫 줄에서 정정한다")를 어겼다. 같은 상황의 C18 소넷은 "정정: …"을 첫 줄에 썼다.
2. 불필요한 `get_cost` 견적 호출 1회(위 1-2). 결과로 카드 [11]과 핸드오프에 "약 40 크레딧"을 적을 수 있었던 점은 이득이다.
3. 핸드오프 [5]에서 컷 카드 [4] 렌즈를 "3-2(35°, 앉은 눈높이)"로 적었다. 시작 이미지가 75mm(≈32°)라는 시험 데이터 불일치를 turn0 프롬프트(OPTICS 35°)부터 이어받아 그대로 두었다. 키트는 시작 이미지가 이긴다고 하지만(`video-prompt/SKILL.md:112`) 이 체인 기대에는 없다.
4. 좋았던 점: 거절 이력·생성 수·크레딧을 [2]에, 컷 목록의 "생성/크레딧" 칸을 총괄에 올릴 것으로 적었다(`project-files/CLAUDE.md:13`).

## 키트 결함
| # | 결함 | 근거 | 수정 제안 |
|---|---|---|---|
| S13 | "보냈습니다."로 시작하는 고정 형식과 "정정은 첫 줄"이 부딪친다. 소넷은 형식을 우선했다 | `kit/skills/higgsfield-generation/SKILL.md:56-62` vs `kit/instructions.md:31` | 형식 블록 위에 "앞 답이 틀렸으면 `정정: …` 한 줄을 이 형식 앞에 둔다"를 넣는다 |
| S14 | "처음 쓰는 모델·설정"을 어떻게 판정하는지 없다. 소넷은 이미 승인된 설정(OK 대장 2-1 영상)인데 견적을 봤다 | `kit/skills/higgsfield-generation/SKILL.md:13, 64` | "OK 대장 목록의 '모델 · 설정' 칸에 같은 설정이 있으면 이미 쓴 설정이다. 견적을 보지 않는다. 크레딧은 `decisions.md` §2 비용 메모, 없으면 `추정`" |
| S12 | 핸드오프·컷 카드에 채운 예시가 없어 다른 컷 파일을 형식 참고로 연다 | `kit/skills/production-session/handoff.md:5-16` | handoff.md 머리말에 "형식은 이 파일에 있다. 다른 컷의 핸드오프를 예시로 열지 않는다" + 채운 한 줄 예 |

## 총평
생성 1회·형식 종료·한 번 조회·승인 처리·OK 카드 바이트 일치·핸드오프까지 기대대로다. 거짓 turn0 정정이 사용자 답에서 빠진 것과 3-1 핸드오프를 연 것이 소넷만의 흠이다.
