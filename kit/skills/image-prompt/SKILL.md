---
name: image-prompt
description: AI 이미지 생성·편집 프롬프트를 쓰거나 고칠 때 쓴다. GPT Image, Nano Banana, Seedream에 해당한다. 대상은 에셋 제작과 영상 시작용 퍼스트 프레임이다. 에셋은 장소, 소품, 인물+의상 시트, 그림체 이미지다. 공통 규칙은 이 파일에 있다. 신규와 편집의 구분, 참조 권한, 편집 문법, 크롭이다. 종류별 규칙과 빈 틀은 따로 있는 파일을 그 종류일 때만 읽는다.
---

# 이미지 프롬프트 — 공통

## 단계 파일 — 하나만 연다

`character.md` 인물 + 의상 시트 · `location.md` 장소(그 안의 표가 `location-view.md` 새 시점 / `location-edit.md` 같은 사진 수정 중 하나를 더 가리킨다) · `prop.md` 소품 · `style.md` 그림체 이미지 · `first-frame.md` 퍼스트 프레임(영상 0:00)

## 0. 쓰기 전 정보 점검

그 종류 파일의 "필요한 정보" 표와 아래 공통 표를 채운다.

| 공통 | 필요한 정보 |
|---|---|
| 형식 | 모델, 해상도(확인용), 화면비, 장 수(1) |
| 저장 | 저장 폴더(`folder_id`) |
| 참조 | 붙일 이미지 job과 붙이는 순서, 각각의 역할 |
| 모드 | 신규 / 편집, 카메라 유지 여부(§1) |

묻는 법은 지침 4번이다.

**참조 태그:** 틀의 `<<<LOC>>>`, `<<<CHAR>>>`, `<<<PROP>>>`, `<<<OK>>>`, `<<<A>>>`는 자리표시다. 실제 요소 이름(`loc_…_v1`)이나 첨부 순서 이름(`image_1`)으로 바꾼다. 참조 수 = 태그 수 = 붙이는 이미지 수.

**고정 설명문이 이 컷과 부딪치면**(빈 장소용 "no cars"인데 버스가 나오는 컷) 문장은 고치지 않는다. 그 문장 바로 뒤(틀의 `[Except: …]` 자리)에 `Except: [이 컷에만 있는 것].` 한 줄을 붙인다.

## 1. 쓰기 전 판별

**① 신규인가, 편집인가.** 마음에 드는 결과가 한 번 나오면 다시 신규로 만들지 않는다. 신규로 다시 만들면 다른 사람, 다른 방이 된다. 그 결과를 참조로 물려 편집한다.

**② 카메라를 유지하는가.** 두 모드를 한 프롬프트에 섞지 않는다. 섞으면 중간값으로 타협한다. `WITHOUT reframing`과 반대 방향·회전(`reverse`, `rotate 180`, `turned round`)을 한 프롬프트에 쓰면 모순이다.

| 모드 | 언제 | 여는 문장 |
|---|---|---|
| `LOCKED EDIT` | 같은 사진의 수정본 | `Edit <<<image_1>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with one change only.` |
| `DERIVED VIEW` | 같은 장소의 새 시점 | `Using <<<image_1>>> as the exact same location, generate a new view from [위치], looking [방향]. Do not inherit its camera angle, framing or composition.` |

**③ 참조가 무엇을 통제하는가.**

| 권한 | 영어 | 통제 범위 |
|---|---|---|
| 같은 사진 | `the exact same photograph` | 카메라·프레이밍·기하까지 |
| 같은 장소 | `the exact same room / location` | 장소 정체성(새 시점 허용) |
| 재료 체계 | `the same building's material register` | 재료·창호·조명 태도 |
| 배치만 | `only for the LAYOUT` | 문·창·가구의 상대 위치 |
| 요소만 | `only for [element]` | 명명한 요소 하나 |

## 2. 참조가 둘 이상일 때 — 권한 블록

```text
REFERENCE AUTHORITY:
- <<<A>>> is the exact same location. It controls geography, materials, landmarks and light direction.
- <<<B>>> controls only [person]'s face, hair and wardrobe.
- <<<C>>> controls only [prop]'s shape, material and state.
DO NOT TRANSFER:
- From <<<B>>>: the backdrop, its lighting, its framing or its pose.
- From <<<C>>>: its background, surface or camera angle.
PRIORITY: If the references conflict, <<<A>>> controls the space and the light; the character
reference controls identity and wardrobe only. Camera and shot size are defined below and override every reference.
```

- 마지막 줄은 LOCKED EDIT이면 `Preserve <<<A>>>'s camera, geometry and placement.`로 바꾼다. 카메라를 갖는 참조는 그 사진 하나뿐이다.

- **카메라를 통제하는 참조는 하나 이하로 둔다.**
- **참조 표기를 통일한다.** 실제 첨부 순서와 맞추고, 한 프롬프트 안에서 한 표기만 쓴다.
- **"구도만 참조"로는 구도가 따라오지 않는다.** 둘 중 하나로 쓴다.
  - 참조를 덩어리별 좌표로 읽어 적는다.
  - "그대로 재현 + 바꿀 것 목록"으로 쓴다.
- **"그대로 재현"이면 다른 속성까지 따라온다.** 속성마다 참조를 나눈다: `Reference 1 gives the composition; take the [sky] only from reference 2.`
- **요소 이미지를 바꾸면 프롬프트 속 설명문도 새 이미지에 맞게 고친다.**
- **콘티 썸네일이나 모니터 촬영 사진은 참조로 붙이지 않는다.** 얼굴·옷·색이 섞인다.

## 3. 편집 문법 — CHANGE / PRESERVE EXACTLY / ONLY CHANGE

```text
[LOCKED EDIT 여는 문장]
CHANGE — [대상과 위치(화면 기준)]: Change [현재 상태] to [새 상태]. Keep its [position / scale /
orientation — only what this edit does not change] locked. [국소 빛·접촉.]
PRESERVE EXACTLY:
- Camera position, height, angle, lens, framing, horizon line, vanishing point and perspective
- The architecture: [walls, doors, windows, ceiling, floor]
- Every unnamed object in its exact position, scale, orientation, material and colour
- Existing light sources, shadows, exposure and reflections; colour grade, contrast, grain, depth of field
ONLY CHANGE: [CHANGE와 같은 항목]. Everything else remains 100% identical.
```

- **보존 목록을 변경보다 구체적으로 쓴다.** 그러지 않으면 나머지도 조금씩 새로 그린다.
- **CHANGE와 ONLY CHANGE의 항목을 같게 한다.**
- **사소하고 명확한 변경은 짧은 지시로도 된다.** Seedream·Nano Banana는 짧은 한국어 지시도 잘 따랐다.

## 4. 크롭과 가림 구역

- **최종 상영 비율에서 보이는 띠를 먼저 계산한다.** 핵심 요소는 그 띠 안에 둔다.
- **가림 구역(자막, 출연자)에는 주요 피사체를 두지 않는다.** 가려져도 되는 부수 요소만 둔다.
- **부감 각도를 높이면 하늘과 먼 대상이 띠 밖으로 밀려난다.** 그것들이 보여야 하면 각도를 낮춘다.
- **% 좌표와 숫자는 대략만 지켜진다.** 구역 단위(왼쪽 1/3, 위 가운데)로 쓴다. 정확해야 하면 배치 스케치(색 블록)를 참조로 쓰고 "배치만 따르라"고 쓴다.

## 5. 모델 메모

| 모델 | 메모 |
|---|---|
| GPT Image 2.5 | 요소를 많이 지정하면 질감이 3D 렌더 쪽으로 돈다. 요소를 줄이거나 질감 문단을 앞에 둔다 |
| Nano Banana Pro | 요청과 다른 모델로 처리될 수 있다. 확정 전에 실제 처리 모델을 기록한다 |

## 6. 보내기 전 점검 (검사 스크립트가 잡지 못하는 것)

- [ ] 참조마다 권한, 가져오지 않을 것, 충돌 우선순위를 적었는가
- [ ] 변경은 한 가지이고, 보존 목록이 더 구체적인가
- [ ] 편집에서 얼굴이나 장소를 다시 묘사하지 않았는가
- [ ] 고정 설명문이 에셋 대장과 글자까지 같은가
- [ ] 크롭 띠와 가림 구역을 확인했는가
- [ ] 자리표시 태그(`<<<LOC>>>` 등)가 남지 않았는가
- [ ] 보이기 전에 검사 스크립트를 돌렸는가. 프롬프트를 파일로 저장하고 `higgsfield-generation` 스킬 폴더의 `check_prompt.py`를 `python3 check_prompt.py --kind image 파일 --refs 태그수 [--must-include 고정문장파일]`로 돌린다(그 스킬을 열 필요는 없다). FAIL은 고친다. WARN은 고치거나 남길 이유를 검사 출력의 숫자와 함께 한 줄 적는다. 코드 실행이 안 되면 그렇다고 적는다
