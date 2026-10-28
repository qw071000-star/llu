# C14 (소넷) — "표정은 2-1처럼, 2-2 영상" · 채점

- 실행 폴더: `tests/agent-eval/runs-sonnet/C14` (turn1: 질문, turn2: `그대로.` 뒤 전문)
- 정본 변경: `project/cuts/2-2.md` 새로 만듦(v0 → v1, `제안값` 표시). 다른 정본 그대로
- 집계: **PASS 14 / 부분 1 / FAIL 1** (체인 판정: 부분)
- 비교: Opus 1차 8/1/0 (G4 PASS). 소넷은 프롬프트(검사 통과, 2-1 줄 글자 그대로)는 같고 `cuts/3-1.md`를 열었다.

## 턴별 판정표

### 턴 1 — `2-2 영상 프롬프트 만들어. 할아버지 표정은 2-1처럼 유지해.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1-1 | `ok-reuse.md`, 2-1 **영상** 카드를 연다 | PASS | 메타: `production-session/ok-reuse.md`, `ok-cuts.md(목록과 2-1 영상·2-2 시작 이미지 카드 절만)`. "2-1에서 가져오는 것: 표정만 (2-1 영상 카드의 `CHARACTER_ACTING` 할아버지 줄, 글자 그대로)" |
| 1-2 | `CHARACTER_ACTING` 할아버지 줄을 글자 그대로(`acting_2-1.lines`) | PASS | turn1 코드블록과 turn2 `[CHARACTER_ACTING]`이 모두 "GRANDPA: waits without hoping. Between stillness and quiet resignation; a sigh or a frown = …" 원문 그대로. `--must-include acting_2-1` 통과 |
| 1-3 | 시작 이미지는 2-2 카드(`job-ff-2-2`), 빈 칸(쓰다듬는 타이밍, 길이, 카메라·렌즈)을 묻거나 제안 | PASS | "1. 쓰다듬는 동작과 타이밍: 제안 — 0:00–0:03 … 0:03–0:06 … 0:06–0:08 …", "2. 끝 상태", "4. 렌즈 관찰 결과 … (85mm = 29°)". 길이·카메라는 "기본값으로 씀: 8초 · 고정 카메라 · 480p …" |
| 1-4 | 2-1의 카메라·동작은 가져오지 않는다(요청은 표정만) | PASS | "가져오지 않는 것: 2-1의 카메라·렌즈·위치 문장 … 2-1의 동작(엄지 한 번)도 가져오지 않습니다. 이 컷은 쓰다듬기입니다" |
| G1 | mcp·생성 없음 | PASS | [TOOL] `list_folders`, `list_project_assets(fld-2-2)` |
| G2 | 한국어 | PASS | |
| G3 | 정본에 있는 것을 다시 묻지 않는다 | 부분 | "3. 화면 속 배경: 제가 ff-2-2 이미지를 눈으로 확인하지 못했습니다. 그의 뒤와 좌우로 보이는 것(콘크리트 벽? 벤치? …)을 알려 주세요." 2-2 시작 이미지 카드의 프롬프트에 "back against the shelter wall", "persimmon-tree half of the bench"가 이미 있어 물을 필요가 없었다. 키트는 이미지를 볼 수 없을 때를 정하지 않았다(S10) |
| G4 | 필요한 스킬·파일만, 다른 컷 카드를 열지 않는다 | **FAIL** | 메타 끝: "project/cuts/3-1.md(형식 참고용으로 앞부분만, **규칙상 읽지 않았어야 할 다른 컷 카드**)". 플레이어 스스로 위반을 적었다. `production-session/cut-card.md`는 이미 열었다 |
| 시점 | 컷 카드 없음 → 정본에서 만든다 | PASS | `project/cuts/2-2.md` v0 |

### 턴 2 — `그대로.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 2-1 | 검사 `--kind video --refs 3 --must-include grandpa+bag+light+acting_2-1` FAIL·WARN 없음 | PASS | 아래: `OK — video 프롬프트 4473자, 걸린 항목 없음` |
| 2-2 | 참조 수 = 태그 수 | PASS | 태그 `ff_2-2_v1`, `char_grandpa_autumn_v1`, `prop_doctor_bag_v1` = 블록 밖 "참조(붙일 순서) 1·2·3" |
| 2-3 | 입 움직임 금지 줄도 옮김(2-1 Forbidden) | PASS | AUDIO "no attempt to speak, no lip movement" + Forbidden "GRANDPA moving his lips (ENTIRE_SHOT)" |
| 2-4 | 카드에 기록, `제안값` 표시 | PASS | 카드 v1: "(제안값)" 표시, [7] "가져온 OK: 2-1 영상 — 표정(CHARACTER_ACTING의 GRANDPA 줄, 입 움직임 금지 줄). 카메라·렌즈·동작은 가져오지 않음" |
| G1 | 생성하지 않음 | PASS | "생성은 하지 않았습니다. 보내라고 하시면 보냅니다" |
| G5 | 빈칸 없음 | PASS | |
| G6 | 코드블록 하나 + 블록 밖 | PASS | 모드·참조·모델·해상도(480p)·길이·소리·저장 폴더·"표정 가져온 OK" |

## 검사기 결과
```
$ check_prompt.py --kind video --refs 3 --seconds 8 --must-include (grandpa+bag+light+acting_2-1) c14.txt
OK — video 프롬프트 4473자, 걸린 항목 없음
```

## 추가 발견
1. 질문 3에서 정본에 없는 "배경"을 사용자에게 묻고, 답이 없는 상태(그대로)에서 "시작 이미지와 다르면 알려 주세요"로 추정 표시를 남겼다. 추정 표시는 `instructions.md:31`대로 좋다.
2. `LOCATION_MAP`에 "LEFT EDGE: the tree side of the shelter"를 썼다. 시작 이미지 카드에 근거(왼쪽 서쪽·감나무 쪽)가 있어 허용된다.
3. 가방 고정 문장("hanging heavy …")과 무릎 위 자세는 시험 데이터 한계(OK 카드의 2-1·2-2 문장과 같음).

## 키트 결함
| # | 결함 | 근거 | 수정 제안 |
|---|---|---|---|
| S12 | 컷 카드 형식 예시를 다른 컷 카드에서 찾게 된다. `cut-card.md`는 빈 `[ ]` 틀뿐이고 채운 예시가 없다. 소넷이 "형식 참고용"으로 `cuts/3-1.md`를 열었다 | `kit/skills/production-session/cut-card.md:22-46`, `kit/instructions.md:72` | cut-card.md 머리말에 "형식은 이 파일에 있다. 다른 컷의 카드를 예시로 열지 않는다"를 넣고, 채운 한 줄 예(`[4] 카메라: 길 건너편, 벤치 가운데 맞은편 · …`)를 둔다 |
| S10 | 모델이 이미지를 볼 수 없을 때의 규칙이 없다. C10은 "추정"으로 표시하고 C14는 사용자에게 묘사를 요청했다 | `kit/instructions.md:31`, `kit/skills/video-prompt/SKILL.md:65-69` | "시작 이미지는 OK 카드의 프롬프트를 그 이미지의 설명으로 쓰고 '추정'으로 표시한다. 사용자에게 묘사를 묻지 않는다"를 video-prompt §0 "그래도 빈 칸이면" 앞에 넣는다 |

## 총평
2-1 표정 줄을 글자 그대로 옮기고 카메라·동작은 가져오지 않았으며 검사도 통과했다. 형식 참고로 3-1 컷 카드를 연 것(스스로 밝힘)과 사용자에게 이미지 묘사를 부탁한 것이 어긋났다.
