# real14-C59 다른 작업 셋을 한 번에 — "구름 느리게, 색 맞추고, 3-4 퍼스트 프레임도" (1턴) — PASS 0 / 부분 1 / FAIL 0 (real13: PASS 0 / 부분 1 / FAIL 0)

G1: 메타상 `mcp__` 도구 호출 없음, RUN 밖 읽기 없음(PASS). `git status`의 `PLAYER-RULES.md`·`SKILLS-INDEX.md` 삭제는 실행기 흔적.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 내용은 맞음: 제안 순서 "14 → 11 → 22, 이번에는 14번만", 1-1은 확정 영상이 없어 "느리게"는 새 배경 영상 프롬프트의 값, `video-prompt` SKILL·`background.md` 열고 질문 3개(구름 이동량 2%·다른 움직임·Keep)를 제안값과 함께, 3-2는 "영상이 아직 없어서 색을 잴 대상이 없습니다", 3-4는 장소 뷰 `—`·연속성 "(미정)"이라 뒤로. 생성·정본 수정 없음. 흠: 답의 첫 줄이 "1번이 아니라 14번입니다. 아래 순서로 진행합니다."이고 정확한 문장 "[14]번 배경 영상으로 진행합니다."는 둘째 줄(`kit/instructions.md:12`, `kit/context/tasks.md:8`: 첫 줄은 항상 그 문장). 플레이어가 "1-1"을 1번으로 잠깐 읽고 고친 흔적이 사용자에게 노출됨 |

## real13 감점 해소 여부
- ① 영상 없는 1-1을 15번으로 시작했다가 14번으로 뒤집음 / `background.md` 미열람: 해소(14번, `background.md` 열림).
- ② 3-2 막힌 이유를 엉뚱하게 씀: 해소(확정 영상 없음).
- ③ 3-4가 `shot-list.md`에 있는지 확인 안 함: 해소(`shot-list.md` 전체 읽음).
- 새 감점: 첫 줄 앞에 잘못 읽은 번호의 정정 문장.

## 검사기
프롬프트 없음

## 추가 발견
- 구름 이동 "2%"는 이전 영상이 없어 기준 없이 정한 값이라고 이유를 밝힘(좋음). §0 속도 줄의 "절반/두 배"는 영상이 있을 때의 규칙.

## 키트 결함
- `kit/instructions.md:31`(규칙 10) "If an earlier report was wrong, correct it in the first line"이 `:12`의 "첫 줄은 항상 [N]번 …"과 충돌해, 플레이어가 자기 번호 정정을 첫 줄에 씀. 고침: 규칙 10을 "correct it in the line right after the task line"으로.
- `kit/context/tasks.md:8`: 번호를 정하기 전에 파일을 읽어야 하는 경우의 순서가 없음. 고침: "Write the task line before reading files; if reading changes the number, show only the final number".
- "[14]번" 대괄호(C49 참고).

## 총평
작업 선택·막힌 이유·질문은 모두 맞았지만 첫 줄에 번호 정정이 먼저 나왔다.
