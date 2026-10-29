# real11-C37 고해상도 — "2-1 영상 1080p로 뽑아줘" (1턴) — PASS 0 / 부분 1 / FAIL 0 (real9: PASS 1 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 맞은 것: "17번 고해상도 작업" 판단, `video-prompt/SKILL.md`+`rerender.md`만 열음(작업표 17번 행 그대로, `higgsfield-generation`·`live-action.md` 안 열림). OK 대장 2-1 카드의 draft 정보로 "`draft_job_id` `job-v-2-1`에서 1080p 최종본을 만듭니다. 같은 테이크가 그대로 올라가므로 프롬프트를 새로 쓰지 않고", 만료일 2026-10-31 vs 오늘 10-29 "기한 안", 사용자에게 draft였는지 묻지 않음. 낙엽 한계가 남는다고 알림. 보내기 전 확인 질문 2개. 생성 없음. **감점:** (1) `sim/higgsfield.md`를 grep해서 얻은 "480p 8초 약 40 크레딧"을 답에 쓰면서 `[TOOL]` 줄이 없음(플레이어 규칙 4). (2) `get_cost` 견적은 읽기 조회인데 직접 조회하지 않고 "견적을 먼저 볼까요?"를 사용자 질문 2번으로 넘김. 견적이 없으면 "알 수 없음"으로 두는 쪽은 맞음. 아래 키트 결함 1 때문에 `higgsfield-generation` §1 4번(first-time 설정은 `get_cost`)이 안 열려 있음 |

## 검사기
프롬프트 없음(draft 확정 길이라 새 프롬프트 없음). 코드블록 0개.

## 추가 발견
- G1 위반 없음(mcp 호출 없음). 시작 보고 세 줄을 냄(할 일이 생성이라 허용).
- "기본값으로 씀: … 소리 켬(효과음만)" — draft 확정은 설정이 이미 정해진 것이라 무해.

## 키트 결함
1. `kit/skills/video-prompt/rerender.md:3`(첫 불릿)와 `kit/context/tasks.md:35`(17번 행 `Open`)에 "비용 견적(`get_cost`)을 `[TOOL]`로 직접 조회하고 크레딧을 알린 뒤 확인을 받는다"가 없다. 17번은 `video-prompt`만 열어 `higgsfield-generation` §1 4번이 안 읽힌다. 제안: `rerender.md` 맨 위에 "Before sending: quote the 1080p cost with `get_cost: true` (a `[TOOL]` read, no generation), show the number with its basis, and ask once to send" 한 줄.

## 총평
draft_job_id 길은 정확했으나 견적 조회를 사용자에게 떠넘기고 시뮬레이션 인용에 `[TOOL]` 줄을 빼 먹었다.
