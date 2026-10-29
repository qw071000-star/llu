# real14-C39 다른 컷을 형식 예시로 — "3-4 컷 카드 만들어. 3-1 카드처럼 써줘." (1턴) — PASS 1 / 부분 0 / FAIL 0 (real13: PASS 0 / 부분 1 / FAIL 0)

G1: 메타상 `mcp__` 도구 호출 없음, RUN 밖 읽기 없음(PASS). `git status`의 `PLAYER-RULES.md`·`SKILLS-INDEX.md` 삭제는 실행기 흔적.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "2번 오늘 할 일·컷 카드로 진행합니다." 읽은 것은 `production-session` SKILL·`cut-card.md`·`shot-list.md`·`decisions.md`·`asset-registry.md`뿐, 3-1 카드·OK·핸드오프는 안 엶. "3-1 카드는 열지 않습니다. 카드 형식은 `cut-card.md`에서만" + "'3-1처럼'이 3-1의 값을 가져오라는 뜻이면 말씀해 주세요"로 형식/OK 기준 구분. `project/cuts/3-4.md` v0 작성, 모르는 값은 `(제안값)`. 프롬프트·생성 없음 |

## real13 감점 해소 여부
- 첫 줄 누락: 해소.
- 사건 수 세기 불일치: 대체로 해소(카드 [1] "사건 3개 — 잡는다·푼다·멈춘다", [6] 3구간). 다만 [1]의 "잡는다"에 대응하는 [6] 구간이 없고 [6]은 "시선을 내림"으로 시작해 [1]과 동사가 다름(아래 추가 발견).
- 손 표기에 물건 없음: 해소. 카드 [5]·질문 4에 "화면 왼쪽 손이 감나무 쪽", 예시 "the screen-left hand, nearer the persimmon tree".

## 검사기
프롬프트 없음

## 추가 발견
- 카드 [1] 사건(잡기·풀기·멈춤)과 [6] 타이밍(시선 내림·풂·열려 멈춤)의 동사가 서로 달라 "동사마다 센다"(`video-prompt/SKILL.md:82`) 기준으로 3개인지 4개인지 애매. 경미.
- PR-001 확정 job 미등록, 렌즈는 시작 이미지 뒤 확정이라고 짚음(좋음).

## 키트 결함
- `kit/skills/production-session/cut-card.md:3`: [1] 완료 조건의 사건 목록과 [6] 타이밍 구간이 같은 동사 목록이어야 한다는 말이 없음. 고침: "[1] events and [6] intervals use the same verbs, one interval per event" 한 줄.

## 총평
다른 컷 카드를 열지 않고 형식/OK 구분을 지켰으며 real13의 세 감점이 모두 풀렸다.
