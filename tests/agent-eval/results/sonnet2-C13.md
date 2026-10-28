# C13 (소넷, 정리된 키트) — "3-1의 색감과 질감으로 3-5 퍼스트 프레임" · 채점

- 실행 폴더: `tests/agent-eval/runs-sonnet2/C13` (turn1 질문, turn2 `그대로.` 뒤 전문). 키트 사본: `.claude/instructions.md`, `.claude/skills/`, `CLAUDE.md`
- 정본 변경: `project/cuts/3-5.md` 새로 만듦(v0 → v1). 다른 정본 그대로
- 집계: **PASS 18 / 부분 1 / FAIL 0** (체인 판정: PASS, 카드 기록 한 군데 부분)
- 지난 소넷 대비: 16/0/1 → 18/1/0. 지난 FAIL(다른 컷 카드 3장·핸드오프 2건·OK 카드 여러 장 열기)이 사라졌다. 연 파일: `production-session/SKILL.md`, `ok-reuse.md`, `cut-card.md`, `image-prompt/SKILL.md`, `first-frame.md`, `higgsfield-generation/SKILL.md`, 정본 5개(shot-list, decisions, asset-registry, ok-cuts의 목록+3-1 시작 이미지 카드 하나), sim. `cuts/3-1~3-3`, 핸드오프, 다른 OK 카드는 열지 않았다.

## 턴별 판정표

### 턴 1 — `3-5 퍼스트 프레임 프롬프트 만들어. 색감이랑 질감은 3-1처럼.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1-1 | `ok-reuse.md`와 3-1 **시작 이미지** 카드를 연다 | PASS | 메타: `production-session/ok-reuse.md`, `project/ok-cuts.md(목록 + 3-1 시작 이미지 카드)`. "3-1 시작 이미지 OK(`job-ff-3-1`, OK 이유 "색감, 질감")에서 색감·질감만 가져오는 것으로 봤습니다" |
| 1-2 | 색·질감 문장이 없음을 알아채고, 3-1 이미지를 색 전용 참조로 붙인다. 문장을 지어내지 않는다 | PASS | "프롬프트에 색·질감 문장이 없습니다. 문장을 지어내지 않고 그 이미지를 색 참조로 붙입니다" |
| 1-3 | 3-5 정보(카메라, 손·가방 상태 — 열림)를 묻거나 제안 | PASS | "1. 카메라 … 85mm", "2. 손의 0:00 상태", "3. 가방 속", "4. 3-4와의 이음 … 가방 열림", "5. 얼굴과 인원" |
| G1 | mcp·생성 없음 | PASS | [TOOL] `list_folders`, `list_project_assets(fld-3-5)`만 |
| G2 | 한국어 | PASS | |
| G3 | 질문 한 묶음, 정본에 있는 것은 안 묻는다 | PASS | "이미 정해져 있어 묻지 않은 것: GPT Image 2.5 · 1k · 16:9 · 1장, 저장 `fld-3-5` …". 질문 5개가 한 묶음 |
| G4 | 자기 컷 카드·앞뒤 줄·기준 OK 카드 하나만. 다른 컷 카드·핸드오프 안 연다 | PASS | 메타에 `cuts/3-1~3-3`, `log/*` 없음. 이번에 만든 `cuts/3-5.md`만. OK 카드는 3-1 시작 이미지 하나 |
| 시점 | 카드가 없으면 정본에서 v0 | PASS | `project/cuts/3-5.md` v0 |

### 턴 2 — `그대로.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 2-1 | 참조 수 = 태그 수 | PASS | 태그 `<<<image_1>>>`~`<<<image_4>>>` 4개 = 블록 밖 "참조(붙이는 순서) image_1~image_4" |
| 2-2 | 가방·LIGHT LOCK(보이면 의상) 글자 그대로 | PASS | `--must-include bag+light+grandpa` 통과 |
| 2-3 | 색 참조 권한을 좁힌 문장 | PASS | "`<<<image_4>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.`" + "DO NOT TRANSFER … From <<<image_4>>>: the girl, the bench, the timetable sign, its framing" |
| 2-4 | 검사 FAIL 없음 | PASS | 아래 |
| 2-5 | 3-4 이후라 가방 열림 | PASS | "`Except: the bag is OPEN here, its brass clasp undone … Ignore the closed state in <<<image_3>>>.`" |
| G1 | 생성하지 않음 | PASS | "보내지는 않았습니다", [TOOL] 없음 |
| G2 | 한국어 | PASS | |
| G3 | 질문 한 묶음 | PASS | 끝 "확인 사항 한 묶음" 2개 |
| G5 | 빈칸 없음 | PASS | |
| G6 | 코드블록 하나 + 블록 밖 | PASS | 모드·참조(순서·역할)·모델·해상도·화면비·길이 "해당 없음"·저장 폴더. 위험 → 막는 문장 6개를 블록 앞에 보임 |
| 기록 | 답을 컷 카드에 적고, 정하지 않은 값은 `(제안값)` | 부분 | 카드 v1은 [4][6][7][10]을 채우고 `(제안값)`을 달았으나 [5] "시작(0:00): (미정 — 사용자 답 대기) / 끝: (미정)"이 그대로다. 턴 1의 제안 2(손의 0:00 상태)를 받아들여 프롬프트 BLOCKING에 썼는데 카드 [5]에는 안 적었다. 카드 머리의 "(제안값)은 제안을 받아들인 것"과 모순 |

## 검사기 결과
```
$ check_prompt.py --kind image --refs 4 --must-include (bag+light+grandpa).lines grade-tmp/p.txt
OK — image 프롬프트 2598자, 걸린 항목 없음
```
(태그 `<<<image_1>>>`~`<<<image_4>>>` 4종. 답의 코드블록과 `tmp/3-5_ff.txt`는 같은 글.)

## 추가 발견
1. 카드 [5] 시작 칸이 "미정"으로 남음(위 기록 행). `instructions.md:27`("답은 컷 카드에 적는다") 위반. 작지만 다음 세션(영상 단계)이 같은 값을 못 이어받는다.
2. 틀 2의 `[PALETTE · ERA LOCK …]` 줄(`first-frame.md:76`)이 프롬프트에 없다. 시험 폴더의 `asset-registry.md`에 ERA LOCK 칸이 없기 때문(키트 `project-files/asset-registry.md:54`에는 있음). 시험 데이터 한계. `Nothing else` 줄은 틀대로 "no-people 항목 없이" 썼다.
3. 좋았던 점: 색 기준 OK가 장소 뷰 그대로가 아니고 3-5가 다른 뷰라서 `first-frame.md:36-37`대로 틀 2 + 색 참조를 골랐다. 빛 방향이 뒤집힐 위험과 구도 위험을 막는 문장으로 올렸다. 새 뷰 등록은 총괄 일로 핸드오프 [5]에 적겠다고 했다(`production-session/SKILL.md:25`).
4. 시험 데이터 한계(키트 탓 아님): 가방 문장 "hanging heavy".

## 키트 결함
| # | 분류 | 결함 | 근거 | 수정 제안 |
|---|---|---|---|---|
| — | — | 이 체인의 플레이어 오류 중 키트 문서 탓은 없음. 지난번 S11·S1·S12(이웃 컷 읽기)는 `instructions.md:57-59`의 "열지 않는다 … (형식 예시로도)"와 `ok-reuse.md:9`의 "그 카드의 프롬프트만 연다"로 해결됐다 | | |
| D5 | 읽기 지도(경미) | 프롬프트만 쓰는 턴인데 `higgsfield-generation/SKILL.md`를 열었다. 검사 스크립트가 거기 있는데 읽기 지도 행은 "생성, 결과 확인, 폴더, 판정, OK 기록"뿐이다. (`image-prompt/SKILL.md:113`이 가리켜서 찾을 수는 있고 해가 없었다) | `.claude/instructions.md:51`(C13 사본은 `:51`), `image-prompt/SKILL.md:113` | 읽기 지도 행에 "(+ 프롬프트 검사 실행)"을 넣거나, 검사 절차를 `image-prompt`·`video-prompt`에 두 줄로 옮긴다 |
| D3 | 모호함(경미) | 질문의 위치가 세 곳에서 다르다: "첫 줄: 프롬프트를 쓰기 전에 확인할 것이 N개" / "시작 보고는 세 줄 … 질문은 그 뒤" / "질문은 답 끝에 한 묶음". 이번엔 시작 보고 → 첫 줄 문구 → 항목 → "이미 정해져 있어 묻지 않은 것" 순으로 써 문제는 없었다 | `instructions.md:24`, `:32`, `:42` | "첫 줄"을 "질문 묶음의 첫 줄"로 바꿔 시작 보고 뒤에 오는 것을 분명히 한다 |

## 총평
지난번 유일한 FAIL(이웃 컷 카드·핸드오프 열기)이 읽기 지도 정리로 사라졌고, 색 참조 + 권한 좁히기 + 가방 열림 처리까지 검사 통과. 남은 흠은 컷 카드 [5]에 받아들인 제안을 안 적은 것 하나.
