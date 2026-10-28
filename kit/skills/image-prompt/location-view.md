# 장소 — 새 시점 (DERIVED VIEW)

카메라를 바꾸는 작업이다. `WITHOUT reframing`을 쓰지 않는다. 같은 사진의 수정이면 `location-edit.md`.

## 필요한 정보

| 필요한 정보 | 틀의 자리 |
|---|---|
| 승인된 부모 job, 계보 유형(VIEW / PROP) | `<<<image_1>>>`, 기록 |
| 어떤 작업인가: 반대 방향 / 같은 쪽 새 시점 / 소품 확대 | 틀 A / B / C |
| 새 카메라: 원본 카메라와의 관계, 높이, 방향 | `CAMERA` |
| 주체 하나, 화면 점유율, 남길 랜드마크 1~3개, 프레임 밖으로 뺄 것 | `FRAMING` |
| 반대 방향이면: 카메라 방식(먼 끝으로 이동 / 제자리 180°), 새 방향의 종점, 반복 요소, 번호·표지 | 틀 A |
| 부모의 MASTER GEOMETRY · LIGHT LOCK · 팔레트 · 시대 잠금 · 마감 (에셋 대장, 글자 그대로) | 상속 줄 |
| 이 뷰의 화면 대응 | 마지막 줄 |

## 공통

- **새 카메라는 원본 카메라와의 관계로 쓴다.** `reverse`나 `close-up` 한 단어로 카메라 관계를 대신하지 않는다.
- **주체는 하나.** 그 디자인·상태, 주변과의 상대 위치, 랜드마크 1~3개를 잠근다. 프레이밍과 화면상 크기는 잠그지 않는다.
- **상속 문장은 글자 그대로 붙이고 CAMERA·FRAMING만 바꾼다.** 에셋 대장에 없는 줄(팔레트·시대 잠금·마감)은 부모 OK 카드의 프롬프트에서 글자 그대로 가져온다. 둘 다 없으면 지어내지 않고 묻는다. 첫 줄 뒤에 `Use <<<image_1>>> as the sole geometry and design authority; do not inherit from discarded variants.`

## 틀 A — 반대 방향

축이 긴 공간은 재료보다 폭·소실점·반복 간격이 먼저다.

```text
Using <<<image_1>>> as the exact same [SPACE] — same [materials, repeated elements and light logic] —
generate the OPPOSITE-FACING view. Do not inherit its camera angle, framing or composition.
CAMERA (exactly one of):
  The camera now stands at the far end, looking back along the same central axis toward the original
  camera position.
  From the same camera point, rotate the camera 180 degrees in place and look down the continuation
  behind it.
At [height]. [Strict one-point / natural] perspective, the vanishing point [position].
SPATIAL CONTINUITY:
- Same width, height and proportions
- Same rhythm and spacing of [repeated elements]; repeated elements diminish evenly toward one vanishing point
- Same materials, wear and light logic
- The perspective ends at [endpoint]. No extra junction, stair, window or side opening.
- [Numbers, plates, signs]: plain and unmarked, text not legible
This is a newly observed opposite direction of the same physical [space], not a horizontal mirror of
the reference.
[Parent's MASTER GEOMETRY with its viewpoint · LIGHT LOCK · palette · era lock · finish — verbatim]
In this view [direction] is screen LEFT and [direction] is screen RIGHT: [landmark] is at screen [side].
```

CAMERA는 두 줄 중 하나만 남긴다. 둘을 섞거나 중간 표현으로 타협하지 않는다.

**교정** 폭·간격이 달라짐 → `Preserve the exact [space] width, ceiling height and regular [element] spacing; repeated elements diminish evenly toward one vanishing point.`

## 틀 B — 같은 장소의 새 시점 (클로즈업·미디엄·탑뷰·사선·낮은 시점)

탑뷰·사선·낮은 시점은 부정 범위를 함께 쓴다(`not from straight above, not from the side`). 상속 문장에 프레임 밖 대상이 나와도 지우지 않는다. FRAMING의 `fall outside` 줄이 이긴다.

```text
Using <<<image_1>>> as the exact same [LOCATION] — same [materials, landmarks and light logic] —
generate a NEW [CLOSE-UP / MEDIUM SHOT / TOP VIEW / OBLIQUE VIEW].
Do not inherit its camera angle, framing or composition.
CAMERA: Move from the reference camera [path and distance]. Place the camera at [height and side],
looking [direction] at [subject] with [perspective]. [Negative range.]
FRAMING: [Subject] fills [amount] of the frame. Keep [1–3 landmarks] visible. [Objects] fall outside
the tighter frame. The background [focus treatment].
CONTINUITY: Preserve the exact design, proportions, material, wear, state and placement relationships
of [subject and anchors]. Keep the same lighting direction, palette and era.
Move in from the same side and along the same line of sight; no reverse angle and no view from behind.
(새 방향이면 위 줄 대신: This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.)
[Parent's MASTER GEOMETRY with its viewpoint · LIGHT LOCK · palette · era lock · finish — verbatim]
In this view [direction] is screen LEFT and [direction] is screen RIGHT: [landmark] is at screen [side].
```

**교정**
- 새 장소처럼 변함 → `This is the exact same [location / object], preserving its design, materials, state and spatial relationships; only the camera view changes.`
- 클로즈업에 주변 가구가 남음 → `Only [subject] and [narrow context margin] remain in frame. [Furniture list] is outside the tighter composition.`
- 탑뷰가 사선으로 나옴 → `The optical axis is perpendicular to the surface; its rectangle is square to the frame with no oblique side view.`

## 틀 C — 장소 속 소품을 별도 에셋으로 (계보 PROP)

촬영 유형은 하나만 고른다: 맥락형 클로즈업(랜드마크 1~3개) / 소품 중심형(접촉면 좁은 테두리만) / 정면판 / 비스듬한 근접판. 맥락형과 무배경 제품 컷(`prop.md`)을 섞지 않는다. 디자인을 새로 설명하지 않고 원본의 속성을 잠근다.

```text
Using <<<image_1>>> as the exact same [LOCATION] and the exact same [PROP], generate a
[CONTEXT CLOSE-UP / PROP-CENTRED CLOSE-UP / STRAIGHT-ON DETAIL VIEW / OBLIQUE DETAIL VIEW].
Do not inherit its camera angle, framing or composition.
PROP CONTINUITY: Preserve the exact silhouette, proportions, construction, component positions,
material, wear, colour and operating state of [PROP].
CAMERA: The camera [moves / stands] [relative position], at [height], looking [direction] from [angle].
[Perspective constraint and negative range.]
FRAMING: [PROP] fills [almost the entire image / most of the frame]. Keep [narrow contact surface or
landmarks]. Exclude [room / furniture list].
DETAIL: [surface detail that must be visible]. Do not redesign or add components. Any lettering on it:
text not legible.
LIGHT: Use the same source direction and colour logic as the location. [Lit practical: lit but does
NOT glow: no halo, no bloom.]
[Parent's finish and era lock — verbatim]
```

**교정**
- 디자인이 달라짐 → `This is the exact same prop, not a redesign: preserve every major contour, component, proportion, material and wear mark.`
- 주변 방이 너무 남음 → `The prop and its immediate contact surface occupy nearly the whole frame; no chairs, couches, walls or unrelated furniture are visible.`
- 장소 정체성이 사라짐 → `Retain [one or two landmarks] at the frame edge, softly out of focus, to confirm the same location.`
- 두께가 사라짐 → `Keep the [physical edge] visible all around, with enough perspective to read the [prop] as a real object.`
