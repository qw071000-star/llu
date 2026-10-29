# 실사 시네마틱 AI 영상용 Claude 도구 조사 (Claude + Higgsfield)

- 조사일: 2026-10-29 · 방법: WebSearch, WebFetch만 썼다. MCP 도구는 부르지 않았고, 가입이나 설치도 하지 않았다.
- 대상: Claude Code와 Claude 앱(claude.ai·Desktop·Cowork)으로 실사 단편, 인물 연기, 장소·인물 일관성 작업을 하는 사람.
- **접근 한계:** 이 세션의 네트워크에서는 `higgsfield.ai`, `techsy.io`, `mindstudio.ai`, `claudefa.st`가 열리지 않았다. 이 사이트들의 내용은 **검색 결과 요약만으로** 적었고 본문은 읽지 못했다. GitHub 저장소는 직접 열어 확인했다.

## 표기

| 표기 | 뜻 |
|---|---|
| **공식** | 서비스 회사 본인의 저장소·문서·블로그에서 확인했다 |
| **커뮤니티** | 제3자가 만들었고, 저장소나 등록 페이지에서 존재를 확인했다 |
| **확인 안 됨** | 검색 요약·애그리게이터·홍보 글에서만 보았다 |
| [사실] / [추정] | 출처에 적힌 내용 / 내 판단 |

---

## 1. Higgsfield 연결

### 1-1. Higgsfield MCP (호스팅 커넥터): 공식
- **하는 일:** Claude에서 Higgsfield 생성(이미지·영상·오디오), 캐릭터, 프로젝트·에셋 관리를 직접 실행한다. 생성하면 내 Higgsfield 크레딧이 빠진다. [사실, 검색 요약]
- **쓰는 곳:** 둘 다. 앱(claude.ai 웹·Desktop, 모바일 제외)과 Claude Code에서 쓸 수 있다.
- **연결:**
  - 앱: 설정 → 커넥터 → 커스텀 커넥터 추가 → URL `https://mcp.higgsfield.ai/mcp` → Higgsfield 로그인·승인. API 키는 필요 없고 **유료 구독이 필요하다**. [사실, Higgsfield 도움말 검색 요약]
  - Claude Code: `claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp`, 첫 호출 때 브라우저 OAuth가 열린다. [확인 안 됨, techsy.io 요약. 공식 문서와 대조하지 못했다]
- **참고 [사실, 이 세션의 도구 목록에서 이름만 봤고 호출하지 않았다]:** 지금 커넥터는 `generate_image/video/audio`, `*_batch`, `jobs_wait`, `upscale_image`, `upscale_video`, `reframe`, `outpaint_image`, `motion_control`, `manage_reference_elements`·`show_reference_elements`(요소), `show_characters`, `create_voice`·`dubbing`·`voice_change`, `video_analysis_create`, `scene_builder_3d_*`(장소 3D 앵글), `models_explore`, `get_project_asset_prompt` 등을 노출한다. 서드파티 블로그는 "도구 5개"라고 적었는데 이는 낡은 정보로 보인다. [추정]
- **출처:** https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent · https://techsy.io/en/blog/higgsfield-mcp-claude-code · https://creatify.ai/blog/what-is-higgsfield-mcp-what-it-does-what-it-costs-and-how-to-use-it

### 1-2. Higgsfield CLI + 공식 스킬 `higgsfield-ai/skills`: 공식
- **하는 일:** 스킬 9개. `higgsfield-generate`(30개 넘는 모델로 이미지·영상·3D·오디오), `higgsfield-soul-id`(사진 5~20장으로 얼굴 ID를 학습해 `reference_id` 반환), product-photoshoot, brandkit, marketplace-cards, websites, faceless-video, video-explainer, youtube-thumbnail. 실사 단편에 직접 쓸 만한 것은 **generate와 soul-id 두 개**이고 나머지는 광고·마케팅용이다. [사실]
- **쓰는 곳:** Claude Code(그리고 Cursor·Codex). 앱에서 쓰는 방법은 적혀 있지 않다.
- **설치:** `npx skills add higgsfield-ai/skills` / `gh skill install higgsfield-ai/skills` / `/plugin marketplace add higgsfield-ai/skills` → `/plugin install higgsfield@higgsfield`. 어느 방법이든 CLI 설치와 `higgsfield auth login`까지 해 준다. MIT, 별 약 1.8k, v0.14.0. [사실]
- **주의:** CLI는 생성마다 크레딧을 쓴다. 웹 UI의 "unlimited" 요금제는 CLI에 적용되지 않는다는 보고가 있다. [확인 안 됨, dev.to 요약] MCP와 CLI 중 어느 쪽이 나은지는 글마다 다르다(MindStudio는 CLI를 권한다). [확인 안 됨]
- **출처:** https://github.com/higgsfield-ai/skills · https://higgsfield.ai/creator-hub/help-center/mcp-cli/how-do-i-access-higgsfield-via-cli · https://dev.to/dineshstack/how-to-automate-ai-video-creation-with-claude-higgsfield-d2j

### 1-3. Composio 경유 Higgsfield: 확인 안 됨
- 제3자 중계 MCP(`https://connect.composio.dev/mcp`)다. 공식 커넥터가 있으니 쓸 이유가 적다.
- **출처:** https://composio.dev/toolkits/higgsfield/framework/claude-cowork

---

## 2. 다른 생성 서비스 MCP

| 도구 | 하는 일 | 쓰는 곳 | 설치·연결 요약 | 신뢰도 | 출처 |
|---|---|---|---|---|---|
| **Runway API MCP** (`runwayml/runway-api-mcp-server`) | 이미지→영상, 이미지, 업스케일, Aleph 영상 편집, TTS. 기본 모델로 Seedance 2, Nano Banana Pro, Aleph 2가 적혀 있다 | Desktop(확장), 원격 HTTP | Node 빌드 + `RUNWAYML_API_SECRET`. **저장소는 보관(archived) 상태**이고 `runway.com/mcp`와 `dev.runwayml.com/agents`로 안내한다 | 공식(옛 버전). 새 경로는 확인 안 됨 | https://github.com/runwayml/runway-api-mcp-server |
| **Luma MCP** (bobtista) | Dream Machine API: t2v, i2v, 키프레임, 연장, 업스케일 | Desktop·Code | `LUMA_API_KEY` | 커뮤니티 | https://mcpservers.org/servers/bobtista/luma-ai-mcp-server |
| **Kling MCP** (199-biotechnologies) | Kling t2v·i2v | Desktop·Code | API 키 | 커뮤니티 | https://glama.ai/mcp/servers/@199-biotechnologies/mcp-kling |
| **PiAPI MCP** | Midjourney와 Kling을 중계 | Desktop | PiAPI 키. 영상 생성이 Claude 타임아웃에 걸릴 수 있다고 적혀 있다 | 커뮤니티 | https://mcpservers.org/en/servers/apinetwork/piapi-mcp-server |
| **fal MCP** (raveenb `fal-mcp-server`, M1Vision) | fal에 올라온 이미지·영상·음악 모델 전반 | Desktop·Code | PyPI, `FAL_KEY` | 커뮤니티(fal 공식 아님) | https://lobehub.com/en/mcp/raveenb-fal-mcp-server · https://pypi.org/project/fal-mcp-server/ |
| **Veo / Gemini 미디어 MCP** (`gemini-media-mcp`, `veo-mcp-server`) | Veo 영상, Gemini 이미지 | Desktop·Code | `uvx gemini-media-mcp setup`. 영상에는 Vertex AI 자격 증명이 필요하다 | 커뮤니티(Google 공식 아님) | https://pypi.org/project/gemini-media-mcp/ · https://pypi.org/project/veo-mcp-server |
| **ComfyUI MCP**: Comfy Org 공식(Cloud 베타, 로컬 버전 2026-08) + 커뮤니티(artokun, zturner1, comfy-pilot) | 워크플로 실행·편집, 노드 스키마, 모델 관리 | Code·Desktop | 공식: Comfy Cloud 얼리 액세스 또는 comfy-cli 로컬. 커뮤니티: npx/설정 | 공식(베타) / 커뮤니티 | https://docs.comfy.org/development/cloud/mcp-server · https://comfyui-wiki.com/en/news/2026-08-11-comfy-mcp-local-server |

[추정] Higgsfield가 Kling·Seedance·Veo·Flux·GPT Image·Nano Banana를 이미 한곳에 묶고 있으니, Higgsfield 사용자가 모델별 MCP를 따로 붙일 이유는 적다. 예외는 Higgsfield에 없는 기능이다. 예를 들어 Runway Aleph의 영상 편집, 그리고 로컬 GPU에서 돌리는 ComfyUI(Topaz 노드, 보간, 디플리커)가 있다.

---

## 3. 편집·후반 작업 도구

| 도구 | 하는 일 | 쓰는 곳 | 설치·연결 요약 | 신뢰도 | 출처 |
|---|---|---|---|---|---|
| **DaVinci Resolve MCP** (samuelgursky) | Resolve 스크립팅 API 전체: 타임라인, 미디어 풀, 렌더, 마커, **그레이딩·LUT**, Fusion, Fairlight. `.drp` 파일을 직접 고치는 서버도 따로 있다 | Code·Desktop | `npx davinci-resolve-mcp setup`. Resolve 18.5+, Python 3.10+. **Studio 권장**: 무료판은 in-app bridge로 쓰는데 21.0.x에서만 확인됐다. 21.1에서 Python 스크립팅이 Studio 전용이 됐다 | 커뮤니티(별 약 3.8k, 활발) | https://github.com/samuelgursky/davinci-resolve-mcp |
| Resolve MCP (Tooflex), resolve-claude-mcp(`set_lut`) | 같은 계열의 작은 프로젝트 | Desktop | uv | 커뮤니티 | https://mcpservers.org/servers/Tooflex/davinci-resolve-mcp |
| **Adobe for creativity 커넥터** | Photoshop, Premiere, Lightroom, Firefly, Express 등에서 도구 50개 넘게 조율 | 앱(커넥터 디렉터리) | Claude 커넥터 추가 + Creative Cloud 구독. 2026-04-28 출시 | 공식(Adobe 블로그) | https://blog.adobe.com/en/publish/2026/04/28/adobe-for-creativity-connector |
| Premiere Pro MCP (antipaster, nepfaff, hetpatel-11, jordanl61) | CEP/UXP 패널로 Premiere 제어. hetpatel-11은 `apply_lut` 도구가 있다 | Desktop·Code | 패널 설치 + Node. 실험적이다(일부 도구는 자리만 있음) | 커뮤니티 | https://github.com/antipaster/Adobe-Premiere-Pro-MCP · https://glama.ai/mcp/servers/hetpatel-11/Adobe_Premiere_Pro_MCP |
| **ffmpeg MCP**: `misbahsy/video-audio-mcp`(도구 약 28개: 트림·이어붙이기·자막·오버레이·속도·페이드), Kush36Agrawal `execute_ffmpeg`(명령 그대로 실행) | 컷 이어붙이기, 트림, 재인코딩, 자막 입히기 | Desktop·Code | uv + ffmpeg가 PATH에 있어야 한다 | 커뮤니티(작고 유지 상태 불명) | https://github.com/misbahsy/video-audio-mcp · https://mcpservers.org/servers/Kush36Agrawal/Video_Editor_MCP |
| Tella MCP(원격) | 클립에 LUT 프리셋이나 `.cube` 적용 | 앱·Code(OAuth) | 호스팅 | 확인 안 됨 | https://www.tella.com/blog/apply-luts-with-mcp-ai-agent-color-grade |
| **Remotion 에이전트 스킬** | 코드로 영상 조립: 자막, 타이틀, 렌더 | Code | `npx skills add remotion-dev/skills` | 공식(Remotion)으로 보이지만 블로그로만 확인했다 | https://www.tella.com/blog/how-to-use-remotion-agent-skills-with-claude-code |
| Frame.io MCP | 찾지 못했다 | — | — | 없음 | — |

[추정] Claude Code를 쓴다면 ffmpeg MCP는 없어도 된다. Bash에서 `ffmpeg`를 바로 부르는 편이 더 투명하다. 스킬 하나에 명령 레시피를 담는 쪽이 낫다(아래 4-1 후보).

---

## 4. 오디오·자막

| 도구 | 하는 일 | 쓰는 곳 | 설치·연결 요약 | 신뢰도 | 출처 |
|---|---|---|---|---|---|
| **ElevenLabs MCP (호스팅)** | TTS, 보이스 디자인·클론, **효과음**, 음악, 오디오 분리, STT | 앱·Code | 원격 `https://api.elevenlabs.io/v1/mcp`, OAuth. 로컬 `elevenlabs-mcp`(uvx)는 **보관 상태이고 호스팅판으로 대체됐다**. 무료 월 1만 크레딧 | 공식 | https://github.com/elevenlabs/elevenlabs-mcp · https://elevenlabs.io/blog/introducing-elevenlabs-mcp |
| Higgsfield 오디오(같은 커넥터 안) | `generate_audio`, `create_voice`, `dubbing`, `voice_change` | 둘 다 | 1-1과 같다 | 공식(도구 이름만 확인) | 1-1 참조 |
| Fast-Whisper MCP / whisper-windows-mcp | 로컬 전사 → SRT/VTT | Desktop | Python 3.10+ / whisper.cpp | 커뮤니티 | https://glama.ai/mcp/servers/Jacobngai/fast-whisper-mcp-server · https://mcpservers.org/servers/eviscerations/whisper-windows-mcp |

---

## 5. 정리·레퍼런스 관리 커넥터

| 도구 | 하는 일 | 쓰는 곳 | 신뢰도 | 출처 |
|---|---|---|---|---|
| Google Drive 커넥터 | 문서·시트·PDF 찾기와 읽기(레퍼런스, 대본) | 앱(코드에서는 원격 MCP) | 공식(Anthropic 디렉터리) | https://www.tomsguide.com/ai/claude-can-now-connect-to-google-drive-canva-slack-and-more-heres-how-to-try-it |
| Notion 원격 MCP | 페이지·DB 읽기와 쓰기(컷 목록·에셋 대장 DB) | 둘 다(OAuth) | 공식 | https://developers.notion.com/docs/hosting-open-source-mcp |
| Airtable | 공식 MCP를 찾지 못했다 | — | 확인 안 됨 | — |
| Canva, Blender(04-28 출시) | 디자인·3D(장소 블로킹) | 앱 | 공식(보도 기준) | https://alternativeto.net/news/2026/4/anthropic-launches-claude-connectors-for-adobe-blender-ableton-and-more/ |

---

## 6. 공유된 Claude 스킬 (영상 프롬프트·시네마토그래피)

| 스킬 | 내용 | 실사 단편에 맞는 정도 | 설치 | 신뢰도 | 출처 |
|---|---|---|---|---|---|
| **OSideMedia/higgsfield-ai-prompt-skill** (별 약 818, MIT) | 하위 스킬 32~35개. MCSLA 구조(Model·Camera·Subject·Look·Action), camera·motion·style·**soul·acting**·cinema·seedance·troubleshoot·negative-constraints, 실패 사례 목록 | **높음.** Higgsfield 실사에 가장 가깝다. 신원과 동작 지시를 떼어 쓰라는 "하드 룰", 연기 0~5점 평가, Kling 3.0은 16:9·9:16·1:1만 낸다는 메모가 있다 | `~/.claude/skills/higgsfield`에 clone. claude.ai 프로젝트에는 파일 업로드 | 커뮤니티 | https://github.com/OSideMedia/higgsfield-ai-prompt-skill |
| cth9191/higgsfield-seedance2 (별 7) | Seedance 2.0 스킬 16개. 01 Cinematic, 05 Fight, 16 Shot Builder 등. 입력 12개·2~15초 제한 메모 | 중간 | SKILL.md 복사 | 커뮤니티 | https://github.com/cth9191/higgsfield-seedance2 |
| rediumvex/ai-video-generator-claude (별 약 443) | Seedance 2.0 스킬 10개. 바이럴, SaaS, 퍼스널 브랜드 등 | **낮음**(마케팅용) | clone + `install.py` | 커뮤니티 | https://github.com/rediumvex/ai-video-generator-claude |
| CyberJ0605/cinematic-video-prompt-engineer-skill | 줄거리 → Kling·Seedance·Veo·Sora 프롬프트. 미세 표정, 사운드, 이어 붙이기 논리 | 중간 | `npx skills add CyberJ0605/...` | 확인 안 됨(목록 페이지만 봄) | https://www.awesomeskills.dev/en/skill/cyberj0605-cinematic-video-prompt-engineer-skill |
| **Shanyin-ai/shanyin-director-master** (별 약 609, 중국어) | 대본 → 톤·페이싱·수정 → 9열 콘티표(xlsx) | 중간. 대본 분해용으로 참고할 만하다 | 스킬 설정에 붙여 넣기 | 커뮤니티 | https://github.com/Shanyin-ai/shanyin-director-master |
| inferen-sh/skills `storyboard-creation` | 샷 종류, 180도 규칙, 매치 컷, 콘티 패널 생성 | 중간 | `npx -y skills add inferen-sh/skills --skill storyboard-creation --agent claude-code` | 커뮤니티 | https://claudemarketplaces.com/skills/inferen-sh/skills/storyboard-creation |
| nolanx storyboard-shot-design, kaigani shot-list-generator / directors-room, majiayu000 create-storyboard | 샷 설계, 커버리지·블로킹, JSON 샷 리스트 | 참고용 | 각 저장소 | 확인 안 됨 | https://tessl.io/registry/skills/github/nolanx-ai/nolanx.ai/storyboard-shot-design/review · https://skill-web-8ek.pages.dev/skill/shot-list-generator-skill |
| claudskills.com: shortfilm-prompt, video-prompting-guide, mf-video-prompt, mf-antislop | 모델별 요령. 예: Seedance는 IP 이름을 막고 Sora는 간결한 프롬프트를 선호한다 | 참고용 | 레지스트리 | 확인 안 됨 | https://claudskills.com/skills/shortfilm-prompt/ |

[추정] 우리 키트의 acting, video-prompt(15블록), image-prompt는 위 커뮤니티 스킬보다 규칙이 촘촘하다. 그대로 가져다 쓸 것은 없고, **OSideMedia의 troubleshoot·negative-constraints 실패 목록**만 키트의 `fixes.md`와 견줘 볼 만하다.

---

## 7. Higgsfield 실사 시네마틱 팁 (사용자·벤더 자료)

출처는 대부분 Higgsfield 자체 블로그(홍보성)와 r/HiggsfieldAI 아카이브다. 일화 수준으로 본다.

**캐릭터 일관성**
- Soul ID는 사진 5장 이상으로 학습하고 3~5분 걸린다. 다양하고 깨끗한 소수 사진이 많은 불균질 사진보다 낫다. 전신 사진 1장 이상, 최근 사진을 넣는다. 다른 가이드는 20장 이상을 권한다. **학습한 모델(Soul 2.0 / Soul Cinema)에서만 쓸 수 있다.** [사실, 벤더]
- Seedance 2.0에서는 `@character` 참조와 Soul ID를 함께 써야 여러 생성에 걸쳐 신원이 유지된다. [사실, 벤더]
- Reddit: 약 15장, 같은 메이크업, 선글라스·모자 금지. 10초가 넘는 클립은 어느 플랫폼이든 얼굴이 흐른다. 얼굴은 유지돼도 **의상·배경·소품은 바뀐다.** [확인 안 됨, 일화]
- 요소(Elements): 캐릭터·소품·장소를 재사용 참조로 등록한다. MCP에서는 `manage_reference_elements`로 다룬다. Higgsfield Academy의 "Working in Claude" 강의가 Hell Grind 팀의 요소·일관성 파이프라인을 다룬다(Cowork 필요). [사실은 목차까지만. 본문은 못 읽었다]

**카메라·모델**
- Cinema Studio는 장르, 카메라 베이스, 렌즈(아나모픽 등), 템포, 감정을 프롬프트가 아니라 **컨트롤로** 정한다. Cinema Studio 4는 카메라 프리셋 30개 이상, 조명 2광원, 팔레트 50종, Seedance 2.5 기반, 최대 30초, 참조 50개라고 한다. [확인 안 됨, LinkedIn과 SEO 페이지]
- 프리셋은 정확한 이름("Dolly In", "FPV Drone", "360 Orbit")으로 따로 한 줄에 쓰고 끝쪽에 둔다. [커뮤니티, OSideMedia]
- Kling 3.0은 3~15초, 시작·끝 프레임, 최대 5샷이다. Kling 4.0은 최대 30초, 키프레임 10개다. 순서는 주체·동작·카메라 → 타이밍·참조·조명·오디오·잠금이다. [벤더]

**Seedance 프롬프트 요령**
- 맨 앞에 샷 수, 총 길이, 화면비를 쓴다. **카메라가 하지 말 것을 적는다**("No cuts, no zoom, natural head movement"). 안 그러면 마음대로 컷을 나눈다. [벤더]
- 대사: 한 줄에 5~10단어, 8초를 넘기면 입 모양이 뭉개진다. 대사 중에는 고개 움직임을 빼고 카메라를 고정한다. 대사는 따옴표로 쓰고 톤을 지정한다. 다인 립싱크는 아직 어렵다. 한국어는 긴 구절에서 가끔 어긋난다. [확인 안 됨, 제3자 가이드]
- 참조에는 `@Image1/@Video1/@Audio1`마다 용도를 한 줄씩 적는다(얼굴 변형 방지). 이미지 9, 영상 3, 오디오 3까지(플랫폼마다 다름). [확인 안 됨]
- 최근 Seedance 2.0 품질이 떨어져 Kling 3.0을 쓴다는 일화가 있다. [일화]

**연속성·후반**
- 다음 샷의 첫 프레임을 앞 샷의 마지막 프레임에 맞춰 편집하거나 다시 만든다("internal keyframes"). 샷 경계마다 마지막과 첫 프레임을 비교한다. [커뮤니티]
- Popcorn·스토리보드(4/6/8프레임)로 생성 전에 페이싱과 연속성을 잡는다. [벤더]
- 업스케일·보간: Higgsfield `upscale_video`, Sora 2 Enhancer(플리커 감소, 벤더 주장), ComfyUI Topaz 노드(Starlight 업스케일 + apo-8 보간). Topaz와 Higgsfield를 묶은 사용자 워크플로 자료는 찾지 못했다. [부분 확인]

---

## 8. 파이프라인에서 Claude가 맡는 일 (사례)

- **기획·프롬프트 계층:** 브리프 → 대본 → 샷 리스트 → 프롬프트를 쓰고, 렌더는 Higgsfield가 한다. Higgsfield 블로그와 Academy가 이 구도를 공식으로 내세운다. [벤더]
- **CSV 샷 리스트 자동 생성:** CSV 하나로 Claude Code와 Higgsfield CLI 일괄 생성을 돌린 사례가 있다. [확인 안 됨, dev.to]
- **8패널 콘티 → 샷별 렌더:** GPT Image 2로 콘티를 먼저 만든다. [커뮤니티]
- **편집 지휘:** Claude Code가 Whisper(전사), ffmpeg(컷), Higgsfield(B롤)를 조율한다. [확인 안 됨, AI Fire]
- **반론:** "MCP로 프롬프트 작업이 끝났다는 건 과장"이라는 영상 후기가 있다. [일화]
- [추정] 실사 단편 사례에서 Claude가 실제로 맡는 일은 대부분 문서 작업이다(대본·샷 리스트·프롬프트·연속성 기록). 편집과 그레이딩까지 Claude가 하는 공개 사례는 드물고 데모 수준이다.

---

## 9. 우리 키트에 없는 것: 만들면 좋을 스킬 후보

키트 README(`instructions.md`)와 6개 스킬의 이름·설명만 훑어 확인했다. 키트는 기획, 프롬프트(이미지·영상·연기), 생성 운영, 세션·정본을 다룬다. 현재 `project-setup`은 시나리오를 컷으로 나눠 적기만 하고, 업스케일은 `higgsfield-generation`에 한 줄 경고로만 있다. 편집, 소리, 색은 다루지 않는다.

1. **`assembly`: 러프컷 조립과 이어 붙이기 프레임**
   - 이유: OK 컷이 쌓여도 순서대로 붙여 볼 수단이 없다. 연속성 팁의 핵심인 "앞 컷 마지막 프레임 → 다음 컷 시작 이미지"에도 프레임 추출이 필요하다.
   - 범위: ffmpeg 레시피(마지막·지정 프레임 추출, 트림, concat, 해상도·fps 통일, 프록시 인코딩), `shot-list.md` 순서로 러프컷 만들기, 경계 프레임 나란히 비교 이미지. Claude Code의 Bash가 대상이고 MCP는 쓰지 않는다. 그레이딩과 사운드는 다른 스킬로 넘긴다.
2. **`sound-design`: 대사·효과음·앰비언스 큐시트와 생성**
   - 이유: 현재 `AUDIO` 블록은 생성 프롬프트 안의 소리만 다룬다. 후반에 따로 입히는 대사, 효과음, 룸톤, 음악 큐가 없다.
   - 범위: 컷별 사운드 큐시트(대사 원문·길이·감정·목소리 ID, SFX, 앰비언스), ElevenLabs 호스팅 MCP나 Higgsfield `generate_audio`·`create_voice`·`dubbing`용 프롬프트, 대사 길이 규칙(한 줄 5~10단어, 8초 이하), ffmpeg 믹스·싱크 확인.
3. **`color-continuity`: 컷 간 색·노출 맞춤과 룩 관리**
   - 이유: 생성 컷마다 색온도와 대비가 흔들린다. 키트에는 "색 참조"가 있지만 생성 단계에서만 쓰고, 후반에서 맞추는 단계는 없다.
   - 범위: 기준 OK 컷 지정, 컷별 평균 색·휘도 측정(`qa-metrics`와 연결), ffmpeg `lut3d`·`eq`나 Resolve MCP `set_lut`로 1차 맞춤, 룩 LUT 1개를 정본(`decisions.md`)에 기록. 창작 그레이딩은 범위 밖이다.
4. **`coverage-breakdown`: 대본 → 장면 커버리지·콘티 설계**
   - 이유: `project-setup`은 시나리오를 줄 단위로 나누기만 한다. 실사 단편에서는 180도 규칙, 마스터·리버스·인서트 커버리지, 장면 길이와 페이싱, AI 제약(샷당 15초, 한 컷에 사건 하나)을 반영한 컷 설계가 먼저 필요하다.
   - 범위: 장면별 블로킹 메모(인물 위치를 화면 기준으로 적어 키트 규칙 6과 맞춘다), 커버리지 표, 컷 길이 배분, 콘티 프레임용 image-prompt 호출 목록, `shot-list.md`로 내보내기. 컷 카드를 만드는 일(`production-session`)과는 겹치지 않게 그 앞 단계만 맡는다.
5. **`finishing`(조건부): 업스케일·보간·디플리커와 납품 스펙**
   - 이유: 키트에는 업스케일 경고 한 줄뿐이다. 최종 해상도, 24fps 보간, 플리커 제거, 납품 코덱을 정하는 절차가 없다.
   - 범위: 언제 `upscale_video`를 쓰고 언제 Topaz·ComfyUI를 쓸지, 질감 손실 검사, 보간 아티팩트 체크, 납품 프리셋(H.264/ProRes, 색공간 태그). 2번이나 1번에 합쳐도 된다.

---

## 10. 추천

### 바로 쓰기 좋은 것
- **Higgsfield MCP 커넥터** (공식): 이미 키트의 중심이다. 업스케일·리프레임·요소·오디오·영상 분석 도구까지 들어 있어 따로 붙일 것이 적다.
- **ElevenLabs 호스팅 MCP** (공식, OAuth, 무료 티어): 대사·효과음·앰비언스를 따로 만들 때 쓴다. 로컬 uvx판은 보관 상태라 쓰지 않는다.
- **Claude Code의 Bash + ffmpeg** (MCP 없이): 프레임 추출, 이어 붙이기, LUT 적용. 위 `assembly` 스킬 후보와 짝을 이룬다.
- **Notion 원격 MCP / Google Drive 커넥터** (공식): 정본을 팀과 같이 쓸 때 쓴다.
- **OSideMedia/higgsfield-ai-prompt-skill**: 설치하지 말고 **참고 자료로만** 쓴다. troubleshoot·negative-constraints를 키트의 `fixes.md`와 비교해 빠진 실패 유형을 찾는다.

### 조건부
- **DaVinci Resolve MCP (samuelgursky)**: Resolve Studio를 쓰고 Claude Code를 로컬에서 돌릴 때만 쓴다. 무료판 브리지는 21.0.x에서만 확인됐다.
- **Adobe for creativity 커넥터**: Creative Cloud 구독이 있고 Premiere·Photoshop으로 마무리할 때만 쓴다(앱 전용).
- **higgsfield-ai/skills (공식 스킬 + CLI)**: Claude Code 배치 생성이 필요할 때 `soul-id`·`generate`만 쓴다. 키트의 `higgsfield-generation` 규칙(승인 전 생성 금지)과 부딪치지 않는지 먼저 본다. CLI 크레딧 과금에도 주의한다.
- **ComfyUI MCP (Comfy Org 공식 로컬)**: GPU가 있고 Topaz·보간 노드를 쓸 때만 쓴다.
- **Runway**: Aleph 영상 편집이 필요할 때만 새 공식 경로(runway.com/mcp)를 확인한 뒤 쓴다.
- **Shanyin director-master, inferen-sh storyboard-creation**: 콘티 설계를 참고할 때만 본다(4번 후보를 만들 때 자료로).

### 권하지 않음
- **rediumvex, cth9191 Seedance 스킬 묶음**: 광고·바이럴용이거나 너무 작다. 키트의 프롬프트 규칙과 부딪친다.
- **Kling·Luma·Veo·fal·PiAPI 커뮤니티 MCP**: Higgsfield 안에 같은 모델이 있다. API 키를 따로 관리해야 하고, 유지 상태도 불명이며, 타임아웃 문제가 보고됐다.
- **ffmpeg 커뮤니티 MCP (misbahsy, Kush36Agrawal)**: Claude Code에서는 Bash가 낫다. `execute_ffmpeg`처럼 명령을 그대로 실행하는 서버는 권한 범위도 넓다.
- **Premiere 커뮤니티 MCP**: 실험 단계이고 자리만 있는 도구가 있다. Adobe 공식 커넥터가 생겼다.
- **Composio 경유 Higgsfield, 옛 로컬 ElevenLabs·Runway 서버**: 공식 대체품이 있거나 보관된 상태다.

---

## 확인하지 못한 것
- Higgsfield 공식 도움말·Academy 본문, techsy.io(Claude Code 설치 명령)는 네트워크 차단으로 열지 못했다. 이 세션에서 `higgsfield.ai`를 허용하면 다시 확인할 수 있다.
- Frame.io와 Airtable의 공식 MCP는 찾지 못했다.
- Cinema Studio 4의 사양(프리셋 30개 이상, 30초, 참조 50개)은 공식 변경 기록과 대조하지 못했다.
