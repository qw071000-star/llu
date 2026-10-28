# llu — AI 이미지·영상 제작 지침 키트

「어머니와 고등어」(실사 단편), 나부코 '히브리 노예들의 합창'(수채 배경 영상), The Prompter 분석, Higgsfield 생성 기록 930건에서 확인된 규칙과 실수를 모아 **어느 작품에나 넣어 쓰게** 만든 Claude용 키트다.

| 누가 | 무엇을 본다 |
|---|---|
| 처음 쓰는 팀원 | [`TEAM-GUIDE.md`](TEAM-GUIDE.md) — 설치, 하루 작업 흐름, 문제가 생겼을 때 |
| 에셋·이미지·영상을 만드는 사람 | Claude Docs 「AI 제작 가이드 — 에셋·장소·소품·이미지·영상」 — 만드는 법과 주의할 점 요약 |
| 키트를 고치는 사람 | 이 파일 |

## 구조

```
kit/                       ← 다른 프로젝트에 넣는 것 (이것만 공유한다)
  instructions.md          [항상 읽힘] 지침 칸 / CLAUDE.md. 규칙 10개 + 읽기 지도. 4,000자 이하
  skills/                  [그 작업 때만] 스킬 6개. 스킬 안에서도 읽기 지도가 가리키는 파일만 연다
    project-setup/         새 작품: 질문 한 번, 정본 초안, Higgsfield 폴더
    production-session/    세션 시작·컷 카드·핸드오프·정본 관리, ok-reuse("3-1처럼")
    higgsfield-generation/ 생성 전 점검·폴더·승인/거절·OK 기록·크레딧 + check_prompt.py
    image-prompt/          공통 + character / location(+ location-view, location-edit) / prop / style / first-frame
    video-prompt/          공통 + live-action / background / fixes / rerender
    acting/                인물 연기
  project-files/           작품마다 복사해 채우는 정본 틀 + Claude Code용 CLAUDE.md
  dist/*.zip               Claude 앱에 올리는 스킬 묶음 (pack-skills.sh로 다시 만든다)
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

**무엇을 언제 읽는지는 `kit/instructions.md`의 "읽기 지도" 표 하나가 정한다.** 스킬 안의 표는 그 스킬 안에서 고르는 것만 정한다.

## 설치

- **Claude 앱:** `TEAM-GUIDE.md` §3. 스킬 zip 6개를 계정에 올리고, 작품 프로젝트의 지침 칸에 `kit/instructions.md`를 붙인다. 프로젝트 지식에는 시나리오·콘티 정도만 넣는다. `reference/`·`archive/`는 넣지 않는다.
- **Claude Code (작품 리포):**

```bash
mkdir -p .claude project/cuts project/log
cp kit/instructions.md .claude/instructions.md
cp -r kit/skills .claude/skills
cp kit/project-files/CLAUDE.md CLAUDE.md
cp kit/project-files/{decisions,asset-registry,shot-list,ok-cuts}.md project/
```

## 키트를 고칠 때

- **새 실수:** `reference/error-registry.md` 맨 아래에 E-48부터 적고, 막는 규칙을 `kit/`의 한 파일에 한 줄로 넣는다. 모든 대화에 해당하면 `instructions.md`, 특정 작업이면 그 스킬.
- **규칙은 한 곳에만 쓴다.** 다른 파일에는 주인 파일을 가리키기만 한다. 주인 표는 `tests/run_kit_tests.py`의 "한 곳" 점검에 있다. 예외는 프롬프트에 글자 그대로 들어가는 영어 문장(틀 안의 고정 문장)뿐이다.
- **원본 문장을 줄이지 않는다.** 원본에서 효과가 확인된 영어 문장은 단계 파일의 틀에 그대로 둔다. 설명은 줄여도 문장은 줄이지 않는다.
- **새 단계 파일을 만들면** 지침의 읽기 지도에 한 줄을 더한다(없으면 점검이 실패한다).
- **한 번만 확인된 것은 "관찰"로 적는다.** 서로 다른 사례 두 개가 모이면 규칙으로 올린다.
- **kit 안에는 규칙과 빈 틀만 둔다.** 사례·작품 이름·통계는 `reference/`에. 이전 작품의 고유 명사는 새 작품 프롬프트로 샌다.
- **고친 뒤:** `python3 tests/run_kit_tests.py` → `kit/pack-skills.sh`로 zip 다시 만들기 → 팀에 zip 다시 배포.
