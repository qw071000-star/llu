# real16-C67 생성 → 확인 → OK → 핸드오프, 3-2 전 과정 (6턴) — PASS 4 / 부분 2 / FAIL 0

## 턴별 판정
| 턴 | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1 | 13번 + 카드 [1] "3-1과 같은 동작"으로 16번(ok-reuse) 병행, 꼭 물을 것만, 생성 없음 | 부분 | "13번 실사·인물 영상으로 진행합니다." 질문 2개(동작·타이밍 / 끝 상태·이음새) 제안값+이유, 카드 35° ↔ 시작 이미지 75mm 충돌을 "시작 이미지를 따릅니다". 그러나 `ok-reuse.md`를 열지 않음(reads에 없음) |
| 1 | 승인 동작이라 사건 수 예외 | PASS | "3-1에서 승인된 구성이라 나누지 않습니다" |
| 2 | "그대로" = 생성 아님, 전문+검사기(`--must-include`)+위험 목록+"보낼까요?" | PASS | 코드블록 전문, 위험 6개, "보낼까요? … '영상으로 만들어' 또는 '보내'라고 해 주세요" |
| 2 | 가져온 3-1 줄을 글자 그대로, 입 잠금 강화 | 부분 | 0:05–0:08 줄의 `his thumb rests` → `the thumb of the screen-left hand, nearer the persimmon tree, rests`로 줄 중간 변경(ok-reuse §3.1 위반, 3-1 줄을 must-include에 넣으면 FAIL). AUDIO는 약한 `no attempt to speak, no lip movement.` 그대로(ok-reuse §3.1 예외/live-action.md:103의 `no parted lips, no mouthing`으로 올려야 함). 카드 [7] "가져온 OK" 미기록(`git diff`) |
| 2 | 카드 [4]-[6]에 `(제안값)` 기록 | PASS | [5][6] 기록. ([4] 렌즈는 t6에서야 고침) |
| 3 | "영상으로 만들어" → `generate_video` 480p draft, `fld-3-2`, `job-ff-3-2`, 카드 [11]·목록 기록, 형식으로 끝 | PASS | "3-2 영상 · Seedance 2.5 · 480p draft · 8초 · job `sim-job-3201` · 약 40 크레딧 … 저장 `fld-3-2` … 볼 점 3개". 카드 [11] "sim-job-3201 — 보냄 — 약 40 크레딧". 비고: `[TOOL]` 줄 없음, "get_cost 견적" 인용만 |
| 4 | `[TOOL]` 상태 확인 → 3201 완료, 항목별 ✔/✘, `검토`, 승인/거절 묻기 | PASS | `[TOOL] job_display(job_id=sim-job-3201) → completed`, `rename_folder … "3-2 [검토]"`, ✔ 대사/할아버지 입/시작 상태/카메라, "봐 주세요: 손녀의 한 걸음…", "승인할까요, 거절할까요?" |
| 5 | OK 대장에 프롬프트 글자 그대로, `fld-3-2-ok`로 이동, 확정 영상 칸·`승인` | PASS | `move_project_asset(plc-3201 → fld-3-2-ok)`, `rename_folder "3-2 [승인]"`. OK 카드 프롬프트 = t2 블록과 바이트 동일(스크립트 비교 `True`), 목록 줄·draft 예(만료일 알 수 없음), shot-list `승인`/`sim-job-3201`/`이미지 2 / 영상 1 · 약 48 크레딧` |
| 6 | `handoff.md` 틀로 핸드오프, 다른 컷 핸드오프 안 엶 | PASS | `project/log/3-2_handoff_2026-10-30.md` — 받는 세션/보낸 세션/컷 상태 + [1]~[6], 14줄. reads = production-session SKILL, handoff.md만 |

## 검사기
`python3 kit/skills/higgsfield-generation/check_prompt.py --kind video <t2 블록> --refs 4 --seconds 8 --must-include (grandpa+girl+bag+light.lines)`
→ `OK — video 프롬프트 5356자, 걸린 항목 없음`
같은 블록에 `motion_3-1.lines`(가져온 줄)를 must-include에 더하면:
→ `FAIL  고정 문장이 글자 그대로 들어 있지 않다: 0:05–0:08 — GRANDPA lowers his eyes to the bag and his thumb… — FAIL 1 · WARN 0`

## 추가 발견
- 카드 [7] `가져온 OK: 없음`이 그대로인데 OK 카드에는 `가져온 OK: 3-1 영상` → 정본 불일치.
- 감나무 위치를 "시작 이미지를 못 봐서 추정"이라며 `at most at the left edge of the frame`로 흐리게 씀 (OK 대장 3-2 시작 이미지 프롬프트에 화면 구도가 있음).
- 승인 후 handoff [3]이 "렌즈 35°→32°"를 적었고 카드 [4] 렌즈 수정은 t6에야 반영.

## 키트 결함
- `kit/context/tasks.md:33` 16번 "User says"가 "3-1처럼"뿐이라, 카드 [1]/컷 목록이 "3-1과 같은 동작"이라고 하는 경우 `ok-reuse.md`가 안 열림(C67 t1, C68 t1) → 약한 입 잠금 유지·가져온 줄 중간 수정·카드 [7] 누락. 고침: 33행에 "또는 컷 카드 [1]/컷 목록이 다른 컷과 같은 동작이라고 한 때"를 덧붙이고 13번 행에도 같은 문구.
- `kit/skills/higgsfield-generation/check_prompt.py:97-98`: `no lip movement`만 있는 약한 입 잠금을 잡지 않음(`live-action.md:103`의 `no parted lips, no mouthing` 표준과 불일치). 고침: AUDIO에 `lip movement`가 있고 `parted lips`가 없으면 WARN.

## 총평
생성→확인→OK→핸드오프 수명주기와 정본 기록은 정확하다. OK 재사용 절차(ok-reuse)를 건너뛰어 가져온 줄이 변형되고 입 잠금이 약하다.
