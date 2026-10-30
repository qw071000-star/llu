# llu — AI 이미지·영상 제작 지침 키트

「어머니와 고등어」(실사 단편), 나부코 '히브리 노예들의 합창'(수채 배경 영상), The Prompter 분석, Higgsfield 생성 기록 930건에서 확인된 규칙과 실수를 모아 **어느 작품에나 넣어 쓰게** 만든 Claude용 키트다.

| 누가 | 무엇을 본다 |
|---|---|
| **처음 보는 사람 (여기부터)** | [`guides/한눈에-보기.md`](guides/한눈에-보기.md) — 어떤 스킬이 있고, 어떤 순서로, 무슨 말을 하면 되는지 한 장으로 |
| 써 보기 전에 | [`guides/알아둘-것.md`](guides/알아둘-것.md) — Claude가 실제로 움직이는 방식, 결과가 이상할 때, 크레딧 아끼기, 알려진 약점 |
| 작업 번호로 고르기 | [`guides/할일-목록.md`](guides/할일-목록.md) |
| 처음 쓰는 팀원 | [`TEAM-GUIDE.md`](TEAM-GUIDE.md) — 설치, 하루 작업 흐름, 문제가 생겼을 때 |
| 에셋·이미지·영상을 만드는 사람 | Claude Docs 「AI 제작 가이드 — 에셋·장소·소품·이미지·영상」 — 만드는 법과 주의할 점 요약 |
| 실사 영상 프롬프트를 읽고 고치는 사람 | [`guides/15블록-가이드.md`](guides/15블록-가이드.md) — 15블록마다 들어가는 것, 예시 문장, 자주 틀리는 것, 어디서 가져오나 |
| 작업을 지시하는 제작자 | [`guides/작업별-팁.md`](guides/작업별-팁.md) — 작업마다 이렇게 말하면 되는 것, Claude가 묻는 것, 흔한 실패, 크레딧 아끼는 법 |
| 키트를 고치는 사람 | 이 파일 |

## 구조

```
kit/                       ← 다른 프로젝트에 넣는 것 (이것만 공유한다)
  instructions.md          [항상 읽힘] 규칙 11개, 대화 시작 순서, 출력 (영어, 약 1,750토큰 이하)
  context/                 [항상 읽힘] tasks.md = 할 일 목록 23개(사용자 말 → 작업 번호 → 스킬), 애매하면 "이 작업을 할까요?" 확인
                                     must-ask.md = 묻지 않을 것 / 먼저 짚을 것 (작업별 질문은 각 스킬의 "필요한 정보" 표)
  skills/                  [그 작업 때만] 스킬 9개. 스킬 안에서도 tasks.md가 가리키는 파일만 연다
    project-setup/         새 작품: 질문 한 번, 정본 초안, Higgsfield 폴더
    production-session/    세션 시작·컷 카드·핸드오프·정본 관리, ok-reuse("3-1처럼")
    higgsfield-generation/ 생성 전 점검·폴더·승인/거절·OK 기록·크레딧 + check_prompt.py
    image-prompt/          공통 + character / location(+ location-view, location-edit) / prop / style / first-frame
    video-prompt/          공통 + live-action / background / fixes / rerender
    acting/                인물 연기
    shot-design/           대본 한 장면 → 블로킹·180도 선·커버리지·컷 길이(컷 카드 이전, 제안만)
    assembly/              Claude Code + ffmpeg: 마지막·지정 프레임, 러프컷 concat, 경계 비교 + assemble.py
    color-continuity/      Claude Code + ffmpeg: 컷 간 색·밝기 재기, 기준 컷에 1차 맞춤, 비교 이미지 + color.py
  project-files/           작품마다 복사해 채우는 정본 틀 + Claude Code용 CLAUDE.md·settings.json
  dist/*.zip               Claude 앱에 올리는 스킬 묶음 (pack-skills.sh로 다시 만든다)
  dist/project-instructions.md  Claude 앱 지침 칸에 붙일 한 파일(지침 + context 둘)
reference/                 [컨텍스트에 넣지 않음] 사람이 근거를 볼 때만
  error-registry.md        오류 대장 E-01~E-47
  higgsfield-history.md    Higgsfield 전 프로젝트 분석: 잘된 것·안 된 것·크레딧
  source-index.md          원본 자료가 키트 어디에 들어갔나
  kit-test-report.md       키트 시험 결과
tests/                     [컨텍스트에 넣지 않음]
  run_kit_tests.py         키트를 고칠 때마다 돌린다
  fixtures/                검사기 통과·실패 예시 프롬프트
  agent-eval/              서브에이전트 맹검 시험(시험 작품, 시나리오, 채점 결과)
archive/어머니와-고등어/     [컨텍스트에 넣지 않음] 원본 문서. 그 작품을 이어갈 때나 근거 확인용
```

**무엇을 언제 여는지는 `kit/context/tasks.md`, 무엇을 꼭 묻는지는 `kit/context/must-ask.md`가 정한다.** 둘 다 지침과 함께 항상 읽힌다. 스킬 안의 표는 그 스킬 안에서 고르는 것과 틀의 자리만 정한다.

## 설치

- **Claude 앱:** `TEAM-GUIDE.md` §3. 스킬 zip 9개를 계정에 올리고, 작품 프로젝트의 지침 칸에 `kit/dist/project-instructions.md`(지침 + tasks + must-ask)를 붙인다. 프로젝트 지식에는 시나리오·콘티 정도만 넣는다. `reference/`·`archive/`는 넣지 않는다.
- **Claude Code (작품 리포):**

```bash
mkdir -p .claude project/cuts project/log
cp kit/instructions.md .claude/instructions.md
cp -r kit/context .claude/context
cp -r kit/skills .claude/skills
cp kit/project-files/CLAUDE.md CLAUDE.md
cp kit/project-files/settings.json .claude/settings.json   # 검사기(check_prompt.py)·조립(assemble.py)·색(color.py) 실행 허용
cp kit/project-files/{decisions,asset-registry,shot-list,ok-cuts}.md project/
echo "tmp/" >> .gitignore   # 검사용 임시 프롬프트 파일(지침 "검사")
```

## 키트를 고칠 때

- **새 실수:** `reference/error-registry.md` 맨 아래에 E-48부터 적고, 막는 규칙을 `kit/`의 한 파일에 한 줄로 넣는다. 모든 대화에 해당하면 `instructions.md`, 특정 작업이면 그 스킬.
- **규칙은 한 곳에만 쓴다.** 다른 파일에는 주인 파일을 가리키기만 한다. 주인 표는 `tests/run_kit_tests.py`의 "한 곳" 점검에 있다. 예외는 프롬프트에 글자 그대로 들어가는 영어 문장(틀 안의 고정 문장)뿐이다.
- **원본 문장을 줄이지 않는다.** 원본에서 효과가 확인된 영어 문장은 단계 파일의 틀에 그대로 둔다. 설명은 줄여도 문장은 줄이지 않는다.
- **새 단계 파일을 만들면** `context/tasks.md` 표와 `guides/할일-목록.md`에 같은 번호로 한 줄씩 더하고, 묻는 것은 그 스킬의 "필요한 정보" 표에, 먼저 짚을 것만 `context/must-ask.md`에 더한다(tasks.md에 없으면 점검이 실패한다).
- **AI에게 주는 파일(`kit/`)은 영어로 쓴다.** 사용자에게 하는 한국어 문장, 사용자 말 예시, 정본 칸 이름만 한국어로 둔다. 정본 틀(`kit/project-files/*.md`)은 팀이 읽으므로 한국어다. 옛 한국어 지침은 사람용 참고로 `guides/지침-한국어/`에 있다.
- **한 번만 확인된 것은 "관찰"로 적는다.** 서로 다른 사례 두 개가 모이면 규칙으로 올린다.
- **kit 안에는 규칙과 빈 틀만 둔다.** 사례·작품 이름·통계는 `reference/`에. 이전 작품의 고유 명사는 새 작품 프롬프트로 샌다.
- **고친 뒤:** `python3 tests/run_kit_tests.py` → `kit/pack-skills.sh`로 zip 다시 만들기 → 팀에 zip 다시 배포.
