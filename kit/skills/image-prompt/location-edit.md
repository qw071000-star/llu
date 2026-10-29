# 장소 — 같은 사진 수정 (LOCKED EDIT)

카메라를 잠그는 작업이다. 여는 문장과 `CHANGE / PRESERVE EXACTLY / ONLY CHANGE` 문법은 `SKILL.md` §1·§3에 있다.

## 필요한 정보

| 필요한 정보 | 틀의 자리 |
|---|---|
| 승인된 부모 job, 계보 유형(STATE / FIX / CLEAN) | `<<<image_1>>>`, 기록 |
| 바꿀 것 하나와 위치(화면 기준) | `CHANGE — [TARGET AND LOCATION]` |
| 작업: 사물 편집(ROTATE / STATE / ADD / REMOVE) / 빛·점유 상태판 / 시대·재료 교체 / 배치만 두고 변환 | 틀 1 / 1 / 2 / 3 |
| 제거면 드러날 표면, 추가면 기존 앵커 | 공식 줄 |
| 보존할 것: 건축, 바꾸지 않는 대상 속성 | `PRESERVE EXACTLY` |

## 규칙

- **변경은 한 가지.** 떼면 성립하지 않는 두 변경(켠 화면과 그 화면빛)만 `two changes`와 CHANGE 블록 둘로 쓴다. 시간대(해 지우기·하늘)와 광원 켜기는 뗄 수 있으니 두 생성으로 나눈다. 나누면 1단계 결과는 아직 요청한 상태(예: 밤)가 아니라고 한 줄 알린다.
- **방향을 바꾸면 위치를 잠그고, 상태를 바꾸면 형태와 방향을 잠근다.**
- **대상은 위치까지 묶어 하나로 식별한다:** `the nearest [object]`, `the [object] on the RIGHT`(화면 기준).
- **장소를 다시 묘사하지 않는다.** 모호한 대상을 넓히지 않는다.
- **A에서 B로 옮기는 편집은 한 생성으로 하지 않는다.** REMOVE → ADD 두 단계로 나누거나 뷰를 나눈다.
- **빛·시간대만 바꾸는 상태판은 STATE다.** 점유 인원만 바꿀 때는 기존 앵커에, 얼굴 없이 더한다.
- **빛을 바꾸는 편집이면** 부모의 LIGHT LOCK을 PRESERVE에서 빼고, 바뀌는 광원만 CHANGE에 쓴다. 바뀌지 않는 광원은 PRESERVE에 남긴다. 확정되면 그 STATE 뷰의 LIGHT LOCK을 에셋 대장에 따로 적는다. 새 LIGHT LOCK 제안에는 광원의 화면 쪽 + 물건을 쓰고, 위치를 모르면 묻는다.

## 틀 1 — 사물 편집과 상태판

`SKILL.md` §3 틀의 CHANGE에 아래 공식 하나를 넣고, `PRESERVE EXACTLY`에 바꾸지 않는 대상 속성을 더한다.

```text
ROTATE  Keep [object] in the exact same position, at the same height and on the same mount. Rotate only
        [named part] [degrees / direction] so that it faces [target]. Preserve its design, scale and support.
STATE   This is the same object in the same position with one state change only: [old state] becomes
        [new state]. Preserve its shape, dimensions, material, orientation and surroundings.
ADD     Add [subject / object] only at [existing anchor], matching its existing scale, perspective, contact
        and light. Do not alter the anchor or surrounding structure.
REMOVE  Remove [object] from [location]. Continue [revealed surface] naturally through the vacated area.
        The object is completely gone; no residual shadow, indentation, fragment or duplicate.
```

**교정**
- 돌리면서 옮겨 감 → `Rotate it in place around its existing mount; do not translate, raise, lower or resize it.`
- 상태를 바꿨더니 디자인이 달라짐 → `The same [object], [its parts], dimensions and orientation remain unchanged; only its [state] changes.`
- 더한 대상이 구조를 가림 → `Place the new subject within the existing [anchor], at its established scale, without moving or covering adjacent landmarks.`
- 주변까지 다시 설계됨 → `Every unnamed object and surface remains in its exact position, scale, orientation, material and colour.`

## 틀 2 — 시대·재료·디자인 교체 (한 생성에 한 층)

시대는 `1960s style` 한 줄이 아니라 층의 묶음이다. 원래 요소마다 목표 시대 대응물을 지정하고, 새 건축 볼륨을 만들지 않는다. 한 층을 바꿔 확정하고 그 확정본을 다음 층의 부모로 쓴다.

층: `IDENTITY AND TEXT`(간판·표지판의 판과 글자 정책) · `STRUCTURAL SURFACES`(벽·바닥·지붕·도로 포장) · `DOORS, WINDOWS AND FRAMES` · `FURNITURE / VEHICLES / FIXTURES`(벤치·표지판 기둥·가로등·차) · `LIGHTING` · `IMAGE CHARACTER`(grain, sharpness, contrast, exposure). 한 요소는 한 층에만 넣는다(표지판 판은 `IDENTITY AND TEXT`, 그 기둥은 `FIXTURES`). `ONLY CHANGE`에는 그 층 이름을 쓴다. 바꾸는 순서도 이 목록 순서다(`IDENTITY AND TEXT` 먼저 → `IMAGE CHARACTER` 끝). 계획의 한 단계에도 층은 하나만.

```text
Edit <<<image_1>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with one change only.
The [SOURCE IDENTITY AND ERA] is turning into [TARGET IDENTITY AND ERA]; this step changes only its [LAYER].
CHANGE — [LAYER]:
[Source element] becomes [its target-era counterpart], in the same position and at the same scale.
[One line per element of this layer.]
REMOVE: [source-era elements of this layer that must not remain].
PRESERVE EXACTLY:
- Camera, framing, perspective and composition
- Every building volume and opening position
- [The other layers, as they are now]
- [Untargeted environment — street, planting, distant background — and retained objects]
ONLY CHANGE: [LAYER]. Everything else remains identical.
[Era lock of the target scene]
```

여러 단계 시대 교체의 중간 단계는 이번 층만 목표 시대로 쓰고, 나머지 층은 `unchanged from the parent image`로 둔다. 마지막 줄의 목표 시대 잠금은 마지막 층에서만 쓰고, 중간 단계에서는 원 시대 이름을 되풀이하지 않는다.

**교정**
- 건물 형태까지 새로 설계됨 → `Preserve every building volume, roofline, wall position, opening, gate and planting location; change only the named design layer.`
- 시대가 섞임 → `Remove every [source-era] vehicle, fixture, sign, handle and light. Nothing from the source era remains unless explicitly preserved.` (명사는 이번 층의 것만)
- 새 조명이 노출을 깨뜨림 → `Replace the source fixtures with the named target sources while preserving the overall night/day exposure and composition.`

## 틀 3 — 배치만 두고 장소를 바꾼다

모드를 먼저 고르고 섞지 않는다.
- **A 카메라까지 고정:** LOCKED EDIT. 배치와 원근·카메라 거리를 잠근다. 층이 여럿이면 틀 2처럼 한 층씩.
- **B 배치만 빌림:** 새 이미지(`only for the LAYOUT`). 카메라·픽셀 구조는 잠그지 않는다. 새 MASTER이므로 `location.md` 틀 1의 지배 요소·`Nothing else`·시대 잠금을 넣는다.

앵커마다 벽 소속·앞뒤·위아래·옆 관계를 적는다. 화면 왼쪽 → 가운데 → 오른쪽 순서로 쓰고, 재료 변환과 가구 보존을 한 문장에 섞지 않는다.

```text
[A: LOCKED EDIT opening]
[B: Using <<<image_1>>> only for the LAYOUT — [anchors and relations] — generate a completely different
    image: [new real space]. Do not copy its camera angle, framing, materials, lighting or original context.
    CAMERA: [new camera position, height, direction and distance]]
PRESERVE THE LAYOUT ([A: as framed in the reference / B: directions as seen from [viewpoint]]; LEFT and
RIGHT are SCREEN directions, never the character's own left or right):
- [Anchor] on the LEFT [relation]
- [Anchor] at the CENTRE [relation]
- [Anchor] on the RIGHT [relation]
- [Furniture] below / beside / in front of [anchor]
[A only: same sizes, angles, perspective and camera distance.]
REMOVE THE ORIGINAL CONTEXT: [what must disappear].
REBUILD AS: [new place, era, permanent surfaces, real depth and functional details].
[A: ONLY CHANGE: [the one layer]. The layout, the named furniture, the camera and the framing stay 100% identical.]
[B: LIGHT: [sources and falloff]. Keep the layout above exactly. Finish and era lock as location.md 틀 1.]
```

**교정**
- 가구 위치가 달라짐 → `Keep every named anchor at the same place, size and angle, preserving all screen left/centre/right and above/below relationships.`
- 남길 가구까지 바뀜 → `Change only the permanent room surfaces. The named furniture remains the exact same objects with the same materials and wear.`
