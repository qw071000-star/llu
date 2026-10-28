# Claude 컨텍스트 운영 — 사용자 사례 조사

> 컨텍스트에 넣지 않는다. 키트를 왜 이렇게 짰는지 확인할 때 사람이 본다.

조사일은 2026-10-28이다. 웹 검색으로 사용자·실무자 사례 43건을 모았다.
- 개별 페이지 열기는 이 세션의 네트워크 정책에 막혀 있었다. 그래서 검색 결과의 요약을 근거로 삼았다.
- 원문의 세부 수치는 직접 확인하지 못한 것이 있다. 그런 곳에는 "원문 미확인"이라고 적었다.
- 공식 문서와 연구는 사례 수에 넣지 않았다(§I).

---

## 결론 — 여러 사람이 독립적으로 같은 결론에 닿은 것

| # | 결론 | 근거 사례 | 키트에 반영한 곳 |
|---|---|---|---|
| 1 | **항상 읽히는 지침은 짧게 쓴다.** 규칙이 많을수록 덜 지킨다. 권장 길이는 60~200줄이다 | 1, 2, 3, 4, 7, 15 | `kit/instructions.md` 하나만 상시. 약 70줄 |
| 2 | **나머지는 필요할 때만 읽힌다.** 처음에는 이름과 한 줄 설명만, 본문은 쓸 때 연다 | 8, 9, 11, 14, 4 | 스킬 5개. 스킬 안에서도 단계별 파일(인물·장소·소품·그림체·퍼스트 프레임·실사·배경·수정) |
| 3 | **규칙 한 줄 = 실제로 난 실수 하나.** 일반론("잘 써라")은 빼고, 낡은 규칙은 지운다. 기계적으로 검사할 수 있는 것은 도구로 막는다 | 15, 16, 17, 2, 3, 1 | 지침의 각 줄이 오류 대장(E-01~E-47)의 사건에 대응한다. 프롬프트 검사 스크립트 `check_prompt.py` |
| 4 | **상태와 결정은 대화가 아니라 파일에 둔다.** 새 세션은 파일만 읽고 이어 간다 | 19, 20, 25, 31, 18 | 정본 세 개, 컷 카드, 핸드오프, Higgsfield `승인`·`거절` 폴더 |
| 5 | **세션은 짧게 쓰고 인계 문서로 넘긴다.** 길게 끌며 압축하는 것보다 낫다 | 18, 21, 22, 23, 24, 26 | 핸드오프 40줄 이하. 컷 승인이나 왕복 8회가 넘으면 새 대화 |
| 6 | **모델이 기다리며 반복 조회하게 두지 않는다.** 조회할 때마다 대화 전체가 다시 처리된다 | 27, 28, 29, 30 | 지침 13번, `higgsfield-generation` §3 |
| 7 | **결과물 상태를 명시하고 폴더로 보이게 한다.** 승인·거절·대체됨이다 | 31, 32, 33, 34 | 지침 14번, `higgsfield-generation` §4 |
| 8 | **Claude 앱 프로젝트 지식은 작게 유지한다.** 목적별로 프로젝트를 나누고, 지식에는 핵심 자료만 둔다 | 5, 6, 7, 35, 36, 37 | 프로젝트 지식에는 그 작품의 정본 세 개만 둔다. 가이드는 스킬로 |
| 9 | **고칠 때는 필요한 부분만 준다.** 전체 문서 대신 해당 절만 준다 | 11, 12 | 확정 프롬프트는 job에서 가져오고, 수정 표의 해당 줄만 읽고, 바뀐 줄만 보인다 |

---

## 사례 목록

### A. 상시 지침을 짧게

| # | 누구 | 한 일 | 출처 |
|---|---|---|---|
| 1 | HumanLayer (Kyle Mistele, "Writing a good CLAUDE.md") | 루트 파일은 60줄 미만으로 쓴다(일반 기준은 300줄 미만). 작업별 지침은 별도 파일로 두고 루트에는 목록과 한 줄 설명만 둔다. 코드 조각 대신 `file:line` 포인터를 쓴다 | [understandingdata.com](https://understandingdata.com/posts/writing-a-good-claude-md), [요약(중국어)](https://redreamality.com/cn/garden/notes/library/writing-a-good-claude-md/) |
| 2 | CLAUDE.md 가이드 작성자들 | 규칙을 더할수록 덜 따른다. 매 세션 읽히니 짧게 쓴다. "잘 짜라" 같은 일반론은 무게만 늘린다. 규칙은 지켰는지 검사할 수 있게 쓴다 | [crystl.dev](https://crystl.dev/guides/claude-md-best-practices/), [memx.app](https://memx.app/blog/claude-md-best-practices/), [techsy.io](https://techsy.io/blog/claude-md-best-practices) |
| 3 | Peter Steinberger (Steven Gonsalvez 정리) | AGENTS.md를 계속 고치고 낡은 지침은 지운다. "반쯤 틀린 긴 파일보다 짧은 파일"이 낫다 | [dev.to](https://dev.to/stevengonsalvez/peter-steinberger-says-just-talk-to-it-and-hes-mostly-right-37bh) |
| 4 | Tyler Burnam | 최상위 CLAUDE.md에는 큰 그림만 두고, 세부 파일을 가리키게 나눈다 | [Medium](https://tylerburnam.medium.com/how-i-use-claude-code-c73e5bfcc309) |
| 5 | 한국 사용자 블로그(브런치 @gdolwon 외) | 자기소개 같은 맥락 파일은 2,000단어 이내로 쓴다. 안 쓰는 기능은 끈다. 무거운 파일은 텍스트로 바꿔 올린다. 폴더를 통째로 넣지 않는다 | [brunch](https://brunch.co.kr/@gdolwon/28), [aimatters](https://aimatters.co.kr/ai-tool/43930/) |
| 6 | 위키독스 「클로드 효율적 활용법」 | 용도별로 프로젝트를 나눈다. 지침은 간결하게, 지식은 핵심 자료만 둔다 | [wikidocs](https://wikidocs.net/424221) |
| 7 | 프로젝트 설정 가이드 작성자들 | 명확한 300단어 지침이 2,000단어 에세이보다 낫다. 지식 파일은 주제를 좁히고 이름을 분명히 붙인다 | [ivee.jobs](https://ivee.jobs/blog/what-are-claude-projects-setup-guide), [handsonai](https://handsonai.info/platforms/claude/projects/claude-projects-setup/) |

### B. 필요할 때만 읽기

| # | 누구 | 한 일 | 출처 |
|---|---|---|---|
| 8 | Simon Willison | Skills는 시작할 때 짧은 설명만 읽고, 관련될 때 본문을 연다. MCP보다 큰 변화일 수 있다고 봤다 | [simonwillison.net](https://simonwillison.net/2025/Oct/16/claude-skills/) |
| 9 | Tyler Folkman | Skills가 컨텍스트 창 문제를 푸는 방식 정리 | [substack](https://tylerfolkman.substack.com/p/the-complete-guide-to-claude-skills) |
| 10 | Shrivu Shankar | Claude Code 기능별로 쓰는 것과 안 쓰는 것을 정리한 참고 글(세부 원문 미확인) | [conffab 재게시](https://conffab.com/?p=9667) |
| 11 | Addy Osmani | 스펙을 먼저 쓰고 작게 나눠 진행한다. 5,000단어 스펙 전체 대신 지금 작업하는 절(예: 인증)만 준다 | [addyosmani.com](https://addyosmani.com/blog/ai-coding-workflow/) |
| 12 | Armin Ronacher | 도구 출력은 빠르고 분명하게 한다. MCP보다 CLI를 쓴다. 서브에이전트로 컨텍스트가 썩는 것을 피한다 | [lucumr.pocoo.org](https://lucumr.pocoo.org/2025/6/12/agentic-coding/) |
| 13 | Charlie Hills | 조사와 초안 작업을 서브에이전트에 맡겨 메인 대화 밖에 둔다 | [substack](https://charliehills.substack.com/p/claude-code-for-normal-people) |
| 14 | Claude Code 이슈 보고자들 | `.claude/rules`의 `paths` 조건부 로딩이 버전에 따라 안 되거나 시작할 때 모두 읽혔다. `/memory`로 확인하라는 결론 | [#22170](https://github.com/anthropics/claude-code/issues/22170), [#17204](https://github.com/anthropics/claude-code/issues/17204) |

### C. 실수를 규칙으로

| # | 누구 | 한 일 | 출처 |
|---|---|---|---|
| 15 | Boris Cherny (Claude Code 개발자) | 팀이 공유 CLAUDE.md를 git에 둔다. Claude가 틀릴 때마다 한 줄을 추가한다. 개인 파일은 공유 파일을 가리키는 두 줄뿐이다. 안전한 명령은 설정에 미리 허용한다 | [InfoQ](https://infoq.com/news/2026/01/claude-code-creator-workflow/), [paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code) |
| 16 | Mitchell Hashimoto | AGENTS.md의 한 줄 한 줄이 과거의 실패 하나다. 스크립트 같은 도구로도 막는다("harness engineering") | [mitchellh.com](https://mitchellh.com/writing/my-ai-adoption-journey) |
| 17 | Kieran Klaassen (Every) | "compound engineering": 작업마다 배운 것을 기록해 다음에 쓴다. 공식 플러그인은 배운 것을 한 건씩 문서로 두고, CLAUDE.md에는 가리키는 줄만 둔다 | [creatoreconomy.so](https://creatoreconomy.so/p/how-to-make-claude-code-better-every-time-kieran-klaassen) |

### D. 세션 인계와 상태 파일

| # | 누구 | 한 일 | 출처 |
|---|---|---|---|
| 18 | Dex Horthy (HumanLayer) | 의도적으로 자주 압축해 컨텍스트 사용량을 40~60%로 유지한다. 조사 → 계획 → 구현 순서로 하고, 사람은 계획 문서를 검토한다 | [ai.engineer](https://ai.engineer/talks/rmvDxxNubIg-context-engineering-for-complex-codebases), [deepwiki](https://deepwiki.com/humanlayer/advanced-context-engineering-for-coding-agents) |
| 19 | Harper Reed | `spec.md` → `prompt_plan.md` → `todo.md` 순서로 만든다. 체크리스트가 세션 사이의 상태를 지킨다 | [harper.blog](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/) |
| 20 | Geoffrey Huntley | "Ralph" 반복: 매번 새 컨텍스트로 시작하고 상태는 파일에 둔다 | [정리 글](https://ai.plainenglish.io/he-ran-claude-in-a-loop-for-three-months-it-built-him-a-programming-language-712ffff48a56) |
| 21 | YK (ykdojo) | `HANDOFF.md`로 미리 압축한다. 최근 맥락만 가진 새 대화로 반쪽 복제한다 | [claude-code-tips](https://github.com/ykdojo/claude-code-tips) |
| 22 | Mejba Ahmed | handoff 스킬로 `/compact`를 대신해 여러 세션 흐름으로 나눴다 | [mejba.me](https://www.mejba.me/blog/handoff-skill-claude-code-multi-session) |
| 23 | claude-handoff 플러그인 작성자 | `/handoff`로 인계 문서를 쓰면 새 세션 시작 때 자동으로 주입된다 | [GitHub](https://github.com/392fyc/claude-handoff) |
| 24 | session-handoff 스킬 작성자 | 인계 문서는 250줄 목표, 400줄 상한이다. 읽는 사람은 다음 세션의 Claude다 | [skillselion](https://skillselion.com/skills/davila7/claude-code-templates/session-handoff) |
| 25 | Steve Yegge | Beads: 할 일과 의존 관계를 git 기반 트래커에 둔다. 지침에 "세션 시작·끝에 확인"이라고 써야 에이전트가 쓴다 | [virtuslab](https://virtuslab.com/blog/ai/beads-give-ai-memory/) |
| 26 | artificialcorner 필자 | 사용 한도에 걸리지 않으려고 긴 대화를 요약해 새 대화로 넘긴다(결정, 미결, 다음 단계) | [artificialcorner](https://artificialcorner.com/p/claude-limits-fix) |

### E. 기다리지 않기와 알림

| # | 누구 | 한 일 | 출처 |
|---|---|---|---|
| 27 | apidog | 추론 루프 안에서 폴링하면 매번 한 턴과 이전 대화 전체가 비용이다. 4분 작업을 2초 간격으로 보면 약 120턴이다 | [apidog](https://apidog.com/blog/ai-agent-long-running-api-operations/) |
| 28 | Upstash | 폴링은 모델이 아니라 호스트가 하고, 모델 컨텍스트에서 뺀다 | [upstash](https://upstash.com/blog/mcp-tasks-and-events) |
| 29 | iboss-ptk | 작업이 끝나면 Stop 훅으로 휴대폰 알림(ntfy)을 받는다. 30초 넘은 세션만 보낸다 | [gist](https://gist.github.com/iboss-ptk/3c036277237f4e483447a9f450244e58) |
| 30 | alexop.dev 필자 | Claude Code 알림 훅(Stop, Notification) 설정 | [alexop.dev](https://alexop.dev/posts/claude-code-notification-hooks/) |

### F. 결과물 상태와 폴더

| # | 누구 | 한 일 | 출처 |
|---|---|---|---|
| 31 | AI 크리에이티브 실무자들 | 상태(탐색, 검토 가능, 승인, 거절)를 파일에 붙여 두고 채팅에 두지 않는다 | [tilnote](https://tilnote.io/pages/6a8815ccc6e5775b117819c5), [hackernoon](https://hackernoon.com/your-ai-creative-stack-has-a-missing-data-type-approved) |
| 32 | oakgen | 교체된 승인본은 "대체됨" 상태로 남겨 기록을 보존한다 | [oakgen](https://oakgen.ai/blog/codex-marketing-images-mcp) |
| 33 | Lottiefiles 도움말 | 단계별 폴더(진행 중, 검토, 승인)와 승인 태그 | [help.lottiefiles.com](https://help.lottiefiles.com/managing-digital-assets) |
| 34 | Pippit | 파일 이름에 프로젝트, 용도, 상태, 버전을 넣는다 | [pippit](https://www.pippit.ai/blog/naming-assets-high-volume-ai-video-project) |

### G. Claude 앱 프로젝트

| # | 누구 | 한 일 | 출처 |
|---|---|---|---|
| 35 | Freshvanroot | 몇 달 매일 써 보니 토큰 한도 때문에 올릴 파일을 신중히 골라야 했다 | [freshvanroot](https://freshvanroot.com/blog/how-to-use-claude-projects/) |
| 36 | practicalbyai 외 | 지식이 커지면 검색(RAG) 모드로 바뀌고, 사용자가 모드를 고를 수 없다. 큰 파일 몇 개가 자리를 다 차지한다 | [practicalbyai](https://practicalbyai.substack.com/p/when-you-drop-a-40-page-file-into), [fast.io](https://fast.io/resources/claude-project-file-limit/) |
| 37 | Your Creative Edge | 목적이 다른 일을 프로젝트 세 개로 나눴다 | [substack](https://yourcreativeedge.substack.com/p/why-i-built-three-different-claude) |
| 38 | Reddit 소설 작가 | 스토리 바이블이 도움은 되지만 문체 표류는 막지 못했다. 대표 문단을 매번 함께 줘야 했다 | [Reddit 스냅샷](https://reddit.sentinel-team.org/posts/1rb65g7/snapshots/2026-02-22T02%3A21%3A26.610158Z) |

### H. Claude로 AI 영상 만들기

| # | 누구 | 한 일 | 출처 |
|---|---|---|---|
| 39 | SSuperWasabi (브런치) | Claude가 컷 구성, 스토리보드, 프롬프트를 쓰고 Higgsfield MCP가 생성했다. Claude Code는 한 줄 지시로 업로드, 이미지→영상, ffmpeg 합본까지 했다 | [205](https://brunch.co.kr/@ssuperwasabi/205), [208](https://brunch.co.kr/@ssuperwasabi/208) |
| 40 | OSideMedia | Higgsfield 프롬프트 스킬: 8단계 과정을 거친다. 같은 인물 설명문을 매 프롬프트에 그대로 쓴다 | [claudeskills.info](https://claudeskills.info/skills/OSideMedia/higgsfield-ai-prompt-skill/) |
| 41 | Ethan McDonnell | Higgsfield용 Claude 스킬 묶음(Seedance 스타일 15종) | [GitHub](https://github.com/EthanMcDonnell/claude-higgsfield) |
| 42 | maciejdzierzek | Kling 프롬프트 생성 스킬: 사용자가 다른 언어로 말해도 프롬프트는 영어로 쓴다 | [openskillindex](https://openskillindex.com/skills/maciejdzierzek-kling-ai-prompt-generator-kling-ai) |
| 43 | MindStudio (벤더 글) | 프로젝트 지침에 파일 이름 규칙을 둔다. 승인된 인물 정보는 캐릭터 폴더에서 매 장면 프롬프트로 넣는다. 보내기 전에 점검한다 | [mindstudio](https://www.mindstudio.ai/blog/ai-film-production-workflow-claude-code-mcp) |

### I. 연구와 공식 문서 (사례 수에 넣지 않음)

- **Chroma "Context Rot" (2025-07):** 18개 모델 모두 입력이 길수록 성능이 떨어졌다. 컨텍스트 한도에 닿기 훨씬 전부터다. [정리](https://www.zenml.io/llmops-database/context-rot-evaluating-llm-performance-degradation-with-increasing-input-tokens)
- **Anthropic 사용 한도 도움말:** 프로젝트에 올린 내용은 캐시되어, 다시 쓸 때 한도에서 덜 차감된다. 긴 대화일수록 많이 쓴다. [support](https://support.anthropic.com/en/articles/9797557-usage-limit-best-practices)
- **Anthropic 프로젝트 RAG:** 지식이 컨텍스트 한도에 가까워지면 자동으로 검색 모드가 된다. [support](https://support.anthropic.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)
- **Anthropic Skills 도움말:** Pro·Max에서 zip으로 업로드한다. 코드 실행이 켜져 있어야 하고, 사용자 개인 단위다. [support](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- **Anthropic Agent Skills 글:** 설명 → SKILL.md 본문 → 딸린 파일의 3단계로 필요한 만큼만 읽는다. [claude.com](https://www.claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills)
- **MCP Tasks 확장:** 오래 걸리는 작업은 핸들을 바로 돌려주고 나중에 확인하게 하는 표준이다. [modelcontextprotocol.io](https://modelcontextprotocol.io/extensions/tasks/overview.md)

---

## 짚어 둘 점

- **Claude 앱 프로젝트 지식의 비용:** 캐시 덕분에 사용 한도 비용은 크지 않다(Anthropic 설명).
  - 문제는 주의력이다. 모든 대화가 모든 가이드를 함께 읽으면 정작 필요한 규칙이 묻힌다(context rot).
  - 지식이 커지면 검색 모드로 바뀌어, 필요한 규칙을 못 찾을 수도 있다.
  - 그래서 가이드는 스킬로 옮기고, 지식에는 정본만 둔다.
- **`.claude/rules`의 조건부 로딩:** 버전마다 동작이 달랐다는 보고가 있다(14). 그래서 Claude Code에서도 rules 대신 skills로 나눴다.

## 반영하지 않은 것

| 사례 | 이유 |
|---|---|
| 서브에이전트로 조사 분리(12, 13) | Claude 앱 대화에는 서브에이전트가 없다. Claude Code에서 쓸 수 있지만, 영상 제작 흐름에는 꼭 필요하지 않다 |
| Beads 같은 별도 트래커(25) | 이 작업은 컷 수십 개 규모다. 컷 목록 표와 Higgsfield 폴더로 충분하다 |
| 알림 훅(29, 30) | Claude Code 전용이고, Higgsfield 렌더는 서버에서 끝난다. 사용자가 Higgsfield 앱에서 완성을 본다. 필요하면 README의 선택 사항으로 둔다 |
| 컨텍스트 40~60% 유지(18) | Claude 앱에는 사용량 계기판이 없다. 대신 "컷 승인 또는 왕복 8회"라는 대리 기준을 썼다 |
