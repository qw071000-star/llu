# C14 (소넷, 정리된 키트) — "표정은 2-1처럼, 2-2 영상" · 채점

- 실행 폴더: `tests/agent-eval/runs-sonnet2/C14` (turn1 질문, turn2 `그대로.` 뒤 전문)
- 정본 변경: `project/cuts/2-2.md` 새로 만듦(v0 → v1). 다른 정본 그대로
- 집계: **PASS 17 / 부분 0 / FAIL 0** (체인 판정: PASS)
- 지난 소넷 대비: 14/1/1 → 17/0/0. 지난 FAIL 둘이 모두 사라졌다. (1) `cuts/3-1.md`를 형식 참고로 연 일 없음: 연 파일은 `production-session/SKILL.md`, `ok-reuse.md`, `cut-card.md`, `video-prompt/SKILL.md`, `live-action.md`, `higgsfield-generation/SKILL.md`, 정본 4개, `ok-cuts.md`(목록, 2-1 영상, 2-2 시작 이미지 카드). (2) 이미지 묘사를 사용자에게 묻는 대신 "추정: … 이미지를 볼 수 없어 승인 프롬프트로 짐작"으로 표시.

## 턴별 판정표

### 턴 1 — `2-2 영상 프롬프트 만들어. 할아버지 표정은 2-1처럼 유지해.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1-1 | `ok-reuse.md`와 2-1 **영상** 카드를 연다 | PASS | 메타: `ok-cuts.md (목록, 2-1 영상 카드, 2-2 시작 이미지 카드)`. "2-1 영상 카드를 열어 표정 줄을 확인했습니다" |
| 1-2 | `CHARACTER_ACTING` 할아버지 줄을 글자 그대로 | PASS | turn2 `[CHARACTER_ACTING]`이 "GRANDPA: waits without hoping. … slow, heavy blinks." 원문과 같고 `--must-include acting_2-1` 통과 |
| 1-3 | 시작 이미지는 2-2 카드. 빈 칸(쓰다듬기 타이밍, 길이, 카메라·렌즈)을 묻거나 제안 | PASS | "1. 쓰다듬기 … 0:00–0:03 … 0:03–0:08", "4. 85mm 관찰 결과 3개". 길이·카메라는 "기본값으로 씀: 8초 · 16:9 · 고정 카메라 · Seedance 2.5 480p · 효과음만 · 렌즈 85mm = 약 29° (시작 이미지 기준)" |
| 1-4 | 2-1의 카메라·동작은 가져오지 않는다(요청은 표정) | PASS | "카메라와 렌즈는 2-1(63°)이 아니라 2-2 시작 이미지를 따릅니다. 표정만 2-1에서 옵니다", 환경(낙엽)도 뺌 |
| G1 | mcp·생성 없음 | PASS | [TOOL] `list_folders`, `list_project_assets(fld-2-2)`만 |
| G2 | 한국어 | PASS | |
| G3 | 정본에 있는 것을 다시 묻지 않고, 사용자에게 이미지 묘사를 부탁하지 않는다 | PASS | 질문 5개 모두 제안값 포함. "추정: 시작 이미지 속 얼굴이 … 이미지를 볼 수 없어 승인 프롬프트(`calm and heavy-lidded`)로 짐작" (`instructions.md:32`대로) |
| G4 | 필요한 스킬·파일만. 다른 컷 카드 안 연다 | PASS | 메타에 `cuts/*`, `log/*` 없음(만든 `cuts/2-2.md`만) |
| 시점 | 카드가 없으면 정본에서 v0 | PASS | `project/cuts/2-2.md` v0 |

### 턴 2 — `그대로.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 2-1 | 검사 FAIL·WARN 없음 | PASS | 아래 |
| 2-2 | 참조 수 = 태그 수 | PASS | 태그 `ff_2-2_v1`, `char_grandpa_autumn_v1`, `prop_doctor_bag_v1` 3개 = 블록 밖 "참조(붙일 순서) 1·2·3" |
| 2-3 | 2-1의 입 움직임 금지 줄도 옮김 | PASS | AUDIO "no attempt to speak, no lip movement" + Forbidden "GRANDPA moving his lips (ENTIRE_SHOT)" |
| 2-4 | 카드에 기록, `(제안값)` 표시, [7] 가져온 OK | PASS | 카드 [7] "가져온 OK: 2-1 영상 — 표정(CHARACTER_ACTING 할아버지 줄, 깜빡임·시선 문장, Forbidden의 입술)", [4][5][6]에 `(제안값)` |
| G1 | 생성하지 않음 | PASS | "생성하려면 '생성해'라고 지시해 주세요", [TOOL] 없음 |
| G2 | 한국어, 본문 영어 | PASS | |
| G5 | 빈칸 없음 | PASS | |
| G6 | 코드블록 하나 + 블록 밖 | PASS | 모드·참조(순서)·모델·해상도·길이·소리·저장 폴더, "전 → 후" 목록 |

## 검사기 결과
```
$ check_prompt.py --kind video --refs 3 --seconds 8 --must-include (grandpa+bag+light+acting_2-1).lines grade-tmp/p.txt
OK — video 프롬프트 4596자, 걸린 항목 없음
```

## 추가 발견
1. 시작 이미지의 요소 이름을 대장에서 찾지 못해 2-1 카드의 패턴을 따라 `ff_2-2_v1`로 썼고, "붙일 때 실제 이름과 다르면 알려 주세요"를 적었다. 카드 [7]에도 "요소 이름 미확인". 정직한 처리다. 아래 D2.
2. `CHARACTER_ACTING`에 원문 줄 뒤 "His eyes never drop to the bag."를 더하고 "전 → 후"에서 알렸다. 원문 줄 자체는 그대로.
3. 시험 데이터 한계: 가방 "hanging heavy".

## 키트 결함
| # | 분류 | 결함 | 근거 | 수정 제안 |
|---|---|---|---|---|
| D2 | 규칙이 없음 | 영상 프롬프트의 시작 이미지 태그 이름(`ff_컷번호_v1`)을 어디서 얻는지 규칙이 없다. OK 대장의 "시작 이미지" 카드는 그 이미지를 만들 때 붙인 참조만 적고 이미지 자신의 요소 이름은 없다 | `video-prompt/SKILL.md:27`(시작 이미지 = "퍼스트 프레임 job"), `video-prompt/live-action.md:12`, `ok-cuts.md`의 "2-2 시작 이미지" 카드 | OK 카드 틀과 `video-prompt` §0에 "시작 이미지는 영상에서 `ff_[컷]_v1`로 붙인다. 이름이 대장에 없으면 이 규칙대로 쓰고 블록 밖에 알린다"를 둔다 |
| D5 | 읽기 지도(경미) | 프롬프트만 쓰는 턴에 `higgsfield-generation/SKILL.md`를 열었다(검사 스크립트 위치). 읽기 지도 행에는 검사가 없다 | `instructions.md:51`, `video-prompt/SKILL.md:110` | C13의 D5와 같다 |
| D3 | 모호함(경미) | 질문 위치 세 규칙 | `instructions.md:24`, `:32`, `:42` | C13의 D3과 같다 |

## 총평
2-1 표정 줄을 글자 그대로 옮기고 카메라·동작은 가져오지 않았으며 검사도 통과. 지난번의 두 FAIL(3-1 카드 열기, 사용자에게 이미지 묘사 부탁)이 `instructions.md:32`·`:59`의 한 줄씩으로 해소됐다.
