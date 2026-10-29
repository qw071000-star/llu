# real13-C55 장면 컷 다시 나누기 — "3장 컷 다시 나눠줘" (1턴) — PASS 0 / 부분 1 / FAIL 0 (real11: PASS 1 / 부분 0 / FAIL 0 (real9: PASS 0 / 부분 1 → real10 재실행 PASS))

G1: 메타상 `mcp__` 도구 호출 없음, RUN 밖 읽기 없음(PASS). `git status`의 `PLAYER-RULES.md`·`SKILLS-INDEX.md` 삭제는 실행기 흔적.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | `shot-design` 열림, 컷 목록 내용 줄을 비트로 쓴다고 밝힘, 블로킹 화면 쪽+물건, 180도 선, 표, 3-4 반응 컷 `새 뷰 필요`, 3-1·3-2·3-3 유지/교체 질문, 정본 안 고침. 그러나 첫 줄에 `[N]번 [작업명]으로 진행합니다.`가 없음(`kit/instructions.md:41`, `kit/context/tasks.md:58`); 또 `shot-list.md`로 옮길 줄(상태 `대기`)을 안 보임(`kit/skills/shot-design/SKILL.md:63` 5번); 표의 3-2 "약 40°"·3-3 "약 40°"는 승인 시작 이미지(75mm 32°, 50mm 47°)와 다른데 `ok-cuts.md`를 안 읽음 |

## 검사기
프롬프트 없음

## 추가 발견
- 인서트(가방·시간표) 샷 없음(선택).

## 키트 결함
- 첫 줄 규칙 미준수.
- `kit/skills/shot-design/SKILL.md:55-56`: 기존 시작 이미지가 있는 컷은 그 OK 카드의 mm·화각을 쓰라는 말이 없음. 고침: "cut with a confirmed start image: copy its lens (°) from the OK card" 추가하고, 템플릿의 `shot-list.md로 옮길 줄` 블록을 항상 보이라고 명시.

## 총평
구조는 맞지만 첫 줄, 옮길 줄, 화각 값에서 빠졌다.
