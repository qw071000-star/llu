# C12 (소넷, 정리된 키트) — "3-1의 모션처럼 3-2 영상 프롬프트" · 채점

- 실행 폴더: `tests/agent-eval/runs-sonnet2/C12` (turn1: 질문, turn2: `그대로.` 뒤 전문). 정본 변경: `project/cuts/3-2.md`만 (`M project/cuts/3-2.md`, `?? out/`, `?? tmp/`)
- 집계: **PASS 19 / 부분 0 / FAIL 0** (체인 판정: PASS)
- 지난 소넷(정리 전): 16 / 1 / 1.

## 턴별 판정표

### 턴 1 — `3-1의 모션처럼 3-2 영상 프롬프트 만들어.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 1-1 | `production-session` → `ok-reuse.md`, OK 대장 **3-1 영상 카드 하나** | PASS | 메타: `production-session/SKILL.md`, `ok-reuse.md`, `ok-cuts.md`("목록 위주, 이어서 `### 3-1 영상` 절과 `### 3-2 시작 이미지` 절만"). `cuts/3-1.md`는 열지 않았다(지난번 FAIL 해결). 3-2 시작 이미지 카드는 자기 컷의 카드라 허용 |
| 1-2 | 카메라·렌즈·위치는 3-2 카드·시작 이미지를 따르고, 35° 대 75mm(≈32°)를 알린다 | PASS | "1. 렌즈 화각: 제안 — 대각 약 32° (이유: 3-2 시작 이미지가 75mm 렌즈로 만들어졌고, 이는 약 32°입니다. 컷 카드의 35°와 달라서 시작 이미지를 따릅니다. 카드 [4]도 이 값으로 고치겠습니다)". "3-1의 카메라와 렌즈는 가져오지 않습니다" |
| 1-3 | 빈 칸만 묻거나 제안값으로 채운다 | PASS | "확인할 것이 6개": 렌즈·관찰 결과·화면 좌표·끝 상태·연기·소리·이음새 모두 제안값 + 이유. 기본값(8초 · 16:9 · 고정 · 480p · 저장 `fld-3-2`)은 한 줄 |
| 1-4 | 3-1 Required·Forbidden 중 가져온 동작·인물에 걸린 줄(할아버지 입 움직임 금지 등) | PASS | "3-1 Required/Forbidden 중 모션에 걸린 줄(대사 한 번, 가방 닫힘, 할아버지 입 움직임 금지, 인원 2명)과 3-2 카드의 'Nobody looks at the camera'를 함께 옮깁니다" |
| 1-5 | 컷 카드 3-2 [7]에 "가져온 OK: 3-1 영상 — 모션(…)" | PASS | diff `+    가져온 OK: 3-1 영상 — 모션(ACTION_TIMING, PHYSICS)` |
| G1 | mcp·생성 없음 | PASS | [TOOL] `list_folders`, `list_project_assets(fld-3-2)`뿐. "이번에는 프롬프트만 만들고 생성하지 않습니다" |
| G2 | 한국어 짧게 | PASS | |
| G3 | 질문은 끝에 한 묶음, 정본 값을 다시 묻지 않는다 | PASS | 번호 6개 한 묶음 + "기본값으로 씀" 한 줄 |
| G4 | 필요한 스킬·파일만, 다른 컷 카드를 열지 않는다 | PASS | 스킬: `production-session`(+`ok-reuse.md`), `video-prompt`(+`live-action.md`). `acting`은 열지 않음(지난번 지적 해결). 다른 컷 카드·핸드오프 없음(3-2 핸드오프는 자기 컷) |

### 턴 2 — `그대로.`

| # | 기대 | 판정 | 근거 |
|---|---|---|---|
| 2-1 | `ACTION_TIMING`·`PHYSICS`를 글자 그대로 (`motion_3-1.lines`) | PASS | `--must-include … motion_3-1` 통과. ACTION_TIMING 3구간과 PHYSICS 4줄이 OK 카드와 같다 |
| 2-2 | 3-1 Required·Forbidden의 입 움직임 금지 줄 | PASS | AUDIO "GRANDPA does not say a single word; no attempt to speak, no lip movement." + Forbidden "GRANDPA moving his lips or speaking (ENTIRE_SHOT)". CHARACTER_ACTING "He never looks at the girl." |
| 2-3 | 본문에 "3-1"·"previous shot" 없음 | PASS | `grep "3-1\|previous\|shot 3"` 결과 없음 |
| 2-4 | 보이기 전에 검사 실행 | PASS | "검사 스크립트: 통과, 5,087자, 걸린 항목 없음". 메타에 `tmp/p32.txt`, `tmp/fixed.txt` |
| 2-5 | 검사 `--refs 4 --seconds 8 --must-include grandpa+girl+bag+light+motion_3-1` FAIL·WARN 없음 | PASS | 아래: 걸린 항목 없음 (5087자) |
| 2-6 | 렌즈 = 시작 이미지 우선(≈32°), 다르다고 알림 | PASS | "[OPTICS] Diagonal field of view about 32°. The bench and the timetable sign fill the frame side by side / the paddies behind are compressed and soft / only the two people and the sign are sharp. Shallow depth of field." (mm 없음). 알림은 1턴 |
| 2-7 | 컷 카드 3-2에 기록 | PASS | diff `[4] 렌즈: 대각 화각 약 32° (제안값; 시작 이미지 75mm 기준, 옛 35°에서 고침)`, `[5] 끝·동선·시선 … (3-1 모션, 제안값)`, `[6] 타이밍 … (3-1 모션, 제안값)` |
| 2-8 | 바꾼 단어를 "전 → 후"로 보인다 (`ok-reuse.md:42`) | PASS | "3-1 OK 프롬프트에서 바뀐 줄 (전 → 후)" 6개, `Neither of them looks at the camera.` → `Nobody looks at the camera.` 포함(지난번 누락 해결) |
| G1 | 생성하지 않음 | PASS | "아직 보내지 않았습니다 … 보내라고 하시면 …" |
| G5 | 빈칸 없음 | PASS | |
| G6 | 코드블록 하나 + 블록 밖 | PASS | 모드 · 참조 4개(순서) · 모델 · 해상도 · 길이 · 소리 · 저장 · 예상 비용 · 검사 결과. 위험 → 막는 문장 5개를 프롬프트 앞에 |

## 검사기 결과
프롬프트: `out/turn2.md`의 코드블록 하나(`runs-sonnet2/C12/grade-tmp/p.txt`), 태그 4개(`ff_3-2_v1`, `char_grandpa_autumn_v1`, `char_girl_raincoat_v1`, `prop_doctor_bag_v1`) = 블록 밖 참조 4개.
```
$ check_prompt.py --kind video --refs 4 --seconds 8 --must-include (grandpa+girl+bag+light+motion_3-1) grade-tmp/p.txt
OK — video 프롬프트 5087자, 걸린 항목 없음
```

## 추가 발견
1. 컷 카드 [4]에 `화면 좌표:` 줄을 즉석에서 만들었다(diff). 컷 카드 틀에 칸이 없다(K6, C10 파일 참고).
2. 컷 카드 [10]에 가져온 위험(입 움직임 금지)을 옮기지 않았다. 다만 3-1 OK 카드에 "실제로 난 실패"가 기록돼 있지 않아 `cut-card.md:26` 기준으로 위반은 아니다.
3. 좋은 점: 시작 이미지 문장에서 `tree`를 뺀 것, `LOCATION_MAP`·`OPTICS`·`CAMERA`가 바뀐 곳을 모두 "전 → 후"로 보였고 감나무가 보이는지는 "추정"으로 표기했다.
4. 시험 데이터: 가방 문장 "hanging heavy"와 3-2 카드 35° 대 시작 이미지 75mm는 일부러 남긴 것이라 감점 없음.
5. 시작 보고는 세 줄이 아니라 한 문단(판단·읽은 것·할 일)이었다. 3-2에서 "3-1의 모션" 요청이 시작 문구라 형식 위반은 경미하다.

## 키트 결함
| # | 분류 | 결함 | 근거 | 수정 제안 |
|---|---|---|---|---|
| K6 | 규칙이 없음 | 컷 카드에 화면 좌표·연기 범위를 적을 칸이 없다(C10 K6과 같음) | `kit/skills/video-prompt/SKILL.md:25,68`, `kit/skills/production-session/cut-card.md:12-21` | C10 K6 참고 |
| K7 | 읽기 지도 | `decisions.md`·`asset-registry.md`가 컷 세션 정본 목록에 없다(C10 K7과 같음) | `kit/instructions.md:58-59` | C10 K7 참고 |
| K5 | 모호함 | `--must-include` 파일 형식이 SKILL.md에 없어 스크립트를 열었다 | `kit/skills/higgsfield-generation/SKILL.md:16` | C08 K5 참고 |

(이 체인에서 플레이어 오류로 이어진 결함은 없다. 위 셋은 읽기·기록 과정의 마찰이다.)

## 지난 소넷 대비
3-1 컷 카드 열기, `acting` 미리 열기, 길이 WARN(5258자 → 5087자 통과), "전 → 후" 누락이 모두 해결돼 FAIL·부분이 0이 됐다.
