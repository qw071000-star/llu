# 채점 규칙 — 채점자

맡은 체인마다 다음을 한다. 플레이어(다른 Claude)는 키트만 보고 일했다. 당신은 그 결과가 키트 규칙대로인지 판정한다.

## 입력
- 시나리오와 기대: `tests/agent-eval/scenarios.md` (공통 기대 G1~G6 + 체인별 기대)
- 플레이어 출력: `runs/<체인>/out/turn*.md` (turn0은 미리 넣어 둔 앞 대화)
- 플레이어가 고친 정본: `cd runs/<체인> && git status --short && git diff` (커밋 `base`가 시작 상태)
- 키트 원문: `kit/instructions.md`, `kit/skills/**`
- 고정 문장: `tests/agent-eval/testbed/grade/*.lines`

## 할 일
1. 체인의 턴마다 기대 항목에 판정을 붙인다: **PASS / FAIL / 부분**.
   - 판정마다 근거를 붙인다: 출력 인용 한 줄, 또는 diff 한 줄.
2. 프롬프트(코드블록)가 있으면 파일로 뽑아 검사기를 돌린다.
   - 실행: `python3 kit/skills/higgsfield-generation/check_prompt.py --kind <video|image> <파일> [--refs N] [--seconds N] [--must-include <여러 .lines를 합친 파일>]`
   - 결과 줄을 그대로 붙인다.
   - 영상 프롬프트에는 `identity_grandpa.lines`를 넣지 않는다(컷 프롬프트에는 WARDROBE 문장만, `image-prompt/character.md` 기록).
   - 기대에 없는 WARN이라도 근거가 있으면 FAIL로 친다. 오탐이면 "검사기 오탐"으로 적는다.
3. 기대 밖이라도 키트 규칙 위반을 보면 "추가 발견"에 적는다. 위치를 `kit/...:줄`로 단다.
4. **키트 결함**을 따로 적는다. 가장 중요하다.
   - 플레이어가 틀린 원인이 키트 문서에 있는 경우다. 규칙이 모호하거나, 서로 모순되거나, 빠졌거나, 찾기 어려운 곳에 있는 경우를 말한다.
   - 결함마다 무엇을 어떻게 고칠지 한 줄로 제안한다.
5. 플레이어가 RUN 밖을 읽었거나 실제 mcp 도구를 불렀으면 G1 FAIL이다. 메타와 출력으로 확인한다.

## 출력
- `tests/agent-eval/results/<체인>.md`에 쓴다. 들어갈 것:
  - 턴별 판정표
  - 검사기 결과
  - 추가 발견
  - 키트 결함
  - 총평 한 줄
- 오케스트레이터에게는 체인별 한 줄씩만 돌려준다: `PASS n / 부분 n / FAIL n`, 그리고 키트 결함 요약.
- 기대가 키트와 어긋난다고 판단하면 "기대 오류"로 적는다. 명세가 틀렸을 수도 있다.
