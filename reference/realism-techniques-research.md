# 더 사실적이고 지시를 더 잘 따르는 AI 이미지·영상: 사용자 기법 조사

- 조사일: 2026-10-30 · 방법: WebSearch 29회, GitHub 저장소 7개 직접 열람(얕은 clone·raw), 공식 PDF 미러 1개 텍스트 추출. 생성 도구(Higgsfield 포함)는 부르지 않았다.
- 대상 모델: GPT Image 2/2.5, Seedance 2.0/2.5, Kling 3.0/4.0, Veo 3.1, Sora 2, Runway Gen-4, Midjourney, Nano Banana.
- 먼저 읽은 것: `guides/주요-기능.md`, `reference/cinematic-tools-research.md`, `kit/skills/video-prompt/{SKILL,live-action,fixes}.md`, `kit/skills/image-prompt/{SKILL,character}.md`, `kit/skills/acting/SKILL.md`, `kit/skills/higgsfield-generation/check_prompt.py`, `reference/error-registry.md`.

**반영 상태(2026-10-30):** Top 10 중 3(대사 뒤 빈 시간), 6(소수 초·"초당 N번" 검사 경고), 7(비유·관용구 금지)만 키트에 넣었다. 나머지는 넣지 않았다.

**접근 한계(중요).** 이 세션의 네트워크에서는 `developers.openai.com`, `docs.cloud.google.com`, `docs.byteplus.com`, `kling.ai`, `higgsfield.ai`, `runway.com`, `help.runwayml.com`, `blog.google`, reddit 미러(`reddit.sentinel-team.org`)가 열리지 않았다. 그래서 출처를 세 가지로 나눴다.
- **본문 읽음:** GitHub에 올라온 것. OpenAI Cookbook 노트북 2개, ByteDance 공식 GitHub(`bytedance/agentkit-samples`), 화산엔진 Seedance 2.5 공식 PDF의 GitHub 미러, 커뮤니티 스킬 저장소.
- **2차 인용:** 다른 저장소가 공식 문서를 인용한 것. 예: Emily2040 저장소가 옮긴 화산엔진 Seedance 2.0 가이드.
- **검색 요약만:** Kling·Veo·Runway·Higgsfield 블로그, Reddit. 본문을 확인하지 못했으니 신뢰도를 한 단계 낮춰 읽는다.

**신뢰도 표기**

| 표기 | 뜻 |
|---|---|
| **공식 문서** | 모델 회사의 문서·저장소에서 본문을 확인했다(미러 포함) |
| **공식(요약)** | 공식 문서지만 검색 요약이나 2차 인용으로만 봤다 |
| **여러 사용자** | 서로 다른 커뮤니티 출처 두 곳 이상이 같은 말을 한다 |
| **한 사람 주장** | 한 출처뿐이거나 측정 없이 한 팀의 경험만 있다 |

---

## 1. 출처 목록 (34개)

| # | 제목 | URL | 날짜 | 유형 | 읽은 정도 | 한 줄 설명 |
|---|---|---|---|---|---|---|
| S1 | OpenAI Cookbook: GPT Image Generation Models Prompting Guide | https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb (원 페이지 developers.openai.com/cookbook/…) | 모델표 기준일 2026-04-21 | guide(공식) | 본문 | gpt-image-2 기준. 프롬프트 기본기, 사실감, 편집 보존 목록, 다중 이미지 참조 |
| S2 | OpenAI Cookbook: Sora 2 Prompting Guide | https://github.com/openai/openai-cookbook/blob/main/examples/sora/sora2_prompting_guide.ipynb | 2026-03 갱신 | guide(공식) | 본문 | 샷 구조, 박자 단위 동작, 카메라 하나·동작 하나, 팔레트 앵커, 한 번에 하나씩 편집 |
| S3 | ByteDance `byted-ark-seedance-pe` / prompt-guide.md | https://github.com/bytedance/agentkit-samples/tree/main/skills/byted-ark-seedance-pe | 2026 | skill/guide(공식 조직, 작성 volcengine/support) | 본문 | Seedance 2.0 기본 공식, 참조 지칭법, 편집·연장 문형 |
| S4 | 같은 저장소 / seedance-2-troubleshooting-guide.md V1.7 | 위 저장소 `references/` | 2026-05-14 | guide(공식) | 본문 | 얼굴 드리프트, 쌍둥이, 자막, 웅얼거림, 연장 이음매 등 문제와 처방, 일부 수치 포함 |
| S5 | 같은 저장소 / typical-effect-cases.md, SKILL.md | 위 저장소 | 2026 | guide(공식) | 해당 줄 확인 | 밀도 규칙(길이에 비해 내용이 적으면 즉흥, 많으면 뭉개짐), 시간 조각 스토리보드 |
| S6 | 화산엔진 Doubao Seedance 2.5 提示词指南 (공식 PDF 미러) | https://github.com/Jdaroro/awesome-seedance-2x-prompts (docs/official-pdfs/zh-CN) | 2026-08-07 | guide(공식, 미러) | 본문(텍스트 추출) | 2.5: 정수 초 타임스탬프, 참조 50개, 다중 뷰 허용 조건, 관용구 줄이기, 전문 용어 풀어 쓰기 |
| S7 | 화산엔진 Seedance 2.0 提示词指南 (doc 82379/2222480) | S8의 docs/EVIDENCE_NOTES_2026-09-26.md에 인용 | 2026 | guide(공식) | 2차 인용 | 2.0은 샷 번호만 듣고 0–3초 같은 범위는 불안정, 블록 순서, 길이 상한(영어 1000단어) |
| S8 | Emily2040/seedance-2.0 (Claude 스킬) | https://github.com/Emily2040/seedance-2.0 | 마지막 커밋 2026-09-27 | skill/repo | 본문 일부 | 출처 등급을 엄격하게 매긴 Seedance 2.0 스킬. failure-atlas, i2v-guide, anti-slop, event-density |
| S9 | OSideMedia/higgsfield-ai-prompt-skill | https://github.com/OSideMedia/higgsfield-ai-prompt-skill | 마지막 커밋 2026-10-24 | skill/repo | 본문 일부 | Higgsfield용 스킬 묶음. negative-constraints, house-rulings(상충 기록), FAILURE-MODES, PRODUCTION-PATTERNS |
| S10 | Higgsfield "Hell Grind" 오픈소스 브리프(95분 AI 장편 제작 시스템) | S9의 `skills/higgsfield-seedance/HELL-GRIND.md`에 정리됨 | 2026 | blog/brief(벤더) | 2차 인용 | 머리 없는 시트, GEO 지도, 첫 1초 와이드, 인원 헤더, 마스크 수정, 반복 규칙 |
| S11 | higgsfield-ai/skills (공식 스킬) | https://github.com/higgsfield-ai/skills | 마지막 커밋 2026-10-27 | skill(공식) | 본문 일부 | prompt-engineering.md(약 200토큰 권장, I2V는 재서술 금지, 긍정형), soul-id 사진 가이드 |
| S12 | dexhunter/seedance2-skill | https://github.com/dexhunter/seedance2-skill | 2026-09-19 | skill | 목차만 | Seedance 2.0 영·중 SKILL.md. 10초 넘으면 시간 구간 분할 권장(공식 2.0 지침과 어긋남) |
| S13 | songguoxs/seedance-prompt-skill | https://github.com/songguoxs/seedance-prompt-skill | 2026-02-13 | skill | 훑음 | 즉몽용 중국어 SKILL.md. 자막·로고·워터마크 금지 문형 |
| S14 | Vertex AI video generation prompt guide | https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide | — | guide(공식) | 검색 요약 | Veo 요소 목록, 부정 프롬프트는 "no/don't" 대신 원치 않는 것을 명사로 |
| S15 | Google Cloud Blog: Ultimate prompting guide for Veo 3.1 | https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1 | 약 2025-10 | guide(공식) | 검색 요약 | ingredients(참조)와 첫·끝 프레임, Nano Banana로 시작 프레임 먼저 |
| S16 | Google Developers Blog: Introducing Veo 3.1 | https://developers.googleblog.com/introducing-veo-3-1-and-new-creative-capabilities-in-the-gemini-api/ | 2025 | blog(공식) | 검색 요약 | 참조 이미지 최대 3장, last_frame 설정 |
| S17 | Google: 7 tips to get the most out of Nano Banana Pro | https://blog.google/products/gemini/prompting-tips-nano-banana-pro/ | 2025-11 | blog(공식) | 검색 요약 | 주체·구도·동작·장소·스타일을 구체적으로, 카메라 각도·빛으로 다듬기 |
| S18 | Runway Gen-4 Video Prompting Guide | https://help.runwayml.com/hc/en-us/articles/39789879462419 | — | guide(공식) | 검색 요약 | I2V는 이미지가 아니라 움직임을 쓴다, 부정 표현은 지원하지 않고 반대 결과가 날 수 있다 |
| S19 | Runway Gen-4 Image Prompting Guide | https://help.runwayml.com/hc/en-us/articles/35694045317139 | — | guide(공식) | 검색 요약 | "Including a negative prompt may result in the opposite happening" |
| S20 | Runway Image to Video Prompting Guide / Gen-4.5 | https://help.runwayml.com/hc/en-us/articles/48324313115155 | — | guide(공식) | 검색 요약 | 이미지 속 모션 단서(모션 블러·먼지)가 원치 않는 움직임을 부른다 |
| S21 | Kling AI Prompt Guide (공식 블로그) | https://kling.ai/blog/kling-ai-prompt-guide | — | blog(공식) | 검색 요약 | 주체 + 주체 움직임 + 장면 + (카메라·빛·분위기), 6축 카메라 |
| S22 | Kling AI Camera Control blog | https://kling.ai/blog/kling-ai-camera-control-video-guide | — | blog(공식) | 검색 요약 | Kling 3.0의 push·pull·pan·tilt |
| S23 | Higgsfield: How to Keep Characters and Locations Consistent Across AI Shots | https://higgsfield.ai/blog/consistent-characters-locations | 2026 | blog(벤더) | 검색 요약 | 얼굴은 학습한 정체성, 장면은 참조 이미지로 같은 생성에 함께 넣는다 |
| S24 | Higgsfield: How to Put Two Consistent Characters in One AI Video Scene | https://higgsfield.ai/blog/two-characters-one-scene-ai-video | 2026 | blog(벤더) | 검색 요약 | 2026년 중반에도 두 인물이 상호작용하면 모든 플랫폼에서 얼굴이 섞인다고 인정 |
| S25 | Higgsfield 블로그 Seedance 2.5 prompting guide / Prompt Guide to Cinematic AI Videos | https://higgsfield.ai/blog/seedance-2-5-prompting-guide · https://higgsfield.ai/blog/Prompt-Guide-to-Cinematic-AI-Videos | 2026 | blog(벤더) | 제목·요약만 | 샷 리스트식 프롬프트, 일관성이 필요한 것은 요소(Element)로 |
| S26 | Reddit r/aivideo 계열 스레드(미러) "fake look is lighting", "prompt for imperfection" | https://reddit.sentinel-team.org/posts/1scxq1m/… 외 | 2026-02~06 | reddit | 검색 요약 | 가짜 느낌은 해상도가 아니라 빛, T2V보다 I2V, 깊은 초점은 가짜 같다, 환경음 |
| S27 | Reddit r/StableDiffusion 피부 사실감 스레드(미러) | https://reddit.sentinel-team.org/posts/1shpbbb/… | 2026-04 | reddit | 검색 요약 | 미화어 빼기, 모공·불완전함, 스페큘러 하이라이트 낮추기, 증류 모델은 질감을 잃는다 |
| S28 | Reddit Kling 첫·끝 프레임 스레드(미러) | https://reddit.sentinel-team.org/posts/1seneno/… | 2026-03~04 | reddit | 검색 요약 | 끝 프레임은 중간을 AI처럼 만든다는 의견과 경로를 잡아 준다는 의견이 갈린다. "static tripod shot"은 정지를 의도로 읽힌다 |
| S29 | Reddit r/HiggsfieldAI(미러), r/ClaudeAI 인용 | https://reddit.sentinel-team.org/subreddits/HiggsfieldAI/… | 2026-03~05 | reddit | 검색 요약 | 긴 시퀀스 드리프트, `@` 지칭, Soul ID 권유, 샷이 중요한 작업은 모델을 직접 지정 |
| S30 | Midjourney V7 prompt guide(Evolink 미러) | https://docs.evolink.ai/en/api-manual/image-series/midjourney/midjourney-v7-prompt-guide.md | 2026 | guide(2차) | 검색 요약 | `--raw`는 기본 미화를 끈다, `--no` 과용 금지 |
| S31 | Tripod/locked-off 용어집, "AI filmmaking shots look fake: the static hack" | https://morphic.com/ai-glossary/Tripod · https://www.aifire.co/p/ai-filmmaking-shots-look-fake-the-static-hack-is-here | 2026 | blog | 검색 요약 | "tripod shot, fixed camera, no zoom, no dolly". 모델 기본값이 카메라 드리프트, handheld 단어 금지 |
| S32 | GPT Image 2.5 캐릭터 일관성 가이드(Leadde), Reddit GPT Image 2+Seedance 워크플로 | https://leadde.ai/blog/how-to-keep-characters-consistent-in-gpt-image-2-5-fix-face-and-pose-drift | 2026-05 | blog/reddit | 검색 요약 | 정면 얼굴 먼저 확정한 뒤 각도별 승인, 배경 인물은 전용 초상을 따로 만들어 붙인다 |
| S33 | ZeroLu/awesome-gpt-image, Anil-matcha/Awesome-GPT-Image-2-API-Prompts, wuyoscar/gpt_image_2_skill | https://github.com/ZeroLu/awesome-gpt-image · https://github.com/Anil-matcha/Awesome-GPT-Image-2-API-Prompts | 2026 | repo(프롬프트 모음) | 존재만 확인 | GPT Image 2 예시 모음. 기법 근거로는 쓰지 않았다 |
| S34 | Seedance 2.0 model card (arXiv 2604.14148) | https://arxiv.org/abs/2604.14148 | 2026-04-15 | paper(공식) | 2차 인용(S8) | 4~15초, 네이티브 480p/720p, 다인 화자 립싱크 오류·연장 시 색·인물 누락을 한계로 적음 |

제외한 것: fal.ai·Atlabs·VEED·Atlas Cloud 같은 모델 재판매 사이트 블로그는 검색 결과에 많이 나왔다. 대부분 공식 가이드를 옮긴 것이라 독립 근거로 세지 않았다. 다만 공식 문서와 같은 말을 하는 경우에는 "여러 사용자"의 보조 근거로만 썼다.

---

## 2. 기법 (분야별)

표의 "왜"는 출처가 주장하는 이유이고 검증한 것이 아니다. ID는 3장 비교표와 연결된다.

### A. 이미지 사실감

| ID | 할 일 | 왜 (주장) | 출처 | 신뢰도 |
|---|---|---|---|---|
| A1 | 프롬프트에 `photorealistic`을 직접 쓴다. `real photograph`, `taken on a real camera`도 도움이 된다 | 모델의 사진 모드를 강하게 켠다 | S1 | 공식 문서 |
| A2 | 카메라·렌즈 사양은 룩과 구도를 위한 단서로만 쓴다 | "detailed camera specs may be interpreted loosely". 정확한 물리 재현을 기대하면 안 된다 | S1 | 공식 문서 |
| A3 | 실제 질감(모공, 주름, 천의 해짐, 불완전함)을 요구하고, 스튜디오 광택이나 연출을 뜻하는 단어는 피한다. 스냅 사진처럼 "그 순간 찍힌 사진"으로 쓴다 | 사실감은 질감과 무연출에서 나온다 | S1, S27 | 공식 문서 + 여러 사용자 |
| A4 | `beautiful, perfect, flawless, model, influencer, symmetrical` 같은 미화어를 뺀다 | 매끈한 화보 쪽으로 끌려간다 | S27, S8(anti-slop) | 여러 사용자 |
| A5 | 와이드·저조도·비·네온 장면에는 규모·대기·색을 더 자세히 쓴다 | 안 쓰면 분위기를 얻는 대신 표면 사실감을 잃는다 | S1 | 공식 문서 |
| A6 | 사람에게는 신체 프레이밍, 시선, 물체 접촉을 쓴다(`full body visible, feet included`, `looking down at the open book, not at the camera`, `hands naturally gripping…`) | 비율, 동작 기하, 시선이 맞는다 | S1 | 공식 문서 |
| A7 | 사실감 예시 프롬프트는 `Avoid cinematic lighting, dramatic color grading`, `no cinematic grading`으로 끝난다 | "영화 포스터" 느낌이 사실감을 깎는다 | S1(5.7·5.8 예시) | 공식 문서(예시 수준) |
| A8 | `film grain`, `soft focus`를 맨 끝에 덧붙이는 꼬리말로 쓰지 않는다. 결은 룩 슬롯에 필름 이름과 함께 쓰고, 불완전함은 "내용"(삐뚤어진 액자, 이 빠진 머그)에 둔다 | 렌더링 지시로 읽혀 화면 전체가 무르게 된다 | S9(negative-constraints, 미측정이라고 스스로 밝힘) | 한 사람 주장 |
| A9 | 범용 업스케일러를 조심한다 | 피부 질감을 뭉갠다 | S27, Higgsfield 피부 가이드(검색 요약) | 여러 사용자 |
| A10 | 정체성 기준 이미지(시트)는 모델에 두 번 통째로 통과시키지 않는다. 고칠 부분만 편집한 뒤 원본 위에 마스크로 합성한다 | 재통과마다 질감이 죽고 색이 흐르며 얼굴이 대칭·플라스틱이 된다. 그 죽은 질감이 영상 연기까지 망친다 | S10(S9 경유), S9 house-rulings P2-3(단일 재통과 효과는 미측정) | 한 사람 주장(벤더 제작팀) |
| A11 | Midjourney는 `--style raw`로 기본 미화를 끈다. `--no`는 과용하지 않는다 | 사실감과 정밀 제어 | S30 | 공식(요약) |

### B. 영상 사실감·움직임 물리

| ID | 할 일 | 왜 (주장) | 출처 | 신뢰도 |
|---|---|---|---|---|
| B1 | 시작 이미지가 있으면 이미지에 이미 있는 것은 다시 쓰지 않는다. 움직임, 카메라, 시간, 보존할 것만 쓴다 | 정적인 내용을 다시 쓰면 드리프트가 생기거나 거의 안 움직인다 | S18, S11, S8(i2v-guide), S9 | 공식 문서(Higgsfield 스킬) + 공식(요약, Runway) + 여러 사용자 |
| B2 | 한 샷에 카메라 동작 하나, 주체 동작 하나 | 움직임이 가장 어렵다. 단순해야 따른다 | S2, S7, S21, S31 | 공식 문서 |
| B3 | 동작은 박자와 횟수로 쓴다(`takes four steps to the window, pauses, and pulls the curtain in the final second`) | 시간이 정확하고 실행 가능해진다 | S2 | 공식 문서 |
| B4 | 짧은 클립이 지시를 더 잘 따른다. 8초 한 개보다 4초 두 개를 붙이는 편이 나을 수 있다 | 길이가 길수록 지시 이행이 떨어진다 | S2 | 공식 문서(Sora) |
| B5 | 동작은 신체 부위까지 쓰고 정도(폭·속도·힘)를 붙인다(`천천히 손을 든다`, `빠르게 고개를 돌린다`) | 동작이 분명해진다 | S4 1.3 | 공식 문서 |
| B6 | 인접 물체가 따라 움직이는 사고를 막으려면 불변을 적는다(`The magnet stays attached to the fridge surface throughout. Only the Polaroid moves.`) | 물리 시뮬레이션이 없어 붙어 있는 물체를 같이 움직인다 | S9 FAILURE-MODES | 한 사람 주장 |
| B7 | 손으로 물체를 바꾸는 동작은 인과 사슬로 쓴다: 처음 구조 → 고정하는 손 → 힘의 위치·방향 → 재질 반응 → 완료 상태 | 동사만 쓰면 손만 움직이고 물체는 그대로다(마임) | S9 FAILURE-MODES | 한 사람 주장 |
| B8 | 짧은 동작이 일찍 끝나면 남은 시간에 되감기가 나온다. 같은 방향 동작 2~3개로 채우거나 끝 자세 유지 시간을 적는다. 카메라 이동은 끝점을 적는다 | 남은 타임라인을 가장 싼 방법(역재생)으로 채운다 | S9 FAILURE-MODES | 한 사람 주장 |
| B9 | 완료 상태를 보이는 사실로 쓰고 컷 전에 잠깐 머물게 한다(`the lid seats flush and stays there`) | 안 쓰면 시도만 있고 결과가 없는 컷이 된다 | S9 | 한 사람 주장 |
| B10 | 정지 장면도 얼어붙게 두지 않는다. 1~2초마다 미세한 사건 하나(숨에 가슴이 오름, 콧구멍, 눈썹)를 넣고 깜빡임을 단계로 쓴다. `nobody moves`는 쓰지 않는다 | 고정 응시는 죽은 얼굴로 읽힌다. 진정시키는 문구가 화면을 얼린다 | S10(S9 경유), S8 failure-atlas | 한 사람 주장(벤더 제작팀) + 여러 사용자 |
| B11 | 가짜 느낌의 원인은 대개 빛이다. 깊은 초점(모든 것이 선명함)은 가짜 같고, 환경음은 믿음을 더한다 | 실제 렌즈는 모든 것을 선명하게 두지 않는다 | S26 | 여러 사용자 |
| B12 | 일부러 넣는 광학 결함은 "내용"으로 쓴다. 대상과 시점을 정해 열 아지랑이, 초점이 맞기 전 짧은 헌팅처럼 쓴다. 대기는 % 램프로 양을 정한다 | 완벽한 렌더가 합성처럼 보인다. 꼬리말로 쓰면 화면 전체가 무르게 된다(A8) | S9 PRODUCTION-PATTERNS(Higgsfield Seedance-4K 튜토리얼 시연) | 한 사람 주장 |
| B13 | 너무 완벽한 배경을 가리려고 핸드헬드를 살짝 넣는다 | AI 배경이 너무 반듯하다 | S28(봇 댓글 포함) | 한 사람 주장(약함) |
| B14 | 걷기·달리기는 접지와 무게 이동으로 쓴다(`weight transfer, realistic foot placement`) | 미끄러지는 발을 막는다 | S28, S9 "Walking is the hardest stunt" | 여러 사용자(약함) |
| B15 | 슬로·젠틀 계열 단어(`slowly, gently, softly`)가 사실적인 결과에 유리하다 | 고에너지 묘사어가 과장된 동작을 부른다 | Atlabs(S26 검색과 함께 나옴) | 한 사람 주장 |

### C. 지시 이행·구조

| ID | 할 일 | 왜 (주장) | 출처 | 신뢰도 |
|---|---|---|---|---|
| C1 | **Seedance 2.0**은 샷 번호(镜头1/2/3)로 순서만 정하고 0–3초 같은 정밀 범위는 피한다. **Seedance 2.5**는 정수 초 타임스탬프를 듣는다. 구간은 끊김 없이 잇고(`0-3초…3-7초…7-15초`, `0-3…5-6` 같은 빈틈 금지), 타임스탬프로 빈도를 제어하지 않는다(`1초에 고개 3번` 금지) | 2.0은 정밀 시간이 불안정하다. 2.5는 1초 단위로 듣지만, 구간에 내용이 적으면 즉흥하고 많으면 과하게 자르거나 빠뜨린다 | S7, S6 | 공식 문서 |
| C2 | 밀도 규칙: 길이에 비해 내용이 적으면 모델이 즉흥하고, 길이에 비해 샷이 많으면 내용과 대사가 뭉개진다. 넘치면 영상 두 개로 나눈다 | 공식 문제 사례 | S5, S7 | 공식 문서 |
| C3 | 대사가 끝난 뒤 빈 꼬리를 남기지 않는다. 클립 길이를 줄이거나 남는 시간에 할 일(이름 붙은 쉼, 소리 하나, 계속되는 손일)을 쓴다. 업무가 허락하면 세로보다 가로가 웅얼거림 확률을 낮춘다(약 70% → 30%, 공식 실측) | 길이가 내용보다 길면 웅얼거림·추가 대사·반복 대사가 나온다. 길이를 맞추면 약 10%로 준다 | S4 V-11, S9(4초에 6단어 이하 줄은 매번 웅얼거림, 기록 불완전) | 공식 문서 + 한 사람 측정 |
| C4 | 중요한 참조와 요구를 프롬프트 앞쪽에 둔다 | 정밀하게 참조해야 할 것일수록 앞에 | S4 4.1 | 공식 문서 |
| C5 | 길이 상한: 중국어 500자, 영어 1000단어. 대본을 그대로 프롬프트로 쓰지 않는다. 반면 Higgsfield 공식 스킬은 "약 200토큰 이하, 길면 왜곡된다"고 하고, 같은 Higgsfield의 Hell Grind 장편은 3,000~4,000단어를 썼다 | 너무 길면 정보가 흩어지고 요소가 빠진다 | S7, S11, S10 | 공식 문서끼리 상충 |
| C6 | 실패 조건 문장: 원하는 상태 + 예산 + 판정(`The dominant color must be cold teal-green. Yellow exists only inside the lamp bulb and a palm-sized halo beneath it. If the frame turns yellow, the frame is wrong.`). 금지 대신 **배분**한다 | "no yellow" 같은 금지는 효과가 없었다 | S9(Higgsfield Studio 브레이크다운 인용) | 한 사람 주장(벤더 제작팀) |
| C7 | 참조에 원치 않는 것이 들어 있으면 금지하지 말고 이 영화의 사실로 진술한다(`That window glowing in the reference is switched off in our film.`) | 참조는 계약이 아니다. 다른 점을 긍정형으로 말하면 받아들인다 | S9 | 한 사람 주장 |
| C8 | 잠금 문장(빛·정체성·위치)은 같은 낱말로 모든 샷 블록에 반복한다 | 한 번만 쓰면 컷 사이에 빛이나 얼굴이 바뀐다 | S8 failure-atlas, S2("reuse phrasing for continuity") | 공식 문서 + 여러 사용자 |
| C9 | 비유·관용구(`his face fell`, 成语)를 쓰지 않는다. 표정은 서술형 문장으로 쓰고, 평이한 감정어 하나에 신체 앵커 하나를 붙인다 | 비유가 문자 그대로 그려진다(얼굴색이 변함 등) | S6("表情建议写描述性语句，减少成语使用"), S8 | 공식 문서 + 한 사람 주장 |
| C10 | 너무 전문적인 용어는 [용어 + 보이는 결과 설명]으로 쓴다(포커스 이동 = 앞 나무가 흐려지고 뒤 인물이 선명해진다) | 모델이 니치 용어를 모른다. 기본 경치·운동 용어는 그냥 써도 된다 | S6 | 공식 문서 |
| C11 | 동작은 대체로 요약해서 쓰고, 기억에 남을 동작 몇 개만 자세히 쓴다. 같은 동작을 반복해 쓰지 않는다 | 모든 동작을 나열하면 흩어진다 | S6 | 공식 문서 |
| C12 | 장면의 첫 1초를 행동 없는 와이드로 두어 위치를 "찍게" 한다. 인물은 첫 프레임부터 화면 안에 있다 | 그 1초가 없으면 이후 샷에서 인물이 자리를 바꾼다 | S10 | 한 사람 주장 |
| C13 | 프롬프트 구조: 장면 → 주체 → 핵심 세부 → 제약, 라벨을 붙인 짧은 단락. 용도(광고·UI)를 적어 "모드"를 정한다 | 유지·디버깅이 쉽다. 형식 자체(JSON 등)보다 의도가 중요하다 | S1 | 공식 문서 |
| C14 | Seedance 샷 블록 안의 순서: 운경(카메라·컷) → 주체 동작·표정 → 위치·공간 변화 → 오디오 | 공식 권장 순서 | S4 1.3, S7 | 공식 문서 |
| C15 | 짧은 프롬프트는 창의성, 긴 프롬프트는 통제다. 다만 길어도 늘 따르지는 않는다 | 트레이드오프 | S2 | 공식 문서 |

### D. 인물·의상 일관성

| ID | 할 일 | 왜 (주장) | 출처 | 신뢰도 |
|---|---|---|---|---|
| D1 | 얼굴만 정확히 잘라낸 클로즈업을 **독립된 참조**로 넣고, 전신·의상은 다른 참조로 넣는다. 프롬프트에 "얼굴은 @그림1(대두샷), 의상은 @그림2(전신)"처럼 나눈다 | 얼굴·전신·의상을 한 장에 합치면 얼굴 비중이 작아 특징 추출이 약해진다 → ID 드리프트·얼굴 바뀜 | S4 V-1 | 공식 문서(2.0) |
| D2 | **Seedance 2.0**: 3면도·다중 뷰 시트를 인물 참조로 쓰지 않는다(쌍둥이 원인). **Seedance 2.5**: 주체 1~5명이면 단일 뷰·다중 뷰 모두 괜찮다. 5명을 넘으면 단일 뷰가 안정적이고, 다중 뷰가 필요하면 한 장에 합치지 말고 뷰마다 다른 이미지로 넣는다 | 버전 차이(2.5 가이드의 버전 차이 목록에 "2.5는 다중 뷰 지원"이 있다) | S4 V-1·V-7, S6 | 공식 문서 |
| D3 | 쌍둥이·복제 방지: 장면 맨 앞에 인원 헤더(`EXACT 3 CHARACTERS — NO DUPLICATES: A, B, C.`), 반복 소품에는 개수(`Two trays, never more.`). 단일 인물 참조라면 끝에 "영상 내내 외형·의상·액세서리가 같은 두 사람이 나오지 않는다. 한 시점에 그 인물은 하나뿐이다"를 넣고, 인물을 언급할 때마다 대응 그림을 같은 형식으로 붙인다 | 복제는 모델의 기본 경향이다. 금지가 정당한 드문 경우다 | S4 V-7, S10, S9 | 공식 문서 + 한 사람 주장 |
| D4 | 참조 인물이 4명을 넘으면(2.0) 이미지를 먼저 만들되 한 장에 4명 이하로 한다. 2.5는 이미지 주체 1~8명이면 양호, 9~12명은 불안정 | 인원이 늘면 사람이 빠지거나 늘거나 중복된다 | S4 V-10, S6 | 공식 문서 |
| D5 | 주체를 정의할 때 2~3개의 안정적인 정적 특징(옷·머리·종류)으로 정의하고, 같은 이름을 끝까지 쓴다. 정보를 그림 속 글자(인물 사진 위에 "张三")에 맡기지 않는다 | 생략하거나 이름이 흔들리면 인물이 섞인다 | S4 1.2, S6 | 공식 문서 |
| D6 | 참조가 정체성을 맡을 때 텍스트 묘사량은 **미결**이다. Higgsfield 프롬프트 스킬은 최소 텍스트를 권하고 Hell Grind는 전체 묘사를 매번 넣는다. 양쪽이 합의한 것은 "고정 문장, 샷마다 안 바꿈, 참조와 모순 금지, 어긋나면 모순되는 텍스트부터 지운다" | — | S9 house-rulings P1-1 | 공식끼리 상충 |
| D7 | 시트는 "지루하게": 중성 회색 배경, 평광, 모공 보이는 피부, 리터치 없음. 그레인·시네마 렌즈를 시트에 굽지 않는다(새 빛에 반응하지 않게 된다). 반대로 Soul 쪽은 "soft natural film grain"을 넣는다 → 미결 | 시네마 룩은 장소와 영상 프롬프트에서 온다 | S10, S9 P2-4 | 한 사람 주장(상충) |
| D8 | 정면 전신 패널의 머리를 없앤다 | 와이드에서 모델이 작고 흐린 전신 얼굴을 가져다 쓴다. 머리를 지우면 얼굴 출처가 클로즈업 하나로 정해진다 | S10 | 한 사람 주장(벤더 제작팀) |
| D9 | 시트 초상은 정면보다 살짝 3/4 | 시트가 더 잘 읽힌다 | S10 | 한 사람 주장 |
| D10 | 나이를 숫자로 쓰지 않는다(어떤 언어로든). 역할·옷·동작으로 쓴다 | 미성년으로 읽히는 순간 내용 필터가 크게 엄격해진다 | S10 | 한 사람 주장 |
| D11 | Soul ID 학습 사진: 5~20장(8~12장이 적당), 한 사람만, 선글라스·짙은 필터·모자·코스튬 금지, 각도(정면·3/4 좌우)·조명·표정·거리 다양 | 다양할수록 정체성 포착이 좋다 | S11 photo-guide | 공식 문서 |
| D12 | 두 인물이 한 샷에서 상호작용하면 아직 어디서나 얼굴이 섞인다 | 벤더도 인정한 한계 | S24 | 공식(요약, 벤더) |
| D13 | 반복 등장하지 않는 배경 인물이 흔들리면 그 사람 전용 초상을 따로 만들어 함께 붙인다 | 스토리보드 전체를 다시 돌리는 것보다 낫다 | S32(Reddit) | 한 사람 주장 |

### E. 카메라·렌즈 언어

| ID | 할 일 | 왜 (주장) | 출처 | 신뢰도 |
|---|---|---|---|---|
| E1 | 고정 카메라는 `tripod shot, fixed camera, no zoom, no dolly` / `locked-off`처럼 상태로 명시한다. 같은 프롬프트에 `handheld`나 다른 카메라 동사를 두지 않는다 | 많은 모델이 기본으로 미세한 카메라 드리프트를 넣는다. "static tripod"는 정지를 실패가 아니라 의도로 읽게 한다 | S31, S28 | 여러 사용자 |
| E2 | Seedance 2.0 API의 `camera_fixed`는 2.0 계열에서 지원하지 않는다(참조 장면 미지원). 고정은 프롬프트 문장으로 해야 한다 | API 문서 | S7(Ark API 미러 인용) | 공식(요약) |
| E3 | "cinematic" 대신 측정 가능한 것을 쓴다: 프레이밍과 각도, 심도(무엇이 선명하고 무엇이 흐린지), 빛 + 팔레트 앵커 3~5색(`amber, cream, walnut brown`) | 모호한 말은 모델이 마음대로 채운다. 색 이름 3~5개가 샷 간 팔레트를 안정시킨다 | S2 | 공식 문서 |
| E4 | 심도는 두 요청을 구분한다: "앞뒤 모두 선명"(`sharp focus throughout, deep depth of field`) vs "주체 선명, 배경은 의도적으로 보케"(`subject in sharp focus, background falling into soft bokeh`). `blurry background`만 쓰지 않는다 | 어느 면이 선명한지 말하지 않으면 주체까지 흐려진다 | S9 | 한 사람 주장 |
| E5 | 영상에서는 렌즈 mm·브랜드보다 결과를 쓴다(공식 Seedance 2.5: 전문 용어는 결과 설명으로). 이미지에서는 카메라 사양이 룩 단서로 일부 먹힌다(A2) | — | S6, S1 | 공식 문서 |
| E6 | Kling: 빠른 주체 동작과 빠른 카메라 이동을 함께 쓰지 않는다. 클립당 카메라 이동 하나 | 아티팩트 | S21(요약), 제3자 가이드 | 공식(요약) + 여러 사용자 |
| E7 | Cinema Studio에서는 렌즈·조리개를 프롬프트가 아니라 UI 설정으로 정한다. 프롬프트는 512자 하드 제한, @ 요소 칩 하나가 숨은 80~100자를 쓴다 | 프롬프트에 쓰면 광학 설정과 충돌한다 | S9 | 한 사람 주장(확인 안 됨) |

### F. 모델별 메모

| 모델 | 메모 | 출처 | 신뢰도 |
|---|---|---|---|
| GPT Image 2 | `quality` low/medium/high. 작은 글씨·클로즈업 초상·정체성 민감 편집은 medium·high로 비교한다. 2560×1440(2K)을 넘으면 실험적이다. `input_fidelity`는 2에서 쓰지 않는다(기본이 고충실도). 편집은 "change only X + keep everything else the same", **매 반복마다 보존 목록을 다시 쓴다**. 의상 교체 예시는 얼굴·체형·포즈·머리·표정을 잠그고 옷만 바꾸며 드레이핑·주름·가림, 같은 빛·그림자·색온도를 요구한다. 다중 이미지는 "Image 1: …, Image 2: …"처럼 번호 + 설명으로 지칭한다 | S1 | 공식 문서 |
| GPT Image 2.5 | 공식 프롬프트 문서를 찾지 못했다. 커뮤니티 스킬(S9)은 "2.5 프롬프트 상태 미확인"이라고 적는다 | S9 | — |
| Seedance 2.0 | 기본 공식: 주체+동작(필수) + 환경·운경·미학·오디오(선택). 특수 부호: （음악） <음효> {대사} 【자막】. 대사 언어는 하나로 통일. 길이·비율은 파라미터지만 프롬프트 앞뒤에 `时长：4秒，比例：9:16`처럼 다시 적으면 좋다("s"가 아니라 "秒"). 연장은 편집·연장 작업에서 "참조 비디오N"이라고 쓰지 말고 `<视频N>`로 쓴다(참조 작업으로 오인 방지). 연장을 반복하면 화질 열화가 누적된다(얼굴에 얼룩진 색 블록) | S3, S4 | 공식 문서 |
| Seedance 2.5 | 30초, 참조 50개(이미지 30·영상 10·오디오 10). 첫·끝 프레임은 `content.role = first_frame/last_frame`을 우선 쓴다(비율이 첫 프레임에 고정된다). 끝 프레임 비율이 다르면 늘어난다. 참조가 충분히 정확하면 "지칭만 하고 재서술을 줄인다". 다주체 영상 참조는 5~10초가 좋다. 네거티브는 자막·오디오(bgm, 효과음, 대사 각각)만 문서화되어 있다. 묘사는 가능한 긍정형으로. 스토리보드 그리드는 선화·졸라맨으로, 15칸 이하, 글자 적게. 그리드는 엄격히 따르지 않으니 엄격해야 하면 키프레임 개별 이미지로 | S6 | 공식 문서 |
| Kling 3.0/4.0 | 공식 공식(formula)은 주체 + 주체 움직임 + 장면 + (카메라·빛·분위기). I2V는 움직임 위주. 요소(Element)는 이미지 2~4장 또는 짧은 영상. 멀티샷에서는 샷마다 식별 특징을 반복한다(빠진 샷이 흐른다). 첫·끝 프레임 효과는 사용자 의견이 갈린다 | S21, S22, 제3자 가이드, S28 | 공식(요약) + 여러 사용자 |
| Veo 3.1 | 요소: 주체, 동작, 장면, 카메라 각도·이동, 렌즈, 스타일, 시간 요소, 오디오. 오디오는 원한다고 분명히 쓰고 별도 문장으로. 참조 이미지 최대 3장(ingredients). 첫·끝 프레임으로 전환을 만든다. 부정 프롬프트는 "no/don't" 대신 원치 않는 것을 명사로(`wall, frame`). Gemini API 표면에는 negative 필드가 없다는 보고가 있다 | S14, S15, S16 | 공식(요약) |
| Sora 2 | 4·8·12·16·20초. 길이·해상도·캐릭터는 파라미터이고 산문으로는 안 바뀐다. 캐릭터는 생성당 2명 이하. 대사는 `Dialogue:` 블록에 분리하고 4초에 짧은 교환 1~2개. 실패가 계속되면 카메라를 고정하고 동작을 단순하게, 배경을 비운 뒤 하나씩 다시 쌓는다 | S2 | 공식 문서 |
| Runway Gen-4 | I2V는 움직임만, 주체는 "the subject"나 대명사로. 부정 표현 미지원(반대 결과 가능). 이미지 속 모션 단서가 원치 않는 움직임을 부른다 | S18~S20 | 공식(요약) |
| Nano Banana Pro | 주체·구도·동작·장소·스타일을 구체적으로. 카메라 각도·빛으로 다듬는다. 텍스트·사실 정확도·복잡한 편집은 한계로 적혀 있다 | S17 | 공식(요약) |

### G. 네거티브 프롬프트

| ID | 할 일 | 왜 (주장) | 출처 | 신뢰도 |
|---|---|---|---|---|
| G1 | 부정 표현 대신 원하는 상태를 긍정형으로 쓴다(`no blur` → `tack sharp`, `no people` → `uninhabited landscape`) | 대부분의 모델에 negative 필드가 없다. Runway는 반대 결과가 날 수 있다고 명시한다 | S11, S18, S19 | 공식 문서 + 공식(요약) |
| G2 | 금지가 정당한 경우를 가리는 기준: "모델의 기본값이 이미 그 실패인가?" 그렇다면 짧고 구체적인 금지를 긍정 진술 **뒤에** 둔다(복제, 싸움 장면의 슬로모션, 원치 않는 배경음악). 그렇지 않다면 긍정형으로 쓴다 | 금지어가 그것을 부를 수 있다 | S9 | 한 사람 주장 |
| G3 | Seedance에서 문서화된 제약 문장은 자막·로고·워터마크(2.5는 오디오 포함)뿐이다. "保持无字幕/避免生成任何文字或字幕", "不要生成logo/水印". 자막은 이 문장과 참조 속 글자 제거로 60~90%에서 10~40%로 줄고, 100% 막을 수는 없다 | 공식 테스트 | S4 V-2·V-3, S7 | 공식 문서 |
| G4 | 행동은 긍정형으로만 쓴다. "does NOT fall on his back"은 무시되거나 반대로 된다 → "falls on his stomach" | — | S10 | 한 사람 주장 |
| G5 | 말하지 않는 인물의 입은 긍정 사실로 쓴다: `lips at rest`, `jaw closed, breath lifting the chest`. `listens without speaking`은 "speaking"을 부른다 | 표시하지 않은 입은 모델이 말하는 입으로 정할 수 있다 | S9(미실험이라고 밝힘) | 한 사람 주장 |
| G6 | Veo: 부정 필드를 쓸 때 명사 나열(`wall, frame`), 지시어 금지 | — | S14 | 공식(요약) |

### H. 참조 이미지 사용

| ID | 할 일 | 왜 (주장) | 출처 | 신뢰도 |
|---|---|---|---|---|
| H1 | 참조마다 역할 하나 + 전이할 것 / 전이하지 않을 것을 쓴다(`[Tag] controls [role] only; ignore […] from that reference`) | 정체성·움직임·카메라·환경이 섞인다 | S3, S8, S1, S10 | 공식 문서 + 여러 사용자 |
| H2 | 업로드 순서대로 번호를 매기고 텍스트에서 그 번호로 부른다. Asset ID는 모델이 대응하지 못하니 `图1`처럼 번호를 쓴다 | 공식 | S4 1.2, S6 | 공식 문서 |
| H3 | 참조 이미지·영상의 불필요한 글자는 먼저 지운다 | 자막·글자 생성이 늘어난다 | S4 V-2, Veo 블로그 요약 | 공식 문서 |
| H4 | 특수 효과·숫자 롤링처럼 글로 안 되는 것은 참조 영상으로 넣는다 | 프롬프트 제약이 무효인 경우가 있다 | S4 V-9 | 공식 문서 |
| H5 | 장소 참조에는 상속 금지를 쓴다(`take only the space and the texture… Do not use as a starting frame, do not inherit the composition, the angle, or the grade`) | 모델이 얼굴 대신 구도를, 구도 대신 색을 가져간다 | S10 | 한 사람 주장 |
| H6 | 장소 시트는 3/4 시점, 장소마다 앵커 하나(기둥·램프·소파), 빛 논리 하나(해 두 개 금지) | 정면 사진은 와이드에서 납작한 벽지가 되고 가장자리 밖을 매번 새로 만든다 | S10 | 한 사람 주장 |
| H7 | 반대 앵글 만들기 2안: 빈 장소를 카메라가 천천히 걸어가는 영상을 생성하고, 필요한 각도를 캡처한 뒤 이미지 모델로 질감·빛만 손본다 | 시트와 일관된 반대편을 그린다 | S10 | 한 사람 주장 |
| H8 | 씬 지도(GEO): 랜드마크·좌우·카메라 쪽·넘지 않는 선만 적고 인물은 적지 않는다. 씬당 한 번 쓰고 모든 샷에 그대로 붙인다. 좌우는 카메라 기준으로만 | 인물이 순간이동하고 자리를 바꾸는 것을 막는다 | S10 | 한 사람 주장 |
| H9 | 참조가 이미 정확하면 재서술 대신 지칭만 한다(`严格参考视频1的动作与运镜`) | 중복 묘사가 충돌한다 | S6 | 공식 문서 |
| H10 | 얼굴·의상·장면 참조를 각각 독립 이미지로 | D1 참조 | S4 4.1 | 공식 문서 |

### I. 반복·QA

| ID | 할 일 | 왜 (주장) | 출처 | 신뢰도 |
|---|---|---|---|---|
| I1 | 한 번에 한 변수만 바꾼다. 나머지는 글자 그대로 | 전체를 다시 쓰면 잘 되던 부분을 잃는다 | S1, S2, S8, S10 | 공식 문서 |
| I2 | 짧고 싸게 먼저(3~5초, 480p/Fast) 시험하고 고해상도는 나중에 | 비용 | S8, DEV/Scenario(검색 요약) | 여러 사용자 |
| I3 | 같은 프롬프트도 매번 다르게 나온다. 2~3번째 결과가 나을 수 있다 | 생성은 확률이다 | S2 | 공식 문서 |
| I4 | 10~15번 고쳐도 안 되면 문장이 문제가 아니다. 샷을 단순화한다(둘로 나누기, 동작 빼기, 각도 바꾸기) | — | S10 | 한 사람 주장 |
| I5 | 이어 가기 전에 **실제** 끝 상태를 기록한다(계획한 끝이 아니다). 끝난 박자는 "이미 일어남"으로 표시하고 미래 박자는 넣지 않는다 | 계획한 끝에서 시작하거나 동작이 다시 시작된다 | S8 failure-atlas·event-density | 한 사람 주장(체계적) |
| I6 | 정체성은 원래 시트로 다시 고정하고, 뽑은 끝 프레임은 자세·상태만 맡긴다 | 드리프트된 프레임을 이어 쓰면 드리프트가 누적된다 | S8 model-mechanics, S4 V-8 | 공식 문서 + 한 사람 주장 |
| I7 | Seedance 연장 이음매에서 튀면 앞 클립 끝 6프레임, 뒤 클립 첫 1프레임을 자른다. 가능하면 연장을 컷 전환에서 끝낸다 | 연장 이음매의 점프·되감기 | S4 V-6 | 공식 문서(2.0) |
| I8 | 영상 끝의 "딱" 소리는 오디오 볼륨 엔벨로프로 페이드아웃한다 | 끝 프레임 클릭 노이즈 | S4 A-1 | 공식 문서 |
| I9 | 결과는 프레임 단위로 검토하고 시트와 원본 크기로 비교한다. 시작 프레임이 통과해도 중간에 얼굴이 바뀐 클립은 거절한다 | 한 장면이 맞아 보여도 중간에 흐른다 | S9, S32 | 여러 사용자 |
| I10 | 발음이 틀리는 고유명사·다음자는 같은 소리의 흔한 글자로 바꾸거나, TTS로 만든 오디오를 (검은 화면 영상으로 변환해) 참조로 넣는다 | 공식 처방 | S4 A-2 | 공식 문서(중국어 기준) |

---

## 3. 우리 키트와 비교

표기: **있음**(같은 규칙이 이미 있다) / **부분**(비슷하지만 빠진 조각이 있다) / **없음**. "충돌"은 키트의 기본값(실사 시네마틱 룩, 고정 카메라, 15블록, 화면 기준 방향, 한 번에 하나, 사건 ≤3, 시작 이미지 → 영상)과 부딪치는지를 본다.

| ID | 기법 요약 | 키트 | 키트 파일·근거 | 충돌 |
|---|---|---|---|---|
| A1 | `photorealistic` 명시 | 부분 | `image-prompt/character.md`, `prop.md`에는 있다. `location.md`, `first-frame.md`, `location-view.md`에는 없다 | 없음 |
| A2 | 카메라 사양은 룩 단서 | 있음 | `location.md` "장비명은 정지 이미지에만", `check_prompt.py` 영상 mm 경고 | 없음 |
| A3 | 실제 질감, 무연출 | 있음 | `character.md` REALISM 줄, `image-prompt/SKILL.md` §3 진단표 5번 | 없음 |
| A4 | 미화어 빼기 | 부분 | `character.md` "객관적 특징 먼저". 금지 단어 목록은 없다 | 없음 |
| A5 | 와이드·저조도에 규모·대기·색 추가 | 없음 | — | 없음(야간·실내 저조도 컷에 유용) |
| A6 | 신체 프레이밍·시선·접촉 | 부분 | `first-frame.md` 블로킹(위치·시선·손). `feet included` 같은 프레이밍 문장은 시트에만 있다 | 없음 |
| A7 | "no cinematic lighting/grading" | 없음 | — | **충돌.** 우리 룩은 시네마틱이다. 가져오지 않는다. 대신 "가짜 같아" 진단에서 색·노출을 먼저 보는 키트 방식(§3 표)이 같은 효과를 노린다 |
| A8 | 맨 `film grain` 꼬리말 금지 | 부분 | `character.md` "같은 룩 대신 palette, contrast, grain, falloff"(grain을 보존 속성으로 쓴다. 꼬리말 금지 규칙은 없다) | 없음 |
| A9 | 업스케일러 주의 | 있음 | `higgsfield-generation/SKILL.md` "Upscaling erases watercolor/film texture" | 없음 |
| A10 | 시트 재통과 대신 마스크 합성 | 부분 | `character.md` "확정본에서만 파생, 파생의 파생 금지". 마스크 합성 절차는 없다 | 없음 |
| B1 | I2V는 이미지를 다시 쓰지 않는다 | 부분 | `video-prompt/SKILL.md` §3 Kling 메모에만 있다. Seedance 15블록은 `LOCATION_MAP`·`FIRST_FRAME`에서 첫 프레임을 다시 서술한다 | **잠재 충돌.** 15블록 구조와 반대 방향이다. 키트는 E-29 등 자체 실험으로 현재 형태에 왔다. Seedance 2.5 공식(S6)도 "참조가 정확하면 지칭만"이라고 한다 → 실제 A/B 시험 전에는 바꾸지 않는다 |
| B2 | 카메라 하나·동작 하나 | 있음 | `video-prompt/SKILL.md` §1 원칙 4, `live-action.md` CAMERA | 없음 |
| B3 | 박자·횟수로 동작 | 있음 | `live-action.md` ACTION_TIMING, §0 "천천히" 행 | 없음 |
| B4 | 짧은 클립 | 부분 | §2 길이 5~10초, 15초 넘으면 나누기 | 없음 |
| B5 | 신체 부위 + 정도 | 부분 | `fixes.md` "head → shoulders → feet over three seconds", 걸음 나이 표 | 없음 |
| B6 | 인접 물체 불변 명시 | 부분 | `live-action.md` PHYSICS `motion_owner`. "이것만 움직이고 저것은 그대로" 문장은 없다 | 없음 |
| B7 | 조작 인과 사슬 | 부분 | `[상태 머신]` "exactly one transition". 고정하는 손·힘·재질 반응 단계는 없다 | 없음 |
| B8 | 되감기 방지(남은 시간 채우기) | 부분 | `fixes.md` "Head turns and then turns back"(증상 하나에만), `check_prompt.py` 빈 구간 경고 | 없음 |
| B9 | 완료 상태 명시 | 있음 | `live-action.md` "The shot ends with [final state]", §1 원칙 2 | 없음 |
| B10 | 미세한 삶, 얼어붙음 금지 | 부분 | `acting/SKILL.md` eye life·깜빡임, `fixes.md` 배경 인물 freeze. "1~2초마다 미세한 사건"과 "nobody moves 금지"는 없다 | 없음 |
| B11 | 빛·심도·환경음 | 부분 | `image-prompt/SKILL.md` §3 2번(모든 것이 같은 선명도), AUDIO 블록 | 없음 |
| B12 | 광학 결함을 내용으로 | 없음 | — | 부분 충돌. 열 아지랑이·초점 헌팅은 고정 카메라와 양립하지만 시네마틱 정갈함과 맞는지는 작품마다 다르다. 기본값으로 넣지 않는다 |
| B13 | 핸드헬드로 배경 가리기 | 없음 | `image-prompt/SKILL.md` "시네마틱 프레임에 폰·핸드헬드 단어 금지" | **충돌.** 가져오지 않는다 |
| B14 | 접지·무게 이동 | 부분 | `acting/SKILL.md` 무게중심, `video-prompt/SKILL.md` 걸음 나이 행 | 없음 |
| B15 | slowly/gently | 있음 | `live-action.md` FORMAT_MODE "All movement is slow and even" | 없음 |
| C1 | 2.0 샷 번호 / 2.5 정수 초·연속 구간·빈도 제어 금지 | 부분 | 연속 구간 검사는 `check_prompt.py`에 있다. 소수 초(`0:02.5`)는 허용되고, 빈도 제어 경고는 없다 | 없음(키트는 2.5) |
| C2 | 밀도 규칙 | 있음 | 사건 1~3개, `video-prompt/SKILL.md` §2 | 없음 |
| C3 | 대사 뒤 빈 꼬리 → 웅얼거림 | 없음 | "대사 한 줄 2~4초"만 있다 | 없음 |
| C4 | 중요한 것 앞에 | 부분 | ACTIVE_REFERENCES가 2번째 블록, 시작 이미지가 첫 참조 | 없음 |
| C5 | 길이 상한 | 부분 | `live-action.md` 약 5,500자 + 사건 먼저 줄이기(E-29). 영어 5,500자는 약 850~950단어로 공식 1000단어 상한 안이다. Higgsfield 스킬의 "200토큰"과는 크게 다르다 | 상충(근거끼리). 키트 쪽 실측이 있으니 유지 |
| C6 | 실패 조건 + 색 배분 | 부분 | `= failed take` 패턴은 연기·속도·걸음에 있다. 색·빛 배분 문장은 없다 | 없음 |
| C7 | 참조 속 요소를 사실로 덮어쓰기 | 없음 | 키트는 그 사진을 빼라고 한다(`fixes.md` "The reference photo's face, colour, or lighting bleeds in") | 없음(빼기가 불가능할 때의 보조책) |
| C8 | 잠금 문장 반복 | 있음 | 지침 26 "고정 문장은 글자 그대로", LIGHT LOCK, `--must-include` | 없음 |
| C9 | 비유·관용구 금지 | 부분 | `live-action.md` CHARACTER_ACTING "Emotion adjectives"가 흔한 실수로 적혀 있다. 비유·관용구는 언급이 없다 | 없음 |
| C10 | 전문 용어 = 용어 + 결과 | 있음 | `live-action.md` OPTICS "FOV + 관찰 결과 3개", `check_prompt.py` mm 경고 | 없음 |
| C11 | 동작 요약, 인상 동작만 자세히 | 부분 | 사건 수 제한이 같은 방향이다 | 없음 |
| C12 | 첫 1초 와이드 | 없음 | `fixes.md` "첫 프레임부터 인물 제자리, 빈 도입 금지" | 부분 충돌. 우리는 시작 이미지가 0:00이고 컷마다 화각이 정해져 있다. 클로즈업 컷 앞에 와이드 1초를 넣으면 컷 설계가 바뀐다. 가져오지 않는다(마스터 컷에서만 검토) |
| C13 | 라벨 블록 구조 | 있음 | 15블록, 이미지 틀 | 없음 |
| C14 | 블록 내 순서 | 부분 | 15블록 순서는 고정이고 공식 순서(카메라 → 동작 → 공간 → 오디오)와 대체로 같다 | 없음 |
| D1 | 얼굴 클로즈업 독립 참조 | 부분 | 시트 오른쪽 패널이 "컷 생성 때 얼굴 참조로 쓰는 패널"이다. 다만 영상에는 3패널 한 장이 요소로 붙는다(`character.md` 스펙) | 없음(조건부 추가) |
| D2 | 다중 뷰 시트(2.0 비권장, 2.5 조건부) | 부분 | 3패널 한 장 시트 | **잠재 충돌.** 2.5 공식은 주체 5명 이하면 허용한다. 우리 컷은 대부분 1~2명이라 지금 방식이 공식 범위 안이다. 얼굴이 흐를 때만 D1로 간다 |
| D3 | 쌍둥이 방지·인원 헤더 | 부분 | `FIRST_FRAME` "Exactly [N] people are visible"(범위가 첫 프레임뿐이다), `fixes.md` 배경 인물 headcount | 없음 |
| D4 | 인원 상한 | 부분 | `live-action.md` "세 명 이상이면 줄이기보다 샷 나누기" | 없음 |
| D5 | 주체 정의·같은 이름 | 있음 | 요소 ID 태그, `ACTIVE_REFERENCES` | 없음 |
| D6 | 묘사량(미결) | 있음(한쪽 선택) | 컷에는 WARDROBE 문장만, IDENTITY는 넣지 않는다 | 없음 |
| D7 | 시트는 지루하게 | 있음 | 단색 스튜디오 배경, 세 패널 같은 빛 | 없음 |
| D8 | 머리 없는 정면 패널 | 있음 | `character.md` 변형 A/B | 없음 |
| D9 | 시트 초상 3/4 | 없음 | 오른쪽 패널은 정면이다 | 없음(시험 필요, 바꾸면 기존 시트와 달라진다) |
| D10 | 나이 쓰지 않기 | 없음 | `ACTIVE_REFERENCES`에 `[NAME] ([age])` | 부분 충돌. 성인이라면 위험이 적다. 아이·10대가 나오는 작품에서만 적용한다 |
| D11 | Soul ID 사진 규칙 | 없음 | 키트는 Soul ID를 쓰지 않는다 | 없음(쓸 때 참고) |
| D12 | 두 인물 상호작용 한계 | 부분 | 사건 수·인원 규칙 | 없음 |
| D13 | 배경 인물 전용 초상 | 부분 | `fixes.md` "이름 없는 사람은 얼굴 없는 실루엣" | 없음 |
| E1 | locked-off 명시, handheld 금지 | 있음 | `live-action.md` CAMERA "Fixed and completely locked…", `check_prompt.py` 고정+이동 동시 경고 | 없음 |
| E3 | 팔레트 앵커 3~5색 | 부분 | LIGHT LOCK, STYLE. 색 이름 앵커는 없다 | 없음 |
| E4 | 심도 두 요청 구분 | 부분 | OPTICS 심도, §3 2번 "the [background] falls off softly" | 없음 |
| E7 | Cinema Studio 512자 | 해당 없음 | 키트는 Seedance 2.5 기본 | — |
| G1 | 긍정형 우선 | 부분 | §1 원칙 6 "원하는 상태 먼저", 금지 범위 좁히기. 다만 입 잠금은 부정형이다 | 없음 |
| G2 | 금지가 정당한 기준 | 있음 | 원칙 6 "실제로 난 실패만 Forbidden에", `live-action.md` "금지어가 그것을 부를 수 있다" | 없음 |
| G3 | 자막·로고·워터마크 | 있음 | 15블록 Forbidden 기본 줄 | 없음 |
| G4 | 행동 긍정형 | 부분 | "Wanted state first, failure as outcome" | 없음 |
| G5 | 말하지 않는 입 = 긍정 사실 | 부분 | `fixes.md`·`live-action.md` "does not say a single word: no attempt to speak, no parted lips, no mouthing"(부정형, 실전에서 쓰인 문장) | 약한 충돌. 기존 문장은 승인 컷에서 왔다. 대체하지 말고 앞에 긍정 사실을 더하는 쪽만 시험한다 |
| H1 | 역할 + 전이 금지 | 있음 | `image-prompt/SKILL.md` §2 권한 블록, `live-action.md` REFERENCE AUTHORITY | 없음 |
| H2 | 번호 지칭 | 있음 | 참조 태그 규칙 | 없음 |
| H3 | 참조 속 글자 제거 | 없음 | — | 없음 |
| H4 | 효과는 참조 영상으로 | 부분 | 별·새는 후반 오버레이 | 없음 |
| H5 | 장소 상속 금지 | 있음 | DO NOT TRANSFER, REFERENCE AUTHORITY | 없음 |
| H6 | 장소 3/4·앵커·빛 하나 | 있음 | `location.md` 대각선 시점(빈 공간 플레이트만), 랜드마크 좌·중·우, LIGHT LOCK | 없음 |
| H7 | 빈 장소 워크스루로 반대 앵글 | 없음 | `location-view.md`는 이미지로 새 시점을 만든다 | 없음(고정 카메라 원칙은 에셋 제작용 영상이라 해당 없음) |
| H8 | GEO 지도 | 있음 | `LOCATION_MAP` 좌표 줄 + 4줄, 화면 기준 좌우 | 없음 |
| H9 | 정확한 참조는 지칭만 | 부분 | 지칭과 서술을 함께 한다 | B1과 같은 쟁점 |
| I1 | 한 번에 하나 | 있음 | 지침 20 | 없음 |
| I2 | 싸게 먼저 | 있음 | 지침 8, draft 480p | 없음 |
| I3 | 같은 프롬프트도 다름 | 부분 | `fixes.md` "같은 테이크는 재현할 수 없다" | 없음 |
| I4 | 10~15회 뒤 단순화 | 있음(더 엄격) | 지침 9 "같은 실패 두 번이면 멈춤" | 없음 |
| I5 | 실제 끝 상태 기록 | 부분 | 연속성 표, `assembly` 마지막 프레임 추출. "계획이 아니라 관찰한 끝"이라는 문장은 없다 | 없음 |
| I6 | 정체성은 시트로 재고정 | 부분 | ACTIVE_REFERENCES에 인물 요소를 늘 붙인다. 뽑은 프레임의 권한 범위는 적혀 있지 않다 | 없음 |
| I7 | 연장 이음매 6/1프레임 | 없음 | `video-prompt/SKILL.md` "Extend may change the aspect ratio"만 있다 | 없음 |
| I8 | 끝 클릭 페이드 | 없음 | — | 없음 |
| I9 | 프레임 단위 검토 | 부분 | 판정 ✔/✘, `qa-metrics.md` 텍스처 지터 | 없음 |

**요약.** 키트는 이미 공식 가이드와 상위 커뮤니티 스킬의 핵심을 대부분 갖고 있다. 15블록, 사건 수, 참조 권한, 화면 기준, 머리 없는 시트, LIGHT LOCK, 한 번에 하나, 실제 난 실패만 금지가 그렇다. 빠진 것은 주로 세 가지다. (1) Seedance 공식 문제 해결 문서의 구체적 처방(얼굴 클로즈업 단독 참조, 쌍둥이 문장, 웅얼거림, 연장 이음매), (2) 움직임 물리의 세부 문장(불변 물체, 조작 인과 사슬, 되감기), (3) 이미지 쪽 `photorealistic`·관용구 같은 작은 단어 규칙이다. 가장 큰 쟁점은 B1/H9다. "시작 이미지가 있으면 다시 서술하지 말라"는 공식 근거가 여럿인데, 키트의 15블록은 다시 서술한다.

---

## 4. 추가 권고 Top 10

순위는 (기대 효과 × 근거 강도 ÷ 도입 비용)으로 매겼다. 문장은 키트 파일 형식에 맞춰 영어로 썼다(AI용 파일은 영어라는 지침 1). **[시험 필요]**가 붙은 것은 실제 Higgsfield에서 480p A/B를 해 보기 전에 기본값으로 넣지 않는다.

**1. 얼굴이 시트와 달라질 때 얼굴만 따로 참조** — `kit/skills/video-prompt/fixes.md` 표에 행 추가. 근거: 공식 문서(S4 V-1·V-7), 2.5에서는 조건부(S6). **[시험 필요: Higgsfield 요소(Element)가 잘라낸 얼굴 한 장과 시트를 함께 받을 때의 동작]**
> | The face drifts away from the sheet, or two copies of the same person appear | Crop the sheet's right panel to the head only (little neck, no background) and attach it as a separate face element before the sheet. In `ACTIVE_REFERENCES`: `<<<[face element]>>> controls only [NAME]'s face. <<<[sheet element]>>> controls only hair, body and wardrobe.` Keep the sheet; never attach a multi-view sheet as the only identity reference when more than five people are referenced |

**2. 쌍둥이·복제 방지를 샷 전체 범위로** — `kit/skills/video-prompt/live-action.md` 빈 틀의 `REQUIRED_AND_FORBIDDEN_CONSTRAINTS` Required에 기본 줄 추가. 지금은 `FIRST_FRAME` 범위에만 인원 수가 있다. 근거: 공식 문서(S4 V-7) + Hell Grind(S10). 원칙 6(실제 난 실패만 금지)과 부딪치지 않도록 금지가 아니라 Required의 개수 상태로 둔다.
> `- Exactly [N] people for the whole shot: [NAME], [NAME]. At no moment are two people with the same face, clothes and accessories on screen. (ENTIRE_SHOT)`

**3. 대사 뒤 빈 꼬리를 남기지 않기** — `kit/skills/video-prompt/SKILL.md` §2 표의 "Event count" 칸 끝 또는 새 행 "Dialogue window". 근거: 공식 문서(S4 V-11: 길이를 맞추면 웅얼거림 약 10%), 한 사람 측정(S9).
> `Dialogue window: the clip must not outlast its content. After the last line, either end the clip within about 1 s or write what fills the rest (a named pause beat, one sound effect, the hands continuing their business). A line of six words or fewer in a 4-second-plus clip invites invented mumbling: lengthen the line or shorten the clip.`

**4. 이미지 틀에 `photorealistic`** — `kit/skills/image-prompt/location.md`, `first-frame.md`, `location-view.md`의 여는 문장. 근거: 공식 문서(S1). 비용이 거의 없다. 그림체 작품(`style.md`)에는 넣지 않는다.
> 여는 문장을 `Create a photorealistic photograph of …` / 편집 틀이면 `… The result stays a photorealistic photograph.`로. `image-prompt/SKILL.md` §5 GPT Image 행에 `Write "photorealistic" in the first sentence; camera body, lens and film-stock names steer the look only, not exact optics (OpenAI guide).` 추가.

**5. 인접 물체 불변 + 조작 인과 사슬** — `kit/skills/video-prompt/live-action.md` "Sentences used as is"에 두 줄 추가, `PHYSICS` 흔한 실수 칸에 "Not naming what stays put next to the moving object". 근거: 한 사람 주장(S9, 실전 코퍼스). 근거는 약하지만 문장이 짧고 기존 `[상태 머신]`과 같은 방향이다.
> `[불변] [ADJACENT OBJECT] stays [attached to / resting on] [surface] throughout. Only [OBJECT] moves.`
> `[조작] [OBJECT] starts [initial structure]. [Screen-side hand] holds [part] still against [surface]; [other hand] [applies force at point, direction]. [Material visibly responds]. It ends [finished state] and stays that way.`

**6. Seedance 2.5 시간 문법 검사** — `kit/skills/higgsfield-generation/check_prompt.py` `check_video`에 경고 2개. 근거: 공식 문서(S6 "以1秒为单位", "不建议用时间戳控制频率/频次").
> (a) `0:02.5`처럼 소수 초가 있으면 `WARN: Seedance 2.5는 1초 단위 타임스탬프를 듣는다. 정수 초로 쓴다`
> (b) `\b(?:twice|three times|\d+ times) (?:per|a|in one) second\b`가 있으면 `WARN: 타임스탬프로 빈도를 제어하지 않는다(공식)`.
> 키트에 이미 소수 초 사례가 있는지 먼저 OK 대장에서 확인한다. 승인 컷에서 가져온 줄은 예외다.

**7. 비유·관용구 금지** — `kit/skills/acting/SKILL.md` 쓰는 법 목록과 `live-action.md` `CHARACTER_ACTING` 흔한 실수 칸. 근거: 공식 문서(S6 "减少成语使用"), 한 사람 주장(S8 failure-atlas). 한국어 사용자의 지시("얼굴이 굳었다", "눈이 휘둥그레")가 영어 관용구로 옮겨지기 쉬워서 효과가 크다.
> `No idioms or figurative phrases ("his face fell", "her heart sank", "eyes like saucers"): the model may draw them literally. Name the feeling in one plain word, then one physical anchor: "hurt — the jaw tightens once and the gaze drops to the cup."`

**8. 되감기 방지와 정지 장면의 미세한 삶** — `kit/skills/video-prompt/fixes.md` 행 2개. 근거: 한 사람 주장(S9 FAILURE-MODES 되감기, S10 미세한 삶). 고정 카메라 원칙과 잘 맞는다(카메라가 아니라 인물만 살린다).
> | The action finishes early and plays back in reverse (steps forward, then back) | Give the remaining seconds an owner: `From 0:0[x] to the end [he] holds [final pose]; [breath lifts the chest every two seconds]. Returning toward the start position = failed take.` A camera move gets its end point: `… and stops on [framing]` |
> | A still shot reads frozen, like mannequins | Replace any "nobody moves / stays perfectly still" with held tension and one micro-event every 1–2 s per visible person (breath, a blink, weight shifting) |

**9. 연장·이어 붙이기 이음매 처방** — `kit/skills/assembly/SKILL.md`(이어 붙이기 단계)와 `video-prompt/SKILL.md` §3 Seedance 행. 근거: 공식 문서(S4 V-6·V-8·A-1). 다만 2.0 문서이고, 2.5는 "더 안정적인 편집·연장"을 내세운다. **[시험 필요: 2.5 연장 결과에서도 점프가 나는지]**
> assembly: `Seedance extend seams: if the join jumps or steps back, trim 6 frames from the end of the earlier clip and 1 frame from the start of the later one, then compare the boundary side by side. If the last clip ends on speech, fade its last 0.2 s of audio to 0 (end-click noise).`
> video-prompt §3: `Each extension degrades the picture (blotchy faces) and the loss adds up: re-attach the original sheet and location elements on every extension; a pulled last frame controls pose and state only, never identity.`

**10. 말하지 않는 인물의 입: 긍정 사실을 앞에 추가** — `kit/skills/video-prompt/live-action.md` AUDIO 틀의 무언 문장 앞. 근거: 한 사람 주장(S9, 스스로 미실험이라고 밝힘) + Runway 공식(부정 표현은 결과가 예측되지 않는다). 기존 문장은 실전에서 쓰인 것이라 지우지 않는다. **[시험 필요: 같은 컷으로 긍정 사실이 있을 때와 없을 때를 비교]**
> `[PERSON 2] keeps lips at rest and jaw closed, breath lifting the chest, eyes on [PERSON 1]. [PERSON 2] does not say a single word: no attempt to speak, no parted lips, no mouthing.`

### Top 10에 넣지 않았지만 시험할 만한 것
- **B1/H9 I2V 재서술 줄이기** **[시험 필요, 영향 큼]**: Runway·Higgsfield 공식 스킬·Seedance 2.5 공식이 모두 "시작 이미지가 있으면 다시 쓰지 말라"고 한다. 한 컷으로 15블록 원본과, `LOCATION_MAP`을 좌표 줄 1줄로 줄이고 `FIRST_FRAME`을 인물 상태만 남긴 판을 480p로 비교해 볼 가치가 있다. 근거는 강하지만 키트의 기존 실험(E-29, 참조 권한 문장)과 방향이 달라서 순위에서 뺐다.
- **C6 색 배분 + 실패 조건 문장**: LIGHT LOCK이 틀어질 때 `fixes.md` 행으로 넣을 만하다(`The dominant colour is [X]. [Y] exists only inside [source] and a [size] halo. If the frame turns [Y], the frame is wrong.`). 한 팀의 경험뿐이다.
- **E3 팔레트 앵커 3~5색**: Sora 공식이다. `decisions.md`의 룩 기준에 색 이름 3~5개를 한 번 정해 STYLE에 그대로 쓰는 방식이다. 컷 간 색 맞춤(`color-continuity`)의 앞 단계로 쓸 수 있다. 우리 모델(Seedance)에서 같은 효과가 나는지는 근거가 없다.
- **H3 참조 속 글자 제거**: 간판·라벨이 있는 장소 플레이트를 영상 참조로 쓰기 전에 글자를 지운다. 공식이고 비용이 적지만, 키트에서 자막이 실제로 문제가 된 기록이 없어 뺐다.
- **D10 나이 숫자 빼기**: 미성년 인물이 나오는 작품에서만.

### 가져오지 말 것 (키트 기본값과 충돌)
- A7 "no cinematic lighting/grading"(OpenAI 사실감 예시), B13 핸드헬드로 배경 가리기, C12 첫 1초 와이드(마스터 컷 외). 모두 시네마틱·고정 카메라·컷 설계 기본값과 부딪친다.
- Higgsfield 공식 스킬의 "약 200토큰" 상한: 키트의 실측(5,000~5,500자에서 확정)과 Seedance 공식 상한(영어 1000단어)이 더 구체적이다.

---

## 근거가 약하거나 확인하지 못한 것
- Kling·Veo·Runway·Higgsfield 블로그와 Reddit은 본문을 열지 못했다. 표의 해당 항목은 검색 요약에 기댄다. 특히 Veo의 negative 필드 지원 여부, Kling 멀티샷 상한(5 vs 6)은 출처끼리 다르다.
- 화산엔진 Seedance 2.0 가이드(S7)는 S8 저장소가 옮긴 인용으로만 봤다. 2.5 가이드(S6)는 제3자가 GitHub에 올린 공식 PDF 미러라 원본과 같은지 해시로 확인하지 않았다.
- S9·S10의 많은 규칙은 한 제작팀(Higgsfield Hell Grind)이나 한 코퍼스의 경험이고, S9는 스스로 "미측정"이라고 표시한 항목이 많다. 키트 기본값을 바꾸는 근거로 쓰기 전에 480p A/B가 필요하다.
- GPT Image 2.5의 공식 프롬프트 문서는 찾지 못했다. OpenAI Cookbook은 gpt-image-2 기준이다.
- arXiv 2608.16717(샷 단위 구조화가 전역 프롬프트보다 낫다는 Seedance 벤치마크, S8 인용)은 검색으로 찾지 못해 목록에서 뺐다.
- 네트워크 허용 목록에 `developers.openai.com`, `docs.cloud.google.com`, `docs.byteplus.com`, `kling.ai`, `higgsfield.ai`, `help.runwayml.com`, `blog.google`를 추가하면 위 항목을 원문으로 다시 확인할 수 있다.
