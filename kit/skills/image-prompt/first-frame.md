# 퍼스트 프레임 (영상의 시작 이미지)

## 필요한 정보

| 필요한 정보 | 틀의 자리 |
|---|---|
| 컷 카메라가 확정 장소 뷰와 같은가 (장소 뷰 job). 컷 목록의 장소 뷰가 확정 뷰 그대로이거나 비어 있으면 첫 질문으로 묻고 "같음(틀 1)"을 제안한다 | 모드: 틀 1 / 틀 2 |
| 장소 뷰 job, 그 뷰의 LIGHT LOCK | `<<<LOC>>>`, `PRESERVE EXACTLY` |
| 인물마다 요소 ID, 의상 상태, 고정 설명문 | `REFERENCE AUTHORITY`, `WARDROBE` |
| 소품: 위치, 상태, 누가 드는가, 크기(cm + 신체) | `PROP` |
| 카메라: 위치(화면 속 물건으로)·높이·무엇을 보는지(발·손 인서트처럼 아래를 보면 높이와 아래 방향을 함께)·거리·샷 크기 (틀 2는 장비명도) | `CAMERA` |
| 인물마다 시작 위치(앵커·거리·접촉), 하던 동작, 시선, 손 | `CHANGE` / `BLOCKING` |
| 보이는 인원 수 | `Exactly [N] people` |
| 최종 화면비 | 설정 |
| 고정 설명문과 부딪치는 이 컷만의 것(소품이 열림 상태, 들고 있다고 쓴 가방이 무릎 위 등) | `Except` 한 줄 |

## 규칙

- **그 컷 영상의 0:00 상태를 만든다.** 썸네일 순간이 아니다.
- **모드를 먼저 고른다.**
  - 컷의 카메라가 확정된 장소 뷰와 같으면: 그 뷰를 `LOCKED EDIT`으로 쓰고 인물·소품만 더한다(틀 1).
  - 카메라가 다르면: `DERIVED VIEW`로 새 시점을 만든다(틀 2). 그 시점을 이 컷만 쓰면 틀 2로 바로 쓰고, 여러 컷이 쓰면 장소 뷰를 먼저 확정하자고 제안한다(`location.md`).
  - 카메라가 장소 뷰의 반대쪽을 보면 화면 좌우가 뒤집힌다(뷰의 왼쪽 랜드마크·광원이 화면 오른쪽). 틀 2 끝의 `In this view …` 줄과 LIGHT LOCK을 화면 기준으로 다시 쓰고 "전 → 후"로 보인다.
  - 틀 1에서 인물·소품을 더하는 것은 한 변경으로 친다(빈 장소에 그 컷의 사람을 놓는 일).
  - 같은 카메라인데 새 시점으로 만들면 장소 뷰와 첫 프레임의 구도가 어긋난다.
  - 틀 2의 고유 문장(`Do not inherit its camera angle, framing or composition.`, 반대편이면 `not a horizontal mirror` 문장)은 OK 카드를 고쳐 쓸 때 거기 없어도 넣는다.
  - "뒤에서"인데 인물이 벽·구조물에 등을 대고 있으면 그 뒤는 벽 밖이다. 카메라를 구조물 안쪽, 인물 옆 어깨 너머에 두자고 제안한다.
- **인물은 기존 앵커에 둔다.**
  - 위치는 거리와 접촉으로 쓴다. "근처에"는 지켜지지 않는다.
  - 동작 도중의 상태로 쓴다.
- **이웃 컷과 비교한다.** 컷 목록의 앞뒤 줄과 연속성 표(인물 자리·자세, 소품 상태)로 본다.
  - 연속성 표에 인물 자리가 없으면 같은 인물이 나온 직전 승인 시작 이미지의 OK 카드 한 장에서 BLOCKING 줄을 가져와 제안한다. 자리를 새로 지어내지 않는다. 시점과 구도가 겹치지 않는지, 빛 방향과 인물 자리가 같은지 본다.
- **하늘·색을 바꾸면** 에셋 대장의 PALETTE·LIGHT LOCK과 부딪치는지 짚고 묻는다.
- **나이만 바꾸는 컷 편집**은 승인 시작 이미지를 LOCKED EDIT(`SKILL.md` §3)로 고치고, 나이 표지는 `character-edit.md` 틀 2의 `CHANGE — AGE` 목록에서 고른다. 표지를 지어내지 않는다.
- **다른 OK의 색감을 가져올 때**
  - 틀 1(LOCKED)이면 색은 그 장소 뷰에서 온다. 색 기준 OK가 같은 뷰에서 나왔으면 이미 같은 색이니 색 참조를 붙이지 않는다.
  - 질감은 색 참조가 맡는다. 질감 문장(`Real material truth` 등)을 새로 쓰지 않는다.
  - 다른 뷰면 틀 2로 쓰고 색 참조를 붙인다. 틀 1을 꼭 써야 하면 한 생성에 한 가지 원칙대로 두 단계(인물 추가 → 색 편집)로 나눈다.

## 틀 1 — 카메라가 확정된 장소 뷰와 같을 때 (LOCKED EDIT + ADD)

```text
Edit <<<LOC>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and
perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with
one change only.
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions, never the character's own left or right.
CHANGE — ADD THE PEOPLE AND PROPS at existing anchors:
- [PERSON]: [anchor by objects, distance and contact], mid-[action], [gaze], [hands].
- [PROP]: [position, state, who holds it, size in cm and body terms].
REFERENCE AUTHORITY:
- <<<LOC>>> is the exact same photograph. It controls the place, the camera, the light and every object already in it.
- <<<CHAR>>> controls only [person]'s face, hair and wardrobe. Same face, same bone structure, same hair, same wardrobe.
- <<<PROP>>> controls only [prop]'s shape, material and state; its size is as described in CHANGE above.
DO NOT TRANSFER: the character sheets' backdrop, studio lighting, pose or framing.
WARDROBE: [asset registry sentence, verbatim].
PRESERVE EXACTLY: camera and perspective · every object already in the place · [this view's LIGHT LOCK, verbatim] · shadows, exposure, grade, grain
ONLY CHANGE: the people and props are added exactly as described. Everything else remains 100% identical.
Exactly [one person is / N people are] visible.
```

## 틀 2 — 카메라가 다를 때 (DERIVED VIEW)

```text
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions, never the character's own left or right.
Using <<<LOC>>> as the exact same location, generate a new view. Do not inherit its camera angle, framing
or composition. [If the camera faces the other way: This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.] [CAMERA: position by objects, height,
direction, distance, shot size + camera body/lens/film stock.]
REFERENCE AUTHORITY:
- <<<LOC>>>: geography, materials, landmarks, light direction
- <<<CHAR>>>: face, hair, wardrobe only — Use the person in this reference. Same face, same bone structure, same hair, same wardrobe.
  Change only the pose, framing, location and lighting.
- <<<PROP>>>: shape, material and state only; size as described below
DO NOT TRANSFER: the character sheet's backdrop, studio lighting, pose or framing.
PRIORITY: the CAMERA block overrides every reference.
BLOCKING: [each person at an existing anchor: distance and contact, mid-[action]].
WARDROBE: [asset registry sentence, verbatim].
PROP: [position, state, who holds it, size in cm and body terms]. [Except: …]
[PALETTE · ERA LOCK from the asset registry, verbatim]
Nothing else except the people and props named above: [the registry's Nothing else list, without its no-people item].
[아래 두 줄: 반대편 카메라면 필수. 이 표시 줄은 지운다]
In this view [landmark] is at screen [side] and [landmark] is at screen [side].
LIGHT LOCK for this view: the light comes from screen [left/right], the [object] side.
Exactly [one person is / N people are] visible.
```
