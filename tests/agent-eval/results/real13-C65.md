# real13-C65 두 스킬을 한 번에 — "러프컷 만들고 색도 맞춰" (1턴) — PASS 0 / 부분 1 / FAIL 0 (real11: PASS 1 / 부분 0 / FAIL 0 (real12 재채점))

G1: 메타상 `mcp__` 도구 호출 없음, RUN 밖 읽기 없음(PASS). `git status`의 `PLAYER-RULES.md`·`SKILLS-INDEX.md` 삭제는 실행기 흔적.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | "22번 색 맞추기로 진행합니다." 순서 "22→21", 3장에서 확정 영상은 3-1뿐이라 짚음, 스크립트 실행 없음(`ls`만). 그러나 기준 색 컷으로 2-1을 제안(이유 "앞선 컷") — 키트는 `OK 이유`가 "색감"인 컷(3-1) 제안(`kit/skills/color-continuity/SKILL.md:111`), `ok-cuts.md`를 안 읽음. 2-1은 노란 시험 파일이라 기준으로 부적절. 2-1을 넣을지/3-2를 기다릴지 묻는 질문도 약함 |

## 검사기
프롬프트 없음

## 추가 발견
- 비프롬프트 작업에 "프롬프트를 쓰기 전에 확인할 것이…" 고정 문장 사용(`kit/instructions.md:22`, 경미).

## 키트 결함
- `kit/skills/color-continuity/SKILL.md:111`: 제안 기준을 정하려면 `ok-cuts.md` 목록의 `OK 이유`를 읽으라는 말이 없음(`tasks.md` §3은 표 밖 파일을 열지 말라). 고침: "read the OK-ledger list's `OK 이유` column to propose the reference".

## 총평
real12 PASS에서 후퇴: 기준 색 컷 제안이 키트 규칙과 다르다.
