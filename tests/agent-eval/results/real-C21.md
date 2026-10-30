# real-C21

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | location-edit.md 틀 2, "시대는 한 번에 한 층씩", 층 순서 제안(FURNITURE → STRUCTURAL → LIGHTING → IMAGE CHARACTER), 정본 1990년대(§3)와 충돌 → 자식 상태판 `loc_busstop_road_2020s_v1`로 따로 기록 제안. 프롬프트 없음 |
| 2 | 부분 | 한 층만, `this step changes only its FURNITURE / FIXTURES`, 요소별 대응물, REMOVE, PRESERVE, `ONLY CHANGE: FURNITURE / FIXTURES`, 목표 시대 잠금, 1990s 잠금 안 남음(여는 문장의 출처 서술만). 검사(내가): `OK — image 프롬프트 1801자, 걸린 항목 없음` (--refs 1). 문제: 여는 문장이 `Edit loc_busstop_road_v1 WITHOUT reframing…`으로 `<<<image_1>>>` 태그가 없음 — 참조 1장인데 태그 0개(검사기가 못 잡음). 플레이어는 검사 승인 거부 |

**PASS 1 / 부분 1 / FAIL 0**

## 키트 결함
- `.claude/skills/image-prompt/location-edit.md:53` 틀 2 코드블록이 `[LOCKED EDIT opening — SKILL.md §1]` 자리표시자라 `<<<image_1>>>` 태그가 빠짐. 고침: 틀 2 첫 줄에 `Edit <<<image_1>>> WITHOUT reframing: … one change only.` 전문을 적는다.
- `location-edit.md:50` 표지판이 IDENTITY AND TEXT(표지판 글자)와 FURNITURE(표지판 기둥) 양쪽에 걸림. 고침: "표지판 판은 IDENTITY AND TEXT, 기둥·벤치는 FIXTURES"로 층 소속을 명시.
- `.claude/skills/higgsfield-generation/check_prompt.py` — 참조 수 > 0인데 프롬프트에 `<<<` 태그가 0개면 WARN을 내도록 보강.

총평: 층 분리는 정확, 참조 태그 누락이 흠.
