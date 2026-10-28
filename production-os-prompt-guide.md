 Production OS 프롬프트 작성 가이드 — FINAL
 
기준: 사용자가 제공한 `Production_OS_01`, `Production_OS_03` 원 명세와 `Production_OS_08 ... FINAL`의 프롬프트·문장 관련 확정 계약  
목적: Production OS에서 이미지·영상 생성용 프롬프트를 **작성·상속·재사용·검증·전송**할 때 필요한 규칙만 독립적으로 정리한다.
 
> 이 문서는 프롬프트 작성 가이드다. DB DDL, API route, queue, Provider adapter 구현 세부는 제외한다.  
> 단, 사용자의 작성 결과와 동작에 직접 영향을 주는 저장·버전·잠금·검증·전송 규칙은 포함한다.
 
> **문서 구성 안내**  
> §1~§31은 원 명세에서 도출된 **규범(normative)** 부분이며 한 글자도 변경하지 않았다.  
> §32 이후의 부록은 **비규범(non-normative) 작성 보조**다. §31의 계약대로 새로운 제품 요구사항을 만들지 않으며, 규범과 충돌하면 언제나 §1~§31이 우선한다.  
> 부록 A–E(§32–§36)는 2026-09-25 정리 때 뺐다 — 규범을 되풀이하거나 앱 전용이었다.
 
---
 
# 1. 가장 먼저 지켜야 할 핵심 원칙
 
## 1.1 15단계 구조는 고정이다
 
- 프롬프트는 **선택형 연속성 pre-slot + 고정 15단계**로 작성한다.
- `PRE_SHOT_CONTINUITY`는 Step 1이 아니다.
- Step 1~15의 **순서와 제목을 바꾸지 않는다.**
- 최종 프롬프트에도 각 단계 제목을 포함한다.
- 특정 모델에 맞추기 위해 단계 순서를 바꾸거나 일부 단계를 몰래 삭제하지 않는다.
- 모델별 자동 요약·자동 재작성·자동 순서 변경을 하지 않는다.
- 빈 블록도 15단계 구조 안에서는 제목을 유지하고 본문만 빈 상태로 둔다.
- pre-slot은 사용하지 않을 때 최종 직렬화에서 완전히 생략한다.
## 1.2 사용자가 작성한 원문이 기준이다
 
- 기본 기준본은 **한국어 원문**이다.
- Provider가 특정 언어를 강제하지 않으면 한국어 원문을 기본 전송 후보로 사용한다.
- 번역 기능이 구성되지 않았으면 번역본을 임의 생성하지 않는다.
- API용 wrapper나 Provider 문법 때문에 원문을 직접 바꾸지 않는다.
- 원문, 번역본, API 전송본을 서로 다른 텍스트 상태로 관리한다.
## 1.3 모델별 옵션은 프롬프트 문장과 분리한다
 
다음과 같은 생성 옵션은 원칙적으로 프롬프트 본문에 억지로 섞지 않고 구조화된 Provider 옵션으로 전달한다.
 
- 화면비
- 해상도
- 길이
- 시드
- 사운드 옵션
- Provider가 별도 필드로 지원하는 모델 옵션
에셋 미디어 역시 Provider가 구조화 입력을 지원하면 프롬프트 문장과 분리한다.
 
예:
 
- `image_references`
- `start_image`
- `end_image`
- `video_references`
- `audio_references`
- `soul_id`
- 제품·아바타 ID
- Provider preset
## 1.4 에셋을 텍스트로 언급했다고 실제 참조가 적용된 것은 아니다
 
프롬프트에 인물 이름, 장소 이름, 에셋 별칭 또는 고정 문구가 들어갔다고 해서 실제 Provider 참조가 적용된 것으로 취급하지 않는다.
 
실제 참조 적용은 최소 다음이 성립해야 한다.
 
1. 정확한 AssetVersion이 선택됨
2. 참조 역할이 지정됨
3. 선택 모델이 해당 역할을 지원함
4. 실제 Provider 입력 필드로 해석됨
5. 필요한 경우 현재 연결에서 사용할 수 있는 원격 리소스가 확인됨
`프롬프트만 적용`과 `참조 파일 전송`을 항상 구분한다.
 
## 1.5 사용자가 선택한 입력을 조용히 빼거나 바꾸지 않는다
 
- 선택한 에셋을 API 전송에서 몰래 제외하지 않는다.
- 지원하지 않는 역할로 선택한 에셋을 다른 역할로 자동 변경하지 않는다.
- 참조 개수가 많다는 이유로 뒤쪽 에셋을 자동 제거하지 않는다.
- 모델이 바뀌어 기존 입력이 유효하지 않으면 사용자에게 알려 직접 수정하게 한다.
- 에셋 하나에 문제가 있다고 나머지만 제출하지 않는다.
## 1.6 확정되지 않은 사실을 AI가 채우지 않는다
 
Source-Locked 모드에서는 특히 다음 원칙을 지킨다.
 
- AI 자체는 최종 프롬프트 사실의 출처가 아니다.
- AI가 추출한 내용은 먼저 `CANDIDATE`다.
- 사용자가 답하지 않은 정보는 `UNSPECIFIED`다.
- AI 추천값을 사실처럼 자동 채우지 않는다.
- 숫자·수량·각도·시간·연도·색온도·횟수에는 근거 Source가 필요하다.
- 원문에 없는 인물, 객체, 행동, 숫자, 최종 상태를 새로 만들지 않는다.
- 부정과 수량의 의미를 잃지 않는다.
예:
 
```text
첫 프레임에서만 오른손
```
 
을
 
```text
영상 전체에서 오른손
```
 
으로 확대하면 안 된다.
 
```text
한 번
```
 
을
 
```text
계속
```
 
으로 바꾸면 안 된다.
 
```text
말하지 않는다
```
 
를
 
```text
말한다
```
 
로 바꾸면 안 된다.
 
---
 
# 2. 권장 작성 흐름
 
Production OS의 프롬프트 작성 흐름은 다음 순서로 이해한다.
 
```text
Brief·에셋 선택
→ 사실·모호성 후보 확인
→ 필요한 질문 답변 또는 미지정 선택
→ Source·Constraint 확정
→ 연속성 pre-slot 결정
→ Step 1~15 작성
→ Phrase·Prompt Memory 필요 시 선택
→ 원문/번역/API 전송본 확인
→ 결정론적 Validator 실행
→ Blocking issue 해결
→ 사용자 최종 검토
→ PromptVersion 잠금
→ 생성 시점 PromptSnapshot
```
 
중요:
 
- `사실 분석` 자체는 생성 작업이 아니다.
- AI가 초안을 작성해도 사용할 수 있는 Confirmed Source와 Constraint 범위 안에서만 작성한다.
- 사용자가 직접 15단계 문서에 새로운 사실을 추가했다면 그 사실의 Source와 Constraint 연결이 필요하다.
- AI 전후 비교 시 특히 다음을 확인한다.
  - Constraint가 새로 생겼는가
  - Constraint가 사라졌는가
  - 의미가 변경됐는가
  - Source 없는 사실이 추가됐는가
  - EXACT 문구가 변형됐는가
---
 
# 3. 연속성 pre-slot — 이전 숏 연속성
 
## 3.1 위치
 
```text
Pre-slot: PRE_SHOT_CONTINUITY
Step 1~15
```
 
- pre-slot은 15단계 번호에 포함하지 않는다.
- 사용하지 않으면 최종 프롬프트에서 생략한다.
- 사용하면 Step 1보다 앞에 직렬화한다.
## 3.2 두 가지 Continuity 모드
 
| 항목 | `STATE_ONLY_NEW_RENDER` | `DIRECT_MEDIA_EXTENSION` |
|---|---|---|
| 의미 | 이전 숏의 선택된 상태만 가져와 새로 생성 | 이전 영상 자체를 Provider 입력으로 보내 연장 |
| 이전 미디어 픽셀 전송 | 금지 | Provider capability가 지원할 때 필수 |
| 이전 PromptVersion | 계승 Source 기준 | 설명·계보 참고 |
| 카메라·프레이밍 계승 | 사용자가 명시적으로 선택한 경우만 | Provider 연장 의미에 따름 |
| Provider 미지원 | 제출 차단 | 제출 차단 |
| 자동 fallback | 금지 | 다른 모드로 몰래 변경 금지 |
 
## 3.3 STATE_ONLY_NEW_RENDER에서 계승할 수 있는 상태
 
사용자가 필요한 것만 선택한다.
 
- 인물 위치
- 몸 방향
- 시선
- 포즈
- 젖음
- 오염
- 부상
- 의상 상태
- 헤어 상태
- 얼굴 상태
- 손 상태
- 소품 소유 상태
- 문·창문 상태
- 날씨
- 환경 상태
- 광원 상태와 방향
- 카메라 위치·프레이밍·렌즈 — **사용자가 별도 선택한 경우에만**
## 3.4 계승하지 않는 것도 명시한다
 
이전 숏에서 가져오지 않는 값도 명확히 구분한다.
 
예:
 
- 이전 픽셀
- 이전 프레이밍
- 이전 렌즈
- 이전 카메라 위치
AI가 이전 이미지나 영상을 관찰해 추정한 상태는 바로 확정하지 않는다.
 
```text
AI_VISUAL_OBSERVATION_PENDING
```
 
상태이며, 사용자가 확인하기 전에는 연속성 Source가 아니다.
 
---
 
# 4. 고정 15단계 작성법
 
## Step 1. 장면 맥락 — `SCENE_CONTEXT`
 
### 목적
 
장면 전체를 이해하는 배경을 정의한다.
 
포함 범위:
 
- 시대
- 장소
- 상황
- 장면의 목표
- 감정적 배경
### 작성 기준
 
- 다른 블록의 카메라·렌즈·세부 행동을 이 블록에 모두 몰아넣지 않는다.
- 장면의 공통 전제가 상위 Project·Sequence·Scene에 이미 있으면 상속을 활용한다.
- 특정 숫자·연도처럼 사실성이 있는 값은 Source-Locked 모드에서 근거가 필요하다.
## Step 2. 활성 참조 — `ACTIVE_REFERENCES`
 
### 목적
 
이번 생성에서 **실제로 선택한 참조와 그 역할**을 명확히 한다.
 
포함 범위:
 
- 인물 AssetVersion
- 장소 AssetVersion
- 소품 AssetVersion
- 의상 AssetVersion
- 스타일 참조
- 일반 이미지 참조
- 시작 프레임
- 종료 프레임
- 영상 참조
- 오디오 참조
- Soul ID
- 제품·아바타
- Provider preset
- 프롬프트 문구만 적용되는 에셋
### 반드시 구분할 것
 
```text
사람이 읽는 텍스트 언급
≠
실제 Provider 입력
```
 
예시 표시 형태:
 
```text
김영훈 · 인물 · 참조 이미지 · AssetVersion 3
호텔 복도 · 장소 · 일반 이미지 참조 · AssetVersion 1
여성 출발 구도 · 시작 프레임 · MediaResult 42
```
 
이 표시 자체를 외부 Provider 토큰으로 사용하지 않는다.
 
해석되지 않은 외부 토큰이나 사라진 참조가 있으면 생성하지 않는다.
 
## Step 3. 공간 지도·위치 관계 — `LOCATION_MAP`
 
### 목적
 
장소 안의 인물·카메라·출입구·가구·광원 등의 **안정된 상대 위치 관계**를 정의한다.
 
포함 범위:
 
- 문
- 출입구
- 복도 끝
- 가구
- 광원
- 인물 위치
- 카메라 위치
- 서로의 상대 위치
- 연결된 공간
### 작성 기준
 
모호한 자연어만 쓰지 않는다.
 
```text
그 문
오른쪽 문
먼 문
```
 
처럼 동일 장면에서 여러 대상을 가리킬 수 있는 표현은 안정된 SpatialAnchor와 연결한다.
 
다음은 서로 다른 의미다.
 
```text
문의 왼쪽 벽
화면 왼쪽
문의 왼쪽 힌지
```
 
## Step 4. 첫 프레임 및 공간 블로킹 — `FIRST_FRAME_AND_SPATIAL_BLOCKING`
 
### 목적
 
영상의 시작 순간에 무엇이 어디에 있고 어떤 상태인지 고정한다.
 
포함 범위:
 
- 첫 프레임 구도
- 인물 최초 위치
- 인물 몸 방향
- 시선
- 손 상태
- 소품 위치와 소유
- 문·창문 상태
- 프레임 안/밖 배치
- 시작 상태
### 주의
 
`첫 프레임` 조건을 영상 전체 조건으로 자동 확대하지 않는다.
 
첫 프레임과 이후 행동은 분리한다.
 
- Step 4: 시작 상태
- Step 8: 이후 시간 흐름과 행동
## Step 5. 영상 형식 — `FORMAT_MODE`
 
### 목적
 
어떤 형식의 생성인지 정의한다.
 
포함 범위:
 
- 실사
- 애니메이션
- 단일 테이크
- 복수 숏
- 컷 구조
- 생성 유형
### 주의
 
`단일 테이크`를 적으면서 Step 8에서 `hard cut`을 요구하는 식의 교차 모순을 만들지 않는다.
 
숏 수를 명시했으면 각 숏에 행동·카메라·시간 구조가 대응되는지 확인한다.
 
## Step 6. 렌즈 설정 — `OPTICS`
 
### 목적
 
화각과 렌즈가 만드는 시각적 특성을 정의한다.
 
포함 범위:
 
- 화각
- 초점거리
- 조리개 느낌
- 심도
- 원근
- 왜곡 특성
### 주의
 
- 실제 물리 렌즈값인지 창작용 시각 표현인지 구분한다.
- 숫자 초점거리·각도 등을 Source-Locked 사실로 사용할 때는 근거를 요구한다.
- 3D calibration이 없는 Reference 이미지로 실제 렌즈값을 단정하지 않는다.
- ReferencePerspectiveProfile은 원근·소실점·프레이밍 유사성을 다루는 참고일 수 있다.
## Step 7. 카메라 설정 — `CAMERA`
 
### 목적
 
카메라의 공간적 상태와 움직임을 정의한다.
 
포함 범위:
 
- 위치
- 높이
- 각도
- 거리
- 이동
- 안정성
- 고정 여부
### 주의
 
카메라 움직임과 화면 내부 객체 움직임을 같은 것으로 취급하지 않는다.
 
예:
 
```text
CAMERA = LOCKED
IMAGE_PLANE = JITTER
```
 
는 모순이 아닐 수 있다.
 
반대로:
 
```text
CAMERA = LOCKED
CAMERA = PUSH_IN
```
 
은 같은 시간 범위라면 충돌할 수 있다.
 
## Step 8. 행동 타이밍 — `ACTION_TIMING`
 
### 목적
 
시간 순서에 따른 행동·대사·정지·컷·전환을 정의한다.
 
포함 범위:
 
- 행동 순서
- 행동 시작/종료
- 대사 시점
- 멈춤
- 컷
- 전환
- 이벤트
- 필요한 경우 PTS/시간 구간
### 주의
 
- 전체 영상 길이와 행동 타임라인이 맞아야 한다.
- 행동 종료 시점이 영상 길이를 넘어가지 않아야 한다.
- 이벤트 사이에 설명되지 않은 gap이 생기지 않는지 확인한다.
- `한 번`, `정확히 두 번`, `계속` 같은 수량사를 잃지 않는다.
- 상태 전이는 초기 상태 → 전환 → 최종 상태가 맞아야 한다.
## Step 9. 인물 연기 — `CHARACTER_ACTING`
 
### 목적
 
인물의 연기와 감정 표현을 정의한다.
 
포함 범위:
 
- 표정
- 시선
- 호흡
- 몸의 긴장
- 감정 강도
- 자세 변화
### 주의
 
행동의 물리적 순서는 Step 8, 연기의 질감과 표현은 Step 9로 구분한다.
 
인물의 오른손·왼손처럼 좌우 의미가 중요하면 좌표계를 함께 확정한다.
 
## Step 10. 움직임·물리 — `PHYSICS`
 
### 목적
 
인물·물체·환경이 어떻게 움직이고 반응하는지 정의한다.
 
포함 범위:
 
- 인물 움직임
- 옷
- 머리카락
- 물체
- 바람
- 중력
- 충돌
- 재질 반응
- 환경 움직임
### 주의
 
`motion_owner`를 구분한다.
 
- `CHARACTER`
- `PROP`
- `CAMERA`
- `ENVIRONMENT`
- `IMAGE_PLANE`
- `REFLECTION`
누가 움직이는지 불분명한 지시는 피한다.
 
## Step 11. 조명 — `LIGHTING`
 
### 목적
 
장면의 광원과 노출 특성을 정의한다.
 
포함 범위:
 
- 광원
- 방향
- 세기
- 색
- 그림자
- 노출
- 시간대
### 주의
 
Reference 이미지의 룩을 보고 실제 물리 Kelvin을 단정하지 않는다.
 
예를 들어 `3800K look`이 단순 시각적 참고라면 실제 광원의 물리값과 구분한다.
 
## Step 12. 음향 — `AUDIO`
 
### 목적
 
모델이 지원할 때 생성 요청의 음향 지시를 정의한다.
 
포함 범위:
 
- 대사
- 환경음
- 효과음
- 정적
- 모델 자체의 사운드 옵션과 연동되는 지시
### 주의
 
- 독립 음향 생성 시스템과 혼동하지 않는다.
- 현재 모델이 음향을 지원할 때만 의미 있게 적용한다.
- Gate C Generation QC에서는 Audio 내용 자체는 판정 범위에서 제외된다.
## Step 13. 영상 스타일 — `STYLE`
 
### 목적
 
장면의 시각적 표현 방식과 룩을 정의한다.
 
포함 범위:
 
- 시대감
- 매체 질감
- 색조
- 렌더링 방식
- 필름 룩
- 스타일 Reference
### 주의
 
스타일 Reference가 인물 Identity까지 자동 통제한다고 가정하지 않는다.
 
## Step 14. 퀄리티 — `QUALITY`
 
### 목적
 
출력의 기술적·시각적 품질 목표를 정의한다.
 
포함 범위:
 
- 해상감
- 디테일
- 노이즈 억제
- 압축 억제
- 왜곡 억제
### 주의
 
Step 13의 미학적 스타일과 Step 14의 품질 목표를 구분한다.
 
## Step 15. 필수 및 금지 조건 — `REQUIRED_AND_FORBIDDEN_CONSTRAINTS`
 
### 목적
 
절대 유지해야 할 것과 발생하면 안 되는 것을 최종적으로 명시한다.
 
두 하위 의미를 유지한다.
 
```text
Required
Forbidden
```
 
### 포함 범위
 
- 반드시 유지해야 할 상태
- 반드시 유지해야 할 인물·소품·공간 관계
- 반드시 유지해야 할 횟수·방향·시간 범위
- 절대 발생하면 안 되는 행동
- 절대 등장하면 안 되는 요소
- 연속성 보호 조건
- 이전 QC에서 보호 대상으로 잠근 중요한 조건
### 주의
 
- 다른 블록의 같은 사실과 별도 사실처럼 분리하지 않는다.
- 동일 요구가 여러 블록에 반복되면 같은 Constraint를 가리킨다.
- 과거 실패를 이유로 금지문을 끝없이 누적하지 않는다.
- 같은 핵심 실패가 연속 2회 또는 최근 4회 중 3회 반복된다면 숏 자체를 분리하는 방향을 우선 검토한다.
---
 
# 5. 상속·재정의·명시적 비우기
 
프롬프트 블록은 다음 계층에서 상속된다.
 
```text
프로젝트
→ 시퀀스
→ 씬
→ 숏
→ 테이크
```
 
각 블록은 독립적으로 다음 세 상태 중 하나다.
 
## `INHERIT` — 상속
 
가장 가까운 상위 범위의 유효한 값을 사용한다.
 
## `OVERRIDE` — 재정의
 
상위 값을 수정하지 않고 현재 범위의 값으로 대체한다.
 
## `EMPTY` — 명시적으로 비움
 
상위 값이 존재하더라도 현재 최종 프롬프트에서는 해당 블록을 빈 값으로 만든다.
 
중요:
 
```text
EMPTY ≠ INHERIT
빈 문자열 ≠ 상속
```
 
작성 시 확인할 것:
 
- 상위 문장이 자동으로 중복 연결되지 않았는가
- 현재 본문이 어디서 상속됐는가
- 현재 단계에서 직접 재정의한 것인가
- 상위 내용을 일부러 제거한 EMPTY인가
---
 
# 6. Source-Locked 작성 규칙
 
## 6.1 SourceRecord와 ConstraintRecord의 역할
 
```text
SourceRecord
= 이 사실이 어디에서 왔는가
 
ConstraintRecord
= 무엇을 어느 범위에서 지켜야 하는가
```
 
자연어 한 문장에 여러 사실이 있으면 Constraint를 여러 개로 분리할 수 있다.
 
하나의 Constraint가 여러 블록에서 반복 표현되더라도 논리적 정체성은 하나다.
 
## 6.2 AI가 출처가 될 수 없는 이유
 
AI가 다음을 생성할 수는 있다.
 
- 사실 후보
- 모호성 후보
- 누락 후보
- 질문
- 표현 후보
하지만 이것만으로 최종 사실이 되지는 않는다.
 
사용자가 확정하거나 원문에서 결정론적으로 검증할 수 있어야 한다.
 
## 6.3 허용 Source 유형
 
| Source | 의미 |
|---|---|
| `USER_BRIEF` | 사용자가 직접 작성한 정확한 Brief 원문 |
| `USER_CLARIFICATION` | 사용자가 질문에 직접 답해 확정한 값 |
| `ASSET_METADATA_CONFIRMED` | 정확한 AssetVersion의 승인된 metadata |
| `ASSET_PROMPT_EXACT` | Asset Prompt Memory에서 사용자가 선택한 EXACT 문구 |
| `PREVIOUS_PROMPT_EXACT` | 특정 과거 PromptVersion에서 사용자가 직접 선택한 EXACT 문구 |
| `RELATED_SCENE_EXACT` | 관련 씬 후보 중 사용자가 정확한 문구를 선택 |
| `PROJECT_LOCKED_RULE` | 프로젝트 범위에서 확정된 규칙 |
| `SCENE_LOCKED_RULE` | 씬 범위에서 확정된 규칙 |
| `SHOT_LOCKED_RULE` | 숏 범위에서 확정된 규칙 |
| `PRIOR_SHOT_CONTINUITY_CONFIRMED` | 사용자가 확정한 이전 숏 상태 계승 |
| `IMPORTED_LEGACY_PROMPT` | 가져온 과거 프롬프트를 사용자가 승인 |
| `DETERMINISTIC_DERIVATION` | 기존 Source와 승인된 규칙으로 손실 없이 계산된 값 |
 
다음은 사용자 확인 전 Composer가 사용하지 않는다.
 
- `AI_SUGGESTION_PENDING`
- `AI_VISUAL_OBSERVATION_PENDING`
- `AI_RELATED_SCENE_CANDIDATE`
## 6.4 Source 상태
 
```text
CANDIDATE
→ CONFIRMED
→ SUPERSEDED
 
CANDIDATE
→ REJECTED
 
CANDIDATE
→ UNSPECIFIED
```
 
- `CONFIRMED`는 현재 작성에서 사용할 수 있다는 뜻이다.
- 미래 모든 프롬프트에 영구 확정되는 것은 아니다.
- 정정할 때 과거 Source를 덮어쓰지 않는다.
- 새 Source를 만들고 과거 Source를 `SUPERSEDED`로 연결한다.
---
 
# 7. 구체화 질문 작성·응답 규칙
 
질문은 세 등급으로 구분한다.
 
| 등급 | 의미 | 생성 영향 |
|---|---|---|
| `REQUIRED` | 답이 없으면 내부 모순·필수 입력 누락·중요 상태 미정 발생 | 해결 전 차단 |
| `RECOMMENDED` | 결과 품질·연속성에 영향이 크지만 미지정도 가능 | 경고 후 미지정 가능 |
| `OPTIONAL` | 창작 세부를 더 정교하게 함 | 미응답 가능 |
 
각 질문에는 반드시 다음을 보여준다.
 
- 질문의 근거가 된 사용자 원문 또는 에셋
- 무엇이 모호하거나 빠졌는지
- 영향을 받는 15단계 블록
- 영향을 받는 Constraint 후보
- 선택지
- 직접 입력
- `미지정으로 둠`
- 선택하면 새로운 사실이 된다는 표시
- 기존 확정값과 충돌할 경우 충돌 이유와 교체 영향
AI가 제시한 option은 사용자가 선택하기 전에는 사실이 아니다.
 
같은 질문을 표현만 바꿔 반복하지 않는다.
 
---
 
# 8. Reference Authority — 참조 이미지가 무엇을 통제하는지 정한다
 
에셋을 선택했다고 해당 이미지의 모든 요소가 자동으로 생성 조건이 되는 것은 아니다.
 
각 ReferenceView가 통제하는 범위를 명시한다.
 
| Scope | 통제 대상 |
|---|---|
| `IDENTITY` | 얼굴·인물 동일성 |
| `WARDROBE` | 의상·장신구 |
| `PROP_APPEARANCE` | 소품 외형·재질·부속 |
| `GEOMETRY` | 공간 구조·문·복도 배치 |
| `MATERIALS` | 벽·바닥·가구 재질 |
| `LIGHTING` | 광원 방향·분포·룩 |
| `ATMOSPHERE` | 안개·습도·먼지·시대 분위기 |
| `FRAMING` | 구도·프레임 기울기 |
| `MOTION` | 동작·카메라 궤적 |
| `STYLE` | 필름 룩·색조·질감 |
 
## 중요한 규칙
 
- Reference가 통제하지 않는 영역을 AI가 임의로 확대하지 않는다.
- 같은 scope, 같은 시간 범위에서 같은 우선순위의 서로 다른 Reference가 충돌하면 해결 전 생성하지 않는다.
- 높은 우선순위 Reference가 낮은 우선순위를 제외하면 제외된 Reference와 이유를 보여준다.
- Soul ID의 기본 authority는 `IDENTITY`다.
- Soul ID만으로 의상·액세서리·신체 무늬·피부 질감·체형·조명·배경을 자동 보장하지 않는다.
- Provider가 입력을 접수한 사실과 결과가 참조를 충실히 재현한 것은 별개의 문제다.
---
 
# 9. 시간 범위를 명확히 쓰는 법
 
허용 Temporal Scope:
 
| 유형 | 의미 |
|---|---|
| `FIRST_FRAME` | 표시상 첫 프레임 |
| `INTERVAL` | 특정 시간 구간 |
| `UNTIL_EVENT` | 특정 이벤트가 발생하기 전 |
| `AFTER_EVENT` | 특정 이벤트 이후 |
| `ENTIRE_SHOT` | 현재 숏 전체 |
| `ENTIRE_VISIBLE_TRACK` | 대상이 보이는 전체 구간 |
| `FINAL_FRAME` | 마지막 디코딩 가능한 presentation frame |
| `SHOT_ROLE` | MAIN·CU 등 명명된 shot segment |
| `UNSPECIFIED` | 범위 미정 |
 
규칙:
 
- `UNSPECIFIED`를 전체 숏으로 자동 확대하지 않는다.
- 시작/종료가 필요한 interval은 두 값이 모두 유효해야 한다.
- 시작이 종료보다 같거나 뒤면 오류다.
- Reference가 시간에 따라 달라지면 겹치지 않는 구간과 전환 정책이 필요하다.
---
 
# 10. 좌우·방향·공간 좌표를 명확히 쓰는 법
 
허용 좌표계:
 
| 값 | 의미 |
|---|---|
| `ANATOMICAL` | 인물 자신의 좌우 |
| `SCREEN` | 특정 숏 화면의 좌우 |
| `CAMERA` | 카메라 rig 기준 좌우·상하·전후 |
| `LOCATION` | LocationMap 기준 축 |
| `OBJECT_LOCAL` | 문·소품 자체의 힌지·손잡이·면 기준 |
| `WORLD` | 프로젝트가 정의한 세계 좌표 |
 
예:
 
```text
Rebecca의 오른손
```
 
은 `ANATOMICAL RIGHT`.
 
정면 카메라에서 그 손이 화면 왼쪽에 있다면:
 
```text
ANATOMICAL RIGHT
+
SCREEN LEFT
```
 
두 관계를 구분한다.
 
`SCREEN LEFT`는 해당 shot에 귀속된다. 컷이 바뀌면 같은 screen-left가 같은 공간 방향이라고 가정하지 않는다.
 
---
 
# 11. Render Domain과 Motion Owner를 구분한다
 
## Render Domain
 
사람·얼굴·그림자·반사를 하나의 숫자로 합치지 않는다.
 
- `PHYSICAL_PERSON`
- `REFLECTION`
- `SHADOW`
- `BACKGROUND_SILHOUETTE`
- `IMAGE_PLANE_FACE`
예:
 
```text
방 안 실제 인물 1명
거울 속 얼굴 1개
```
 
이면:
 
```text
physical_person_count = 1
reflection_count = 1
```
 
이다.
 
## Motion Owner
 
움직임의 주체를 구분한다.
 
- `CHARACTER`
- `PROP`
- `CAMERA`
- `ENVIRONMENT`
- `IMAGE_PLANE`
- `REFLECTION`
---
 
# 12. 객체 상태 변화는 상태 머신으로 생각한다
 
문·가방·손·소품·인물 자세처럼 시간에 따라 변하는 것은 다음을 구분한다.
 
```text
초기 상태
→ 허용된 전이
→ 중간 상태
→ 최종 상태
```
 
예:
 
```text
CLOSED
→ OPENING
→ OPEN
→ CLOSING
→ CLOSED
```
 
확인할 것:
 
- 초기 상태가 명시됐는가
- 누가 상태를 바꾸는가
- 몇 번 바뀌는가
- 언제 바뀌는가
- 마지막 상태는 무엇인가
- 허용되지 않은 상태 점프가 없는가
순간적으로 가려져 보이지 않는 것을 상태 변화로 해석하지 않는다.
 
---
 
# 13. 일반 저장 문장·추천 문장 사용법
 
일반 Phrase 추천은 **프로젝트 안의 서로 다른 Shot 사용 이력**을 기준으로 한다.
 
## 13.1 사용 횟수
 
- 같은 Shot의 여러 Take에서 같은 문장을 여러 번 사용해도 1회다.
- 같은 Scene의 서로 다른 Shot이면 각각 센다.
- 서로 다른 Scene이면 각각 센다.
- 다른 Project의 사용량은 합산하지 않는다.
- 3개 이상의 서로 다른 Shot에서 사용된 문장은 추천 후보가 된다.
- 추천 후보가 됐다고 자동 승인하지 않는다.
## 13.2 동일 문장 판정
 
일반 Phrase 비교에서는 다음을 정규화한다.
 
- Unicode NFC
- 앞뒤 공백 제거
- 연속 whitespace/linebreak를 하나의 공백으로
- 단순 문장부호 일부 차이: `.`, `,`, `。`, `，`, `、`
하지 않는 것:
 
- 소문자화
- stemming
- AI 의미 병합
- 동의어 병합
- 숫자 변환
- 최소 길이 기준으로 제외
에셋 고정 문구와 AssetPreset 원문은 일반 추천 집계에서 제외한다.
 
## 13.3 삽입
 
Phrase는:
 
- 원하는 15단계 블록에 삽입
- 현재 커서 위치 또는 블록 끝에 삽입
- 삽입 전 preview
- 사용자가 적용한 뒤 일반 텍스트처럼 수정 가능
단, 사용된 원본 Phrase 자체의 의미를 나중에 바꾸지 않는다.
 
이미 사용 이력이 있는 저장 문장을 수정하고 싶다면:
 
```text
새 문장으로 저장
```
 
한다.
 
---
 
# 14. Prompt Memory 사용법
 
Prompt Memory는 단순히 자주 쓰는 문장 목록이 아니다.
 
```text
PromptMemoryEntry
=
AssetVersion
+ Attribute
+ Context
+ Exact Text
+ Source PromptVersion
+ Source Constraint
+ Provenance
+ Source Outcome
```
 
context 예:
 
- 프로젝트
- 씬 태그
- 시대
- 장소
- 인물 상태
- 의상 상태
- 표정
- 행동
- Prompt block
- Final·대안·폐기
- QC PASS·FAIL·REVIEW
Provider나 모델 정보는 검색·필터 정보일 뿐 해당 문구의 품질을 자동 보장하지 않는다.
 
## 14.1 추천 우선순위
 
1. 동일 AssetVersion + Final + 관련 QC PASS
2. 동일 AssetVersion + 관련 QC PASS
3. 동일 AssetVersion + 동일 상태·속성
4. 동일 Asset + 동일 Prompt block·context
5. 사용자가 즐겨찾기·승인한 기타 문구
6. 결과는 있으나 미평가인 문구
7. 실패·폐기 Take의 문구
실패 문구도 조사용으로 볼 수 있지만 기본 적용 시 경고한다.
 
---
 
# 15. EXACT 재사용
 
EXACT는 **문구를 한 글자도 임의로 바꾸지 않는 재사용**이다.
 
정규화 허용:
 
```text
Unicode NFC
line ending → LF
```
 
변경 금지:
 
- 공백
- 탭
- 문장부호
- 대소문자
- 단어
- 부정어
AI가 EXACT 문장을 직접 다시 쓰게 하지 않는다.
 
흐름:
 
```text
placeholder 배치
→ AI가 주변 문장을 작성
→ 서버가 승인된 exact literal 삽입
→ hash 검증
```
 
한 글자라도 다르면:
 
```text
EXACT_REUSE_MUTATED
```
 
blocking issue다.
 
EXACT를 수정하고 싶다면 다음 중 하나를 선택한다.
 
1. `SEMANTIC`으로 전환
2. 새 사용자 문구로 복제
3. 취소
원래 MemoryEntry는 바꾸지 않는다.
 
---
 
# 16. SEMANTIC 재사용
 
SEMANTIC은 사용자가 명시적으로 선택한 경우에만 허용한다.
 
의미를 보존해 재표현할 수 있지만 다음을 임의로 추가·삭제할 수 없다.
 
- 인물
- 객체
- 숫자
- 시간
- 좌표
- 부정
- 수량
- 횟수
- 최종 상태
검증할 것:
 
- unsupported claim 추가 여부
- temporal scope 확대 여부
- negation loss 여부
- 숫자·수량 변화
- entity 변경
- 최종 상태 변경
Validator가 의미 동일성을 확정하지 못하면 원문과 결과를 나란히 보고 사용자가 판단한다.
 
---
 
# 17. 일반 추천 Phrase와 Prompt Memory의 차이
 
| 항목 | 일반 추천 Phrase | Prompt Memory |
|---|---|---|
| 기준 | 프로젝트 내 서로 다른 Shot 사용 이력 | AssetVersion·속성·상황·원본 PromptVersion·성과 |
| 편집 | 삽입 후 자유 편집 | EXACT 또는 명시적 SEMANTIC |
| 자동 삽입 | 금지 | 금지 |
| 우선순위 | 사용 이력·즐겨찾기 | 동일 AssetVersion, Final, QC PASS, context |
| 실패 문구 | 추천 정책에 따라 표시 | 후순위 + 경고 |
| AssetVersion mismatch | 일반 문장 | 자동 적용 차단 |
 
관련 Scene이나 semantic search 결과는 **후보일 뿐 Source가 아니다.**
 
---
 
# 18. 에셋 프리셋과 고정 문구
 
에셋에는 다음이 함께 존재할 수 있다.
 
- 고정 Prompt 문구
- 여러 Prompt preset
- 여러 참조 파일
Preset은:
 
- 어느 Step에 들어갈지 지정
- 하나 또는 여러 개 선택 가능
- 삽입 전 변경 내용을 보여줌
- 현재 Prompt를 자동 덮어쓰지 않음
- 프로젝트별로 다르게 구성 가능
사용자는 다음을 독립적으로 선택할 수 있다.
 
```text
문구만
참조 파일만
둘 다
```
 
`문구만`을 선택했으면 실제 Provider 참조가 적용됐다고 표시하지 않는다.
 
---
 
# 19. 생성 요청에서 사용할 에셋 역할
 
선택 모델이 지원하는 역할만 사용한다.
 
| 역할 | 용도 |
|---|---|
| 일반 이미지 참조 | 인물·장소·제품·의상·스타일의 시각적 참조 |
| 시작 프레임 | 첫 장면·구도 고정 |
| 종료 프레임 | 마지막 장면·도착 구도 |
| 영상 참조 | 동작·카메라·편집 리듬 |
| 오디오 참조 | 음색·배경음·대사 |
| 캐릭터 ID | 인물 Identity 유지 |
| 제품·아바타 | Provider의 제품·아바타 리소스 |
| Provider preset | 스타일·카메라·액션 preset |
| 프롬프트 문구만 | 파일 전송 없이 설명·고정 문구만 사용 |
 
규칙:
 
- 모델 선택 후 역할 호환성을 최종 확인한다.
- 하나의 파일을 두 역할에 동시에 쓰려면 모델이 허용하는지 확인한다.
- 시작/종료 프레임처럼 순서 의미가 있는 입력을 일반 참조 배열에 섞지 않는다.
- 참조 순서를 보존한다.
- Provider가 참조별 이름/label을 지원하지 않으면 임의 비공개 필드를 만들지 않는다.
---
 
# 20. 원문·번역본·API 전송본
 
세 종류를 완전히 분리한다.
 
## 원문 — `ORIGINAL`
 
- 사용자가 작성한 한국어 기준본
- 기본 전송 후보
## 번역본 — `TRANSLATION`
 
- 사용자가 직접 작성·붙여넣거나 승인된 번역 기능으로 생성
- 기능이 없으면 비워 둠
- 원문이 바뀌면 기존 번역이 오래된 상태인지 확인
## 직접 편집 API 전송본 — `CUSTOM_API_TEXT`
 
- 원문·번역본과 별도
- 관리자 wrapper·Provider 문법이 적용될 수 있음
- 원문 자체를 덮어쓰지 않음
## STALE 규칙
 
원문이 바뀌어 번역본이나 API 전송본의 기준 hash가 과거 원문을 가리키면:
 
```text
STALE
```
 
이다.
 
사용자가 확인·갱신하기 전 생성 제출을 막는다.
 
번역본의 EXACT는 원문의 EXACT를 그대로 의미하지 않는다.
 
번역 literal 자체를 별도로 승인해야 한다.
 
---
 
# 21. 최종 프롬프트 직렬화
 
최종 프롬프트는 다음 원칙으로 직렬화한다.
 
정규화:
 
```text
Unicode NFC
line ending → LF
```
 
하지 않는 것:
 
- 단어 변경
- 공백 자동 축약
- 문장부호 자동 변경
- 자동 번역
- 자동 요약
- 자동 truncate
형식 개념:
 
```text
[SCENE_CONTEXT] 장면 맥락
{body}
 
[ACTIVE_REFERENCES] 활성 참조
{body}
 
...
 
[REQUIRED_AND_FORBIDDEN_CONSTRAINTS] 필수 및 금지 조건
{body}
```
 
활성 pre-slot이 있다면 이 앞에 `PRE_SHOT_CONTINUITY`가 온다.
 
15개 제목은 항상 같은 순서로 유지한다.
 
---
 
# 22. 길이 제한 처리
 
모델이 문자·토큰·필드 제한을 실제 capability로 제공하면 사용량과 남은 용량을 표시한다.
 
제한을 알 수 없으면:
 
```text
제한 미확인
```
 
으로 둔다.
 
추정 숫자를 보장값처럼 만들지 않는다.
 
제한을 초과하면 자동으로 다음 행동을 하지 않는다.
 
- 뒤 블록 삭제
- 자동 요약
- 낮은 우선순위 문장 삭제
- 자동 축약
- 자동 truncate
사용자가 선택한다.
 
1. 문제 fragment를 직접 줄임
2. 구조화 Provider 옵션으로 이동
3. 에셋 역할 필드로 이동
4. 숏을 분리
수정 결과는 새 PromptVersion에 저장한다.
 
---
 
# 23. 저장·버전·잠금
 
## 23.1 자동 저장
 
마지막 입력 후:
 
```text
서버 commit <= 5초
```
 
가 목표다.
 
5초 안에 저장이 되지 못하면 지속적인 오류 상태가 사용자에게 보여야 한다.
 
- 저장 중
- 저장 완료
- 저장 실패
를 구분한다.
 
한글 IME 조합 중 미완성 자모는 최종 저장 내용으로 확정하지 않는다.
 
## 23.2 잠금
 
실제 생성에 사용되는 PromptVersion은 잠근다.
 
잠긴 버전은 직접 수정하지 않는다.
 
사용자가 수정하려 할 때 선택:
 
1. 새 PromptVersion 만들기
2. 새 Take로 복제
3. 취소
일반 UI에서 잠긴 버전을 다시 unlock하는 기능은 두지 않는다.
 
## 23.3 PromptSnapshot
 
실제 생성에 사용된 순간의 값은 불변 snapshot으로 남는다.
 
포함 대상:
 
- resolved 15개 블록
- 상속 출처
- 원문
- 실제 API 전송 문자열
- 정확한 AssetVersion
- 입력 역할과 순서
- 실제 로컬 hash
- 실제 Provider field
- 원격 리소스 ID
- Provider
- 모델
- 모델 버전
- 옵션
- 예상 크레딧
- 요청 사용자
- 요청 시각
실제 생성에 필요한 값이 아직 확정되지 않았다면 완전한 Generation PromptSnapshot을 미리 만든 것으로 취급하지 않는다.
 
---
 
# 24. 오프라인·저장 실패 복구
 
단일 사용자 recovery draft는 브라우저 로컬에 임시 보존할 수 있다.
 
보존 대상은 프롬프트 편집 내용과 기준 버전 정보다.
 
보존하지 않는 것:
 
- 미디어 원본
- session token
- CSRF token
- password
- Provider secret/token
- signed URL
- Provider response
로컬 draft는:
 
- 서버 동기화 성공 시 제거
- 로그아웃 시 제거
- 최대 7일
- 다른 사용자의 session에 노출 금지
재연결 시 서버 버전이 달라졌다면 자동 last-write-wins 하지 않는다.
 
충돌 화면을 보여주고 사용자가 해결한다.
 
---
 
# 25. 기존 프롬프트 이관 규칙
 
과거 PromptSnapshot 원문은 절대 변경하지 않는다.
 
기존 구조를 새 구조로 옮길 때:
 
```text
기존 CONTINUITY REFERENCE Step 1
→ PRE_SHOT_CONTINUITY 후보
 
기존 Step 2~13
→ 새 Step 1~12 후보
 
기존 STYLE & QUALITY
→ STYLE + QUALITY 후보
 
기존 Positive/Negative Constraints
→ Step 15 Required/Forbidden
```
 
자동 분류가 확실하지 않으면 사용자가 경계를 확정한다.
 
이관 과정에서 자동으로 번역·정리·의역하지 않는다.
 
---
 
# 26. Prompt Validator — 생성 전 필수 검수
 
생성 전에 최소 다음 항목을 검사한다.
 
| Validator | 검사 |
|---|---|
| `SCHEMA_VALIDITY` | 블록·Source·Constraint·시간·좌표 구조 |
| `SOURCE_COVERAGE` | 사실성 fragment에 허용 Source가 있는가 |
| `NUMERIC_SOURCE` | 숫자·시간·각도·수량·연도의 출처 |
| `EXACT_REUSE` | EXACT literal과 hash 보존 |
| `SEMANTIC_REUSE` | 의미·entity·숫자·부정 보존 |
| `NEGATION_QUANTIFIER` | not·never·only·once·exactly 등 보존 |
| `TEMPORAL_SCOPE` | FIRST/INTERVAL/ENTIRE/FINAL 범위 |
| `ENTITY_BINDING` | 이름·대명사·그 물체의 stable ID |
| `COORDINATE_SYSTEM` | anatomical·screen·camera·location·object 좌표 |
| `REFERENCE_AUTHORITY` | Reference scope·시간·우선순위·충돌 |
| `MOTION_OWNER` | camera·character·image plane 등 움직임 주체 |
| `RENDER_DOMAIN_COUNT` | physical·reflection·shadow·silhouette 구분 |
| `STATE_MACHINE` | initial·transition·횟수·final state |
| `TIMELINE_COVERAGE` | 총 길이·행동·대사·event gap |
| `SHOT_STRUCTURE` | shot 수·cut·lens·camera·action 대응 |
| `CROSS_BLOCK_CONFLICT` | 서로 다른 block의 모순 |
| `FINAL_STATE` | 마지막 상태 뒤의 모순 행동 |
| `PROTECTED_PASSED_CONSTRAINT` | 보호된 과거 중요 조건 누락·변경 |
| `PROVIDER_READINESS` | 실제 전송 text·에셋 역할·capability |
| `GENERATION_READINESS` | 전체 blocking issue·stale 상태 |
 
## 판정 상태
 
- `PASS`: 문제 없음
- `WARN`: 경고는 있지만 제출 가능할 수 있음
- `FAIL`: 규칙 위반 확정
- `REVIEW_REQUIRED`: 자동 판단 불가, 사람이 판단
- `NOT_APPLICABLE`: 현재 모드에 해당 없음
- `ANALYZER_ERROR`: 검사 시스템 오류
- `UNSUPPORTED`: 현재 Provider·버전 미지원
## Blocking 규칙
 
다음은 해결 전 제출하지 않는다.
 
- blocking FAIL
- required Source 문제
- Reference 충돌
- Provider 입력 문제
- stale translation/API text
- 미응답 REQUIRED 질문
- EXACT mutation
- Source 없는 숫자
- 지원하지 않는 DIRECT_MEDIA_EXTENSION
- 권리·개인정보 문제
- Provider capability 실패
검사 시스템 오류를 프롬프트 자체 FAIL로 바꾸지 않는다.
 
검사하지 못한 항목을 PASS로 처리하지 않는다.
 
---
 
# 27. 생성 직전 최종 확인 체크리스트
 
## 구조
 
- [ ] pre-slot 사용 여부가 명시됐는가
- [ ] Step 1~15가 모두 존재하는가
- [ ] 단계 순서가 고정 순서인가
- [ ] 단계 제목이 그대로 유지됐는가
- [ ] 빈 블록과 상속이 구분돼 있는가
## 상속
 
- [ ] 각 블록이 INHERIT / OVERRIDE / EMPTY 중 무엇인지 분명한가
- [ ] 상위 문장이 중복 연결되지 않았는가
- [ ] EMPTY를 INHERIT처럼 처리하지 않았는가
## Source
 
- [ ] 사실성 fragment에 허용 Source가 있는가
- [ ] AI 후보를 사용자 확정 없이 사용하지 않았는가
- [ ] 숫자·시간·각도·수량·연도·횟수의 Source가 있는가
- [ ] REQUIRED 질문이 남아 있지 않은가
- [ ] 미정값을 AI가 기본값으로 채우지 않았는가
## 시간·좌표·상태
 
- [ ] FIRST_FRAME과 ENTIRE_SHOT 범위를 혼동하지 않았는가
- [ ] 좌우가 ANATOMICAL / SCREEN / CAMERA 중 무엇인지 분명한가
- [ ] `그 문`, `그 물체`가 안정 ID로 해석되는가
- [ ] 초기 상태와 최종 상태가 연결되는가
- [ ] 행동 횟수와 상태 전이가 일치하는가
## 참조
 
- [ ] 실제 AssetVersion이 맞는가
- [ ] 대표 이미지와 실제 전송 파일을 혼동하지 않았는가
- [ ] Prompt-only와 실제 Provider 참조를 구분했는가
- [ ] Reference Authority scope가 명시됐는가
- [ ] 같은 scope의 참조가 충돌하지 않는가
- [ ] Soul ID를 Identity 이상으로 자동 확대하지 않았는가
- [ ] 시작/종료 프레임이 일반 이미지 참조로 섞이지 않았는가
- [ ] 현재 모델이 각 역할을 지원하는가
## Phrase·Prompt Memory
 
- [ ] 일반 추천 Phrase와 Prompt Memory를 구분했는가
- [ ] EXACT 문구가 한 글자도 변형되지 않았는가
- [ ] SEMANTIC 재사용이 사용자 선택으로 이루어졌는가
- [ ] SEMANTIC 재작성에서 숫자·부정·수량·시간·entity가 변하지 않았는가
- [ ] 현재 AssetVersion과 다른 Prompt Memory를 자동 적용하지 않았는가
- [ ] 실패 문구가 경고 없이 우선 적용되지 않았는가
## 원문·번역·API 전송본
 
- [ ] 한국어 원문이 기준본으로 보존됐는가
- [ ] 번역이 필요하지 않은데 임의 생성되지 않았는가
- [ ] 번역본이 STALE이 아닌가
- [ ] API 전송본이 STALE이 아닌가
- [ ] wrapper가 원문을 덮어쓰지 않았는가
- [ ] 실제 전송할 텍스트를 사용자가 확인했는가
## 길이·모델
 
- [ ] Provider가 실제로 제공한 길이 제한을 기준으로 확인했는가
- [ ] 미확인 길이를 추정치로 강제하지 않았는가
- [ ] 길이 초과 때문에 자동 삭제·요약·truncate가 발생하지 않았는가
## Validator
 
- [ ] blocking FAIL이 0개인가
- [ ] 해결되지 않은 REQUIRED source/reference issue가 0개인가
- [ ] REVIEW_REQUIRED 중 제출 차단 범위가 해결됐는가
- [ ] Provider readiness가 확인됐는가
## 잠금·생성
 
- [ ] 생성에 사용할 PromptVersion을 최종 검토했는가
- [ ] 잠긴 과거 버전을 직접 수정하지 않았는가
- [ ] 정확한 에셋·역할·순서·옵션이 생성 시점 snapshot에 들어가는가
---
 
# 28. 빠른 작성용 구조 템플릿
 
아래 템플릿은 **명세의 고정 제목과 순서를 그대로 보여주기 위한 빈 구조**다. 내용은 각 프로젝트와 Source에 따라 작성한다.
 
```text
[PRE_SHOT_CONTINUITY] 이전 숏 연속성
(필요할 때만 사용)
 
[SCENE_CONTEXT] 장면 맥락
 
 
[ACTIVE_REFERENCES] 활성 참조
 
 
[LOCATION_MAP] 공간 지도·위치 관계
 
 
[FIRST_FRAME_AND_SPATIAL_BLOCKING] 첫 프레임 및 공간 블로킹
 
 
[FORMAT_MODE] 영상 형식
 
 
[OPTICS] 렌즈 설정
 
 
[CAMERA] 카메라 설정
 
 
[ACTION_TIMING] 행동 타이밍
 
 
[CHARACTER_ACTING] 인물 연기
 
 
[PHYSICS] 움직임·물리
 
 
[LIGHTING] 조명
 
 
[AUDIO] 음향
 
 
[STYLE] 영상 스타일
 
 
[QUALITY] 퀄리티
 
 
[REQUIRED_AND_FORBIDDEN_CONSTRAINTS] 필수 및 금지 조건
 
Required:
 
Forbidden:
```
 
---
 
# 29. 이 가이드에서 절대 자동화하지 않는 것
 
다음은 작성 편의를 이유로 자동 처리하지 않는다.
 
- 15단계 순서 변경
- 모델별 프롬프트 자동 재작성
- 모델별 자동 요약
- 길이 초과 시 자동 truncate
- 뒤쪽 블록 자동 삭제
- 낮은 우선순위 문장 자동 제거
- AI가 미정 사실 자동 채우기
- AI 질문 option 자동 선택
- semantic search 결과 자동 Source 승격
- 다른 AssetVersion Prompt Memory 자동 적용
- EXACT 문구 자동 수정
- 부정·수량·시간 범위 자동 확대
- 미지원 Continuity 모드의 자동 fallback
- 선택 에셋 자동 제거
- 선택 에셋 역할 자동 교체
- 번역 기능 미구성 상태에서 임의 번역
- stale 번역/API 전송본으로 생성
- 잠긴 PromptVersion 직접 수정
- 오프라인 충돌의 last-write-wins
---
 
# 30. 용어 요약
 
| 용어 | 의미 |
|---|---|
| Prompt | Take에 연결된 현재 프롬프트 편집 상태 |
| PromptVersion | 특정 시점의 15단계 프롬프트 버전 |
| PromptSnapshot | 실제 생성 시점의 불변 프롬프트·입력 사본 |
| PromptBrief | 사용자가 자유롭게 작성하는 장면 설명 |
| PromptBriefVersion | 특정 시점의 Brief 불변 버전 |
| SourceRecord | 프롬프트 사실의 출처 |
| ConstraintRecord | 무엇을 어떤 범위에서 지켜야 하는지 정의한 제약 |
| PromptFragment | Prompt 텍스트의 특정 조각과 Source·Constraint의 연결 |
| PromptMemoryEntry | AssetVersion·context·성과와 연결된 재사용 문구 |
| Phrase | 프로젝트 안에서 저장·추천되는 일반 문장 |
| ContinuityReference | 이전 숏 상태 또는 미디어 연장 참조 |
| ReferenceView | AssetVersion의 특정 각도·ROI·상태 view |
| ReferenceAuthority | 해당 ReferenceView가 통제하는 범위 |
| LocationMap | 공간 내 안정된 객체·위치 관계 |
| SpatialAnchor | 문·가구·출입구·광원 등 안정된 공간 객체 |
| EXACT | 원문을 문자 단위로 보존하는 재사용 모드 |
| SEMANTIC | 사용자가 선택했을 때만 의미 보존 재표현을 허용하는 모드 |
| UNSPECIFIED | 사용자가 확정하지 않은 값 |
| STALE | 현재 원문과 기준이 달라져 갱신·확인이 필요한 번역/API 전송본 |
| Blocking Issue | 해결 전 생성 제출을 허용하지 않는 문제 |
 
---
 
# 31. 원문 근거 범위
 
이 독립 가이드는 다음 프롬프트 작성 관련 계약을 통합한 것이다.
 
- `Production_OS_01` §7 — 15단계 프롬프트
- `Production_OS_01` §8 — 문장·고정 문구·추천
- `Production_OS_01` §9 — 에셋·프리셋·실제 참조 입력
- `Production_OS_03` §53 — Source-Locked 작성 모델
- `Production_OS_03` §54 — 15단계·Continuity·직렬화
- `Production_OS_03` §55 — Reference Authority·시간·좌표·상태
- `Production_OS_03` §56 — Prompt Memory·EXACT·SEMANTIC
- `Production_OS_03` §57 — Prompt Validator
- `Production_OS_03` §58 — Prompt Composer 사용자 흐름
- `Production_OS_08 ... FINAL` §6 — Prompt core, 상속, 저장, 버전, 직렬화, 원문/번역/API 전송본, offline recovery
- `Production_OS_08 ... FINAL` §7 — Phrase 추천·삽입·불변 사용 이력
이 문서는 위 범위의 **사용자 작성·검토·재사용·전송 규칙만 분리한 편집용 가이드**이며, 별도의 새로운 제품 요구사항을 추가하지 않는다.
 
---
---
 
> **여기부터는 비규범 부록이다.** 새로운 제품 요구사항이 아니며, §1~§31의 규칙을 실제로 적용할 때 쓰는 작성 보조다. 규범과 충돌하면 §1~§31이 우선한다.
 
---
 
# 37. 부록 G — 장소·공간 통제와 이 가이드의 접속
 
프로젝트 문서 `location-guide.md` 는 장소를 통제하는 절차를 다룬다. 이 가이드의 **Step 3 `LOCATION_MAP`** 한 칸을 깊게 판 문서이므로, Step 3을 쓸 때 그쪽을 먼저 본다. 접속점만 여기 적는다.
 
- 확정된 장소 레퍼런스는 인물 시트와 같은 자격의 **AssetVersion** 이며, 다시 뽑으면 새 버전이지 덮어쓰기가 아니다.
- Step 2 `ACTIVE_REFERENCES` 에 올릴 때 Authority scope를 적는다.
```text
현재 집 · 장소 · 일반 이미지 참조 · AssetVersion 1 · Authority: GEOMETRY, MATERIALS, ATMOSPHERE
```
 
- **장소 참조는 `FRAMING` 을 통제하지 않는다.** 이 scope를 장소 참조에 붙이면 그 사진의 앵글이 숏의 앵글이 된다. 카메라는 Step 7 `CAMERA` 가 정한다. §8의 scope 분리가 여기서 가장 자주 깨진다.
- `LIGHTING` 은 선택이다. 그 장소의 광원 배치를 그대로 쓸 때만 넣고, 시간대가 다르면 넣지 않는다.
- Step 3 본문에 들어가는 장소 정보는 **좌표 줄 + 네 줄을 넘지 않는다**(`location-guide.md` §3). 장소를 길게 쓰면 Step 2의 인물 참조가 텍스트에 밀린다.
- 인물 위치는 형용사가 아니라 **거리와 접촉**으로 쓴다. §10의 좌표계 규칙과 같은 취지이며, 실제 문장 형태는 `location-guide.md` §4에 있다.
- 시대 표현은 Step 13 `STYLE`의 색보정이 아니라 Step 3의 물건·재질로 쓴다(`film-decisions.md` §1).
- 프롬프트 속 참조 권한 문장(`location-guide.md` §0·§6)은 §8의 Authority scope를 실제 프롬프트 문장으로 옮긴 형태이며, 아무거나 바꿔 쓰면 scope 선언이 무력해진다.
- 장소 자산은 `MASTER / CLEAN / VIEW / PROP / STATE / FIX` 의 부모–자식 계보를 가진다(`location-templates.md` §12). **승인된 자식만 다음 단계의 부모가 된다.**
- 작업별 프롬프트 문법은 `location-templates.md`, 그 근거가 된 실제 프롬프트 20개는 `힉스필드_장소_에셋_실제_프롬프트_모음.md` 에 있다.
---
 
# 38. 부록 H — 광학·카메라 실전 메모
 
Step 6 `OPTICS` 와 Step 7 `CAMERA` 를 실제로 쓸 때 결과가 안정되는 표현 방식만 모았다.
 
## 38.0 이미지와 영상은 렌즈 표기가 다르다
 
아래 38.1~38.4는 **영상 생성**의 규칙이다. 정지 이미지(Nano Banana 계열)의 장비·필름 스톡 표기는
`location-guide.md` §8.1에 있다(근거: `힉스필드_장소_에셋_실제_프롬프트_모음.md` 원문 11).
 
## 38.1 mm 대신 대각 화각(도)
 
생성 모델은 렌즈 메타데이터보다 **관찰 가능한 결과**에 반응한다. mm·조리개·ISO·렌즈 브랜드명은 1차 통제 수단으로 쓰지 않는다. 콘티에는 mm로 적되, 프롬프트에는 화각으로 옮긴다.
 
| 콘티 | 프롬프트 | 성격 | 이 영화에서의 용도 |
|---|---|---|---|
| 24mm | 84° | 광각 | 공간을 보여주는 컷. 시장 통로, 강의실 전경 |
| 28mm | 77° | 준광각 | 좁은 방 전체 |
| 35mm | 63° | 자연광각 | 인물 + 공간. 이 영화의 관찰용 기본 |
| 50mm | 47° | 표준 | 인물 중심 기본. 눈높이의 정직한 거리 |
| 65mm | 약 37° | 준망원 | 원래 표에 없던 값. 풀프레임 대각 43.3mm 기준 계산 |
| 85mm | 29° | 단망원 | 얼굴. 배경이 부드럽게 눌린다 |
| 100mm | 24° | 망원 | 거리를 둔 관찰. 아주 아껴 쓴다 |
| 135mm 이상 | 18° / 8° | 관찰용 망원 | |
 
## 38.2 내용에 따른 렌즈 선택
 
숏의 **내용 종류**가 렌즈를 정한다. 취향이 아니다.
 
- 얼굴 중심: 29°(중간 인물) / 18°(감정 클로즈업) / 84°(공간이 함께 보이는 친밀한 광각)
- 환경 액션: 47°(자연스러운 관찰) / 84°(환경 액션) / 107°(대규모 지리)
- 디테일·인서트: 29° 또는 18°, **별도 비트로 분리**
- 멀리서의 관찰: 8°, 전경 가림(foreground occlusion) 필수
**내용-화각 정합 규칙**: 얼굴 + 환경 지리 + 매크로 디테일을 한 비트에 섞으면 렌즈가 표류한다. 내용 종류가 바뀌면 컷을 나누고 컷마다 렌즈 성격을 따로 지정한다.
 
## 38.3 관찰 가능한 결과를 함께 쓴다
 
화각만 쓰면 모델이 편한 중간값으로 흘러간다. 결과 문장을 붙인다.
 
- 망원: 배경이 압축되어 뭉개진다 / 인물만 선명하다 / 가까운 프레임이 물리적 근접이 아니라 렌즈 거리로 얻어졌다 / 카메라가 물리적으로 멀다 — **3개 이상**
- 광각: 환경이 프레임 끝까지 보인다 / 직선이 직선으로 유지된다 / 카메라가 물리적으로 가깝다 / 망원 압축 없음 — **3개 이상**
## 38.4 드리프트 방지 잠금
 
필요할 때만 쓴다. 숏 안에서 렌즈 성격이 바뀌는 사고를 막는다.
 
```text
이 숏의 어느 프레임도 광각이나 표준 화각이 되지 않는다.
넓은 프레임이 필요하면 렌즈를 바꾸는 것이 아니라 카메라가 더 멀어진다.
배경은 모든 프레임에서 압축된 상태를 유지한다.
```
 
## 38.5 카메라는 물리적 조작으로 쓴다
 
"역동적인 카메라", "영화적인 움직임" 같은 말은 통제가 아니다. 다음을 쓴다.
 
- 렌즈 성격 / 카메라 높이 / 피사체까지의 거리 / 앵글 / 카메라가 선 쪽(180도 선) / 피사체 크기 / 화면 내 배치 / 움직임 / 초점 거동 / 피사계 심도 / 핸드헬드의 질
한 숏에 **복합 카메라 움직임을 겹치지 않는다.** 이 영화는 전 컷 고정·아이레벨이 기본이므로(콘티가 팬·틸트를 명시한 컷만 예외 — 예: C#3 PAN RIGHT, C#4 PAN+FOCUS, C#6 PAN+TILT UP, `film-decisions.md` §2) 이 항목은 대부분 "camera fixed"로 끝난다.
 
## 38.6 컷을 모델에게 맡기지 않는다
 
기본은 **단일 연속 테이크**다. 컷을 나눠야 한다면 컷마다 다음을 전부 지정한다: 길이 / 카메라 / 첫 프레임에 보이는 인물 / 공간 배치 / 동작 / 컷 종류. 지정하지 않은 컷을 모델이 만들게 두지 않는다. 내부 컷 사이에도 화면 방향·시선·조명 방향·인물 위치·의상·소품 상태가 유지되어야 한다(§10, §12와 같은 취지).
 
## 38.7 문맥 격리
 
최종 프롬프트는 **그 숏만의 봉인된 문서**다. 씬 번호, 대본 헤더, 이전 씬 요약, 이 숏에 안 나오는 인물·태그, "앞과 동일", "계속", "이전처럼" 은 넣지 않는다. §5의 상속은 작성자의 도구이지 프롬프트에 찍는 문구가 아니다.
 
## 38.8 밀도 배분
 
프롬프트는 통제가 필요한 곳에서만 촘촘해야 한다. 촘촘히 쓸 곳: 정체성 앵커, 공간 배치, 첫 프레임, 시선. 얇게 쓸 곳: 분위기 형용사, 장르 비유, 문학적 수사. 금지 목록을 길게 붙이는 것보다 **필요한 자리에 짧은 국소 잠금**을 넣는 편이 훨씬 잘 듣는다.
 
---
 
# 39. 부록 I — 연기와 이 가이드의 접속
 
프로젝트 문서 `acting-guide.md` 는 인물의 연기를 설계한다. 이 가이드의 **Step 9 `CHARACTER_ACTING`** 한 칸을 깊게 판 문서다.
 
- 연기 문장은 Step 9에만 쓴다. Step 7 `CAMERA`, Step 11 `LIGHTING`, Step 13 `STYLE` 에 연기를 섞지 않는다.
- 감정 형용사("슬프게", "긴장한")는 Step 9의 내용이 아니다. **관찰 가능한 상태**로 쓴다 — 무엇을 보고 있는가, 어디에 무게가 실려 있는가, 손이 무엇을 하고 있는가, 호흡이 어떤가.
- 인물의 마스터 프로필 문장은 인물 시트의 묘사 문장과 같은 자격의 재사용 자산이다. 재사용 등록하면 `ASSET_PROMPT_EXACT` 가 되고 §15의 보호를 받는다.
- 목소리는 `acting-guide.md` §9대로 고정한다. 연기 지시가 대사 문구를 바꾸지 않는다.
- 상태(state)를 쓰고 전환(transition)을 쓰지 않는다. "점점 무너진다"는 생성 단위 안에서 통제되지 않는다. 시작 상태와 끝 상태를 각각 고정하고, 그 사이는 생성 단위를 나눈다(§9의 시간 범위 규칙).
---
 
# 40. 부록 K — 실제 생성 기록에서 확인된 작성 패턴
 
다른 작품 The Prompter 씬 1(Higgsfield Seedance 2.5 영상 66개)을 고쳐 가며 만든 기록에서 확인된 것만 모았다. 영상 번호와 근거는 `the-prompter-씬1-분석.md`에 있다. 규범 §1~§31, `film-decisions.md`의 확정 사항과 어긋나면 그쪽이 이긴다. (40.1 — 이 가이드에 이미 있는 규칙의 재확인 목록 — 은 2026-09-25 정리 때 뺐다.)
 
## 40.2 Step별로 새로 확인된 문장
 
| Step | 이럴 때 | 쓰는 문장 | 근거(분석 문서) |
|---|---|---|---|
| 2 `ACTIVE_REFERENCES` | 한 생성 안에서 같은 인물의 상태가 바뀐다 | 두 요소를 함께 붙이고 시간을 나눈다: "[요소 A]는 [수건을 쓴 동안], [요소 B]는 [0:09부터]" (§9) | §4.2 |
| 2 | 참조가 특정 영역·시간에만 나와야 한다 | "[요소]는 [거울 안]에서만, [시작~끝]에만 나타난다" | §3·§5.3 |
| 2 | 음성 참조가 둘 이상이다 | 붙인 순서대로 audio_1·audio_2로 부르고, 인물 줄 끝에 "목소리는 audio_N과 같다"를 붙인다. 그 작품의 사용 방식이며 Higgsfield 문서로 확인한 것은 아니다 | §4.4 |
| 2 | 요소 이미지를 바꿨다 | 그 요소의 설명문을 새 이미지에 맞게 다시 쓴다 — `location-guide.md` §6 | §5.5 |
| 2 | 소품이 손을 바꾸거나 모양이 변한다 | 소품 요소를 붙이고 "[어느 손] · 내려놓지 않음"을 적는다. 손은 `오른손`·"화면 오른쪽 손"이 아니라 화면 속 물건으로 가리킨다(예: 신발장 쪽 손 — `film-decisions.md` §8) | §4.3 |
| 3 `LOCATION_MAP` | 한 생성 안에 카메라 위치가 둘 이상이다 | 카메라마다 고정 물건이 화면 어느 쪽에 오는지 적는다 — `location-guide.md` §3.2 | §5.4 |
| 3 | 거울·유리 같은 반사면이 있다 | 비치는 것과 비치지 않는 것을 적는다 — `location-guide.md` §3.3. §11의 반사 수 구분과 함께 | §5.5 |
| 4 `FIRST_FRAME_AND_SPATIAL_BLOCKING` | 인물이 문을 열고 들어오며 시작한다 | 첫 프레임에 이미 동작 중으로 쓴다(이미 걷는 중, 문은 뒤에서 닫히는 중) | §5.5 |
| 5·8 | 컷 너머에서 인물이 사라진다 | 컷을 동작 중간(걷는 도중)에 건다. 그래도 안 되면 컷을 없앤다 | §5.2 |
| 9 `CHARACTER_ACTING` | 감정 범위, 도는 동작, 말하지 않는 입, 멈춤, 배경 인물 | `acting-guide.md` §17 | §5.1·§5.2·§5.3 |
| 15 | 나오면 안 되는 결과가 있다 | 원하는 상태를 먼저 쓰고 실패를 결과로 적는다: "[원하는 상태]. [나오면 안 되는 결과] = 실패 테이크" | §3 |
 
## 40.3 `DIRECT_MEDIA_EXTENSION`을 쓸 경우 (§3.2)
 
이 영화는 두 번에 나눠 생성하는 컷을 `start_image`로 잇기로 확정했다(`film-decisions.md` §3). 아래는 연장 모드를 쓸 일이 생길 때만 참고한다.
 
- 첫 프레임: "직전 영상의 마지막 프레임과 다른 새 프레이밍으로 시작한다. 직전 프레이밍을 반복하지 않는다." (그 작품의 연장 42개 중 39개)
- 참조 요소는 연장할 때도 전부 다시 붙인다. 이전 영상은 위치·자세·빛 같은 상태만 넘긴다.
- Higgsfield Seedance 2.5 Extend의 결과는 원본이 21:9여도 16:9 1280×720이었다.
- 앞 생성을 다시 만들면 뒤 생성의 프롬프트는 그대로 두고 원본 영상만 바꿔 다시 돌린다.
## 40.4 프롬프트 길이
 
`film-decisions.md` §8은 "영상 프롬프트는 짧게 쓴다"로 확정돼 있다. 그 작품의 기록은 이것을 뒤집지도 뒷받침하지도 않는다.
 
- 평균 10,224자(우리 C#2의 두 배쯤)였고, 고칠수록 길어졌다(최대 16,566자). 그래도 핵심 샷마다 5~10번 생성했다.
- 풀린 판은 대개 한 생성에 넣는 사건(컷·동작·요소·대사 수)을 줄인 판이었다. 리빌 한 곳은 반대로 지시를 더 적어서 풀렸다.
- 그래서 글자 수보다 **한 생성에 넣는 사건 수**를 먼저 본다. 38.8(밀도 배분), §4 Step 15(숏 분리)와 같은 방향이다.
---
 
# 41. 부록 J — 문서 이력
 
| 날짜 | 변경 |
|---|---|
| 2026-09-23 | §1~§31 전문을 프로젝트 문서로 확정. 부록 §32~§37 추가. |
| 2026-09-23 | 부록 G·H·I 추가. 부록 F → 부록 J. |
| 2026-09-24 | 부록 G·H·I의 Step 번호·이름을 규범 §4에 맞춤. |
| 2026-09-25 | 부록 K 추가(근거 `the-prompter-씬1-분석.md`). 부록 J → §41. |
| 2026-09-25 | 정리: 부록 A–E 삭제, 부록 H 렌즈 표 통합, 상호참조 수정, 40.1 삭제. 규범 §1~§31 변경 없음. |
 
부록을 고칠 때도 §1~§31은 건드리지 않는다. 규범을 바꿔야 한다면 원 명세(`Production_OS_01`, `Production_OS_03`, `Production_OS_08 ... FINAL`)를 먼저 개정하고, 그 결과를 이 문서에 반영한다.