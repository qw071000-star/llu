# C10 (소넷) — 영상, 일부만 답함 (3-3) · 채점

- 실행 폴더: `tests/agent-eval/runs-sonnet/C10` (turn1~3; 2턴에 다시 물어서 3턴 추가)
- 정본 변경: `project/cuts/3-3.md` ([3]~[6], [10]에 `제안값` 표시). 다른 정본 그대로
- 집계: **PASS 17 / 부분 1 / FAIL 0** (체인 판정: PASS). "키트 모호" 1건은 판정 제외.
- 비교: Opus 1차 15/0/0, Opus 2차도 같은 흐름(2턴에 렌즈 충돌을 묻고 3턴에 전문). 소넷은 길이 WARN을 남긴 것만 다르다.

## 턴별 판정표

### 턴 1 — `3-3 영상 프롬프트 만들어. 손녀가 시간표를 다시 보고 돌아서는 거야.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1-1 | `video-prompt` + `live-action.md` + `acting`을 연다 | PASS | 메타: video-prompt/SKILL.md, live-action.md, acting/SKILL.md |
| 1-2 | 컷 카드 빈 칸을 제안값·이유와 함께 한 번에 묻는다(카메라/인물/타이밍), 정본 기본값은 "기본값으로 씀" | PASS | "**기본값으로 씀:** 8초 · 16:9 · Seedance 2.5 · 480p 확인 · 고정 카메라 … 효과음만" 뒤에 [카메라] 1, [인물: 손녀] 2~5, [타이밍] 6, [이음새] 7. 질문마다 "이유:" |
| 1-3 | 시작 이미지 `job-ff-3-3`을 안다, 말하지 않은 칸도 묻는다 | PASS | "승인된 시작 이미지 `job-ff-3-3`만 있습니다 … 이 이미지를 0:00으로". 렌즈·끝 위치·동선·시선·연기 범위·타이밍을 모두 물음. 대사 유무는 "대사는 컷 목록에 '돌아선다'뿐이라 없는 컷으로 봤습니다. 대사가 있으면 알려 주세요"로 열어 둠 |
| G1 | mcp·생성 없음 | PASS | [TOOL] `list_folders`, `list_project_assets(fld-3-3)` |
| G2·G3 | 한국어, 질문 한 묶음 | PASS | |

### 턴 2 — `렌즈는 망원으로 해. 대사는 없어. 나머지는 몰라.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 2-1 | 렌즈·대사 반영, 나머지는 제안값, 컷 카드 [3]~[6]에 기록·`제안값` 표시 | PASS | "'나머지는 몰라'는 반영했습니다 … 제안값으로 확정". 카드 diff: "[5] 끝(마지막 프레임): … (제안값)", "[6] 타이밍: … (제안값)", "[3] … 소리 효과음만(대사 없음 — 사용자 답 2026-10-28)", "[10] 알려진 위험 → 막는 문장 (제안값)" |
| 2-2 | 망원과 시작 이미지(50mm)가 부딪친다고 짚는다 | PASS | "승인된 시작 이미지 `job-ff-3-3`는 50mm(대각 약 47°)로 만들어졌고 … 망원(예: 85mm, 약 29°)으로 쓰면 구도가 달라져서 시작 이미지와 맞지 않습니다." 환산표를 맞게 썼다 |
| 2-3 | 15블록 전문 | 키트 모호(판정 제외) | 렌즈 A/B를 다시 물었다. `kit/instructions.md:24`("사용자 말이 정본·OK와 다르면 어느 쪽을 따를지 묻는다")를 따른 것이고 `video-prompt/SKILL.md:112`("시작 이미지가 이긴다. 알린다")와 모순이라 시나리오 3턴 조건에 해당한다. B안은 "시작 이미지를 새로 만들어 승인받아야 합니다 … 이미지 1k 약 4 크레딧"으로 방식 변경 비용까지 밝혔다 |

### 턴 3 — `몰라, 알아서 해. 렌즈는 시작 이미지 그대로 둬.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 3-1 | 제안값으로 쓰고 컷 카드에 기록·표시 | PASS | 카드 [4] "렌즈: 대각 약 47°(시작 이미지 50mm 그대로 — 사용자 답 2026-10-28, '망원' 요청은 시작 이미지와 충돌해 철회) … (추정)" |
| 3-2 | 15블록 전문 | PASS | 15개 제목이 순서대로(`SCENE_CONTEXT` … `REQUIRED_AND_FORBIDDEN_CONSTRAINTS`) |
| 3-3 | 렌즈는 화각(도) + 관찰 결과 3개, mm 없음 | PASS | "Diagonal field of view about 47°. The girl and the timetable sign fill the right half of the frame / the end of the shelter sits at the left edge / the road edge and the paddies behind are all visible, without strong compression." |
| 3-4 | 의상(girl)·LIGHT LOCK 글자 그대로, 소리 = 효과음만 | PASS | `--must-include girl+light` 통과. "[AUDIO] No dialogue. The girl does not say a single word … Sound effects only: faint evening wind …" |
| 3-5 | 검사 `--refs 2 --seconds 8 --must-include girl+light` FAIL·WARN 없음 | 부분 | 아래 검사기 결과: FAIL 0, **WARN 1 (5233자)**. 플레이어가 "WARN 1개: 길이 5,233자 … 그대로 두었습니다"라고 이유를 적었다. 키트는 이유 한 줄을 허용하지만(`higgsfield-generation/SKILL.md:18`) 기대는 WARN 없음이다. Opus는 4993자로 WARN이 없었다 |
| G1 | mcp·생성 없음 | PASS | 3턴 [TOOL] 없음. "아직 생성하지 않았습니다" |
| G2 | 한국어, 본문 영어 | PASS | |
| G3 | 질문 한 묶음 | PASS | 3턴에 새 질문 없음 |
| G4 | 필요한 스킬·파일만 | PASS | production-session/SKILL.md, higgsfield-generation(검사용), 3-3 파일만. 다른 컷 카드는 열지 않았다 |
| G5 | 빈칸 없음 | PASS | |
| G6 | 코드블록 하나 + 블록 밖 | PASS | "모드 … 참조(붙일 순서): 1 시작 이미지 `job-ff-3-3` … 2 `char_girl_raincoat_v1` … 모델·해상도·길이·소리·저장 폴더" |

## 검사기 결과
```
$ check_prompt.py --kind video --refs 2 --seconds 8 --must-include (girl.lines+light.lines) c10.txt
WARN  길이 5233자. 5,000자 안팎이 안전했다
— FAIL 0 · WARN 1 · 5233자
```
태그 2개(`ff_3-3_v1`, `char_girl_raincoat_v1`) = 블록 밖 참조 2개.

## 추가 발견
1. `REQUIRED_AND_FORBIDDEN_CONSTRAINTS`의 Forbidden에 "No walking away", "No second person, no vehicle"처럼 **아직 나온 적 없는 예상 위험**을 넣었다. `live-action.md:27`은 "실제로 나온 실패만"이다. 플레이어는 "위 위험은 이 컷에서 실제로 난 실패가 아니라 예상입니다"라고 밝혔다. `instructions.md:26`(위험마다 막는 문장)과 `live-action.md:27`이 부딪쳐서 생긴 일이다.
2. 좋았던 점: 관찰 결과 3개가 "시작 이미지 프롬프트 기준이라 이미지를 직접 보고 확인한 것은 아닙니다(추정)"라고 밝혔다. 3-2 끝 상태를 모른다는 것도 "추정"으로 적었다.
3. 턴 2에서 사용자 지시를 카드에서 철회한 이유를 카드 [4]에 남겼다.

## 키트 결함
| # | 결함 | 근거 | 수정 제안 |
|---|---|---|---|
| S7 | 5,000자 WARN이 15블록 빈 틀을 채우면 거의 항상 난다(C10 5233, C12 5258, C18 5058, C17 turn0 4997). 소넷은 이유만 적고 남겼고, 줄이는 방법이 키트에 없다 | `kit/skills/higgsfield-generation/check_prompt.py:32-33`, `kit/skills/video-prompt/live-action.md:29-36`, `:42-115` | 임계를 5,500으로 올리거나, live-action.md "덜어내는 법"에 "5,000자를 넘으면: SCENE_CONTEXT 한 문장, REFERENCE AUTHORITY 한 문장, QUALITY 한 줄로 줄인다"를 넣는다 |
| S8 | "위험마다 막는 문장"과 "Forbidden은 실제 실패만"이 충돌해 예상 위험의 자리가 없다 | `kit/instructions.md:26` vs `kit/skills/video-prompt/live-action.md:27` | "예상 위험의 막는 문장은 Required나 해당 블록(AUDIO·CAMERA)에 쓴다. Forbidden은 실제 실패만"을 live-action.md:27 옆에 한 줄 |
| S9 | 사용자 지시(망원)와 시작 이미지가 부딪칠 때 "묻는다"와 "알린다"가 모순(시나리오에 이미 있는 모호) | `kit/instructions.md:24` vs `kit/skills/video-prompt/SKILL.md:112` | 영상 렌즈는 시작 이미지가 이기고 "알린다 + 바꾸려면 시작 이미지부터"로 한 문장 통일. 그러면 2턴에 전문이 나온다 |

## 총평
"몰라"를 제안값으로 처리하고 망원 충돌을 정확한 환산(47°)으로 짚었으며 15블록·고정 문장은 맞았다. 5233자 WARN만 남았고 원인은 키트 임계와 템플릿 길이다.
