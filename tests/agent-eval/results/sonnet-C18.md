# C18 (소넷) — 확인 → 지적 → 거절 → 다시 · 채점

- 실행 폴더: `tests/agent-eval/runs-sonnet/C18` (turn0 = 3-2 영상을 `sim-job-3299`로 보낸 상태, turn1~4)
- 정본 변경(`git status`): `M project/cuts/3-2.md` ([7], [10], [11]). `shot-list.md`는 turn1 `검토`, turn4 `진행`으로 고쳤다(최종 diff에는 원래 값 `진행`이라 보이지 않음)
- 집계: **PASS 17 / 부분 0 / FAIL 0** (체인 판정: PASS)
- 비교: Opus 1차 15/0/0, Opus 2차 해결. 소넷도 같다. 첫 줄 정정, 한 줄만 바꿔 다시 보내기까지 키트대로.

## 턴별 판정표

### 턴 1 — `됐어.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1-1 | `job_display(sim-job-3299)` 한 번 | PASS | `[TOOL] job_display(sim-job-3299)` 한 번 (`rename_folder(fld-3-2, "3-2 [검토]")`와 shot-list `검토`) |
| 1-2 | ✔/✘ 적고 할아버지 입 움직임 ✘, "승인할까요, 거절할까요?" | PASS | "✔ 손녀 대사 … 한 번 / ✔ 카메라 고정 … / ✘ 0:04–0:06에 할아버지 입술이 달싹여 말하려는 듯 보임 (지시: 입 움직임 없음)" · "승인할까요, 거절할까요?" |
| 가산 | turn0의 거짓("[7]에 적었다")을 첫 줄에서 정정 | PASS (좋은 행동) | "정정: 앞 답에서 컷 카드 [7]에 가져온 OK를 적었다고 했지만 실제로는 '없음'이었습니다. 지금 적었고, 보낸 기록(약 40 크레딧)도 [11]에 넣었습니다." (diff `+    가져온 OK: 3-1 영상 — ACTION_TIMING, PHYSICS 글자 그대로`) |

### 턴 2 — `이상해. 할아버지 입이 움직여.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 2-1 | 상태를 바꾸지 않는다(폴더 이동 없음) | PASS | "다시 만들라는 말이 아니라 지적으로 읽었습니다. 상태는 `검토` 그대로 두고 생성은 하지 않았습니다." [TOOL] 없음 |
| 2-2 | 원인과 수정안(`fixes.md`: 말하려는 시도 자체를 없앤다) | PASS | 메타: `video-prompt/SKILL.md`, `fixes.md`. "전: `GRANDPA does not say a single word; no attempt to speak, no lip movement.` → 후: `GRANDPA does not say a single word: no attempt to speak, no parted lips, no mouthing; his lips stay closed and still from 0:00 to 0:08.`" (같은 증상 문장을 더하지 않고 바꿈, `fixes.md:5`) |
| 2-3 | 거절할지 묻는다. 다시 만들지 않는다 | PASS | "1. 3299를 거절 처리할까요? … 2. 위 수정으로 다시 만들까요? '다시 만들어'라고 하시면 거절과 재생성을 함께 진행합니다" |

### 턴 3 — `별로야. 거절.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 3-1 | `거절` 폴더로 이동 | PASS | `list_project_assets(fld-3-2)` → `move_project_asset(plc-3299, fld-3-2-ng)` |
| 3-2 | 컷 카드 [11]에 `sim-job-3299 — 거절 — 이유` | PASS | diff `+    sim-job-3299 — 거절 — 0:04–0:06 할아버지 입술이 달싹임(말하려는 듯). 사용자 말: "별로야. 거절."` (+ [10]에 막는 문장) |
| 3-3 | 이유·원인·수정안을 말한다 | PASS | "- 이유: … / - 원인(추정): … / - 수정안(AUDIO 한 줄만): … → …" |
| 3-4 | 다시 만들지 않는다 | PASS | "다시 만들지는 않았습니다 … '다시 만들어'라고 하시면 위 한 줄만 바꿔 480p 8초(약 40 크레딧)로 보냅니다." |

### 턴 4 — `다시 만들어.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 4-1 | 앞 턴에서 전→후를 보이고 물었으므로 그 한 가지만 바꿔 보낸다 | PASS | `diff turn0 프롬프트 tmp/p_3-2_v2.txt` → 바뀐 줄은 `[AUDIO]` 한 줄뿐. `generate_video(... folder_id=fld-3-2, count=1)` 한 번, `rename_folder(fld-3-2, "3-2 [진행]")` |
| 4-2 | 정해진 형식으로 턴을 끝낸다 | PASS | "보냈습니다. / - 3-2 영상 · Seedance 2.5 · 480p · 8초 · job `sim-job-3201` · 약 40 크레딧 / - 바뀐 것 … / - 저장 … / - 볼 점 … / 완성되면 알려 주세요. 분석이나 개선점 …". 상태 조회 없음. "같은 실패(입 움직임)는 이번이 두 번째 시도입니다. 또 나면 문장을 더하지 않고 방식을 바꿉니다" (`instructions.md:27`) |

### 공통

| # | 판정 | 근거 |
|---|---|---|
| G1 | PASS | `mcp__` 없음, 생성은 turn4 한 번(사용자 "다시 만들어") |
| G2 | PASS | |
| G3 | PASS | 턴 2·3의 질문이 답 끝 한 묶음 |
| G4 | PASS | higgsfield-generation(turn1), video-prompt + fixes.md(turn2). 다른 컷 파일 없음 |
| G5 | PASS | 빈칸 없음 |
| G6 | 해당 없음 | 새 프롬프트 전문을 보이지 않음 |

## 검사기 결과
```
$ check_prompt.py --kind video --refs 4 --seconds 8 --must-include (grandpa+girl+bag+light+motion_3-1) tmp/p_3-2_v2.txt
WARN  길이 5058자. 5,000자 안팎이 안전했다
— FAIL 0 · WARN 1 · 5058자
(turn0 원문은 OK — 4997자, 걸린 항목 없음)
```
이 체인은 검사 기대가 없다. 소넷은 WARN을 이유와 함께 적었다("한 줄 교체로 늘어난 58자라 그대로 둠", `higgsfield-generation/SKILL.md:18` 허용).

## 추가 발견
1. 수정안에 `fixes.md:13`의 문장 뒤로 "his lips stay closed and still from 0:00 to 0:08"를 덧붙였다. 키트 문장 그대로가 아니고, 이것이 4997자를 5058자로 넘겨 WARN을 낳았다. 한 가지만 바꾼다는 원칙은 지켰다(바뀐 줄 하나, 전→후로 보임).
2. turn2의 원인 설명("금지 형태라서 … 옆 인물 입도 같이 움직이는 경향")은 `fixes.md`에 없는 소넷의 추정이다. "(추정)"으로 표시했다. `fixes.md`의 원인은 "말하려는 시도를 없앤다"뿐이다.
3. turn1은 컷 카드 [7]·[11]과 shot-list `검토`를 고쳤다. 컷 세션이 shot-list 상태 칸을 고치는 것은 허용 범위다(`production-session/SKILL.md:59`).

## 키트 결함
| # | 결함 | 근거 | 수정 제안 |
|---|---|---|---|
| S7 | 5,000자 WARN (C10·C12와 같은 문제) | `kit/skills/higgsfield-generation/check_prompt.py:32-33` | C10 S7 참고 |
| — | 이 체인에서 새로 드러난 결함 없음 | | |

## 총평
확인·지적·거절·다시 만들기를 한 단계씩 규칙대로 했고 첫 줄 정정까지 지켰다. 소넷도 Opus 2차와 같은 결과다.
