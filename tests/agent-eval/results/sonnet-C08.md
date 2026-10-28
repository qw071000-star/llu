# C08 (소넷) — 퍼스트 프레임, 정보 부족 (3-4) · 채점

- 실행 폴더: `tests/agent-eval/runs-sonnet/C08` (turn1, turn2)
- 정본 변경: `project/cuts/3-4.md` 새로 만듦(2615자). 다른 정본 그대로
- 집계: **PASS 21 / 부분 3 / FAIL 1** (체인 판정: 부분)
- 비교: Opus 1차 25/1/0, Opus 2차(고친 키트)는 "감나무 쪽 절반"까지 해결. 소넷은 자리 제안에서 1차 Opus와 같은 실수를 했다.

## 턴별 판정표

### 턴 1 — `3-4 퍼스트 프레임 프롬프트 만들어.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1-1 | 컷 카드 없음 → 정본에서 만든다 | PASS | "컷 카드가 없어 정본에서 초안(v0)을 만들었습니다(`project/cuts/3-4.md`)" |
| 1-2 | `first-frame.md`를 연다 | PASS | 메타 `image-prompt/first-frame.md` |
| 1-3 | 모드를 정하는 질문(카메라가 LC-001-V1과 같은가) | PASS | "1. 모드·카메라: 제안 — 새 시점(DERIVED VIEW) … 이유: LC-001-V1은 길 건너편에서 본 원경이라 무릎 위 가방과 손이 보이지 않습니다" (사용자가 "똑같이"로 뒤집을 수 있게 열어 둠) |
| 1-4 | 카메라·렌즈 | PASS | "눈높이 약 1.5m, 북쪽을 보는 허리 위 미디엄, 35mm 렌즈, 삼각대 고정" |
| 1-5 | 할아버지 시작 위치·자세·동작·손·시선을 앞 컷 자리(벤치 감나무 쪽 절반)와 맞춘다 | **FAIL** | "2. 0:00 할아버지: 제안 — **벤치 가운데에 앉아** 무릎 위 닫힌 가방에 두 손을 얹고". 승인된 2-2·3-1·3-2 시작 이미지는 모두 "persimmon-tree half of the bench". 다른 승인 컷을 확인하지 않았다. 최종 프롬프트도 "sits at the centre of the wooden bench". 자세·손·시선 다섯 항목은 모두 물었다 |
| 1-6 | 가방 닫힘·인원 수는 정본 값으로 제시 | PASS | "연속성 표의 2-1·3-1과 같은 자세 … 가방은 0:00에 닫혀 있어야" · "3. 인원: 제안 — 할아버지 1명만" |
| 1-7 | 모델·해상도·저장 폴더는 묻지 않는다 | PASS | "이미 정해진 값은 묻지 않습니다: GPT Image 2.5 · 1k · 16:9 · 1장 · 저장 `fld-3-4` · 참조 3장 …" |
| G1 | mcp·생성 없음 | PASS | [TOOL] `list_folders`, `list_project_assets(fld-3-4)`뿐 |
| G2 | 한국어 짧게 | PASS | |
| G3 | 질문 끝 한 묶음, decisions 다시 묻지 않음 | 부분 | 질문 5 "룩 문장: 제안 — decisions §3의 `Live-action film look…`을 씁니다"는 질문 모양이지만 decisions에 이미 있는 값이다. 질문 4(화면 대응)는 2턴에 "카메라 똑같이"로 사라졌다 |
| G4 | 필요한 스킬·파일만 | 부분 | production-session(+cut-card.md), image-prompt(+first-frame.md)는 맞다. 퍼스트 프레임 턴에 `video-prompt/SKILL.md`(앞 60줄)·`higgsfield-generation/SKILL.md`도 열었다. `first-frame.md:5`가 video-prompt §0을 가리키므로 근거는 있으나 Opus는 열지 않았다. 2턴에 `check_prompt.py` 소스(앞 60줄)를 읽었다 |
| 시점 | turn1 정본 수정 | PASS | 컷 카드 v0만 만들었다 |

### 턴 2 — `카메라는 LC-001-V1이랑 똑같이. 나머지는 제안대로.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 2-1 | 틀 1 LOCKED EDIT, `WITHOUT reframing`, DERIVED와 섞이지 않음 | PASS | 첫 줄 "Edit <<<loc_busstop_road_v1>>> WITHOUT reframing: camera position … this is the same photograph with one change only." "달라진 점: … 새 시점(DERIVED VIEW) 대신 … LOCKED EDIT 틀을 씁니다" |
| 2-2 | 의상·가방·LIGHT LOCK 글자 그대로 | PASS | `--must-include grandpa+bag+light` 통과 |
| 2-3 | 화면 대응 문장(서 = 화면 왼쪽) | PASS | PRESERVE EXACTLY 안에 "In this view the west is screen LEFT." |
| 2-4 | `Exactly 1 person` | PASS | 마지막 줄 "Exactly 1 person is visible." |
| 2-5 | 자리표시 태그가 남지 않음 | PASS | `<<<loc_busstop_road_v1>>>`, `<<<char_grandpa_autumn_v1>>>`, `<<<prop_doctor_bag_v1>>>` 실제 이름 |
| 2-6 | 손은 물건 기준 | PASS | "Both hands rest on top of the closed bag, fingertips near the brass clasp". "right hand" 없음 |
| 2-7 | 컷 카드 [4], [5]에 값 기록 | PASS | 카드 v0.1: "[4] 카메라: LC-001-V1과 똑같이(사용자 답, 2026-10-28)", "(제안값)" 표시. 렌즈·끝 위치·타이밍 칸은 `[ ]`로 남았으나 퍼스트 프레임 작업이라 허용 |
| 2-8 | 검사 + 참조 수 = 태그 수 | PASS | 태그 3, 블록 밖 참조 3 (아래) |
| 충돌 | 고정 문장과 이 컷이 부딪치면 문장은 그대로 두고 바로 뒤 `Except:` 한 줄 (`image-prompt/SKILL.md:44`) | 부분 | 가방 고정 문장("hanging heavy from its handles")과 무릎 위 자세의 충돌을 알아채고 `Except: here the bag rests on his knees and does not hang from its handles.`를 썼다. 그런데 이 줄은 CHANGE 둘째 불릿("lid flat on top. Except: …") 안에 있고, 고정 문장이 있는 `PROP:` 줄 바로 뒤에는 없다. `PROP: … hanging heavy from its handles.`가 그대로 홀로 남았다. 총괄에 올릴 것에는 적었다 |
| G1 | mcp·생성 없음 | PASS | [TOOL] `get_project_asset_prompt(job=job-lc001v1)` 한 번(OK 카드가 있어 불필요했으나 무해). "아직 생성하지 않았습니다. 생성하려면 '생성해'" |
| G2·G3 | 한국어, 새 질문 없음 | PASS | |
| G5 | 빈칸 없음 | PASS | 검사기 통과 |
| G6 | 코드블록 하나 + 블록 밖 | PASS | "모드: … / 참조(붙이는 순서) … / 모델: GPT Image 2.5 · 해상도 1k(확인용) · 16:9 · 1장 / 저장 폴더: 「빈 정류장」/ 3-4, `fld-3-4`" |

## 검사기 결과
프롬프트: `out/turn2.md`의 코드블록 하나(`<<<>>>` 태그 3개).
```
$ check_prompt.py --kind image --refs 3 --must-include (grandpa.lines+bag.lines+light.lines) c08.txt
OK — image 프롬프트 2326자, 걸린 항목 없음
```

## 추가 발견
1. 자리 불일치(1-5)가 컷 카드 [5]에 "벤치 가운데 … (제안값)"으로 기록되어 3-4 영상 프롬프트로 이어질 위험이 있다. 사용자가 "나머지는 제안대로"라고 해서 그대로 확정됐다.
2. 총평에 쓸 만한 좋은 점: 와이드라 가방이 작게 나올 위험을 "주의 하나"로 짚었고, 가방 충돌을 총괄에 올릴 것으로 적었다.
3. 카드 `[12] 확정 프롬프트: 없음`, `[11]`에 "퍼스트 프레임 프롬프트만 작성, 생성 안 함"을 적어 두었다(허용).

## 키트 결함
| # | 결함 | 근거 | 수정 제안 |
|---|---|---|---|
| S4 | 인물 자리를 정본에서 못 찾을 때 대체 출처가 없다. 이웃 컷 비교는 "연속성 표"를 가리키는데 시험 데이터 표에는 자리 열이 없고, 다른 컷 카드는 읽지 말라고 한다. 소넷은 "가운데"를 지어냈고 Opus 2차는 "3-1 OK 카드의 위치 블록"을 제안했다 | `kit/skills/image-prompt/first-frame.md:14, 32`, `kit/instructions.md:21` | first-frame.md:32 뒤에 "연속성 표에 자리가 없으면 같은 인물·같은 장소의 가장 가까운 승인 시작 이미지 OK 카드에서 BLOCKING 줄을 가져와 제안한다. 지어내지 않는다"를 넣는다 |
| S5 | `Except:` 줄을 넣을 자리가 틀에 없다. 소넷은 CHANGE 불릿 안에 넣었다 | `kit/skills/image-prompt/first-frame.md:52, 73`(PROP 줄), `kit/skills/image-prompt/SKILL.md:44` | 두 틀의 `PROP:` 줄 끝에 `[Except: …]` 슬롯을 보이고, "고정 문장 바로 뒤"를 틀 안에서 보이게 한다 |
| S6 | 퍼스트 프레임 작업이 `video-prompt` §0을 열게 만든다 | `kit/skills/image-prompt/first-frame.md:5` | "영상 점검표와 같은 값"이라는 말만 두고 "video-prompt를 열 필요는 없다"를 덧붙인다 |

## 총평
정보 점검·틀 1 전환·고정 문장·태그·손 표현·검사까지 맞았지만, 승인 컷과 다른 "벤치 가운데"를 제안한 것과 Except 줄 위치가 소넷에서 다시 나왔다. 둘 다 키트의 출처·슬롯 빈틈이다.
