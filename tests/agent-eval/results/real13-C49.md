# real13-C49 막연한 정리 요청 — "에셋 대장 정리해줘" (1턴) — PASS 0 / 부분 1 / FAIL 0 (real11: PASS 1 / 부분 0 / FAIL 0)

G1: 메타상 `mcp__` 도구 호출 없음, RUN 밖 읽기 없음(PASS). `git status`의 `PLAYER-RULES.md`·`SKILLS-INDEX.md` 삭제는 실행기 흔적.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 후보를 보임(CH-003 빈 틀, PR-001 job 칸 비어 있음, CH-002 주근깨 불일치), 확정 문장 안 고침, 3개 질문. `production-session` 열림. 그러나 첫 줄에 `[N]번 [작업명]으로 진행합니다.`가 없음(`kit/instructions.md:41`, `kit/context/tasks.md:58`): "**판단**: '대장 정리'는 2번으로 봤습니다"로 시작 |

## 검사기
프롬프트 없음

## 추가 발견
- 비프롬프트 작업인데 "확인할 것이 3개 있습니다"로 문구를 바꿈(`kit/instructions.md:22` 고정 문장은 프롬프트용) — 허용.

## 키트 결함
- 첫 줄 규칙 미준수(`kit/instructions.md:41`).

## 총평
정리 후보와 질문은 맞고 첫 줄 형식만 빠졌다.
