# C10 (소넷, 정리된 키트) — 영상, 일부만 답함 (3-3) · 채점

- 실행 폴더: `tests/agent-eval/runs-sonnet2/C10` (turn1~3; 2턴에 렌즈를 다시 물어서 3턴 추가). 정본 변경: `project/cuts/3-3.md`만 (`M project/cuts/3-3.md`, `?? out/`, `?? tmp/`)
- 집계: **PASS 22 / 부분 1 / FAIL 0** (체인 판정: PASS)
- 지난 소넷(정리 전): 17 / 1 / 0 (길이 WARN 때문에 부분).

## 턴별 판정표

### 턴 1 — `3-3 영상 프롬프트 만들어. 손녀가 시간표를 다시 보고 돌아서는 거야.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1-1 | `video-prompt` + `live-action.md` + `acting`을 연다 | PASS | 1턴 메타: `video-prompt/SKILL.md`, `live-action.md`. `acting/SKILL.md`는 3턴(15블록을 쓸 때)에 열었다. 읽기 지도 `kit/instructions.md:55`가 "연기 블록을 새로 쓸 때"라 지침대로다(시나리오 기대보다 늦지만 키트와 맞음) |
| 1-2 | 컷 카드 빈 칸을 제안값·이유와 함께 한 번에 묻는다(카메라/인물/타이밍), 정본 기본값은 "기본값으로 씀" 한 줄 | PASS | "**기본값으로 씀:** 8초 · Seedance 2.5 · 16:9 · 480p(확인용) · 삼각대 고정 카메라 · 저장 폴더 `fld-3-3`" 뒤에 "확인할 것이 7개 있습니다" [카메라] 1, [인물] 2~4, [타이밍] 5~6, [연기] 7. 질문마다 "이유:" |
| 1-3 | 시작 이미지 `job-ff-3-3`을 안다. 말하지 않은 칸(끝 위치·동선·시선·타이밍·대사 유무·연기 범위)도 묻는다 | PASS | "승인에 `job-ff-3-3`(시작 이미지)만 있고", 2번 끝 자세·동선, 4번 시선, 5번 타이밍, 6번 "이 컷에 대사가 있으면 알려 주세요", 7번 연기 |
| G1 | mcp·생성 없음 | PASS | [TOOL] `list_folders`, `list_project_assets(fld-3-3)` |
| G2 | 한국어 짧게 | PASS | |
| G3 | 질문은 끝에 한 묶음 | PASS | |
| G4 | 필요한 스킬·파일만 | 부분 | 스킬은 `production-session`(+`ok-reuse.md` 제안용, `cut-card.md` 카드 기록용), `video-prompt`+`live-action.md`로 읽기 지도 안이다. 그러나 `ok-cuts.md`를 "3-1 영상 카드를 찾으려 파일 전체를 열었음"(메타). `production-session/SKILL.md:69`는 "제목으로 찾아 그 절만"이라고 한다 |

### 턴 2 — `렌즈는 망원으로 해. 대사는 없어. 나머지는 몰라.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 2-1 | 렌즈·대사만 반영, 나머지는 제안값으로 컷 카드 [3]~[6]에 기록하고 제안값 표시 | PASS | "대사 없음은 반영했습니다 … '나머지는 몰라'는 제 제안값을 쓰는 것으로 보고 컷 카드 3-3에 `(제안값)`으로 적었습니다". diff: `[5] 끝(마지막 프레임): … (제안값 …)`, `[6] 타이밍: … (제안값)`, `[3] … 소리 효과음만, 대사 없음(사용자 답 2026-10-28)` |
| 2-2 | 망원과 시작 이미지(50mm)가 부딪친다고 짚는다 | PASS | "말씀하신 망원은 승인된 시작 이미지(`job-ff-3-3`, 50mm = 대각 약 47°)와 다릅니다 … A. 시작 이미지 유지 / B. 망원으로 변경: 85mm = 대각 약 29°로 시작 이미지를 새로 만들고 …" 환산이 표와 맞다 |
| 2-3 | (기대) 제안값으로 15블록 전문 | PASS (기대 오류 의심) | 렌즈 A/B를 다시 물었고 프롬프트는 쓰지 않았다. 키트가 이제 일관되게 "묻는다"이다: `kit/instructions.md:26`("사용자 말이 … 시작 이미지와 다르면 어느 쪽인지 묻는다"), `kit/skills/video-prompt/SKILL.md:89`("사용자 말과 시작 이미지가 다르면 묻는다"). 지난번의 "묻는다 대 알린다" 모순이 풀렸으므로 이 턴은 키트대로다. 시나리오 2턴 기대를 "렌즈 충돌을 묻는다"로 고치길 권한다 |
| G1 | mcp·생성 없음 | PASS | [TOOL] 없음. "이미지 생성은 지시하실 때만 합니다" |
| G3 | 질문은 남은 것만 한 묶음 | PASS | "확인할 것이 1개 있습니다" 렌즈 하나 |

### 턴 3 — `몰라, 알아서 해. 렌즈는 시작 이미지 그대로 둬.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 3-1 | 제안값으로 쓰고 컷 카드에 기록·표시 | PASS | diff `[4] 렌즈: 시작 이미지 50mm = 대각 약 47° 그대로 (사용자 답 2026-10-28, "망원" 대신 시작 이미지 유지) · … (제안값)`. 앞 제안 하나를 고쳤고 첫 줄에서 "**정정(제안값 하나):** 끝 자세 '시간표에서 반 걸음 떨어져' → '시작 위치 그대로'"라고 밝혔다 |
| 3-2 | 15블록 전문 | PASS | `[SCENE_CONTEXT]`~`[REQUIRED_AND_FORBIDDEN_CONSTRAINTS]` 15개 순서대로, 검사기가 빠진 제목·순서 문제 없음 |
| 3-3 | 렌즈는 화각(도) + 관찰 결과 3개, mm 없음 | PASS | "Diagonal field of view about 47°. The girl and the timetable sign fill the right half of the frame / the end of the shelter sits at the left edge / the bench is out of frame." |
| 3-4 | 의상(girl)·LIGHT LOCK 글자 그대로, 소리 설정이 정본과 맞음 | PASS | `--must-include girl+light` 통과. "[AUDIO] No dialogue. GIRL does not say a single word … Distant wind over the paddies and the soft rustle of her raincoat … No music." |
| 3-5 | 검사 `--kind video --refs 2 --seconds 8 --must-include girl+light` FAIL·WARN 없음 | PASS | 아래: 걸린 항목 없음, 5007자 (임계가 5,500자로 올랐다: `check_prompt.py:32`) |
| G1 | mcp·생성 없음 | PASS | [TOOL] 없음. "생성은 하지 않았습니다" |
| G2 | 한국어, 본문 영어 | PASS | |
| G3 | 질문은 끝에 한 묶음 | PASS | 끝 "이 프롬프트로 480p 한 번 생성할까요?" 한 줄 |
| G4 | 필요한 스킬만 | PASS | 3턴에 새로 연 파일: `higgsfield-generation/SKILL.md`(검사), `acting/SKILL.md`(연기 블록 작성), `check_prompt.py`(사용법). 다른 컷 카드 없음 |
| G5 | 빈칸 없음 | PASS | |
| G6 | 코드블록 하나 + 블록 밖 | PASS | "모드: image-to-video (시작 이미지 포함 참조 2개 …) / 모델 · 해상도 · 길이 · 화면비 · 소리 / 저장 폴더 `fld-3-3` / 예상 비용" + 위험 → 막는 문장 8개를 프롬프트 앞에 |

## 검사기 결과
프롬프트: `out/turn3.md`의 코드블록 하나(`runs-sonnet2/C10/grade-tmp/p.txt`), 태그 2개(`ff_3-3_v1`, `char_girl_raincoat_v1`) = 블록 밖 참조 2개.
```
$ check_prompt.py --kind video --refs 2 --seconds 8 --must-include (girl.lines+light.lines) grade-tmp/p.txt
OK — video 프롬프트 5007자, 걸린 항목 없음
```

## 추가 발견
1. 컷 카드 [10] "알려진 위험"에 아직 난 적 없는 예상 위험("말 없는 인물의 입 움직임", "시간표 글씨가 읽힘")을 채웠고, 프롬프트 Forbidden에 `GIRL moving her lips (ENTIRE_SHOT)`을 넣었다. `cut-card.md:26`은 [10]을 "실제로 났던 실패"로 정의하고 `video-prompt/SKILL.md:82`는 "예상 위험은 Required나 해당 블록 문장으로 막는다"고 한다. 지난번 지적(S8)의 같은 문제가 남았다. 경미하다(AUDIO와 Required에도 같은 내용이 있음).
2. 컷 카드에 `연기:` 줄을 [6] 아래에 새로 만들었다(diff). 컷 카드 틀에 연기 범위 칸이 없다(K6).
3. 좋은 점: 3턴 끝 상태 제안값의 모순(반 걸음 대 걸음 없음)을 스스로 찾아 정정으로 밝혔다. 렌즈 관찰 결과는 "시작 이미지 프롬프트 기준 … 추정"으로 표기했다.
4. 프롬프트에 "3-1"·"previous shot"이 없고, 3-1 영상에서 가져온 줄은 "전 → 후" 목록으로 보였다.

## 키트 결함
| # | 분류 | 결함 | 근거 | 수정 제안 |
|---|---|---|---|---|
| K6 | 규칙이 없음 | 영상 정보 점검 표는 장소(화면 좌표)·연기 범위를 묻고 "답은 컷 카드 [4]~[6]에 적는다"고 하는데, 컷 카드 틀에는 그 둘을 적을 칸이 없다. 플레이어가 `연기:`(C10), `화면 좌표:`(C12) 줄을 즉석에서 만들었다 | `kit/skills/video-prompt/SKILL.md:25,34,68`, `kit/skills/production-session/cut-card.md:12-21` | `cut-card.md` [5]에 `연기: [인물별 목표 · 범위]`, [4]에 `화면 좌표: [좌 · 중 · 우 · 전경]` 줄을 더한다 |
| K7 | 읽기 지도 | 컷 세션 정본 목록과 "표에 없는 파일은 열지 않는다"에 `decisions.md`·`asset-registry.md`가 없다. 4번 규칙(기본값 `decisions.md`, 고정 설명문 대장)이 이 둘을 요구해 플레이어가 열 수밖에 없다(C08, C10, C12) | `kit/instructions.md:23,28`(필요) 대 `:58-59`(목록에 없음) | 58줄 컷 세션 정본에 "`decisions.md`의 해당 줄, `asset-registry.md`의 해당 에셋·고정 설명문"을 넣는다 |
| K8 | 모호함 | `ok-cuts.md`를 "절만" 열라고 하나 열 방법이 없어 C10은 파일 전체를 열었다 | `kit/skills/production-session/SKILL.md:69` | "`grep -n '^### ' project/ok-cuts.md`로 줄 번호를 찾고 그 구간만 읽는다"를 덧붙인다 |
| — | 기대 오류 | 시나리오 C10 2턴 기대("15블록 전문")가 키트의 현재 규칙(묻는다)과 어긋난다 | `scenarios.md` C10 2턴, `kit/instructions.md:26`, `kit/skills/video-prompt/SKILL.md:89` | 2턴 기대를 "망원 대 50mm 충돌을 묻고 A/B 제안을 낸다"로 고치고 3턴을 정규 기대로 한다 |

## 지난 소넷 대비
길이 WARN이 사라졌고(5233자 WARN → 5007자 통과, 임계 5,500) 질문·정정·검사까지 흠이 없다. 남은 것은 `ok-cuts.md` 전체 열기 하나뿐이다.
