# Higgsfield 공개 프로젝트 연구 — Cully Hill Boys · BESA · The Kiss (1차)

> 컨텍스트에 넣지 않는다. 사람이 보는 연구 자료다.
> 조사일: 2026-10-28

## 확인한 범위

**본 것**
- 각 프로젝트 공개 페이지가 서버에서 내려준 정보: 브리프, 생성 수, 사용 크레딧, 용량, 모델 사용 비율, 최종 영상 규격, 프롬프트·캔버스 공개 여부
- 외부 보도와 인터뷰

**아직 못 본 것**
- 개별 에셋, 영상 프롬프트, 레퍼런스, 캔버스
- 이 정보는 페이지가 열린 뒤 Higgsfield API로 따로 불러온다.
- 이 세션의 권한 정책이 그 API 호출을 막았다. Higgsfield MCP로도 다른 사용자의 프로젝트는 읽히지 않는다(404).

## 1. 한눈에 비교

| 항목 | Cully Hill Boys | BESA | The Kiss |
|---|---|---|---|
| 만든 이 | Higgsfield Studio (사내 28명, 감독 9명 포함) | OLL KORRECT (Elena Kelmendi, Lirim Berisha) | seifhussam (개인) |
| 브리프 | 무명 런던 래퍼 3명이 마약 전쟁에 휘말리는 액션 코미디 | 알바니아 전설 콘스탄틴과 도룬티나. "한 번 한 약속(besa)은 죽은 자도 깨운다" | 형제 중 한 명은 키스를 받고, 다른 한 명은 걸려 온 전화로 악몽에 빠진다 |
| 최종 길이 | 1:54:49 | 10:22 | 3:38 |
| 화면 | 4096×1716 (2.39:1) | 3840×1646 (2.33:1) | 1280×720 (16:9) |
| 생성 수 | 473,214 | 960 | 391 |
| 사용 크레딧 | 표시 0 (사내). 보도로는 예산 200만 달러 중 약 100만 달러가 컴퓨트 | 29,477 | 11,598 |
| 프로젝트 용량 | — | 31 GB | 5.5 GB |
| 기간 | 4주 (보도) | 8/24 시작 → 9/13 최종 제출 (약 3주) | 8/12 시작 → 9/13 최종 제출 (약 4.5주) |
| 대회 | — | Global Film Festival Top 50 | Global Film Festival Top 50 |
| 프롬프트·캔버스 공개 | 예 | 예 | 예 |

**최종 1초를 만드는 데 든 생성 수**

| 프로젝트 | 최종 1초당 생성 | 최종 1분당 크레딧 | 생성 1회당 크레딧 |
|---|---:|---:|---:|
| BESA | 약 1.5회 | 약 2,840 | 약 31 |
| The Kiss | 약 1.8회 | 약 3,200 | 약 30 |
| Cully Hill Boys | 약 69회 | — | — |

## 2. 모델 사용 비율 (페이지 표시)

비율의 기준은 생성 횟수로 보이지만 확인하지 못했다.

| BESA | % | The Kiss | % |
|---|---:|---|---:|
| Seedance 2.5 | 34.4 | Nano Banana Pro | 41.2 |
| Cinematic Studio Soul Location | 23.3 | Seedance 2.5 | 24.0 |
| Topaz Video (업스케일) | 17.5 | Soul Cinematic | 9.7 |
| Soul Cinematic | 5.6 | Higgsfield Soul V2 | 9.2 |
| GPT Image 2.0 | 4.3 | Seedream 5.0 Pro | 5.6 |
| Higgsfield Soul V2 | 3.8 | GPT Image 2.0 | 4.9 |
| Seedream 5.0 Pro | 2.9 | Cinematic Video Editor | 2.1 |
| Nano Banana Pro | 1.8 | Seedance 2.0 | 1.5 |
| Cinematic Studio Image | 1.7 | Soul Cinema Studio | 1.0 |
| Cinematic Video Editor | 1.3 | Seedream 4.5 | 0.5 |
| Nano Banana 2 | 1.0 | Cinema Studio 4.0 | 0.3 |
| Seed Audio 1.0 | 0.6 | | |
| Genjutsu Motion Transfer | 0.4 | | |
| Voice Change | 0.3 | | |
| 기타 (GPT Image 2.5, 영상 업스케일, Relight, Angles, Object Swap, 영상 Relight 등) | 각 0.1~0.3 | | |

Cully Hill Boys는 페이지에 비율이 없다. 보도에 따르면 다음과 같다.
- 영상과 대사: Seedance 2.5
- 이미지 편집과 다듬기: Seedream, Nano Banana
- 프롬프트 작성: Claude

## 3. 작업 방식 — 확인된 사실

**Cully Hill Boys** (출처: 보도)
- **각본:** 사람이 쓴 기존 각본이다(Black List에 올렸던 미제작 시나리오).
- **배우:** 실제 배우의 사진과 음성으로 캐릭터 시트를 만들었다. 배우가 촬영한 장면은 없다. 격투 장면만 스턴트맨이 휴대폰으로 찍은 영상을 동작 참조로 썼다.
- **규모:** 에셋 약 1,000개, AI 장소 약 100곳.
- **프롬프트:** 샷마다 15블록 구조를 썼다(공간 지도, 광학, 블로킹, 연기, 조명, 오디오). 실패작을 거르는 이름 붙은 "잠금(lock)"을 약 150개 썼다.
- **공개한 것:** 모든 프롬프트, 캐릭터 시트, 장소 에셋, 137항목 제작 로그. 그리고 사내 Claude 스킬 3개(내려받기 가능).
- **매뉴얼의 금지 사항 예:** 캐릭터 시트에 "studio"라는 말을 쓰지 않는다.

**BESA** (출처: 알바니아 언론 인터뷰)
- **사람이 한 것:** 기획, 각본, 연출, 편집, 색보정.
- **AI가 한 것:** 첫 영상 소재와 음악.
- **작업 단위:** 장면마다 따로 만들고 따로 편집했다.

**The Kiss**
- 외부 보도는 찾지 못했다. 위 페이지 수치가 전부다.

## 4. 해석 — 수치에서 읽히는 작업 방식 (추정 포함)

1. **이미지를 먼저 고정하고 움직인다.**
   - The Kiss는 생성의 약 70%가 이미지 모델이고 영상은 약 26%다. 장면을 스틸로 확정한 뒤 영상으로 옮겼다고 보인다.
   - 키트의 "퍼스트 프레임 → 영상" 순서와 같다.
2. **장소에 크게 투자했다.**
   - BESA는 장소 전용 도구(Cinematic Studio Soul Location)가 23%다.
   - Cully Hill Boys도 장소 100곳을 에셋으로 만들었다.
   - 키트의 "장소는 작품의 자산이다"와 같은 방향이다.
3. **고해상도는 마감 단계에서 업스케일로 했다.**
   - BESA는 Topaz Video가 17.5%이고 최종본이 3840 폭이다. 낮은 해상도로 확정한 뒤 마지막에 키운 것으로 보인다.
   - 실사에서는 표준 마감이다. 수채처럼 질감이 중요한 그림체에서는 키트대로 업스케일을 피한다.
4. **다시 만들기보다 부분 수정 도구를 썼다.**
   - BESA 스택에 Relight, Angles, Motion Transfer, Object Swap, Voice Change가 있다.
   - 키트의 "같은 실패 2회면 방식을 바꾼다"를 Higgsfield 안의 도구로 실행한 셈이다.
5. **화면비는 영화 비율이다.** 두 작품이 2.33~2.39:1이다.
6. **선택이 엄격했다.**
   - 개인·소규모 팀은 최종 1초당 1.5~1.8회만 생성했다. 샷을 줄이고 확정본을 재사용했다고 보인다.
   - 사내 장편은 1초당 약 69회다. 대량 생성 후 고르는 방식이다.
7. **Higgsfield Studio도 같은 15블록 구조를 쓴다.**
   - 키트의 영상 프롬프트 형식은 Higgsfield Studio의 방식과 같은 계열이다.
   - 그들의 "잠금 약 150개"는 키트의 "위험마다 막는 문장"과 같은 개념이다.

## 5. 키트에 반영할 후보 (아직 반영하지 않음)

| 후보 | 근거 | 반영 위치 |
|---|---|---|
| 반복 실패 때 Relight·Angles·Object Swap·Motion Transfer 같은 부분 수정 도구를 먼저 검토 | BESA 스택 | `higgsfield-generation` §5 |
| 실사는 확정 뒤 업스케일 마감 허용, 그림체는 금지 유지 | BESA Topaz 17.5% | `higgsfield-generation` §6 |
| 장소 전용 도구(Soul Location)로 장소 마스터 만들기 검토 | BESA 23% | `image-prompt/location.md` |
| 캐릭터 시트에 "studio"를 쓰지 않는다 | Cully Hill Boys 매뉴얼(보도) | `image-prompt/character.md` |
| 프롬프트 공개 시 개별 "잠금" 목록과 비교해 키트의 막는 문장 보강 | Cully Hill Boys 잠금 약 150개 | `video-prompt/fixes.md` |

## 6. 끝내려면 필요한 것

에셋, 프롬프트, 레퍼런스를 직접 보려면 다음 중 하나가 필요하다.
1. **권한 허용:** 공개 페이지가 쓰는 Higgsfield API(`fnf-api-gw.higgsfield.ai`) 읽기를 이 세션에 허용한다.
2. **프로젝트 복제:** 각 공개 프로젝트를 Higgsfield 웹에서 내 워크스페이스로 복제할 수 있다면 복제한다. 그러면 MCP로 에셋과 프롬프트를 읽을 수 있다. 복제 버튼이 다른 사용자에게도 열려 있는지는 확인하지 못했다.
3. **직접 복사:** 핵심 샷 몇 개의 프롬프트를 페이지에서 직접 복사해 준다.

Cully Hill Boys는 생성이 47만 건이라 전부 볼 수 없다. 확정 샷 위주로 표본을 뽑는다. 사내 Claude 스킬 3개를 내려받아 주면 키트와 직접 비교할 수 있다.

## 출처

- 공개 페이지:
  - [Cully Hill Boys](https://higgsfield.ai/@higgsfield.studio/projects/cully-hill-boys)
  - [BESA](https://higgsfield.ai/@ollkorrect/projects/besa)
  - [The Kiss](https://higgsfield.ai/@seifhussam/projects/the-kiss)
- Cully Hill Boys:
  - [Semafor](https://www.semafor.com/article/08/19/2026/ai-startup-produces-fully-ai-generated-feature-length-film)
  - [Higgsfield X](https://x.com/higgsfield/status/2086893641549992326)
  - [AlphaSignal](https://alphasignal.ai/news/higgsfield-made-a-2m-ai-film-with-licensed-celebrity-likenesses)
  - [Magica](https://magica.com/news/higgsfield-ai-cully-hill-boys-feature-film)
  - [XiaoHu](https://best.xiaohu.ai/en/article/cully-hill-boys/)
  - [Hyper.ai](https://beta.hyper.ai/en/stories/70410d3b984c144343d68690002ec3ab)
  - [Mindplex](https://magazine.mindplex.ai/post/a-110-minute-ai-movie-for-2-million-the-making-and-open-sourcing-of-cully-hill-boys)
- BESA:
  - [Telegrafi 인터뷰](https://telegrafi.com/nje-legjende-shqiptare-mes-50-filmave-me-te-mire-ne-nje-gare-boterore-me-afro-7-mije-pjesemarres-historia-e-besa-filmit-te-realizuar-me-ai/)
  - [Illyria](https://www.illyria.com/filmi-besa-renditet-mes-me-te-mireve-ne-higgsfield-global-film-festival/)
  - [Zhurma](https://zhurma.press/filmi-besa-shortlistohet-ne-festivalin-globall-higgsfield-20260918/)
- 대회:
  - [Higgsfield Global Film Festival 규칙](https://higgsfield.ai/contests/higgsfield-global-film-festival?tab=rules)
  - [RuntimeWire](https://runtimewire.com/article/higgsfield-1-million-ai-film-festival-public-prompts)
