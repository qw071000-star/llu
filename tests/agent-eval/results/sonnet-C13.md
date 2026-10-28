# C13 (소넷) — "3-1의 색감과 질감으로 3-5 퍼스트 프레임" · 채점

- 실행 폴더: `tests/agent-eval/runs-sonnet/C13` (turn1: 질문, turn2: `그대로.` 뒤 전문)
- 정본 변경: `project/cuts/3-5.md` 새로 만듦(2792자, 3천 자 이하). 다른 정본 그대로
- 집계: **PASS 16 / 부분 0 / FAIL 1** (체인 판정: 부분 — 내용은 전부 맞고 읽기 범위가 크게 벗어남)
- 비교: Opus 1차 18/0/0 (읽은 파일: production-session, image-prompt, ok-cuts 절만). 소넷의 프롬프트 품질은 Opus와 같거나 낫고, 읽기 범위만 다르다.

## 턴별 판정표

### 턴 1 — `3-5 퍼스트 프레임 프롬프트 만들어. 색감이랑 질감은 3-1처럼.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1-1 | `ok-reuse.md`를 열고 3-1 **시작 이미지** 카드를 연다 | PASS | 메타: `production-session/ok-reuse.md`, `ok-cuts.md (… 3-1 시작 이미지 …)`. "OK 대장의 `3-1 시작 이미지`(job-ff-3-1, OK 이유 '색감, 질감')에서 가져옵니다. 영상 카드가 아니라 이미지 카드로 읽었습니다" |
| 1-2 | 색·질감 문장이 없음을 알아채고, 3-1 이미지를 색·질감 전용 참조로 붙이고 권한을 좁힌다. 색 문장을 지어내지 않는다 | PASS | "그 프롬프트에는 색·질감 문장이 따로 없습니다 … 문장을 지어내지 않고 3-1 이미지를 색 참조로 붙이고, 권한을 '색·콘트라스트·질감만'으로 좁히겠습니다. 구도·인물·빛 방향은 가져오지 않습니다" |
| 1-3 | 3-5 정보(카메라, 손·가방 열림)를 묻거나 제안 | PASS | "1. 카메라 … 85mm", "2. 가방 안 … 어두운 안감만", "3. 손 … 걸쇠가 열린 입구 가장자리 위에 한 손", "5. 이음새: 3-4 끝의 열린 가방 상태에서 시작", 확정 사항 "가방은 열림(§6)" |
| G1 | mcp·생성 없음 | PASS | [TOOL] `list_folders`, `list_project_assets(fld-3-5)` |
| G2 | 한국어 | PASS | |
| G3 | 질문 끝 한 묶음, decisions 다시 묻지 않음 | PASS | "정본에서 가져온 값은 다시 묻지 않습니다. GPT Image 2.5 · 1k · 16:9, 저장 `fld-3-5` …". 질문 6 "이 컷의 영상 쪽도 같이 정할까요"는 범위 밖이지만 "첫 프레임만 정하고 영상은 승인 뒤에"로 닫았다 |
| G4 | 컷 세션은 자기 컷 카드, 앞뒤 줄, 기준 OK 카드 하나만 | **FAIL** | 메타: `cuts/3-1.md, cuts/3-2.md, cuts/3-3.md, log/3-1_handoff_2026-10-26.md, log/3-2_handoff_2026-10-27.md` (다른 컷 카드 3장과 핸드오프 2건), `ok-cuts.md`의 "LC-001-V1 / 3-2 시작 이미지 / 3-3 시작 이미지 카드"까지 열었다. 기준 OK는 3-1 시작 이미지 하나여야 한다. 앞 컷 3-4는 카드가 없는데 3-1·3-2·3-3을 읽어 "벤치 감나무 쪽 절반"을 얻은 것으로 보인다(카드 [5]) |
| G5·G6 | 프롬프트 없음 | 해당 없음(1턴) | |
| 시점 | turn1 정본 수정 | PASS | 컷 카드 v0만 만들었다. 모르는 칸은 비워 둠 |

### 턴 2 — `그대로.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 2-1 | 참조 수 = 태그 수 | PASS | 태그 `<<<image_1>>>`~`<<<image_3>>>` 3개 = 블록 밖 "image_1 loc_busstop_road_v1 · image_2 prop_doctor_bag_v1 · image_3 3-1 시작 이미지". 얼굴이 프레임 밖이라 인물 시트를 붙이지 않았다고 이유를 적음 |
| 2-2 | 의상(보이면)·가방·LIGHT LOCK 글자 그대로 | PASS | 소매가 보여 WARDROBE 포함. `--must-include bag+light`(+grandpa) 통과 |
| 2-3 | 색 참조 권한을 좁힌 문장 | PASS | "<<<image_3>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction." + "DO NOT TRANSFER: … from <<<image_3>>>, its people, its framing and its light direction." |
| 2-4 | 검사 `--kind image --must-include bag+light` FAIL 없음 | PASS | 아래: `OK — image 프롬프트 2317자, 걸린 항목 없음` |
| 2-5 | 3-4 이후라 가방 열림 | PASS | "It is OPEN: the brass clasp undone, the lid folded back, the mouth about 40 cm wide, only dark worn cloth lining visible inside" |
| G1 | 생성하지 않음 | PASS | "생성은 지시하신 게 아니라서 보내지 않았습니다 … '생성해'라고 하시면 보냅니다" |
| G3 | 질문 | PASS | 마지막 "이 프롬프트로 생성할까요?" 하나 |
| G5 | 빈칸 없음 | PASS | |
| G6 | 코드블록 하나 + 블록 밖 | PASS | 모드·참조(붙이는 순서·역할)·모델·해상도(1k)·저장 폴더·견적. 위험→막는 문장 7개를 블록 앞에 먼저 보임(`instructions.md:26`) |

## 검사기 결과
```
$ check_prompt.py --kind image --refs 3 --must-include (bag.lines+light.lines) c13.txt
OK — image 프롬프트 2317자, 걸린 항목 없음
```
(추가: `grandpa.lines`를 넣어도 통과. 태그 3개 = 블록 밖 참조 3개.)

## 추가 발견
1. 가방 충돌을 `Except:`가 아니라 고정 문장 바로 뒤의 "It is OPEN: …"으로 처리했다. 효과는 같고, 막는 문장에도 올렸다. 형식은 `image-prompt/SKILL.md:44`("Except: [이 컷에만 있는 것].")와 다르다.
2. 틀 2의 `[PALETTE · ERA LOCK …]` 줄(`first-frame.md:74`)이 프롬프트에 없다. 에셋 대장에 해당 문장이 없어 `Nothing else: … nothing more recent than the early 1990s`로 대신했다. 합리적이다.
3. 좋았던 점: "생성 후 색감이 3-1과 같은지 봐 주세요"로 확인 지점을 남겼고, 3-4 끝 구도와 맞는지를 "총괄에 올릴 것"으로 적었다(이웃 카드를 고치지 않음).

## 키트 결함
| # | 결함 | 근거 | 수정 제안 |
|---|---|---|---|
| S11 | 컷 세션에게 "이웃 컷에도 같은 값을 쓴다"고 시키는 문장이 있어, 작은 모델이 이웃 컷 카드와 핸드오프를 열고 쓰려 한다. 같은 지침 72줄은 "다른 컷은 읽지 않는다" | `kit/instructions.md:25` vs `:72` | :25를 "…이웃 컷 카드는 고치지 않는다. 맞출 값은 핸드오프 [5] '총괄에 올릴 것'에 쓴다"로 고친다 |
| S3 | "이웃 컷의 끝 상태"를 어디서 얻는지 정하지 않았다 | `kit/skills/video-prompt/SKILL.md:63`, `kit/skills/image-prompt/first-frame.md:32` | "컷 목록의 이음새·연속성 표에서만. 그 표에 없으면 묻는다" |
| S4 | 인물 자리 출처가 없어 이웃 카드로 간다 | `kit/skills/image-prompt/first-frame.md:14` | C08 S4 참고 |
| S1 | 3-1 시작 이미지 외 OK 카드(LC-001-V1, 3-2, 3-3)까지 열었다. "그 카드 하나만"이 플레이어에게 단계별로 읽히지 않는다 | `kit/skills/production-session/ok-reuse.md:9` | 9줄을 "그 카드의 프롬프트만 연다. 이름 외의 카드는 열지 않는다(장소 뷰 카드도 job 이름이면 충분)"로 |

## 총평
"색 문장이 없으면 지어내지 말고 색 참조 + 권한 좁히기"를 정확히 따랐고 프롬프트는 검사를 통과했다. 3-5 세션이 이웃 컷 카드 3장·핸드오프 2건·OK 카드 3장을 연 것이 유일한 큰 어긋남이다.
