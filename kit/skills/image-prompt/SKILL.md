---
name: image-prompt
description: AI 이미지 생성·편집 프롬프트를 쓰거나 고칠 때 쓴다. GPT Image, Nano Banana, Seedream에 해당한다. 대상은 에셋 제작과 영상 시작용 퍼스트 프레임이다. 에셋은 장소, 소품, 인물+의상 시트, 그림체 이미지다. 공통 규칙은 이 파일에 있다. 신규와 편집의 구분, 참조 권한, 편집 문법, 크롭이다. 종류별 규칙과 빈 틀은 따로 있는 파일을 그 종류일 때만 읽는다.
---

# 이미지 프롬프트 — 공통

근거:
- 「어머니와 고등어」 인물·장소 작업
- The Prompter 장소 원문 20개
- 나부코 수채 배경 (약 240장)

## 읽을 파일 — 이 파일 + 해당하는 것 하나

| 만드는 것 | 파일 |
|---|---|
| 인물 + 의상 시트 (신규, 의상·헤어 수정, 파생) | `character.md` |
| 장소 (마스터, 새 시점, 상태·소품 편집) | `location.md` |
| 소품 에셋 | `prop.md` |
| 그림체 이미지 (수채·일러스트) | `style.md` |
| 퍼스트 프레임 (장소 + 인물 + 소품 → 영상 0:00) | `first-frame.md` |

**고칠 때는 빈 틀을 다시 읽지 않는다.**
1. 확정 프롬프트를 가져온다. Higgsfield에서는 `get_project_asset_prompt`로 그 job의 프롬프트를 받는다.
2. 실패 증상에 해당하는 규칙만 찾는다.
3. 바뀐 줄만 "전 → 후"로 보인다.

## 1. 쓰기 전에 세 가지를 판별한다

**① 신규인가, 편집인가.**
- 마음에 드는 얼굴이나 장소가 한 번 나오면 다시 신규로 만들지 않는다. 신규로 다시 돌리면 다른 사람, 다른 방이 된다.
- 그 결과를 참조로 물려 편집한다.

**② 카메라를 유지하는가.**

| 모드 | 언제 | 여는 문장 |
|---|---|---|
| `LOCKED EDIT` | 같은 사진의 수정본(소품 하나, 상태 하나, 하늘만) | `Edit <<<image_1>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with one change only.` |
| `DERIVED VIEW` | 같은 장소의 새 시점 | `Using <<<image_1>>> as the exact same location, generate a new view from [위치], looking [방향]. Do not inherit its camera angle, framing or composition.` |

둘을 한 프롬프트에 섞으면 모델이 중간값으로 타협한다. 현관 한 컷에 열 번 넘게 돈 원인이 이것이었다.

**③ 참조가 무엇을 통제하는가.** "참고해"라고만 쓰지 않는다.

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
- <<<B>>> controls only the woman's face, hair and wardrobe.
- <<<C>>> controls only the bag's shape, material and state.
DO NOT TRANSFER:
- From <<<B>>>: the studio backdrop, its lighting, its framing or its pose.
- From <<<C>>>: its background, surface or camera angle.
PRIORITY: If the references conflict, <<<A>>> controls the space and the light; the character
reference controls identity and wardrobe only. Camera and shot size are defined below and override every reference.
```

- **카메라를 통제하는 참조는 하나 이하로 둔다.**
- **참조 표기를 통일한다.** `<<<image_1>>>`, `<<<UUID>>>` 같은 표기는 실제 첨부 순서와 맞추고, 한 프롬프트 안에서 한 가지만 쓴다.
- **"구도만 참조"라고만 쓰면 구도가 따라오지 않는다.** 실제로 전혀 다른 대칭 구도가 나왔다. 둘 중 하나로 쓴다.
  - 참조를 덩어리별 좌표로 읽어 적는다.
  - "그대로 재현할 그림"으로 지정하고, 바꿀 것만 목록으로 쓴다.
- **"그대로 재현"이면 다른 속성까지 따라온다.** 실제로 파란 하늘까지 따라왔다. 속성마다 참조를 나눈다: `Reference 1 gives the composition; take the sky only from reference 2.`
- **요소 이미지를 바꾸면 프롬프트 속 설명문도 새 이미지에 맞게 고친다.**
- **콘티 썸네일과 모니터 촬영 사진은 참조로 붙이지 않는다.** 그 사진의 얼굴, 옷, 색이 섞인다.

## 3. 편집 문법 — CHANGE / PRESERVE EXACTLY / ONLY CHANGE

```text
[LOCKED EDIT 여는 문장]
CHANGE — [대상과 위치(화면 기준)]: Change [현재 상태] to [새 상태]. Keep its position, scale
and orientation locked. [국소 빛·접촉.]
PRESERVE EXACTLY:
- Camera position, height, angle, lens, framing, horizon line, vanishing point and perspective
- The architecture: [walls, doors, windows, ceiling, floor]
- Every unnamed object in its exact position, scale, orientation, material and colour
- Existing light sources, shadows, exposure and reflections; colour grade, contrast, grain, depth of field
ONLY CHANGE: [CHANGE와 같은 항목]. Everything else remains 100% identical.
```

- **보존 목록을 변경보다 구체적으로 쓴다.** 실제로 "디테일만 올려"에 밝기, 식생 개수, 빛줄기까지 바뀌었다.
- **CHANGE와 ONLY CHANGE에는 같은 항목을 적는다.** 어긋나면 반쯤만 그린다.
- **한 생성에 한 가지만 바꾼다.**
- **사소하고 명확한 변경은 짧게 써도 된다.** Seedream·Nano Banana에서는 짧은 한국어 지시("식탁을 90도 돌려서 의자가 주방 쪽을 보게")가 잘 들었다.

## 4. 화면비·크롭·가림 구역

1. **최종 상영 화면부터 계산한다.** 예: 21:9를 4094×940으로 쓰면 위에서 23~77%만 보인다. 핵심 요소는 그 띠 안에 둔다.
2. **가림 구역(합창단, 자막)은 "주요한 것을 거기에만 두지 않는 곳"이다.** 가려져도 되는 부수 요소만 둔다.
3. **부감 각도를 높이면 하늘과 먼 대상이 띠 위로 밀려난다.** 그것들이 띠 안에 보여야 하면 각도를 낮춘다(약 30도).
4. **% 좌표와 밝기 숫자는 대략만 지켜진다.** 23개 좌표를 줘도 1% 단위로는 따르지 않았다.
   - 구역 단위(왼쪽 1/3, 위 가운데)로 쓴다.
   - 정확해야 하면 배치 스케치(색 블록)를 참조로 쓰고 "배치만 따르라"고 쓴다.

## 5. 모델 메모

| 모델 | 메모 |
|---|---|
| GPT Image 2.5 | 21:9를 지원한다. 요소를 많이 지정하면 질감이 3D 렌더 쪽으로 돈다. 그럴 때는 요소를 줄이거나 질감 문단을 앞에 둔다. 12,000자 프롬프트는 뒤쪽 금지문이 약해졌다. 반복을 지워 5,000자로 줄여도 결과는 유지됐다 |
| Nano Banana Pro | 인물 시트와 장소 편집의 주력이다. 요청과 다른 모델로 처리될 수 있다(pro 요청 → 2 처리). 확정 전에 실제 처리 모델을 기록한다 |
| Seedream 5.0 Pro | 짧은 한국어 편집 지시가 잘 들었다 |
| 업스케일 | 수채·필름 질감을 지운다. 쓰기 전에 묻는다 |

## 6. 보내기 전 점검 (공통)

- [ ] 신규인지 편집인지, LOCKED인지 DERIVED인지가 첫 문장에서 분명한가
- [ ] 참조마다 권한, 가져오지 않을 것, 충돌 우선순위를 적었는가
- [ ] 변경이 한 가지이고, CHANGE와 ONLY CHANGE가 같은가. 보존 목록이 더 구체적인가
- [ ] 편집에서 얼굴이나 장소를 다시 묘사하지 않았는가
- [ ] 인물·의상·장소 설명문이 에셋 대장과 글자까지 같은가
- [ ] 크롭 띠와 가림 구역 안에서 핵심 요소의 위치를 확인했는가
- [ ] 해상도가 확인용(1k)인가
- [ ] 저장 폴더가 정해졌는가
