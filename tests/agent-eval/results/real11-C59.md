# real11-C59 다른 작업 셋을 한 번에 — "구름 느리게, 색 맞추고, 3-4 퍼스트 프레임도" (1턴) — PASS 0 / 부분 1 / FAIL 0 (real9: PASS 0 / 부분 1 / FAIL 0 → real10 재실행 PASS)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 맞은 것: 세 작업에 번호를 달아 순서 제안("1. 14번 배경 영상 … 2. 22번 색 맞추기 … 3. 11번 퍼스트 프레임, 세 요청은 이 순서로 하나씩 진행"), 첫 작업(1-1 구름)만 질문 3개로 묻고 나머지 둘의 프롬프트·질문은 미룸(`must-ask.md` Flag first "Several tasks in one message"). 1-1에 확정 영상이 없다고 정확히 짚음("시작 이미지만 승인 … 더 느리게를 줄일 기준 값이 없습니다"), 이미 영상이 있으면 `Motion` 줄만 전 → 후라고 안내. 프롬프트·생성 없음. **감점:** (1) `background.md`를 열지 않고 `video-prompt/SKILL.md`만 열어(14번 행은 `background.md`) 규칙을 놓침: 카메라를 질문 2번으로 물음(고정이 `decisions.md` §4에 있으므로 "기본값으로 씀" 줄에 넣을 것, `background.md`·`must-ask.md` Never ask). 구름 외 움직임도 질문으로 만듦. (2) 길이를 "배경 영상 기본값(10~15초)"으로 잘못 씀 — `decisions.md` §1이 "컷당 8초"로 정본에 있으므로 8초여야 함(`video-prompt/SKILL.md:78` "Follow the canon's cut length"). (3) "보통 속도를 약 6%로 보고 그 절반"의 근거 없는 수치. (4) 3-2도 확정 영상이 없어 색 맞출 파일이 없다는 점(기대)을 이 답에서 안 짚음 |

## 검사기
프롬프트 없음.

## 추가 발견
- G1 위반 없음. 질문 항목 3개 중 실질 질문은 구름 속도 하나뿐이어야 하는데 기본값 줄에 넣을 항목을 질문으로 올림(`must-ask.md` Never ask: camera/length).

## 키트 결함
- `kit/skills/video-prompt/SKILL.md:78`의 "background 10-15 s" 기본값이 "Follow the canon's cut length"와 같은 칸에 붙어 있어 정본 길이(8초)를 두고 10~15초를 고르는 오독이 난다. 제안: "(canon first: `decisions.md` §1 cut length; the 10-15 s default applies only when the canon has none)"을 앞에 명시하고, `kit/context/tasks.md:30` 14번 행에 "open `background.md` before asking"을 굵게 쓴다.
- `kit/context/tasks.md:10`·`must-ask.md:17`의 "Several tasks in one message" 규칙에는 첫 작업만 묻되 나머지 둘이 막힌 이유(3-2 확정 영상 없음, 3-4 정보 부족)를 한 줄씩 알리라는 문장이 없다. 제안: "Name in one line why each deferred task is blocked, ask nothing about it."

## 총평
순서 제안·첫 작업만 질문은 지켰으나 배경 영상 규칙(카메라·길이 기본값)을 읽지 않아 정본과 어긋난 질문을 만들었다.
