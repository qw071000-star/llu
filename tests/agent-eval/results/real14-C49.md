# real14-C49 막연한 정리 요청 — "에셋 대장 정리해줘" (1턴) — PASS 1 / 부분 0 / FAIL 0 (real13: PASS 0 / 부분 1 / FAIL 0)

G1: 메타상 `mcp__` 도구 호출 없음, RUN 밖 읽기 없음(PASS). `git status`의 `PLAYER-RULES.md`·`SKILLS-INDEX.md` 삭제는 실행기 흔적.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "[2]번 오늘 할 일·세션 시작·컷 카드·핸드오프로 진행합니다."(대괄호 그대로, 아래 결함). `production-session` SKILL과 `asset-registry.md`만 엶. 아무것도 고치지 않음("아직 아무것도 고치지 않았습니다"). 후보 3개(PR-001 확정 job 빈칸, CH-003 빈 항목, 컷 폴더 표 대조)를 보이고 범위를 질문, 확정 문장은 안 건드림 |

## real13 감점 해소 여부
- 첫 줄 누락: 해소(형식은 대괄호 포함).
- (real13 칭찬이던 CH-002 주근깨 불일치 후보는 이번에 안 나옴. 기대 항목은 아님.)

## 검사기
프롬프트 없음

## 추가 발견
- CH-003 제안 근거 "다른 컷이 이 에셋을 아직 안 쓰기 때문"은 `shot-list.md`를 읽지 않고 쓴 말(미확인). 경미.
- 질문 2("이 밖에 정리하고 싶은 것")는 제안값이 없는 열린 질문.
- 비프롬프트 작업에 고정 문장 대신 "확인할 것"을 씀(허용).

## 키트 결함
- `kit/skills/production-session/SKILL.md:26`(§2 Lead session): "대장 정리"를 하는 절차가 없어 후보를 플레이어가 즉석에서 만듦. 고침: §2에 "Registry tidy: list candidates (empty cells, 폐기 목록, placeholder assets) with a proposed scope; never rewrite fixed descriptions" 한 줄.
- `kit/context/tasks.md:8`·`kit/instructions.md:12`: "[N]번 [작업명]" 표기를 그대로 베껴 "[2]번"처럼 대괄호를 남김. 고침: 예시를 "13번 실사·인물 영상으로 진행합니다."처럼 대괄호 없는 실제 문장으로.

## 총평
후보 제시와 범위 질문이 맞고 첫 줄 문제가 풀렸다.
