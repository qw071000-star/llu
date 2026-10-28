# C08 (소넷, 정리된 키트) — 퍼스트 프레임, 정보 부족 (3-4) · 채점

- 실행 폴더: `tests/agent-eval/runs-sonnet2/C08` (turn1, turn2). 정본 변경: `project/cuts/3-4.md` 새로 만듦(v1). 나머지 그대로(`git status`: `?? project/cuts/3-4.md`, `?? out/`, `?? tmp/`)
- 집계: **PASS 22 / 부분 4 / FAIL 0** (체인 판정: 부분 → 사실상 PASS에 가까움)
- 지난 소넷(정리 전): 21 / 3 / 1.

## 턴별 판정표

### 턴 1 — `3-4 퍼스트 프레임 프롬프트 만들어.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1-1 | 컷 카드 없음 → 정본(컷 목록·연속성 표)에서 만든다 | PASS | "3-4 컷 카드가 없어서 정본으로 초안(v0)을 `project/cuts/3-4.md`에 만들었습니다" |
| 1-2 | `first-frame.md`를 연다 | PASS | 메타: `image-prompt/SKILL.md`, `image-prompt/first-frame.md` |
| 1-3 | 모드를 정하는 질문(카메라가 LC-001-V1과 같은가) | PASS | "1. 카메라와 모드: 제안 — 새 시점(DERIVED VIEW) … 확정 뷰 LC-001-V1은 정류장 전체를 보는 35mm라 가방 여는 손이 작게 나옵니다". 사용자가 뒤집을 수 있게 열어 둠 |
| 1-4 | 카메라·렌즈 | PASS | "길 건너편, 벤치 감나무 쪽 절반 맞은편, 앉은 눈높이, 50mm 미디엄 샷" |
| 1-5 | 할아버지 시작 위치·자세·동작·손·시선을 앞 컷 자리(벤치 감나무 쪽 절반)와 맞춘다 | PASS | "2. … 벤치 감나무 쪽 절반, 등을 정류장 벽에 기댐 (이유: 연속성 표의 3-4 인물 자리가 '미정'이라 … 직전 승인 시작 이미지인 3-2 카드의 BLOCKING을 가져왔습니다)". 시선(3)·손(4)도 물음. 지난번 FAIL("벤치 가운데")이 `first-frame.md:34`로 해결됨 |
| 1-6 | 가방 닫힘·인원은 정본 값으로 제시 | PASS | "가방은 닫힘(걸쇠 잠김, 컷 목록에 확정)", "할아버지 1명 … (이유: 컷 목록의 3-4 인물이 CH-001과 PR-001뿐)" |
| 1-7 | 모델·해상도·저장 폴더(`fld-3-4`)는 묻지 않는다 | PASS | "정본에 이미 있어서 묻지 않은 것: GPT Image 2.5 · 1k · 16:9 …, 저장 폴더 `fld-3-4`, 참조 3장 …" |
| G1 | mcp·생성 없음 | PASS | [TOOL] `list_folders`, `list_project_assets(fld-3-4)` |
| G2 | 한국어 짧게 | PASS | |
| G3 | 질문 한 묶음, 정본에 있는 것을 다시 묻지 않는다 | 부분 | 한 묶음 5개로 형식은 맞다. 다만 4번(가방 닫힘)과 5번(1명)은 정본 값인데 번호 질문으로 올렸다("정본에 있으면 묻지 않고 제시해도 된다"는 허용이라 경미) |
| G4 | 필요한 스킬만, 스킬 안에서는 SKILL.md와 단계 파일 하나 | PASS | 열린 스킬: `production-session`(SKILL.md + `cut-card.md`: 카드를 새로 쓰므로 읽기 지도 2행), `image-prompt`(+`first-frame.md`). `video-prompt`는 열지 않음(지난번 FAIL 해결). `ok-cuts.md`는 목록 + 3-2·3-3 절 |
| 정본 | turn1 정본 수정 | PASS | 카드 v0만 만들었다. 프롬프트는 아직 보이지 않음(G5 해당 없음) |

### 턴 2 — `카메라는 LC-001-V1이랑 똑같이. 나머지는 제안대로.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 2-1 | 틀 1(LOCKED EDIT), `WITHOUT reframing`, DERIVED와 섞이지 않는다 | PASS | 첫 줄 `Edit <<<loc_busstop_road_v1>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and perspective are LOCKED …`. "새 시점이 아니라 그 뷰를 잠그고 … LOCKED EDIT으로 바뀝니다" |
| 2-2 | 의상·가방·LIGHT LOCK 글자 그대로 | PASS | `--must-include grandpa+bag+light` 통과(아래) |
| 2-3 | 화면 대응 문장(서 = 화면 왼쪽) | PASS | PRESERVE EXACTLY 안에 "In this view the west is screen LEFT." (단, 대장 문장 그대로는 아님: 추가 발견 1) |
| 2-4 | `Exactly 1 person` | PASS | 마지막 줄 "Exactly 1 person is visible." |
| 2-5 | 자리표시 태그가 남지 않는다 | PASS | `<<<loc_busstop_road_v1>>>`, `<<<char_grandpa_autumn_v1>>>`, `<<<prop_doctor_bag_v1>>>`만 있음 |
| 2-6 | 손은 물건 기준 | PASS | "both hands resting on the bag on his lap". "right hand" 없음 |
| 2-7 | 컷 카드 3-4 [4], [5]에 값 기록 | PASS | 카드 v1: "[4] 카메라: LC-001-V1과 같음 (사용자 2026-10-28) … 렌즈: 35mm = 대각 화각 63°", "[5] 시작(0:00): 벤치 감나무 쪽 절반 … 걸쇠는 두 손 사이에 보임 (사용자 확정 …)" |
| 2-8 | 검사 + 참조 수 = 태그 수 | PASS | 태그 3 = 블록 밖 참조 3. 검사 통과(아래). 보이기 전에 돌림("자동 검사: 통과 (1997자 …)") |
| 충돌 | 고정 문장과 부딪치면 문장은 그대로, 바로 뒤에 `Except:` 한 줄 | 부분 | 위험 3번에서 "고정 문장에 'hanging heavy from its handles'가 있음"을 알아챘고 CHANGE 불릿에 "lies across the man's thighs"를 썼다. 그러나 `PROP: … hanging heavy from its handles.` 뒤에 `Except:` 줄이 없다(틀 1에 자리가 없음: 키트 결함 K2). 시험 데이터 한계(가방 문장)라 감점은 부분으로 제한 |
| G1 | mcp·생성 없음 | PASS | [TOOL] 없음. "아직 생성하지 않았습니다" |
| G3 | 새 질문 없음 | PASS | 끝에 "이 프롬프트로 만들까요?" 한 줄 |
| G5 | 빈칸 없음 | PASS | 검사기 통과 |
| G6 | 코드블록 하나 + 블록 밖 | PASS | 모드 · 참조(붙이는 순서 1~3) · 모델 · 해상도·비율 · 길이 · 저장 폴더 · 자동 검사 |
| 위험 | 생성 전 위험 → 막는 문장 | PASS | 위험 7개와 막는 문장, 7번은 "막는 문장이 없다"고 밝힘, 추정 표기 |
| G4 | 필요한 스킬·파일만 | 부분 | `higgsfield-generation/SKILL.md`(검사용, 정당), `ok-reuse.md`("LC-001-V1이랑 똑같이" → 읽기 지도 3행, 정당). 그러나 OK 카드를 LC-001-V1 + 3-1 시작 이미지 두 장 열었고(`instructions.md:58` "기준 OK 카드 하나"), `check_prompt.py` 소스를 열어 사용법을 읽었다(키트 결함 K5) |

## 검사기 결과
프롬프트: `out/turn2.md`의 코드블록 하나(`runs-sonnet2/C08/grade-tmp/p.txt`), 태그 3개.
```
$ check_prompt.py --kind image --refs 3 --must-include (grandpa.lines+bag.lines+light.lines) grade-tmp/p.txt
OK — image 프롬프트 1997자, 걸린 항목 없음
```

## 추가 발견
1. 화면 대응 문장이 대장 문장 그대로가 아니다. 대장은 `In this view the west, the persimmon-tree side, is screen LEFT.`(`asset-registry.md:91`)인데 프롬프트는 `In this view the west is screen LEFT.`를 썼다. `first-frame.md:55`가 대장 문장 verbatim을 요구한다. 플레이어는 OK 카드(`ok-cuts.md:240, 273`)의 짧은 문장을 따랐다. 시험 데이터에서 대장과 OK 카드 문장이 다른 것도 원인이다(키트 결함 K3).
2. 틀 1에는 `PROP:` 줄이 없는데(`first-frame.md:39-58`) 플레이어가 `PROP:` 줄을 따로 만들어 가방 고정 문장을 넣었다. 검사기(`bag.lines`)는 통과한다.
3. 컷 카드의 값을 "(사용자 확정)"으로 적고 `(제안값)`은 소리 칸에만 남겼다. 사용자는 "나머지는 제안대로"라고만 했다. `instructions.md:27`은 "사용자가 정하지 않은 값은 … (제안값)"이라 이 경우에 붙이는지 불명확하다(K4). 지난 소넷 채점은 이를 PASS로 보았다.
4. 좋은 점: 인물 자리 출처를 밝혔고(3-2 카드 BLOCKING) 카드 [10]에 3-2 폐기 job의 실패를 `asset-registry.md:113`에서 가져왔다(다른 컷 카드를 열지 않음).
5. 좋은 점: 와이드(35mm)라 걸쇠·시선이 작게 나올 위험을 "막는 문장 없음, 추정"으로 정직하게 보고했다.

## 키트 결함
| # | 분류 | 결함 | 근거 | 수정 제안 |
|---|---|---|---|---|
| K2 | 규칙이 없음 | 틀 1(LOCKED EDIT)에 소품 고정 문장 줄(`PROP:`)과 `[Except: …]` 자리가 없다. 규칙·표에는 `Except`가 있는데 틀 2에만 슬롯이 있다. 고정 문장과 컷이 부딪쳐도 틀 1에서는 둘 곳이 없어 `Except` 줄이 빠졌다 | `kit/skills/image-prompt/first-frame.md:17`(표), `:39-58`(틀 1, 슬롯 없음), `:75`(틀 2의 `[Except: …]`), `kit/skills/image-prompt/SKILL.md:27` | 틀 1의 `WARDROBE:` 줄 아래에 `PROP: [asset registry sentence, verbatim]. [Except: …]` 줄을 넣는다 |
| K3 | 모호함 | "고정 설명문(에셋 대장)과 가져온 OK 줄은 글자 그대로"인데, 화면 대응 문장처럼 대장과 OK 카드 문장이 다르면 어느 쪽이 정본인지 정해져 있지 않다 | `kit/instructions.md:28`, `kit/skills/image-prompt/first-frame.md:55`, 테스트베드 `asset-registry.md:91` 대 `ok-cuts.md:240` | 5번에 "고정 설명문은 대장 문장이 이긴다. OK 카드 문장이 다르면 대장 것으로 쓰고 알린다"를 한 줄 넣는다 |
| K4 | 모호함 | 사용자가 "제안대로/그대로"로 받아들인 값에 `(제안값)`을 붙이는지 불명확하다. C08은 "사용자 확정", C10·C12는 `(제안값)`으로 갈렸다 | `kit/instructions.md:25`("그대로면 제안값을 쓴다"), `:27`("정하지 않은 값은 … (제안값)") | "'그대로'로 받은 값도 사용자가 고르지 않았으면 (제안값)을 유지한다. 사용자가 값을 직접 말했거나 제안을 골라 답했으면 뗀다" 중 하나로 못 박는다 |
| K5 | 모호함 | `--must-include`가 받는 파일 형식(한 줄에 하나, 문장 그대로)이 SKILL.md에 없고 스크립트 docstring에만 있어서 플레이어가 스크립트를 열었다(C08, C10, C12 모두) | `kit/skills/higgsfield-generation/SKILL.md:16`(`[--must-include 고정문장파일]`), `check_prompt.py:2-12` | SKILL.md:16에 "고정문장파일 = 한 줄에 하나씩, 대장의 고정 설명문 그대로"를 덧붙인다. 스크립트 소스는 열지 않아도 된다고 쓴다 |

## 지난 소넷 대비
인물 자리 지어내기(벤치 가운데)와 `video-prompt` 미리 열기가 해결됐다. 남은 것은 틀 1의 `Except` 슬롯 부재와 문장 출처(대장 대 OK 카드)다.
