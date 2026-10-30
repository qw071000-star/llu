# real13-C39 다른 컷을 형식 예시로 — "3-4 컷 카드 만들어. 3-1 카드처럼 써줘." (1턴) — PASS 0 / 부분 1 / FAIL 0 (real11: PASS 1 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 잘한 것: `production-session` SKILL·`cut-card.md`·`shot-list.md`·`decisions.md`·`asset-registry.md`만 읽고 3-1 카드·OK·핸드오프를 열지 않았다(meta). "3-1 카드는 열지 않고 `cut-card.md` 양식에…", [7]에 "'3-1 카드처럼'은 카드 형식으로 이해함. 3-1 OK의 요소를 가져오려면 알려 주세요"로 형식과 OK 기준을 구분. 되묻지 않고 `project/cuts/3-4.md` v0 작성, 모르는 값은 `(제안값)`. 렌즈는 시작 이미지가 없어 63°(V1)로 표시. 프롬프트·생성 없음. 흠: ① 첫 줄이 카드 작성 보고로 시작하고 "2번 … 으로 진행합니다."가 없다. ② 사건을 1개로 셌다: 카드 [1] "이벤트 1개(걸쇠 풀고 뚜껑 열기)"인데 [6]은 `0:02–0:05 걸쇠를 푼다 / 0:05–0:07 뚜껑을 연다`로 동사가 둘이다(`video-prompt/SKILL.md:82` "Count every verb … Do not count them in groups"). 3개 이하라 쪼갤 필요는 없지만 세는 법이 틀렸다. ③ 질문 2의 손 표기 "화면 오른쪽 손이 걸쇠를, 화면 왼쪽 손이 손잡이를"에 물건이 없다(카드에는 `nearer the timetable sign` 등을 붙임) |

검사기: 프롬프트 없음.

추가 발견
- 카드 [4]에 카메라를 "화면 오른쪽 시간표 표지판 쪽에서 벤치를 비스듬히"로 제안하고 V1과 방향이 달라지면 새 뷰·LIGHT LOCK이 필요할 수 있다고 미리 알림(좋음).
- PR-001 확정 job 미등록, 연속성 표 3-4 "(미정)"을 컷 세션 권한상 건드리지 않았다고 알림.

키트 결함
- `kit/skills/production-session/cut-card.md:3` 및 `video-prompt/SKILL.md:82`: 통합 후 "events"를 세는 규칙이 `video-prompt` §2 한 곳에만 있고(acting·shot-design은 링크), 카드 [1] "완료 조건"을 쓰는 `cut-card.md`에서는 링크도 없다. 고침: `cut-card.md` 도입 문단의 "When the number of events or actions changes …" 뒤에 "(count every verb: `video-prompt` §2 "Event count")" 추가.
- `kit/instructions.md:41`: 첫 줄 누락(카드 작성 턴에서도).

총평: 다른 컷 카드를 열지 않는 규칙과 형식/OK 구분은 지켰지만, 사건 수 세기와 첫 줄에서 감점.
