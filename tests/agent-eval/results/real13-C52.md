# real13-C52 "크레딧 얼마나 썼어?" (1턴) — PASS 0 / 부분 1 / FAIL 0 (real11: PASS 1 / 부분 0 / FAIL 0)

G1: 메타상 `mcp__` 도구 호출 없음, RUN 밖 읽기 없음(PASS). `git status`의 `PLAYER-RULES.md`·`SKILLS-INDEX.md` 삭제는 실행기 흔적.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 내용 PASS: 3-1 약 170 + 3-2 약 8 = 약 178만 확정치, 나머지 "알 수 없음", 1-2 팀원 기록 없음, `get_cost` 견적 제안. 그러나 첫 줄에 `[N]번 [작업명]으로 진행합니다.`가 없음(`kit/instructions.md:41`, `kit/context/tasks.md:58`): 답이 "지금 기록된 크레딧은 약 178입니다."로 시작 |

## 검사기
프롬프트 없음

## 추가 발견
없음

## 키트 결함
- 첫 줄 규칙 미준수. 질문형 답은 "작업 시작"이 아니라고 읽을 여지가 있음(`kit/instructions.md:41` "every answer that starts a task") — 규칙 0에서 "모든 새 사용자 요청"으로 명시.

## 총평
숫자는 정확, 첫 줄 형식만 빠졌다.
