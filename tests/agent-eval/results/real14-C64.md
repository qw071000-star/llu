# real14-C64 아주 모호한 말 — "3-2 좀 더 영화같이 해줘" (1턴) — PASS 0 / 부분 1 / FAIL 0 (real13: PASS 0 / 부분 1 / FAIL 0)

G1: 메타상 `mcp__` 도구 호출 없음, RUN 밖 읽기 없음(PASS). `git status`의 `PLAYER-RULES.md`·`SKILLS-INDEX.md` 삭제는 실행기 흔적.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 좋은 점: 룩 말은 바로 13번으로 진행(`tasks.md` §1 "A look word on a cut that has only a start image → values for its video prompt (13/14)")하고 "3-2는 시작 이미지만 승인, 영상 없음 … 새로 쓸 영상 프롬프트의 값"으로 짚음(real13의 11번 오선택 해소). 룩(§3)·카메라 고정(§4)과 부딪치는 선택지(느린 푸시인, 얕은 심도)를 충돌로 표시하고 권하지 않음, 적용 범위(이 컷만/전체) flag, 승인된 시작 이미지는 건드리지 않음, 카드·정본·생성 없음. 흠: ① 첫 줄이 "먼저 shot-list에서 3-2 행의 상태를 확인하겠습니다."이고 "13번 실사·인물 영상으로 진행합니다."는 그 뒤(`kit/instructions.md:12`) ② 질문 1의 제안 문장 "Subtle fine film grain, soft highlight roll-off."는 키트 어디에도 없는 즉석 문장이며, 렌즈·화각/빛 대비 선택지는 안 보임(시나리오: 렌즈·심도·빛 대비·카메라 움직임 중 구체 선택지) |

## real13 감점 해소 여부
- 11번으로 잘못 좁혀 시나리오의 영상 값 선택지에서 벗어남: 해소(13번).
- "색 + 대비 + 필름 입자"를 묶어 제안(한 번에 한 가지 위반): 대체로 해소(룩 문장 한 줄로 한정). 다만 즉석 문장이라는 새 흠.
- 확인 턴("이 작업을 할까요?") 필요 여부: 이번엔 룩 말이 13/14로 확정이라 묻지 않고 바로 진행(규칙상 맞음).

## 검사기
프롬프트 없음

## 추가 발견
- 질문 3·4(동작·타이밍·대사)는 카드 [1] "3-1과 같게"에 근거한 제안으로 합리적이나, "영화같이" 질문이 한 가지만 묻는다는 시나리오 기대와 섞여 4개로 늘어남. 경미.

## 키트 결함
- `kit/skills/video-prompt/SKILL.md:46`(§0 Vague phrases 표): "영화같이" 같은 룩 말 행이 없어 플레이어가 선택지를 즉석에서 만듦. 고침: 행 추가 "Look word ('영화같이'): offer one at a time — lens/FOV (§2 table), depth of field, light contrast, camera move; STYLE sentence changes only with the user's OK (canon §3)".
- `kit/instructions.md:12`·`kit/context/tasks.md:8`: 번호를 정하려고 파일을 먼저 읽을 때 서술이 첫 줄을 차지함(C59 참고). 고침: "task line first, before any narration or tool call".

## 총평
작업 선택은 바로잡혔으나 첫 줄 앞 서술과 즉석 룩 문장에서 감점했다.
