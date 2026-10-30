# C12 (소넷) — "3-1의 모션처럼 3-2 영상 프롬프트" · 채점

- 실행 폴더: `tests/agent-eval/runs-sonnet/C12` (turn1: 질문, turn2: `그대로.` 뒤 전문)
- 정본 변경: `project/cuts/3-2.md` ([4] 렌즈, [5] 끝·동선·시선, [6] 타이밍·이음새, [7] 가져온 OK, 모두 `제안값`/`3-1 모션` 표시)
- 집계: **PASS 16 / 부분 1 / FAIL 1** (체인 판정: 부분)
- 비교: Opus 1차 11/0/1(검사 미실행), Opus 2차는 검사 실행·입 금지 줄·75mm=32°를 모두 해결. 소넷은 검사·입 금지·32°는 맞췄고, 3-1 컷 카드를 열었다.

## 턴별 판정표

### 턴 1 — `3-1의 모션처럼 3-2 영상 프롬프트 만들어.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1-1 | `production-session` → `ok-reuse.md`, OK 대장 **3-1 영상 카드 하나** | PASS | 메타: production-session/SKILL.md, ok-reuse.md, `ok-cuts.md(목록과 ### 3-1 영상, ### 3-2 시작 이미지 절)`. "기준은 OK 대장 '3-1 영상'(`job-v-3-1`)" |
| 1-2 | 카메라·렌즈·위치는 3-2 카드·시작 이미지를 따르고, 35° 대 75mm(≈32°)를 알린다 | PASS | "컷 카드는 35°인데 승인된 시작 이미지는 75mm 렌즈로 만들었습니다(≈32°). 시작 이미지가 이기므로 제안 — 대각 약 32°" . "3-1의 63°·깊은 초점은 카메라 요소라 가져오지 않았습니다" |
| 1-3 | 빈 칸만 묻거나 제안값으로 채운다 | PASS | 질문 3개(화각·관찰 결과, 연기 범위, 3-3 이음새). 끝 위치·동선·시선·타이밍은 3-1에서 가져와 카드에 기록 |
| 1-4 | 3-1의 Required·Forbidden 중 가져온 동작·인물에 걸린 줄 | PASS | "같이 가져오는 위험: 할아버지 입 움직임 → `no attempt to speak, no lip movement`, 대사 두 번 → `exactly once`, 할아버지가 손녀를 봄 → `He never looks at the girl`" |
| 1-5 | 컷 카드 3-2 [7]에 "가져온 OK: 3-1 영상 — 모션(…)" | PASS | diff `+    가져온 OK: 3-1 영상 — 모션(ACTION_TIMING, PHYSICS)` |
| G1 | mcp·생성 없음 | PASS | [TOOL] `list_folders`, `list_project_assets(fld-3-2)` |
| G2·G3 | 한국어 짧게, 질문 끝 한 묶음 | PASS | "프롬프트를 쓰기 전에 확인할 것이 3개 있습니다. 제안값이 괜찮으면 '그대로'" |
| G4 | 필요한 스킬·파일만, 다른 컷 카드를 열지 않는다 | **FAIL** | 메타: `project/cuts/3-1.md`를 열었다(핸드오프·3-2 카드 다음). 3-1 거절 사유("할아버지가 손녀를 봄", "대사 두 번")는 OK 카드에 없는 정보라 컷 카드에서 온 것이다. `acting/SKILL.md`·`higgsfield-generation/SKILL.md`도 질문 턴에 미리 열었다(모션만 가져오는 컷이라 acting은 불필요) |

### 턴 2 — `그대로.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 2-1 | `ACTION_TIMING`·`PHYSICS` 글자 그대로 (`motion_3-1.lines`) | PASS | `--must-include grandpa+girl+bag+light+motion_3-1` 통과. ACTION_TIMING 3구간·PHYSICS 4줄이 OK 카드와 같다 |
| 2-2 | 3-1 Required·Forbidden의 입 움직임 금지 줄 | PASS | AUDIO "GRANDPA does not say a single word; no attempt to speak, no lip movement." + Forbidden "GRANDPA moving his lips or speaking (ENTIRE_SHOT)" |
| 2-3 | 본문에 "3-1"·"previous shot" 없음 | PASS | `grep "3-1\|previous"` 결과 없음 |
| 2-4 | 보이기 전에 검사 실행 | PASS | "검사 스크립트(`check_prompt.py`, 영상, 참조 4, 고정 문장 포함)를 돌렸고 FAIL 0, WARN 1입니다." 메타에 `tmp/p32.txt`, `tmp/fixed32.txt` |
| 2-5 | 검사 `--refs 4 --seconds 8 --must-include …` FAIL·WARN 없음 | 부분 | 아래: FAIL 0, **WARN 1 (5258자)**. "승인된 3-1 프롬프트와 같은 구조라 그대로 둡니다(줄이면 가져온 문장이 달라집니다)"로 이유를 적었다. 키트는 이유 한 줄을 허용한다(`higgsfield-generation/SKILL.md:18`) |
| 2-6 | 렌즈 = 시작 이미지 우선(≈32°) | PASS | "Diagonal field of view about 32°. The bench and the sign are fully visible side by side in one frame / straight lines stay straight / the paddies behind are compressed and soft. Shallow depth of field …" (mm 없음) |
| 2-7 | 카드 3-2 기록 | PASS | [4] "렌즈: 대각 화각 32° (제안값 · 시작 이미지 75mm가 카드 35°보다 우선) …", [6] "(3-1 모션)" |
| G1 | 생성하지 않음 | PASS | "이 프롬프트로 480p를 생성할까요? 생성은 지시하셔야 보냅니다" |
| G5 | 빈칸 없음 | PASS | |
| G6 | 코드블록 하나 + 블록 밖 | PASS | 모드·참조(1~4 순서)·모델·해상도·길이·소리·저장 폴더 |

## 검사기 결과
```
$ check_prompt.py --kind video --refs 4 --seconds 8 --must-include (grandpa+girl+bag+light+motion_3-1) c12.txt
WARN  길이 5258자. 5,000자 안팎이 안전했다
— FAIL 0 · WARN 1 · 5258자
```
태그 4개(`ff_3-2_v1`, `char_grandpa_autumn_v1`, `char_girl_raincoat_v1`, `prop_doctor_bag_v1`) = 블록 밖 참조 4개.

## 추가 발견
1. "3-1에서 바꾼 줄(전 → 후)" 목록에서 `Neither of them looks at the camera.` → `Nobody looks at the camera.` 교체가 빠졌다(`ok-reuse.md:44-45`는 바꾼 단어를 모두 "전 → 후"로 보이라고 한다). 내용상 문제는 없다.
2. 좋았던 점: 3-3 시작 이미지의 손녀 위치와 맞는지는 "아직 보지 않았습니다"라고 밝히고 다른 컷 카드를 열지 않았다.
3. 블록 밖 `해상도: 480p(확인용)`, `길이: 8초 · 16:9 · 소리 켬(대사)` 등 표기는 `instructions.md:92`와 같다.
4. 가방 고정 문장("hanging heavy from its handles")과 "bag stays on his lap"는 시험 데이터 한계라 감점하지 않는다(3-1 OK 카드 문장과 같다).

## 키트 결함
| # | 결함 | 근거 | 수정 제안 |
|---|---|---|---|
| S1 | "기준 OK 카드"와 "컷 카드" 혼동으로 `cuts/3-1.md`를 열었다 (C02와 같은 원인) | `kit/project-files/CLAUDE.md:19`, `kit/skills/production-session/ok-reuse.md:9` | C02 S1 참고. ok-reuse.md §1에 "OK 카드는 `ok-cuts.md`의 절이다. `project/cuts/<번호>.md`는 열지 않는다" |
| S2 | 3-1 영상의 실패 이력을 OK 카드 밖에서 찾게 된다 | `kit/skills/production-session/ok-reuse.md:47` | C02 S2 참고 |
| S7 | 5,000자 WARN 필연 | `kit/skills/higgsfield-generation/check_prompt.py:32-33` | C10 S7 참고 |
| S15 | 질문 턴에 스킬을 미리 여는 행동을 막는 말이 없다(acting은 "연기를 쓸 때"만) | `kit/instructions.md:77`, `kit/skills/video-prompt/SKILL.md:12` | video-prompt 표의 "인물·소품·대사가 있는 실사 컷 … (+ 연기는 `acting`)"에 "연기 블록을 새로 쓸 때만. 모션만 가져오는 컷은 열지 않는다" |

## 총평
OK 카드 하나에서 글자 그대로 가져오기, 입 금지 줄, 32° 환산, 검사 선실행, 카드 기록까지 Opus 2차와 같다. 3-1 컷 카드를 연 것과 5258자 WARN이 남았다.
