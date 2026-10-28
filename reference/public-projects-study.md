# Higgsfield 공개 프로젝트 연구 — Cully Hill Boys · BESA · The Kiss

> 컨텍스트에 넣지 않는다. 사람이 보는 연구 자료다.
> 조사일: 2026-10-28

## 확인한 범위

**공개 페이지에서 본 것**
- 브리프, 생성 수, 사용 크레딧, 모델 사용 비율, 최종 영상 규격

**Higgsfield MCP로 본 것** (공개 스냅샷 폴더 ID를 프로젝트 ID로 써서)
- 폴더 구성(이름과 계층)
- 폴더별 생성물의 모델, 종류, 생성 시각
- 결과 이미지 몇 장(직접 열어 봄)

**보지 못한 것**
- 프롬프트 원문
  - 다른 사용자에게는 생성 설정의 `prompt`가 빈칸으로 내려온다.
  - 프롬프트 전용 조회는 403(권한 없음)이었다.
  - 웹페이지는 프롬프트를 보여 주지만, 그 API 호출은 이 세션의 권한 정책이 막았다.

| 프로젝트 | 공개 페이지 ID | 스냅샷 폴더 ID (MCP의 project_id로 사용) |
|---|---|---|
| Cully Hill Boys | `0efa70c1-07ec-410a-813b-8629502a7de3` | `b619c13c-83ba-4ea3-b85c-de9be41bd01b` |
| BESA | `80b66780-ce19-415e-93c7-209b09960f59` | `5d395ad3-b520-4620-9db5-816481b73b56` |
| The Kiss | `655325cc-46d9-4b0b-b03d-d177defa4b3f` | `2bae3b00-dadd-4fcf-8e81-d734c46a3467` |

MCP 호출 방법:
- `workspace_id`에는 내 워크스페이스 ID를 넣고, `project_id`에는 스냅샷 폴더 ID를 넣는다.
- 결과에는 원작자의 워크스페이스 ID가 찍혀 나오지만, 그 ID로 다시 호출하면 403이다.

## 1. 한눈에 비교

| 항목 | Cully Hill Boys | BESA | The Kiss |
|---|---|---|---|
| 만든 이 | Higgsfield Studio (사내 28명) | OLL KORRECT (2인) | seifhussam (개인) |
| 브리프 | 무명 런던 래퍼 3명이 마약 전쟁에 휘말리는 액션 코미디 | 알바니아 전설 콘스탄틴과 도룬티나. 약속(besa)은 죽은 자도 깨운다 | 형제 중 한 명은 키스를, 다른 한 명은 전화와 악몽을 받는다 |
| 최종 길이 · 화면 | 1:54:49 · 4096×1716 (2.39:1) | 10:22 · 3840×1646 (2.33:1) | 3:38 · 1280×720 |
| 생성 수 · 크레딧 | 473,214 · 예산 200만 달러(보도) | 960 · 29,477 | 391 · 11,598 |
| 최종 1초당 생성 | 약 69회 | 약 1.5회 | 약 1.8회 |
| 기간 | 준비 6월 초 → 공개 8/10 | 8/11 시작 → 9/13 제출 | 8/11 시작 → 9/13 제출 |

**모델 비율 (페이지 표시)**
- **BESA:** Seedance 2.5 34%, Soul Location(장소) 23%, Topaz 업스케일 18%, Soul Cinematic 6%, GPT Image 2.0 4%, 기타 다수
- **The Kiss:** Nano Banana Pro 41%, Seedance 2.5 24%, Soul Cinematic 10%, Soul V2 9%, Seedream 5.0 Pro 6%, GPT Image 2.0 5%, Cinematic Video Editor 2%
- **Cully Hill Boys:** 페이지 표시 없음. 보도로는 Seedance 2.5(영상·대사), Seedream·Nano Banana(이미지 수정), 프롬프트 작성에 Claude

## 2. 폴더 구성 — 세 작품 모두 "에셋 / 장면 / 상태"로 나눴다

**Cully Hill Boys (사내 장편)**
```
PRE PROD
├─ ASSETS / Cal · Ollie · SIDE CHAR · doberman · COSTUMES · PROPS · LOCATIONS · CAR PARK · Cal's_room …
├─ Character Test · Costumes · CLEAN UP
└─ Test_v1 ~ Test_v5 · Test_scene16          ← 본 제작 전 룩 테스트 5회
1 ACT (1-49) / 01-02 scene · 04 scene · … · 49 scene   ← 장면 번호 폴더(2~3개 묶기도)
2 ACT (50-93) · 3 ACT (93-120) · 4ACT_Epilogue (121-137)
0 Regenerations                               ← 다시 만든 것만 모은 곳
```
- 장면 137개가 보도의 "137항목 제작 로그"와 일치한다.

**BESA (2인 팀)**
```
Character sheets · Locations · Props · Extras · Genjutsu
SCENES / 1. INTRO · 2. Door knock · 3. The wedding · 4. The promise · … · 25. New home   ← 이야기 비트 이름
Approved generations · BEST · UPSCALED · Deleted generations    ← 상태별 모음
AUDIO · SOUND TRACK · TEXT · LOGO · Poster · TEASERS
```
- 같은 job이 장면 폴더와 `Approved generations`에 동시에 들어 있다. 옮기지 않고 승인 모음에 한 번 더 넣는 방식이다.

**The Kiss (개인)**
```
Characters · Locations · Props · Sound
Test_Images · Test_Videos          ← 시도는 모두 여기
Scene_01 · Scene_02 · Scene_03 · Scene_05   ← 고른 것만 (Scene_01은 영상 1개)
Editing                             ← Cinematic Video Editor 결과
```

## 3. 장면 하나를 만드는 흐름 (생성 기록으로 재구성)

**BESA "4. The promise"**
- 8/13 00:12~10:50 사이에 Seedance 2.5로 약 16번 생성했다.
- 11:15에 고른 테이크 하나를 Topaz로 업스케일했다.
- 다음 날 3번 더 생성했고, 8/24에 2번 더 생성해 고쳤다.
- 고른 것은 `Approved generations`에도 넣었다.

**The Kiss**
- 8/11~8/15: 인물 이미지를 여러 모델로 시험했다(Soul Cinema Studio, Soul V2, GPT Image 2, Seedream 5.0 Pro, Nano Banana Pro).
- 8/20~8/22: `Test_Videos`에서 Seedance 2.5를 밤새 반복했다(새벽 2~3시, 오후 1~4시 연속).
- 사이사이에 `Editing`에서 Cinematic Video Editor로 편집했다.
- 장면 폴더에는 최종본만 넣었다.

**Cully Hill Boys**
- 인물(Cal)은 6/9에 Soul Cast와 Soul Cinema Studio로 4장씩 묶어 생성했다. 공개 두 달 전이다.

## 4. 에셋 실물 (직접 본 이미지)

| 작품 | 에셋 | 형식 | 특징 |
|---|---|---|---|
| Cully Hill Boys | 인물 Cal (Soul Cinema Studio) | 2528×1088 가로 4분할: 얼굴 클로즈업 / 뒤 / 앞 전신 / 뒤 | 머리 포함. 짙은 회색 배경. 의상 문구("CHEERFUL WATER DELIVERY")와 로고까지 또렷하게 고정 |
| BESA | 캐릭터 시트 (GPT Image 2) | 3840×2160 한 장에 말 탄 인물 5명 | 인물 + 말 + 시대 의상을 그룹으로 한 번에 고정. 얼룩진 회색 배경 |
| BESA | 장소 (GPT Image 2) | 3840×1648 (최종 화면비 2.33:1) | 밤의 언덕 묘지. 최종 화면비와 최종 조명(아주 어두움)으로 만들었다 |
| The Kiss | Characters 폴더의 최종 이미지 (Nano Banana) | 2752×1536 | 시트가 아니라 장면 속 이미지다. 두 형제 + 소품(주황 인형) + 거실을 한 장에 담았다 |

## 5. 정리 — 이 작품들은 이렇게 만들었다

1. **본 제작 전에 룩 테스트를 버전으로 남긴다.** Cully는 Test_v1~v5와 장면 하나 시험(Test_scene16)을 거쳤다.
2. **에셋은 인물, 의상, 소품, 장소별 폴더로 따로 만든다.**
   - 인물은 4장 묶음으로 뽑아 고른다.
   - 시트 형식은 작품마다 다르다: 4분할 턴어라운드, 그룹 라인업, 장면 속 키 이미지.
3. **장소는 최종 화면비와 최종 조명으로 만든다.** 영상의 출발점을 처음부터 완성 화면에 맞춘다.
4. **영상은 장면 폴더 안에서 한 장면에 여러 번 반복하고 하나를 고른다.**
   - 소규모 팀은 한 장면에 대략 15~20번 생성했다.
   - 고른 테이크만 업스케일했다(BESA는 Topaz).
5. **상태는 폴더로 관리한다.**
   - BESA: 승인, 베스트, 업스케일 완료, 삭제
   - The Kiss: 시험 폴더와 장면 폴더(최종)를 분리
   - Cully: 재생성 모음 폴더
6. **장면 폴더 이름이 곧 컷 목록이다.** BESA의 "4. The promise"처럼 번호와 이야기 비트를 함께 쓴다.
7. **편집과 부분 수정도 Higgsfield 안에서 한다.** Cinematic Video Editor, Relight, Angles, Genjutsu(동작 옮기기, 물체 교체), Voice Change를 썼다.
8. **Cully Hill Boys는 키트와 같은 계열의 방식이다(보도).** 샷마다 15블록 프롬프트를 썼고, 실패작을 거르는 "잠금"이 약 150개였으며, 프롬프트 작성에 Claude를 썼다.

## 6. 키트에 반영할 후보 (아직 반영하지 않음)

| 후보 | 근거 | 반영 위치 |
|---|---|---|
| 본 제작 전 `01 룩 테스트` 폴더와 버전(v1, v2 …) 단계 | Cully PRE PROD / Test_v1~v5 | `higgsfield-generation` §2 폴더 구성, `project-setup` |
| 승인은 "옮기기" 대신 "승인 모음에 함께 넣기(attach)"도 선택지로. 최종 편집용 `BEST`·`업스케일 완료` 모음 폴더 | BESA | `higgsfield-generation` §4 |
| 시도 폴더와 최종 폴더 분리(컷 폴더에는 최종만) | The Kiss | `higgsfield-generation` §2 |
| 장소 마스터는 최종 화면비·최종 조명 상태로 만든다 | BESA 장소 | `image-prompt/location.md` |
| 인물 시트 형식 선택지 추가: 머리 포함 4분할 턴어라운드, 그룹 라인업(말·탈것 포함) | Cully, BESA | `image-prompt/character.md` |
| 인물 탐색 단계에서는 4장 묶음 생성 허용, 그 뒤로는 한 장씩 | Cully Soul Cast | `higgsfield-generation` §6 |
| 실사는 고른 테이크만 업스케일로 마감 | BESA Topaz | `higgsfield-generation` §6 |
| 반복 실패 때 Relight·Angles·Genjutsu 같은 부분 수정 도구를 먼저 검토 | BESA 스택 | `higgsfield-generation` §5 |
| 컷 폴더 이름에 번호 + 이야기 비트 | BESA SCENES | `higgsfield-generation` §2 |

## 7. 프롬프트까지 보려면

- **권한 허용:** 웹페이지가 쓰는 Higgsfield API(`fnf-api-gw.higgsfield.ai`) 읽기를 이 세션에 허용한다.
- **직접 복사:** 로그인한 브라우저에서 `https://higgsfield.ai/generate?projectId=<스냅샷 폴더 ID>`를 열고 필요한 샷의 프롬프트를 복사해 준다.
- **Cully Hill Boys:** 공개 자료의 사내 Claude 스킬 3개 파일을 받아 주면 키트와 직접 비교할 수 있다.

## 출처

- 공개 페이지:
  - [Cully Hill Boys](https://higgsfield.ai/@higgsfield.studio/projects/cully-hill-boys)
  - [BESA](https://higgsfield.ai/@ollkorrect/projects/besa)
  - [The Kiss](https://higgsfield.ai/@seifhussam/projects/the-kiss)
- Cully Hill Boys:
  - [Semafor](https://www.semafor.com/article/08/19/2026/ai-startup-produces-fully-ai-generated-feature-length-film)
  - [AlphaSignal](https://alphasignal.ai/news/higgsfield-made-a-2m-ai-film-with-licensed-celebrity-likenesses)
  - [Magica](https://magica.com/news/higgsfield-ai-cully-hill-boys-feature-film)
  - [XiaoHu](https://best.xiaohu.ai/en/article/cully-hill-boys/)
  - [Hyper.ai](https://beta.hyper.ai/en/stories/70410d3b984c144343d68690002ec3ab)
- BESA:
  - [Telegrafi 인터뷰](https://telegrafi.com/nje-legjende-shqiptare-mes-50-filmave-me-te-mire-ne-nje-gare-boterore-me-afro-7-mije-pjesemarres-historia-e-besa-filmit-te-realizuar-me-ai/)
  - [Illyria](https://www.illyria.com/filmi-besa-renditet-mes-me-te-mireve-ne-higgsfield-global-film-festival/)
- 대회 규칙:
  - [Higgsfield Global Film Festival 규칙](https://higgsfield.ai/contests/higgsfield-global-film-festival?tab=rules)
