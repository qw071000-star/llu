# C17 (소넷, 정리된 키트) — 생성 → 확인 → OK → 핸드오프 · 채점

- 실행 폴더: `tests/agent-eval/runs-sonnet2/C17` (turn0 = 3-2 영상 프롬프트를 보인 상태, turn1~4)
- 정본 변경: `M project/cuts/3-2.md`, `M project/ok-cuts.md`, `M project/shot-list.md`, `?? project/log/3-2_handoff_2026-10-28.md`
- 집계: **PASS 19 / 부분 0 / FAIL 0** (체인 판정: PASS)
- 지난 소넷 대비: 17/1/0 → 19/0/0. 지난 흠 셋이 모두 고쳐졌다. (1) turn0의 거짓 "[7]에 적었다"를 사용자 답 맨 앞에서 정정함. (2) `get_cost` 없이 `generate_video` 한 번만 보냄(`SKILL.md:13`의 "OK 대장 목록에 같은 설정이 있으면 처음이 아니다"를 따름). (3) 3-1 핸드오프를 열지 않음(핸드오프 단계에서 연 것은 `production-session/SKILL.md`, `handoff.md`뿐. 3-2 자기 컷의 앞 핸드오프만 읽음).

## 턴별 판정표

### 턴 1 — `만들어.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1-1 | 생성 전 점검: 폴더 `fld-3-2`, 480p, 이미 쓴 모델 | PASS | 메타: "보내기 전에 check_prompt.py 통과(4,997자, 참조 4 …)". 호출에 `resolution=480p … folder_id=fld-3-2`. "약 40 크레딧(추정, 2-1·3-1과 같은 설정)" |
| 1-2 | `generate_video` 한 번, `count: 1`, `folder_id: fld-3-2`. 불필요한 견적 없음 | PASS | [TOOL] `generate_video(model=seedance_2_5, … count=1, folder_id=fld-3-2)` 한 줄뿐. `get_cost` 없음 |
| 1-3 | 정해진 형식으로 끝낸다. 조회 없음 | PASS | "보냈습니다. / - 3-2 · 영상 · Seedance 2.5 · 480p·8초·16:9·소리 켬 · job `sim-job-3201` · 약 40 크레딧 / - 저장 … / - 볼 점 … / 완성되면 알려 주세요. 분석이나 개선점 …". `jobs_wait`·`job_display` 없음 |
| 정정 | (가산) turn0의 거짓 "[7]에 적었다"를 정정 | PASS | 형식 위 첫 줄: "정정: 앞 답에서 컷 카드 [7]에 가져온 OK를 적었다고 했지만 실제 카드에는 '없음'이 그대로 있었습니다. 지금 적었고 …" (diff `+    가져온 OK: 3-1 영상(job-v-3-1) — ACTION_TIMING·PHYSICS 글자 그대로`). `higgsfield-generation/SKILL.md:54`대로 형식 앞에 둠 |

### 턴 2 — `됐어.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 2-1 | 그 job만 한 번 조회 | PASS | [TOOL] `jobs_wait(job_ids=["sim-job-3201"], timeout_seconds=0)` 한 번. `rename_folder(fld-3-2, "3-2 [검토]")`와 shot-list `검토`(`SKILL.md:76`) |
| 2-2 | ✔/✘ 3~5줄, "승인할까요, 거절할까요?", 숫자 분석 없음 | PASS | ✔ 4줄 + "봐 주세요: 손녀 돌아서는 속도가 3-1과 같은 느낌인지(재지 않음, 화면으로 판단)" + "승인할까요, 거절할까요?" |

### 턴 3 — `좋아, 3-2 영상 OK.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 3-1 | `승인` 폴더로 이동 | PASS | `list_project_assets(fld-3-2)` → `move_project_asset(placement_id=plc-3201, to_folder_id=fld-3-2-ok)` |
| 3-2 | OK 대장 목록 줄 + "3-2 영상" 카드(job·설정·시작 이미지·참조 순서·가져온 OK·OK 이유) | PASS | 목록 줄 `\| 3-2 \| 영상 \| sim-job-3201 \| Seedance 2.5 · 480p · 8초 \| 2026-10-28 \| …`. 카드: `참조(붙인 순서): 1 ff_3-2_v1 … 4 prop_doctor_bag_v1`, `가져온 OK: 3-1 영상(job-v-3-1) — ACTION_TIMING, PHYSICS 글자 그대로`, `OK 이유: "좋아, 3-2 영상 OK."`, `위험 → 막는 문장`, `한계: 없음` |
| 3-3 | 프롬프트는 turn0 전문을 글자 그대로 | PASS | `cmp turn0 코드블록 ↔ OK 카드 코드블록` 동일(4,997자), `tmp/p32.txt`도 동일 |
| 3-4 | shot-list: 확정 영상 job, 상태 승인. 폴더 `3-2 [승인]` | PASS | diff `\| 3-2 \| … \| 승인 \| … \| job-ff-3-2 \| sim-job-3201 \| 이미지 2 / 영상 1 \|`, `rename_folder(fld-3-2, "3-2 [승인]")` |
| 3-5 | 다시 생성하지 않음 | PASS | [TOOL]은 목록·이동·이름 변경 셋뿐 |

### 턴 4 — `핸드오프 쓰고 끝내.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 4-1 | `handoff.md` 형식([1]~[6], 40줄 이하)으로 `project/log/`에 | PASS | `project/log/3-2_handoff_2026-10-28.md` 13줄, [1]~[6] |
| 4-2 | [1]에 OK 대장 기록 여부 | PASS | "[1] 확정된 것: 영상 · job `sim-job-3201` … · OK 대장 카드 기록함 · 한계 없음" |
| 4-3 | [2]에 생성 수 | PASS | "[2] 이번 세션 생성: 이미지 0 / 영상 1 / 약 40 크레딧(추정, 2-1·3-1과 같은 설정이라 견적 안 봄) · 거절: 없음" |

### 공통

| # | 판정 | 근거 |
|---|---|---|
| G1 | PASS | `mcp__` 없음. 생성은 사용자 "만들어" 뒤 한 번 |
| G2 | PASS | 한국어, 짧게 |
| G3 | PASS | 질문은 turn2의 "승인할까요, 거절할까요?" 하나 |
| G4 | PASS | turn1: `higgsfield-generation/SKILL.md`, 3-2 카드, 3-2의 마지막 핸드오프(자기 컷), OK 대장 3-1 영상 카드 하나. turn4: `production-session/SKILL.md`, `handoff.md`. 3-1 핸드오프 열지 않음 |
| G5 | PASS | 보낸 프롬프트에 `[ ]` 없음 |

## 검사기 결과
```
$ check_prompt.py --kind video --refs 4 --seconds 8 --must-include (grandpa+girl+bag+light+motion_3-1).lines turn0.txt
OK — video 프롬프트 4997자, 걸린 항목 없음
$ (같은 옵션) OK 카드의 프롬프트
OK — video 프롬프트 4997자, 걸린 항목 없음
```
(turn0 코드블록과 OK 카드 코드블록은 바이트 동일.)

## 추가 발견
1. **컷 카드 [12]가 낡았다.** 승인 뒤 [12]는 `OK 대장 "3-2 시작 이미지"(job-ff-3-2) / 영상: 3-1 영상 OK 프롬프트에서 … 보낸 글자는 turn1 기준 tmp/p32.txt`로 남았다. 카드 틀은 "[12] 확정 프롬프트: OK 대장 카드 이름과 job. 전문은 그 카드에만 둔다"(`cut-card.md:28`)인데, 임시 파일 경로를 가리키고 새 "3-2 영상" 카드를 가리키지 않는다. 턴 3은 [11]만 고쳤다. 아래 D1.
2. 컷 카드 [4]에 렌즈 "대각 화각 35°"를 `(제안값)` 관찰 결과와 함께 적었으나, 3-2 시작 이미지(`ok-cuts.md:374`)는 75mm(≈32°)다. 키트는 시작 이미지가 이긴다고 하고 알리라고 한다(`video-prompt/SKILL.md:89`). turn0의 프롬프트(OPTICS 35°)부터 이어진 시험 데이터 불일치라 이 체인 기대 밖이다. 플레이어가 짚지 않았다.
3. 크레딧 "약 40"은 `decisions.md` §2 비용 메모(시험 폴더에 없음)가 아니라 시뮬레이터 표의 견적 값이다. "추정"으로 표시했으니 `SKILL.md:64`대로다.
4. 시험 데이터 한계: turn0의 "[7]에 적었다"는 거짓 → 정정은 좋은 행동. 가방 문장 "hanging heavy".

## 키트 결함
| # | 분류 | 결함 | 근거 | 수정 제안 |
|---|---|---|---|---|
| D1 | 규칙이 없음 | OK 기록 절차에 "컷 카드 [12] 확정 프롬프트를 새 OK 카드 이름과 job으로 고친다"가 없다. 컷 세션이 [12]를 쓴다고만 되어 있고(`production-session/SKILL.md:18`), OK 기록 1~4단계는 OK 대장·컷 목록·옛 OK만 다룬다. 그래서 [12]가 승인 뒤에도 옛 값 + 임시 파일 경로로 남았다 | `higgsfield-generation/SKILL.md:100-110`, `production-session/cut-card.md:28`, `production-session/SKILL.md:18` | OK 기록 3번에 "컷 카드 [12]를 `OK 대장 "3-2 영상" · job`으로, [11]에 `job — 승인`을 적는다. 임시 파일 경로는 카드에 쓰지 않는다"를 더한다 |
| D4 | 모호함(경미) | `decisions.md` §2 "비용 메모"가 없을 때 `약 N 크레딧`의 출처 규칙이 "모르면 추정"뿐이다. 이번엔 `추정`을 붙여 문제없음(C18은 붙이지 않음) | `higgsfield-generation/SKILL.md:13`, `:64` | "비용 메모에 값이 없으면 직전 같은 설정의 견적을 쓰고 `추정`을 붙인다" |

## 총평
생성 1회(견적 없이)·형식 종료·한 번 조회·승인 처리·OK 카드 바이트 일치·핸드오프까지 기대대로이고, 지난번 흠 셋(거짓 정정 누락·불필요한 견적·3-1 핸드오프 열기)이 모두 사라졌다. 남은 것은 승인 뒤 컷 카드 [12]를 안 고치는 키트 공백 하나.
