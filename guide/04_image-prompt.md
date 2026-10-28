# 04 이미지 프롬프트 가이드 — 인물 시트 · 장소 · 소품 · 그림체 · 퍼스트 프레임

근거: 「어머니와 고등어」 인물·장소 가이드(Nano Banana Pro·GPT Image·Seedream), The Prompter 장소 원문 20개, 나부코 수채 배경(GPT Image 2.5, 이미지 약 240장). 빈 틀은 `templates/image-prompts.md`.

---

## 0. 프롬프트를 쓰기 전 세 가지 판별

**① 신규 생성인가, 편집인가.** 마음에 드는 얼굴·장소가 한 번 나오면 다시 신규 생성하지 않는다. 그 결과를 참조로 물려 편집한다. 신규를 다시 돌리면 다른 사람·다른 방이 된다.

**② 카메라를 유지하는가.**

| 모드 | 언제 | 여는 문장 |
|---|---|---|
| `LOCKED EDIT` | 같은 사진의 수정본(소품 하나, 상태 하나, 하늘만) | `Edit <<<image_1>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with one change only.` |
| `DERIVED VIEW` | 같은 장소의 새 시점(반대 방향, 클로즈업, 부감) | `Using <<<image_1>>> as the exact same location, generate a new view from [위치], looking [방향]. Do not inherit its camera angle, framing or composition.` |

둘을 한 프롬프트에 섞으면 모델이 중간값으로 타협한다(현관 한 컷에 열 번 넘게 돈 원인). DERIVED VIEW에는 `WITHOUT reframing`을 쓰지 않는다. 새 방향이면 `This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.`를 붙인다.

**③ 참조가 무엇을 통제하는가 — 다섯 단계.** "참고해"라고 쓰지 않는다.

| 권한 | 영어 표현 | 통제 범위 |
|---|---|---|
| 같은 사진 | `the exact same photograph` | 카메라·프레이밍·기하까지 |
| 같은 장소 | `the exact same room / location` | 장소 정체성(새 시점 허용) |
| 재료 체계 | `the same building's material register` | 재료·창호·조명 태도만 |
| 배치만 | `only for the LAYOUT` | 문·창·가구의 상대 위치만 |
| 요소만 | `only for [element]` | 명명한 요소 하나 |

---

## 1. 참조가 둘 이상일 때 — 권한 블록

```text
REFERENCE AUTHORITY:
- <<<A>>> is the exact same location. It controls geography, materials, landmarks and light direction.
- <<<B>>> controls only the woman's face, hair and wardrobe.
- <<<C>>> controls only the bag's shape, material and state.
DO NOT TRANSFER:
- From <<<B>>>: the studio backdrop, its lighting, its framing or its pose.
- From <<<C>>>: its background, surface or camera angle.
PRIORITY:
If the references conflict, <<<A>>> controls the space and the light; the character reference
controls identity and wardrobe only. Camera and shot size are defined below and override every reference.
```

- 카메라를 통제하는 참조는 하나 이하. 컷 생성은 보통 **어느 참조도 카메라를 갖지 않고** CAMERA 블록이 정한다.
- 인물과 장소가 충돌하면 얼굴·의상·체형은 인물이 이긴다. 조명·공간은 장소가 이긴다(인물 시트의 스튜디오 조명이 따라오면 안 된다).
- 참조 표기(`<<<image_1>>>`, `Reference image 2`, `<<<UUID>>>`)는 실제 첨부 순서에 맞추고 한 프롬프트 안에서 하나로 통일한다.
- **"구도만 참조"라고만 쓰면 구도가 안 따라온다**(E-20). 구도를 가져오려면 ① 참조에 10% 눈금을 대고 덩어리마다 좌표를 읽어 적거나 ② 그 이미지를 "그대로 재현할 그림"으로 지정하고 **바꿀 것만 목록**으로 쓴다.
- **"그대로 재현"으로 쓰면 그 이미지의 다른 속성도 따라온다**(하늘색 등). 일부만 원하면 그 속성만 다른 참조에서 가져온다고 쓴다: `Reference 1 gives the composition; take the sky only from reference 2.`(E-45)
- 모니터를 찍은 사진은 참조로 쓰지 않는다. 원본 파일을 받는다(E-21).
- 요소 이미지를 바꾸면 프롬프트 속 그 요소의 설명문도 새 이미지에 맞게 고친다(E-33).

---

## 2. 편집 문법 — CHANGE / PRESERVE EXACTLY / ONLY CHANGE

```text
[LOCKED EDIT 여는 문장]

CHANGE — [대상과 위치(화면 기준)]:
Change [현재 상태] to [새 상태]. Keep its [position / scale / orientation] locked. [국소 빛·접촉.]

PRESERVE EXACTLY:
- Camera position, height, angle, lens, framing, horizon line, vanishing point and perspective
- The room's architecture: [walls, doors, windows, ceiling, floor]
- Every unnamed object in its exact position, scale, orientation, material and colour
- Existing light sources, shadows, exposure and reflections
- Colour grade, contrast, grain and depth of field

ONLY CHANGE: [CHANGE와 같은 항목]. Everything else remains 100% identical.
```

- **보존을 변경보다 구체적으로.** 바꿀 것만 적으면 나머지도 조금씩 새로 그린다.
- CHANGE 목록 == ONLY CHANGE 목록. 어긋나면 반쯤 그린다(재킷이 반만 그려진 사고).
- 한 생성 = 한 가지. 시대를 바꿀 때도 층마다(표지 → 표면 → 문·창 → 가구 → 조명 → 화질) 한 생성씩.
- 사물 작업 공식: ROTATE(제자리 회전, 위치 잠금) / STATE(켜짐·열림, 형태 잠금) / ADD(기존 앵커에) / REMOVE(드러날 표면 지정 + `no residual shadow, indentation, fragment or duplicate`).
- 바뀐 광원이 방을 밝히면: `lit but does NOT glow: no halo, no bloom, no light spilling onto [surfaces]`.
- 짧은 편집 지시가 잘 들은 경우도 있다(Seedream/Nano Banana: "식탁을 90도 돌려서 의자가 주방 쪽을 보게, 왼쪽 벽에 붙여"). 변경이 사소하고 명확할 때만 짧게 쓴다.

---

## 3. 인물 시트 (얼굴·의상 고정용)

**규격(바꾸지 않는다)**: 16:9 가로 한 장, 세로 3분할(왼쪽 목 아래 정면 전신 · 가운데 후면 전신 · 오른쪽 가슴 위 정면 클로즈업), 같은 배경·같은 조명. 한 작품 안에서 모든 인물 시트 규격을 같게.

**신규 생성 정보 순서**: 결과물 종류 → 인물 정체성(나이·출신·피부·얼굴 구조) → 패널 레이아웃 → 체형 → 의상(겉옷→여밈→칼라→안쪽→하의→신발→허용 소품→금지 소품) → 헤어(길이·질감·가르마·뒷모습·색) → 배경·조명 → 일관성 잠금 → 금지.

꼭 넣는 문장
```text
The three panels must depict one and the same person: identical face, age, skin tone, body
proportions, hair color, outfit materials and color. Do not create three similar models.

visible fine skin texture with natural pores, age spots, fine lines, subtle asymmetries and uneven
skin tone, no digital smoothing, no beauty filter, no AI-airbrushed look, matte natural complexion

eyes have genuine moisture and a small specular catchlight, the gaze has a definite focal distance
rather than staring blankly at the lens, one eyelid sits very slightly lower than the other, the iris
shows real fibrous texture and a soft pupil edge
```

- 왼쪽 패널 머리 없음: `intentionally HEADLESS … This is an editorial clothing crop, not an injury: no head, no face, no wound` (안 쓰면 상해 이미지). 고스트 마네킹이면 `hollow ghost-mannequin, invisible person, empty collar` (`mannequin`만 쓰면 플라스틱 마네킹).
- 직업 소품이 저절로 생긴다 → `No profession-signaling props unless explicitly requested`(E-42).
- **수정할 때 얼굴을 다시 묘사하지 않는다.** 얼굴은 보존 지시만: `Change the hair around the existing face; do not regenerate, reinterpret, beautify, age or reshape the face.`
- 여는 문장에 `including the intentionally HEADLESS left panel`, 헤어는 `only in the center and right panels`, 옛 의상은 이름으로 `GONE … Do not layer, merge or hybridize old and new clothing.`
- 파생(외출복, 젊은 시절)은 항상 ★확정본에서 갈라낸다. 파생의 파생을 만들지 않는다. 파일명 끝에 job ID 앞 8자리.
- 영상 요소로 쓸 때 **의상·헤어 상태마다 요소를 따로** 만든다(`char_<인물>_<상태>_v1`). 한 영상 안에서 상태가 바뀌면 두 요소를 붙이고 시간을 나눈다.
- 컷 생성에 물릴 때: `Use the person in reference image 1. Same face, same bone structure, same hair, same wardrobe. Change only the pose, framing, location and lighting.` 의상 문장은 에셋 대장 문장을 글자 그대로.

---

## 4. 장소

**장소는 컷의 속성이 아니라 영화의 자산이다.** 새 축이 필요하면 프롬프트로 카메라를 돌리지 말고 **뷰를 하나 더 확정**한다. 뷰는 축이 바뀔 때만 늘린다(같은 방향에서 더 가깝게·인물 위치만 다름 = 같은 뷰).

계보: `MASTER`(정본) → `VIEW`(카메라 변경, DERIVED) / `PROP`(소품 확대) / `STATE`(빛·점유·소품 상태, LOCKED) / `FIX`(오류 제거, LOCKED). **승인된 자식만 다음 부모가 된다. 자식끼리 물리지 않는다.** 형제 뷰는 부모 프롬프트에서 CAMERA·전중후경 블록만 바꾸고 나머지는 글자까지 같게.

**빈 공간 마스터의 블록 순서**: 참조·권한 + 생성 선언 → 카메라·구도 → **지배 요소**(가장 먼저 눈에 들어오는 것 하나) → 방향별 벽(`At the FAR END` / `The RIGHT wall` / `At the LEFT`, 기준 시점을 괄호로) → 바닥·천장·광원 → `Nothing else: no …`(물건 목록 닫기) → `Empty deserted [place], still air.` → 팔레트 → 재질 증거 → 광원 논리 한 문장 → 촬영 마감 → 시대 잠금 → (레퍼런스판만) 구도 마감.

```text
Palette of roughly 80% [주조 — 항목] — 15% [보조] — 5% [악센트].
Real material truth: [재질 증거]. Real aged surfaces: [마모의 위치까지 — scuffs at chair height …].
[광원 논리: Pendant over the table as the only key; the kitchen is never cooler than the room.]
[시대 잠금: Early autumn 1980, South Korea. Nothing more recent anywhere in frame.]
Hand-lettered signage, text not legible. No legible text anywhere.
```

- **시대는 색이 아니라 물건·재질·글자·마감으로.** 과거를 노랗게·세피아로 만들지 않는다. 과거판은 필름 그레인, 현재판은 없음으로 질감을 가른다(E-37).
- 정지 이미지는 장비·필름 스톡이 룩 프리셋처럼 작동한다(예: `ARRI Alexa LF, Cooke S4 35mm, Kodak Vision3 500T 5219`). 영상은 장비명을 듣지 않는다 → 화각(도).
- 축이 긴 공간(복도·플랫폼)은 `Rule of thirds`를 빼고 소실점 위치를 직접 쓴다.
- 인물 위치는 거리와 접촉으로: "식탁에서 1미터 안, 한 손이 식탁 모서리에 닿아 있다". "근처에"는 안 지켜진다.
- 다른 장소로 문장을 옮기면 명사가 샌다 → 광원·재질·가구 명사를 한 줄씩 검사(E-43).
- 형태가 자꾸 틀리는 물건은 화면에 투영된 모양으로: `reads as a TALL NARROW RECTANGLE`, `its bottom sags lower than its handles`.
- 군중·행인은 얼굴 없이: `seen from behind … no faces visible anywhere`.

---

## 5. 소품

- 이야기에서 상태·손·크기가 바뀌는 소품은 **독립 에셋**으로 만든다: 무배경 회색 스튜디오, 소품만, `nothing else in frame — no hands, no people`, 사용감(`small scratches from daily use`).
- **크기는 소품 에셋이 아니라 장면에서 정한다.** 흰 배경에 선 봉지 셋을 참조로 쓰자 봉지가 인물 상체만큼 커졌다 → 실제 장면 프레임에서 잘라 만든 요소로 교체해 해결(E-18). 크기를 cm와 신체 기준(무릎 위, 허벅지 폭)으로 함께 적는다.
- 물성은 무게로 쓴다: "두 마리 무게로 아래가 처진다. 공기로 부풀지 않는다. 각이 서지 않는다."
- 상태 머신을 컷 사이에 표로 관리한다(묶임 → 풀림 → 들고 감).

---

## 6. 그림체(스타일) 이미지 — 수채·일러스트 계열

나부코 수채 배경에서 정착한 방식.

```text
Reference images: the first is [기준 컷] and sets the painting style above all ([기법 요약]);
the second, third and fourth are further style paintings of the same kind. Take only technique,
brushwork and paper texture from these four, never their subjects, colors or composition.
The fifth is [색 기준 컷]: take only its colors, light and mood, never its landscape and never its
direction of light.
```

- 그림체 참조는 "기법만, 내용·색·구도 금지"를 반드시 명시한다. 아침 이미지 참조에서 버드나무·새·언덕이 섞인 기록이 있다.
- 표면이 돌 무늬·타일로 읽히면: 벽·지붕은 `large, smooth, softly mottled plaster washes laid with a wide wet brush`로 범위를 지정한다.
- 디테일을 올리라는 요청에 식생·밝기·빛까지 바뀌었다 → 참조 하나만 넣고 "그대로 다시 그리되 존재하는 표면의 붓터치만 더 곱게. 식생 늘리지 않음, 빛줄기 약해지지 않음, 밝기 그대로"(E-04).
- **업스케일은 수채 질감을 지운다.** 큰 해상도가 필요하면 그 해상도로 생성하거나, 사용자에게 방법을 묻는다(E-36).
- 모델 재생성으로 안 풀리는 국소 수정(하늘만 옮기기, 나무 하나 지우기, 연기 한 줄)은 **직접 편집(픽셀 합성)**이 빠르고 싸다. 편집본은 "모델이 생성한 것이 아님"을 기록한다.
- 그림체 수치 점검(가장자리 비율, 밝기)은 `06_qa-and-cost.md`.

---

## 7. 화면비·크롭·가림 구역

1. **최종 상영 화면부터 계산한다.** 예: 21:9 이미지를 4094×940(4.36:1)으로 쓰면 위아래 약 23%씩 잘리고 위에서 23~77%만 보인다. 핵심 요소는 이 띠 안에.
2. 너무 좁으면 이미지를 캔버스 가운데 60%로 줄여 놓고 주변을 채운다(`The central painting stays exactly as it is … paint only the empty margins … no empty margin left`).
3. **가림 구역(합창단·자막·로고)은 "아무것도 두지 않는 곳"이 아니라 "주요한 것을 거기에만 두지 않는 곳"이다.** 주요 피사체는 좌우·위쪽에, 그 구역에는 가려져도 손해 없는 부수 요소만.
4. 부감 각도를 높이면 하늘·능선·먼 도시가 띠 위로 밀려난다. 하늘이나 먼 대상이 띠 안에 보여야 하면 각도를 낮춘다(E-44).
5. 프롬프트의 % 좌표는 대략만 따른다. 큰 덩어리 단위(왼쪽 1/3, 위 가운데)로 쓰고, 정확해야 하면 배치 스케치(색 블록, 글자 없음)를 참조 1번으로 쓰고 "배치만 따르고 모양은 따르지 말 것"(E-28).

---

## 8. 퍼스트 프레임 이미지 (영상의 시작 이미지)

- **그 컷 영상의 0:00 상태**를 만든다. 썸네일 순간이 아니다(E-19).
- 장소 뷰(DERIVED VIEW) + 인물 시트 + 소품 요소를 권한 블록으로 묶고, CAMERA 블록이 모든 참조를 이긴다.
- 인물은 기존 앵커에 배치한다(새 위치 발명 금지). 동작 도중의 상태로 쓴다(`mid-step toward the bag`).
- 콘티 썸네일은 참조로 붙이지 않는다. 필요하면 그 구도로 **빈 장소 이미지**를 먼저 만들어 장소 참조로 쓴다(E-16).

---

## 9. 모델 메모 (관찰한 것)

| 모델 | 메모 |
|---|---|
| GPT Image 2.5 | 21:9 지원. 요소를 많이 지정할수록 질감이 렌더 쪽으로 돈다 → 요소를 줄이거나 질감 문단을 앞으로. 12,000자 프롬프트는 뒤쪽 금지문이 약해졌다 → 5,000자 수준으로 줄여도 결과 유지(E-29). `--ar` 같은 다른 툴 문법은 쓰지 않는다 |
| Nano Banana Pro | 인물 시트·장소 편집의 주력. 요청한 모델과 실제 처리 모델이 다를 수 있다(`nano_banana_pro` 요청 → `nano_banana_2` 처리) → 확정 전에 처리 모델 기록(E-31) |
| Seedream 5.0 Pro | 짧은 한국어 편집 지시(배치 수정, 인물 넣기)가 잘 들었다 |
| 업스케일(이미지·영상) | 질감을 지우거나 바꾼다. 수채·필름 질감 작업에서는 쓰기 전에 묻는다 |

---

## 10. 보내기 전 점검

- [ ] 신규/편집, LOCKED/DERIVED가 첫 문장에 분명한가. 둘이 섞이지 않았는가
- [ ] 참조마다 권한 한 줄, 가져오지 않을 것, 충돌 우선순위가 있는가
- [ ] 변경은 한 가지인가. CHANGE == ONLY CHANGE인가
- [ ] 보존 목록이 변경보다 구체적인가
- [ ] 편집에서 얼굴·장소를 다시 묘사하지 않았는가
- [ ] 인물·의상·장소 설명문이 에셋 대장과 글자까지 같은가
- [ ] 시대를 색이 아니라 물건으로 썼는가. `Nothing else:`로 물건 목록을 닫았는가
- [ ] 최종 크롭 띠와 가림 구역 안에서 핵심 요소 위치를 확인했는가
- [ ] 퍼스트 프레임이면 영상 0:00 상태인가
- [ ] 해상도가 확인용(1k)인가 — 확정 뒤에만 2k 이상
