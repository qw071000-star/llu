# 장소 이미지 — 작업별 템플릿
 
> 장소 이미지 작업별 **완성 템플릿**. 모드 판별은 `location-guide.md` §0, 참조 권한은 §6, 잠금·마감 문장은 §14가 정본이고 겹치면 그쪽을 따른다. 아래의 `§N`은 따로 적지 않으면 `location-guide.md`의 절, `02`처럼 숫자만 쓴 것은 이 문서의 절이다. 계보 유형 정의는 `location-assets.md` §1.
> 절 번호는 옛 `장소가이드/NN`과 같다(04 화면 UI·09 무대 세트는 이 영화에 없어 없다). "원문 N" = `힉스필드_장소_에셋_실제_프롬프트_모음.md`의 번호(다른 작품 — 결함은 §14.4).
> 프롬프트 블록은 영어. 모드·참조 권한·참조 실체(요소 `@tag` / 첨부 / 문구만)·job_id·처리 모델은 블록 밖에 한국어로 적는다. 참조 이름은 JSON `tag` 그대로. `[ ]`는 채울 자리.
>
> **옮기며 우리 규칙에 맞춰 고친 곳 (2026-09-25)**
> - 잠금 문장은 §14.5 표준형, DERIVED VIEW(05·06·07·08 B·11)는 `Do not inherit its camera angle` + CAMERA 블록. 카메라 권한은 하나 이하(01).
> - 한 생성에 한 가지(`[one / two / N]`·번호 나열 삭제, 10은 층마다). 부모 문장은 글자 그대로 두고 CAMERA 블록만 바꾼다(06·12 — "상속 설명 반복 안 함"·`LOC_…_v01` 명명 폐기). STATE·FIX는 카메라를 잠근다.
> - 07에 지배 요소·`Nothing else:`·씬 연도 시대 잠금. 글자는 무문자(10·11), 좌우는 화면 기준 + 기준 시점(08). 원문 발췌·공통 문법·내부 절차·점검표(→ §15)·출력 규칙은 옮기지 않았다.
 
---
 
## 01 레퍼런스 권한 분리
 
**언제** 참조가 둘 이상이고 역할이 다르다 — 장소 + 요소(컷 생성), 재료 체계만(→ 07), 배치만(→ 08). 실제 사례: `LC-002-V6`(`location-assets.md` §4).
**쓰지 않음** 참조 없는 새 장소(→ §13.1) / 한 장에서 대상 하나 제거(→ 03) / 모든 참조가 같은 역할일 때.
 
**먼저 잠글 것** 쓰는 순서 — ① 편집인지 새 이미지인지 ② 기준 참조의 권한(§6) ③ 보조 참조마다 역할 하나(한 명사구) ④ 가져오지 않을 속성(최소 한 줄) ⑤ 충돌 우선순위 한 문장 ⑥ 실제 내용.
 
완성 템플릿(셋째 참조부터 `controls only`·`From …` 줄을 더한다):
 
```text
[TASK OPENING]
 
REFERENCE AUTHORITY:
- <<<image_1>>> is the [exact same photograph / exact same location / same building's material register / layout authority]. It controls [closed list: geometry / layout / object positions — the camera only if it is the exact same photograph].
- <<<image_2>>> controls only [one element or design domain].
 
DO NOT TRANSFER:
- From <<<image_2>>>: [camera / framing / lighting / surrounding objects / room geometry].
 
PRIORITY:
If any references conflict, <<<image_1>>> controls [domains]; apply the other references only inside their named domains.
[CAMERA LINE]
 
[TASK-SPECIFIC INSTRUCTIONS]
```
 
- `[TASK OPENING]` LOCKED EDIT → 02 / DERIVED VIEW → 05·06 / 새 공간 → 07의 여는 문장.
- `[CAMERA LINE]` LOCKED EDIT(카메라는 `<<<image_1>>>`만): `Preserve <<<image_1>>>'s camera, geometry and placement.` / 그 밖(어느 참조도 카메라를 갖지 않는다): `Camera and shot size are defined below and override every reference.`
**교정** 보조 참조의 카메라가 따라옴 / 배치 참고가 사진 복제가 됨 / 두 참조가 같은 영역을 다르게 지시함 → §6 표.
근거: 원문 1, 3, 5, 6, 14–16, 19–20(6·16은 권한·제외가 없다 — §14.4-2).
 
---
 
## 02 고정 구도 부분 수정
 
**모드** LOCKED EDIT. **언제** 같은 사진의 수정본 — 명명한 한 가지만 바뀐다. 이 영화: 씬 10 식탁 인서트(`LC-002-V4` 빈 상판에 접시를 얹는 STATE — `location-assets.md` §4).
**쓰지 않음** 카메라 변경(→ 05·06) / 배치만 차용(→ 08) / 새 방(→ §13.1) / 사물 하나의 방향·상태·추가·제거(→ 03).
 
**먼저 잠글 것**
- `PRESERVE EXACTLY`는 카메라만이 아니라 아래 다섯 층을 다 적는다.
- CHANGE는 대상 → 위치 → 새 상태 → 영향 범위, 긍정형으로. **CHANGE와 ONLY CHANGE가 일치해야 한다.** `100% identical otherwise`는 구체적인 보존 목록 뒤에만.
- 장소 전체를 다시 묘사하지 않고, 모호한 대상을 넓히지 않는다. 카메라 변경이 끼면 DERIVED VIEW로 나눈다.
```text
Edit <<<image_1>>> WITHOUT reframing: camera position, camera height, angle, lens,
framing, horizon line and perspective are LOCKED — zero reframing, zero recentering,
zero zoom — this is the same photograph with one change only.
 
CHANGE — [TARGET AND LOCATION]:
Change [current state] to [new state]. Keep its [position / footprint / scale /
orientation] [locked / intentionally changed]. [Local light or contact behaviour.]
 
PRESERVE EXACTLY:
- Camera position, height, angle, lens, framing, horizon line, vanishing point and perspective
- The room's architecture: [walls, doors, windows, ceiling, floor]
- Every unnamed object in its exact position, scale, orientation, material and colour
- Existing light sources, shadows, exposure and reflections
- Colour grade, contrast, grain and depth of field
 
ONLY CHANGE: [the same item as CHANGE]. Everything else remains 100% identical.
```
 
- 첫 문장은 §14.5 표준형의 `[N]`을 `one`으로 채운 것. 떼면 성립하지 않는 두 변경만 `two` + CHANGE 블록 둘. `[TARGET AND LOCATION]`의 위치는 화면 기준.
**교정** 주변까지 다시 설계됨 → `Every unnamed object and surface remains in its exact position, scale, orientation, material and colour.` / 바꾼 불빛이 방을 밝힘 → §12.7-3 / 뺀 자리의 흔적 → 03.
근거: 원문 12·18(본보기), 6, 8, 14, 16. 원문 5·10은 본보기가 아니다(§14.4).
 
---
 
## 03 사물 방향·상태·추가·제거
 
**모드** LOCKED EDIT. **언제** 같은 사진에서 사물 하나를 제자리에서 돌리거나(ROTATE), 작동 상태를 바꾸거나(STATE — 켜짐/꺼짐, 열림/닫힘), 기존 앵커에 더하거나(ADD), 뺀다(REMOVE).
**쓰지 않음** A→B 이동(→ §13.3) / 다른 디자인으로 교체, 재질·손잡이만 바꾸기(규칙 없음 — 원문 부족) / 카메라가 같이 바뀜(→ 06).
 
**먼저 잠글 것**
- 네 작업 중 하나. 바뀌는 속성을 동사 하나로 쓰고, 바뀌지 않는 속성을 바로 잇는다.
- **방향을 바꾸면 위치를 잠그고, 상태를 바꾸면 형태와 방향을 잠근다.**
- 대상은 위치까지 묶어 하나로 식별한다(`the nearest [object]`, `the [object] on the RIGHT` — 화면 기준). 돌린 결과는 화면에 투영된 모양으로(§12.7-5).
- 추가는 기존 앵커에(사람이면 §12.7-4). 제거는 드러날 표면을 지정하고, 한두 문장이라도 표면 처리 문장을 붙인다(§14.4-5).
```text
ROTATE  Keep [object] in the exact same position, at the same height and on the same mount. Rotate only [named part] [degrees / direction] so that it faces [target]. Preserve its design, scale and support.
STATE   This is the same object in the same position with one state change only: [old state] becomes [new state]. Preserve its shape, dimensions, material, orientation and surroundings.
ADD     Add [subject / object] only at [existing anchor], matching its existing scale, perspective, contact and light. Do not alter the anchor or surrounding structure.
REMOVE  Remove [object] from [location]. Continue [revealed surface] naturally through the vacated area. Preserve everything else exactly.
```
 
완성 템플릿: 02의 틀에서 CHANGE에 위 공식 하나를 넣고, `PRESERVE EXACTLY`에 `[Target attributes not being changed]`를 더한다.
 
**교정**
- 돌리면서 옮겨 감 → `Rotate it in place around its existing mount; do not translate, raise, lower or resize it.`
- 상태를 바꿨더니 디자인이 달라짐 → `The same [object], [its parts], dimensions and orientation remain unchanged; only its [state] changes.`
- 더한 대상이 구조를 가림 → `Place the new subject within the existing [anchor], at its established scale, without moving or covering adjacent landmarks.`
- 뺀 자리에 흔적 → `The object is completely gone; the underlying surface continues naturally with no residual shadow, indentation, fragment or duplicate.`
근거: 원문 6, 12, 17, 18.
 
---
 
## 05 카메라 역방향 전환
 
**모드** DERIVED VIEW. **언제** 축이 긴 공간을 반대 방향에서 본다 — 폭·재료·반복 리듬·원근은 이어진다. 이 영화: `LC-002-V3`(`location-assets.md` §4 VIEWS 표·V3 프롬프트 기록).
**쓰지 않음** 픽셀 유지(→ 02) / 클로즈업(→ 06·11) / 같은 방향에서 가까워질 뿐(새 뷰 아님 — `location-assets.md` §1).
 
**먼저 잠글 것**
- 축이 긴 공간은 재료보다 **폭·소실점·반복 간격이 먼저**다(소실점을 직접 쓰고 `Rule of thirds`는 뺀다 — §12.7-1).
- 카메라는 **A 먼 끝으로 이동 / B 같은 지점에서 180° 회전** 중 하나만. 중간 표현으로 타협하지 않고, `reverse` 한 단어로 카메라 관계를 생략하지 않는다.
- 새 방향의 **종점**(문 / 어둠 / 이어지는 통로)을 정하고, 번호·표지는 한 줄로 따로 통제한다.
```text
Using <<<image_1>>> as the exact same [AXIAL SPACE] — same [materials, repeated
elements and light logic] — generate the [REVERSE / OPPOSITE-FACING] view.
Do not inherit its camera angle, framing or composition.
 
CAMERA (exactly one):
A  The camera now stands at the far end, looking back along the same central axis
   toward the original camera position.
B  From the same camera point, rotate the camera 180 degrees in place and look down
   the continuation behind it.
At [height]. [Strict one-point / matching natural] perspective, the vanishing point [position].
 
SPATIAL CONTINUITY:
- Same width, height and proportions
- Same rhythm and spacing of [repeated elements]; repeated elements diminish evenly toward one vanishing point
- Same materials, wear and light logic
- The perspective ends at [endpoint]. No extra junction, stair, window or side opening.
- [Numbers, plates, signs]: plain and unmarked / text not legible
 
This is a newly observed opposite direction of the same physical [space], not a
horizontal mirror of the reference.
 
[The parent's finish, verbatim]
```
 
**교정** 폭·간격이 달라짐 → `Preserve the exact [space] width, ceiling height and regular [element] spacing; repeated elements diminish evenly toward one vanishing point.`
근거: 원문 4(카메라 서술), 10(연속성 문장만 — 잠금 어투는 버린다, §14.4-1).
 
---
 
## 06 같은 장소의 새 시점
 
**모드** DERIVED VIEW. **언제** 장소는 그대로, 카메라 위치·거리·높이·각도를 바꾼다 — 클로즈업·낮은 시점·탑뷰·사선·다른 쪽. 이 영화: `LC-002-V4`(식탁 상판 직부감)·`V5`·`V6`(`location-assets.md` §4).
**쓰지 않음** 같은 사진 일부 수정(→ 02·03) / 배치만 가져와 다른 장소(→ 08) / 소품이 주체(→ 11) / 180° 반대(→ 05).
 
**먼저 잠글 것**
- 주체는 하나. 그 디자인·상태, 주변과의 상대 위치, 고유 랜드마크 1–3개는 잠그고, 프레이밍과 화면상 크기는 잠그지 않는다.
- 새 카메라는 **원본 카메라와의 관계**로 쓴다(`from the SAME side and the same direction`). 탑뷰·사선·낮은 시점은 **부정 범위를 함께**(`not from straight above, not from the side`).
- **형제판**: 부모 프롬프트에서 CAMERA·FRAMING 블록만 바꾸고 MASTER GEOMETRY·LIGHT·팔레트 등 나머지는 글자까지 같게 둔다. 자식끼리 물리지 않는다(§14.3).
```text
Using <<<image_1>>> as the exact same [LOCATION] — same [materials, landmarks and
light logic] — generate a NEW [CLOSE-UP / MEDIUM SHOT / TOP VIEW / OBLIQUE VIEW].
Do not inherit its camera angle, framing or composition.
 
CAMERA:
Move from the reference camera [path and distance]. Place the camera at [height and
side], looking [direction] at [subject] with [perspective]. [Negative range.]
 
FRAMING:
[Subject] fills [amount] of the frame. Keep [1–3 landmarks] visible. [Objects] fall
outside the tighter frame. The background [focus treatment].
 
CONTINUITY:
Preserve the exact design, proportions, material, wear, state and placement
relationships of [subject and anchors]. Keep the same lighting direction, palette and era.
 
[If the direction is new: the mirror sentence of 05]
[The parent's remaining blocks, verbatim]
```
 
**교정**
- 새 장소처럼 변함 → `This is the exact same [location / object], preserving its design, materials, state and spatial relationships; only the camera view changes.`
- 원치 않은 역방향 → `Move in from the same side and along the same line of sight; no reverse angle and no view from behind.`
- 클로즈업에 주변 가구가 남음 → `Only [subject] and [narrow context margin] remain in frame. [Furniture list] is outside the tighter composition.`
- 탑뷰가 사선으로 나옴(예: 식탁 상판 직부감) → `The optical axis is perpendicular to the surface; its rectangle is square to the frame with no oblique side view.`
근거: 원문 4, 7, 13, 19, 20.
 
---
 
## 07 같은 건물의 새 공간
 
**모드** 새 MASTER(참조는 `material register`). **언제** 같은 건물 안의 안 보이던 공간을 처음 만든다 — 공통 재료·창호·조명 규칙만 받고 기능·동선·카메라는 새로 짠다. 이 영화: 현관 `LC-002-V1`, 시장 네 곳의 공통 재료(`location-assets.md` §4·§5).
**쓰지 않음** 기존 방의 카메라만 바꿈(→ 05·06) / 벽·가구만 고침(→ 02) / 외관 사진 한 장으로 내부 추론(규칙 없음 — 원문 부족).
 
**먼저 잠글 것**
- 참조에서 **공통으로 반복되는 것만** 건물 규칙으로 잠근다 — 재료군, 문·창·창틀의 언어, 조명 방식·색온도, 시대·기술 수준, 관리 상태, 장식·문자 정책.
- 참조에 없는 내부 평면을 사실처럼 주장하지 않는다. 영구 구조와 동선(출입·순환·작업 영역)을 먼저, 기능 가구를 다음에 쓴다.
- 새 MASTER이므로 §14.1 13블록 — 특히 **지배 요소**, `Nothing else: no …`, **그 씬 연도의 시대 잠금**(§13.1).
```text
Using [REFERENCES] as the same building's material and architectural register —
[floor], [wall], [window / frame], [door] and [lighting rule] — generate a NEW [SPACE]
belonging to the same [BUILDING TYPE]. Do not copy the reference rooms' camera,
framing, furniture or layout.
 
CAMERA:
[Shot size], camera at [height and position], looking [direction] — [the room read at
an angle, not square-on / for a long axis, the vanishing point (§12.7-1)].
 
THE DOMINANT ELEMENT: [the one thing seen first, ideally the light source].
 
SPATIAL GEOGRAPHY:
(Directions as seen from [camera position]; LEFT and RIGHT are SCREEN directions.)
At the FAR END, [..]. The RIGHT wall [..]. At the LEFT, [..]. [Floor, ceiling,
openings and circulation.]
 
FUNCTION:
[Required landmarks, furniture and fixtures], arranged for [real use], with a clear
entry, circulation path and working zone. Nothing else: no [..].
 
CONTINUITY:
Use the same [materials, frame profiles, door language, lighting temperature and
maintenance level] as the references.
 
LIGHT:
[Visible / hidden sources, direction, falloff.] [One-sentence light logic (§12.3).]
 
Empty deserted [space], still air.
[§14.6 finish set + §13.1 era lock for that scene's year]
```
 
**교정**
- 참조 방의 가구가 복사됨 → `Transfer only the building-wide material and architectural language. Do not copy the reference room's furniture, layout or camera.`
- 같은 건물로 안 보임 → `Repeat the same [floor material], [glass-frame profile], [door language] and [light rule] as the references.`
- 기능 없는 전시장처럼 나옴 → `Arrange the permanent openings and required fixtures for the real operation of [space function], with a clear entry, circulation path and working zone.`
근거: 원문 1, 2, 3(`THE DOMINANT ELEMENT`는 원문 2, `Nothing else:`는 1–3).
 
---
 
## 08 레이아웃 고정 변환
 
**언제** 문·창·가구 같은 공간 앵커의 상대 위치는 두고 장소의 현실·시대·재료·기능을 바꾼다. 이 영화: 같은 방의 다른 시대(→ 10).
**쓰지 않음** 소품 하나만(→ 02·03) / 다른 카메라(→ 06) / 앵커를 자유롭게 옮겨도 될 때.
 
**모드를 먼저 고른다 — 섞지 않는다.** **A 카메라까지 고정** — LOCKED EDIT(`exact same photograph`), 배치 + 원근·카메라 거리를 잠근다(원문 14·16). **B 레이아웃만 차용** — 새 이미지(`only for the LAYOUT`), 카메라·픽셀 구조는 잠그지 않는다(원문 15).
 
**먼저 잠글 것**
- 앵커마다 벽 소속·앞뒤·위아래·옆 관계·화면상 크기와 방향을 다시 적는다. 화면 왼쪽 → 가운데 → 오른쪽 순서, 기준 시점은 괄호로 먼저(§14.2).
- 보존층·제거층·재구축층을 나누고, 재료 변환과 가구 보존을 한 문장에 섞지 않는다. 공간 관계를 먼저 쓰고 끝에서 배치를 다시 닫는다.
- A에서 층이 여럿이면 한 생성에 한 층(→ 10) — REMOVE와 REBUILD AS는 그 층의 앞뒤, 빛은 따로 한 단계(원문 14는 세 층을 한 번에 바꿨다).
- B로 새 MASTER를 만들면 07처럼 지배 요소·`Nothing else:`·시대 잠금을 넣는다.
```text
[A: the 02 LOCKED EDIT sentence]
[B: Using <<<image_1>>> only for the LAYOUT — [anchors and relations] — generate a
    completely different image: [new real space]. Do not copy its camera angle, framing,
    materials, lighting or original context.
    CAMERA: [new camera position, height, direction and distance]]
 
PRESERVE THE LAYOUT:
([A: as framed in the reference / B: Directions as seen from [viewpoint]]; LEFT and RIGHT are SCREEN directions.)
- [Anchor] on the LEFT [relation]
- [Anchor] at the CENTRE [relation]
- [Anchor] on the RIGHT [relation]
- [Furniture] below / beside / in front of [anchor]
[A only: same sizes, angles, perspective and camera distance.]
 
REMOVE THE ORIGINAL CONTEXT:
[What must disappear.]
 
REBUILD AS:
[New place, era, permanent surfaces, real depth and functional details.]
 
LIGHT:  [B — or A when light is this step's layer]
[New practical / daylight sources and falloff.]
 
[A: ONLY CHANGE: [the one layer]. The layout, the named furniture, the camera and the framing stay 100% identical.]
[B: Keep the layout above exactly. Finish and era lock — §14.6, §13.1]
```
 
**교정**
- 가구 위치가 달라짐 → `Keep every named anchor at the same place, size and angle, preserving all screen left/centre/right and above/below relationships.`
- B인데 원본 카메라가 따라옴 → §6 표.
- 새 재료와 함께 남길 가구까지 바뀜 → `Change only the permanent room surfaces. The named furniture remains the exact same objects with the same materials and wear.`
근거: 원문 14·16(A), 15(B).
 
---
 
## 10 시대·재료·디자인 교체
 
**모드** LOCKED EDIT, 층마다 한 생성. **언제** 구조·배치·카메라는 두고 시대·정체성·재료·가구 언어·질감을 바꾼다. 이 영화: 두 시대에 쓰는 LC-008 시골집(씬 6 / 8)·LC-003 골목(씬 2 / 8) — STATE로 가른다(`location-assets.md` §5, §13.1).
**쓰지 않음** 카메라·구조까지 새로 짜도 될 때(→ §13.1) / 소품 하나만(→ 03) / `1960s style` 같은 한 줄(원문 9 — 비교 사례일 뿐).
 
**먼저 잠글 것**
- 시대는 `style` 한 단어가 아니라 **층의 묶음**이다. 원래 요소마다 **목표 시대 대응물을 지정**하고, 새 건축 볼륨을 발명하지 않는다.
- **한 생성에 한 층.** 한 층을 바꿔 확정하고 그 확정본을 다음 층의 부모로 물린다(`location-assets.md` §1). 층: `IDENTITY AND TEXT` · `STRUCTURAL SURFACES`(walls, floor, ceiling, facade) · `DOORS, WINDOWS AND FRAMES` · `FURNITURE / VEHICLES / FIXTURES` · `LIGHTING`(sources, temperature, falloff) · `IMAGE CHARACTER`(grain, sharpness, contrast, exposure).
- `IDENTITY AND TEXT`는 이름·문구가 아니라 무문자 정책(`Hand-lettered Korean signage, text not legible.`).
```text
Edit <<<image_1>>> WITHOUT reframing: camera position, camera height, angle, lens,
framing, horizon line and perspective are LOCKED — zero reframing, zero recentering,
zero zoom — this is the same photograph with one change only.
The [SOURCE IDENTITY AND ERA] is turning into [TARGET IDENTITY AND ERA]; this step
changes only its [LAYER].
 
CHANGE — [LAYER]:
[Source element] becomes [its target-era counterpart], in the same position and at
the same scale. [One line per element of this layer.]
 
REMOVE:
[Source-era elements of this layer that must not remain.]
 
PRESERVE EXACTLY:
- Camera, framing, perspective and composition
- Every building volume and opening position
- [The other layers, as they are now]
- [Untargeted environment — street, planting, distant background — and retained objects]
 
ONLY CHANGE: [LAYER]. Everything else remains identical.
[§13.1 era lock of the target scene]
```
 
**교정**
- 건물 형태까지 새로 설계됨 → `Preserve every building volume, roofline, wall position, opening, gate and planting location; change only the named design layer.`
- 시대가 섞임 → `Remove every [source-era] vehicle, fixture, sign, handle and light. Nothing from the source era remains unless explicitly preserved.` (명사는 이번 층의 것만 남긴다.)
- 새 조명이 원래 노출을 깨뜨림 → `Replace the source fixtures with the named target sources while preserving the overall night/day exposure and composition.`
근거: 원문 8(원문은 여섯 층을 한 생성에 바꿨다), 14, 16, 9.
 
---
 
## 11 소품 독립 에셋 파생
 
**모드** DERIVED VIEW(계보 유형 PROP). **언제** 장소 안에 이미 있는 소품을 같은 디자인의 별도 에셋으로 확대한다.
**쓰지 않음** 새 디자인 발명 / 원본 사진에서 소품 상태만 바꿈(→ 03) / 장소 전체의 다른 방향(→ 05·06).
 
**촬영 유형 — 하나만, 맥락형과 무배경 제품 컷을 섞지 않는다.** ① 맥락형 클로즈업 — 랜드마크 1–3개를 남긴다 ② 소품 중심형 — 접촉면의 좁은 테두리만 ③ 정면판 — 표면을 정면으로(직부감이면 06의 광축 문장) ④ 비스듬한 근접판 — 형태와 표면을 함께 읽는 완만한 원근(부정 범위는 06).
 
**먼저 잠글 것** 디자인을 새로 설명하지 말고 원본의 고정 속성과 접촉면·랜드마크 관계를 잠근다. 점유율(`fills almost the entire image` / `fills most of the frame`)과 남길 범위를 함께 쓰고, 주변 가구는 제외 목록으로 뺀다.
 
```text
Using <<<image_1>>> as the exact same [LOCATION] and the exact same [PROP], generate a
[CONTEXT CLOSE-UP / PROP-CENTRED CLOSE-UP / STRAIGHT-ON DETAIL VIEW / OBLIQUE DETAIL VIEW].
Do not inherit its camera angle, framing or composition.
 
PROP CONTINUITY:
Preserve the exact silhouette, proportions, construction, component positions,
material, wear, colour and operating state of [PROP].
 
CAMERA:
The camera [moves / stands] [relative position], at [height], looking [direction]
from [angle]. [Perspective constraint and negative range.]
 
FRAMING:
[PROP] fills [almost the entire image / most of the frame]. Keep [narrow contact
surface or landmarks]. Exclude [room / furniture list].
 
DETAIL:
[Surface or interior detail that must be visible.] Do not redesign or add components.
Any lettering on it: text not legible.
 
LIGHT:
Use the same source direction and colour logic as the location. [If it is a lit
practical: lit but does not glow (§12.7-3).]
 
[The parent location's finish and era lock]
```
 
**교정**
- 디자인이 달라짐 → `This is the exact same prop, not a redesign: preserve every major contour, component, proportion, material and wear mark.`
- 주변 방이 너무 남음 → `The prop and its immediate contact surface occupy nearly the whole frame; no chairs, couches, walls or unrelated furniture are visible.`
- 장소 정체성이 사라짐 → `Retain [one or two landmarks] at the frame edge, softly out of focus, to confirm the same location.`
- 소품 두께가 사라짐(④) → `Keep the [physical edge] visible all around, with enough perspective to read the [prop] as a real object.`
근거: 원문 7, 13, 19, 20(19·20의 `clearly readable` 화면 문장은 뺐다 — 무문자).
 
---
 
## 12 다단계 제작과 버전 계보
 
**언제** 한 장소에 시점·상태가 여럿 / 변경이 많다 / 위치·재료·카메라를 따로 검증 / 같은 장소를 되풀이해 쓴다. 실제 계보: `location-assets.md` §4 LC-002.
**쓰지 않음** 대상 하나를 명백히 빼는 단순 수정(→ 03) / 파생판이 없는 일회성 이미지.
 
**먼저 잠글 것**
- 유형의 정의, "승인된 자식만 부모", 새 뷰를 여는 기준은 `location-assets.md` §1. 이름은 JSON `tag`, 유형은 그 문서의 계보 표에만.
- 모든 자식에 **승인된 부모 하나**. 자식끼리 물리지 않는다(§14.3).
- 카메라: `VIEW`·`PROP`은 바꾸고(DERIVED VIEW — 05·06·11), `STATE`·`FIX`는 잠근다(LOCKED EDIT — 02·03).
- 한 단계 = 변경 하나(떼면 성립하지 않는 두 변경만 예외). 구조·카메라·상태 변경은 서로 다른 단계다.
- `VIEW`·`PROP` 단계는 상속 문장(MASTER GEOMETRY·LIGHT·팔레트·material truth·시대 잠금·마감)을 **글자 그대로 붙이고** CAMERA 블록만 바꾼다(지침 #7, §14.3). `STATE`·`FIX`는 같은 사진의 LOCKED EDIT라 장소를 다시 묘사하지 않는다(02).
```text
PARENT: [approved parent — its JSON tag]
CHILD TYPE: [one type — location-assets §1]
 
[Opening of the matching template: STATE / FIX → the 02 sentence;
 VIEW / PROP → the 05 · 06 · 11 opening]
Use [approved parent] as the sole geometry and design authority; do not inherit
from discarded variants.
 
INHERIT (VIEW / PROP only) — unchanged from the parent, pasted verbatim:
- [MASTER GEOMETRY]
- [Materials and landmarks]
- [Object designs and approved states]
- [LIGHT, palette, material truth, era lock and finish]
 
CHANGE IN THIS STEP ONLY:
- [One change]
 
[Body of the matching template: PRESERVE EXACTLY · ONLY CHANGE (02 · 03) /
 CAMERA · FRAMING (05 · 06 · 11)]
```
 
**교정** 한 단계에서 너무 많이 바꿈 → 구조·카메라·상태를 세 자식으로 나눈다. / 자식판에서 장소가 흔들림 → `Inherit the approved location geometry, materials, landmarks and light logic unchanged from the parent.` / 상태판에 카메라 변경이 섞임 → `This is a STATE child, not a VIEW child.` 뒤에 02의 잠금 문장.
 
근거: 원문 3, 5–7, 11–20의 부모–자식 제작.