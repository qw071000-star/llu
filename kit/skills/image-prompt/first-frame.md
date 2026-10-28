# 퍼스트 프레임 (영상의 시작 이미지)

## 필요한 정보

값은 컷 카드 [4]~[5]에 적고, 영상도 같은 값을 쓴다.

| 필요한 정보 | 틀의 자리 |
|---|---|
| 컷 카메라가 확정 장소 뷰와 같은가 (장소 뷰 job). 컷 목록의 장소 뷰가 확정 뷰 그대로면 "같음(틀 1)"을 제안한다 | 모드: 틀 1 / 틀 2 |
| 장소 뷰 job, LIGHT LOCK, 이 뷰의 화면 대응 줄 | `<<<LOC>>>`, `PRESERVE EXACTLY` |
| 인물마다 요소 ID, 의상 상태, 고정 설명문 | `REFERENCE AUTHORITY`, `WARDROBE` |
| 소품: 위치, 상태, 누가 드는가, 크기(cm + 신체) | `PROP` |
| 카메라: 위치(물건 기준)·높이·방향·거리·샷 크기 (틀 2는 장비명도) | `CAMERA` |
| 인물마다 시작 위치(앵커·거리·접촉), 하던 동작, 시선, 손 | `CHANGE` / `BLOCKING` |
| 보이는 인원 수 | `Exactly [N] people` |
| 최종 화면비 | 설정 |
| 고정 설명문과 부딪치는 이 컷만의 것(소품이 열림 상태 등) | `Except` 한 줄(고정 문장은 그대로 두고 뒤에 `Except: in this frame the bag is open.`) |

## 규칙

- **그 컷 영상의 0:00 상태를 만든다.** 썸네일 순간이 아니다.
- **모드를 먼저 고른다.**
  - 컷의 카메라가 확정된 장소 뷰와 같으면: 그 뷰를 `LOCKED EDIT`으로 쓰고 인물·소품만 더한다(틀 1).
  - 카메라가 다르면: `DERIVED VIEW`로 새 시점을 만든다(틀 2).
  - 같은 카메라인데 새 시점으로 만들면 장소 뷰와 첫 프레임의 구도가 어긋난다.
- **장소 뷰, 인물 시트, 소품 요소를 권한 블록으로 묶는다.** CAMERA 블록이 모든 참조를 이긴다.
- **인물은 기존 앵커에 둔다.**
  - 위치는 거리와 접촉으로 쓴다. "근처에"는 지켜지지 않는다.
  - 동작 도중의 상태로 쓴다.
- **인물 시트의 배경·조명·포즈는 `DO NOT TRANSFER`에 적는다.**
- **콘티 썸네일은 참조로 붙이지 않는다.** 그 구도가 필요하면 같은 구도의 빈 장소 이미지를 먼저 만들어 장소 참조로 쓴다.
- **소품 크기는 cm와 신체 기준으로 적는다.**
- **이웃 컷과 비교한다.** 컷 목록의 앞뒤 줄과 연속성 표(인물 자리·자세, 소품 상태)로 본다.
  - 연속성 표에 인물 자리가 없으면 같은 인물이 나온 직전 승인 시작 이미지의 OK 카드에서 BLOCKING 줄을 가져와 제안한다. 자리를 새로 지어내지 않는다. 시점과 구도가 겹치지 않는지, 빛 방향과 인물 자리가 같은지 본다.
- **다른 OK의 색감을 가져올 때**
  - 틀 1(LOCKED)이면 색은 그 장소 뷰에서 온다. 색 기준 OK가 같은 뷰에서 나왔으면 이미 같은 색이니 색 참조를 붙이지 않는다.
  - 다른 뷰면 틀 2로 쓰고 색 참조를 붙인다. 틀 1을 꼭 써야 하면 한 생성에 한 가지 원칙대로 두 단계(인물 추가 → 색 편집)로 나눈다.

## 틀 1 — 카메라가 확정된 장소 뷰와 같을 때 (LOCKED EDIT + ADD)

```text
Edit <<<LOC>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and
perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with
one change only.
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions.
CHANGE — ADD THE PEOPLE AND PROPS at existing anchors:
- [PERSON]: [anchor by objects, distance and contact], mid-[action], [gaze], [hands].
- [PROP]: [position, state, who holds it, size in cm and body terms].
REFERENCE AUTHORITY:
- <<<LOC>>> is the exact same photograph. It controls the place, the camera, the light and every object already in it.
- <<<CHAR>>> controls only [person]'s face, hair and wardrobe. Same face, same bone structure, same hair, same wardrobe.
- <<<PROP>>> controls only [prop]'s shape, material and state; its size is as described above.
DO NOT TRANSFER: the character sheets' backdrop, studio lighting, pose or framing.
WARDROBE: [asset registry sentence, verbatim].
PRESERVE EXACTLY: camera and perspective · every object already in the place · [LIGHT LOCK, verbatim] + [the view's screen-mapping sentence from the asset registry, verbatim] · shadows, exposure, grade, grain
ONLY CHANGE: the people and props are added exactly as described. Everything else remains 100% identical.
Exactly [one person is / N people are] visible.
```

## 틀 2 — 카메라가 다를 때 (DERIVED VIEW)

```text
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions.
Using <<<LOC>>> as the exact same location, generate a new view. Do not inherit its camera angle, framing
or composition. [CAMERA: position by objects, height,
direction, distance, shot size + camera body/lens/film stock.]
REFERENCE AUTHORITY:
- <<<LOC>>>: geography, materials, landmarks, light direction
- <<<CHAR>>>: face, hair, wardrobe only — Same face, same bone structure, same hair, same wardrobe.
  Change only the pose, framing, location and lighting.
- <<<PROP>>>: shape, material and state only; size as described below
DO NOT TRANSFER: the character sheet's backdrop, studio lighting, pose or framing.
PRIORITY: the CAMERA block overrides every reference.
BLOCKING: [each person at an existing anchor: distance and contact, mid-[action]].
WARDROBE: [asset registry sentence, verbatim].
PROP: [position, state, who holds it, size in cm and body terms]. [Except: …]
[PALETTE · ERA LOCK from the asset registry, verbatim]
Nothing else except the people and props named above: [the registry's Nothing else list, without its no-people item].
[LIGHT LOCK, verbatim] [The view's screen-mapping sentence from the asset registry, verbatim]
Exactly [one person is / N people are] visible.
```
