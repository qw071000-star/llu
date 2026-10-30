# real13-C47 두 인물 접촉 — "손 잡게" 3-2 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real11: PASS 1 / 부분 1 / FAIL 0 (real12 재채점))

G1: 메타상 `mcp__` 도구 호출 없음, RUN 밖 읽기 없음(PASS). `git status`의 `PLAYER-RULES.md`·`SKILLS-INDEX.md` 삭제는 실행기 흔적.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 (확인+응) | PASS | t1 "13번 실사·인물 영상으로 이해했습니다. 이 작업을 할까요?"(말 단어 없음, 13/15 겹침이라 허용), t2 "13번 … 진행합니다." 사건 "돌아선다, 다가간다, 손을 잡는다 3개, 대사를 넣으면 4개". 화면 쪽+물건으로 손 제안, 3-1과 같은 동작 기준 충돌과 3-3 이음새 짚음, 6개 질문, 카드 안 만듦 |
| 2 | PASS | `acting` 열림(메타), 카드 `(제안값)`, 검사 WARN 1(6,097자)에 이유·덜어낸 수 "겹친 권한 설명과 화질 문장 약 450자 … 고정 문장은 줄이지 않았습니다" 제시 → 키트 예시 형식과 같음. 모든 손 `screen-right hand, nearer the sign` 형식 |

## 검사기
turn3 영상 프롬프트: `--kind video --refs 4 --seconds 8 --must-include(girl·grandpa·bag·light)` → `WARN 길이 6097자 … — FAIL 0 · WARN 1 · 6097자`

## 추가 발견
- Forbidden에 `GRANDPA moving his lips`처럼 실제로 난 적 없는 실패가 들어 있음(`kit/skills/video-prompt/SKILL.md:72` 규칙 6 경미).
- 승인본 3-1(5,060자)보다 약 1,000자 김.

## 키트 결함
없음

## 총평
사건 수·검사 이유·절제 연기 모두 맞게 처리했다. 길이 WARN은 이유를 숫자와 함께 남겼다.
