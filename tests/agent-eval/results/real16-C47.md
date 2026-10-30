# real16-C47 두 인물 접촉 — 손 잡게 (2턴) — PASS 10 / 부분 3 / FAIL 0

> 채점: tests/agent-eval/runs-real16/C47/out/turn*.md·meta.json, git diff. 기준: grader-rules.md, scenarios.md(G1–G9 + C47), kit/.

## 턴별 판정표

| 턴 | 기대 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄과 작업 선택(기능 3) | 부분 | "13번 실사·인물 영상으로 진행합니다." — 3-2에는 시작 이미지만 있고 영상이 없어 13은 타당하나 사용자 말에 "영상" 등 일치 단어가 없고(11/13 가능) 기능 지도는 "확인 필요". 기대 오류 가능성 있음 |
| 1 | 카드·이음새("3-1과 같은 동작")와 다름을 먼저 짚음 | PASS | "1. 카드와 다른 동작: 제안 — 이 컷만 새 동작으로 갑니다 … 3-1 승인본은 건드리지 않습니다." |
| 1 | 사건 수 세기(기능 19/66): 4개면 샷 나누기 제안 | 부분 | "대사 → 한 걸음 → 손잡음 3개 … 돌아서기까지 넣으면 4개라 쪼개야 합니다"로 몸 돌림을 뺐으나, 프롬프트에 "stops tracing … drops to her side; she turns only her head … says the line"이 남아 SKILL §2 "Count every verb"(turns, says, steps, takes = 4 → split)로 세면 4 이상. 샷별 목록 제안 없음 |
| 1 | 누가 어느 손(화면 쪽 + 물건)으로 무엇을 | PASS | "손녀가 자기 화면 왼쪽 손을, 무릎 위 가방 위에 놓인 할아버지의 화면 오른쪽 손 위에 얹습니다" |
| 1 | 가방 위 두 손·가방 닫힘(§6) 충돌 짚기, 절제 연기 | PASS | "할아버지 손은 가방에서 떼지 않고, 가방은 닫힌 채" · "4. 할아버지 반응 … §5 절제 연기" |
| 1 | 시작 이미지를 못 봐 좌우를 "추정" 표시 | PASS | "시작 이미지를 직접 볼 수 없어 좌우는 "추정"입니다." |
| 1 | 읽기(G4/G8): 질문 턴에 acting 안 엶 | PASS | reads: shot-list, decisions, 3-2 카드·핸드오프(자기 컷), video-prompt/SKILL.md, ok-cuts, live-action.md. acting 안 엶 |
| 2 | acting 열고 15블록 작성(기능 23) | PASS | reads에 acting/SKILL.md, cut-card.md. 블록 15개 + PRE_SHOT_CONTINUITY |
| 2 | 검사기 실행·WARN 이유에 숫자(G7) | PASS | 7회 실행. 마지막 "경고는 길이 6,925자 하나 … 겹치는 설명 약 130자만 뺐습니다" (live-action.md 예시 형식) |
| 2 | 손 표기·화면 기준(G9) | PASS | "The girl's screen-left hand, nearer the old man, lowers slowly onto his screen-right hand" 등 전부 화면 쪽 + 물건, 동서남북 없음 |
| 2 | 카드 갱신: 사용자가 말하지 않은 값은 (제안값) 유지 | 부분 | [4] 렌즈 줄 "관찰 결과 배경이 압축되어 흐림 / … · 심도·초점 두 사람에 맞춤"에 (제안값) 없음. [1]·[5]·[6]은 표기함. 35° → 32° 정정은 환산표 근거로 사용자에게 알림(옳음) |
| 2 | 블록 밖 모드·참조·모델·해상도·길이·저장 + 위험 목록 | PASS | "- 모드 … - 저장 폴더: fld-3-2", "실패 위험 (위험마다 막는 문장 하나)" 6개 |
| 2 | 생성 없음, "그대로/좋아"는 생성 아님 고지(G1) | PASS | "영상으로 만들어라고 하시면 480p로 보냅니다. "그대로"나 "좋아"는 보내라는 말로 받지 않습니다." |

## 검사기 결과

C47 T2 코드블록 1개(영상, 참조 4, 8초), must-include = grandpa/girl/bag/light 4문장:
`WARN  길이 6925자. 5,500자 이하가 안전했다. 남기려면 이 숫자를 그대로 적고 이유를 쓴다` / `— FAIL 0 · WARN 1 · 6925자` (종료 0)
WARN은 플레이어가 숫자와 이유를 적었음(live-action.md "How to trim" 형식).

## 추가 발견

- 프롬프트 [REQUIRED_AND_FORBIDDEN]에 "Readable characters on the timetable sign"를 Forbidden으로 넣음 — SKILL §1-6은 "실제로 난 실패만"인데 근거 기록 없음(경미).
- 프롬프트 AUDIO에서 보이스 문장은 대장 VOICE와 글자 일치.

## 키트 결함

- `kit/skills/video-prompt/SKILL.md:83` "Count every verb"가 머리 돌림·손 내림 같은 하위 동작을 세는지 불명 → 예시에 "고개/시선 이동, 손 내리기도 동사로 센다" 한 줄(또는 세지 않는 목록).
- `kit/context/tasks.md:30`(13행)에 동작만 있고 "영상/프롬프트" 단어가 없는 요청("손 잡게 해 줘")의 처리 지침이 없음 → 13행 말에 "cut number + 동작 서술 (시작 이미지만 있음) → 13 바로" 또는 확인 대상이라고 명시.

## 총평

지침(카드와 다름·화면 손·acting·검사)은 충실했으나 사건 수를 문자 그대로 세지 않아 샷 분할 제안이 빠졌다.
