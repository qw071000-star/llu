# 장소

## 규칙

**장소는 컷의 속성이 아니라 작품의 자산이다.**
- 새 축이 필요하면 프롬프트로 카메라를 돌리지 말고 뷰를 하나 더 확정한다.
- 뷰는 축이 바뀔 때만 늘린다. 같은 방향에서 더 가깝게 찍거나 인물 위치만 다른 것은 같은 뷰다.

**계보:** `MASTER`(정본)에서 갈라진다.
- `VIEW`: 카메라 변경, DERIVED
- `PROP`: 소품 확대
- `STATE`: 빛·점유·소품 상태, LOCKED
- `FIX`: 오류 제거, LOCKED
- 승인된 자식만 다음 부모가 된다. 자식끼리는 물리지 않는다.
- 형제 뷰는 부모 프롬프트에서 CAMERA·전중후경만 바꾸고, 나머지는 글자까지 같게 둔다.

**쓰는 법**
- **시대는 색이 아니라 물건·재질·글자·마감으로 쓴다.** 과거를 노랗게 만들지 않는다. 과거판은 필름 그레인, 현재판은 그레인 없음으로 질감을 가른다.
- **시대·고증은 자료로 확인한다.** 수양버들(중국 원산), 헤롯 시대 성전 터, 현대식 차양이 시대 착오로 들어간 기록이 있다. 의도한 시대 착오라면 그렇다고 기록한다.
- **장비명은 정지 이미지에만 쓴다.** 정지 이미지는 장비·필름 스톡이 룩처럼 작동한다. 영상은 장비명 대신 화각(도)으로 쓴다.
- **축이 긴 공간(복도, 플랫폼)은** `Rule of thirds`를 빼고 소실점 위치를 직접 쓴다.
- **같은 종류 물건이 둘이면 이름과 위치로 구분한다.** 봉지가 식탁이 아니라 거실 탁자에 놓인 사고가 있었다.
- **다른 장소로 문장을 옮기면 옛 명사가 샌다.** 광원·재질·가구 명사를 한 줄씩 검사한다.
- **모양이 자꾸 틀리는 물건은 화면에 보이는 모양으로 쓴다.** 예: `reads as a TALL NARROW RECTANGLE`
- **군중은 얼굴 없이 쓴다.** 예: `seen from behind … no faces visible anywhere`
- **새 방향 뷰에는 이 문장을 붙인다:** `This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.`
- **사물 편집(LOCKED)은 네 공식 중 하나로 쓴다.**
  - ROTATE: 제자리 회전, 위치 잠금
  - STATE: 켜짐·열림 같은 상태 변경, 형태 잠금
  - ADD: 기존 앵커에 추가
  - REMOVE: 드러날 표면을 지정하고 `no residual shadow, indentation, fragment or duplicate`
  - 켠 광원이 방을 밝히지 않게 할 때: `lit but does NOT glow: no halo, no bloom`

**기록:** 확정되면 에셋 대장에 적는다. MASTER GEOMETRY(3~4문장), LIGHT LOCK(한 문장), `Nothing else` 목록, 뷰 계보 표.

## 틀 1 — 마스터 (빈 공간, 새로)

```text
[Using <<<A>>> as the same building's material register — … — generate a NEW / Generate] [SPACE].
CAMERA: [shot size], camera at [height and position], looking [direction] — [read at an angle, not
square-on / for a long axis: the vanishing point at …].
THE DOMINANT ELEMENT: [the one thing seen first, ideally the light source].
SPATIAL GEOGRAPHY (as seen from [camera position]; LEFT and RIGHT are SCREEN directions):
At the FAR END, [ ]. The RIGHT wall [ ]. At the LEFT, [ ]. [Floor, ceiling, openings.]
Nothing else: no [ ].
Empty deserted [space], still air.
Palette of roughly 80% [ ] — 15% [ ] — 5% [ ].
Real material truth: [ ]. Real aged surfaces: [wear with location — scuffs at chair height …].
[Light logic, one sentence.] [Practicals lit but do not glow.]
[Image finish: camera body, lens mm, film stock.] [Era lock: Early autumn 1980, South Korea. Nothing
more recent anywhere in frame.] No legible text anywhere.
```

## 틀 2 — DERIVED VIEW (같은 장소, 새 시점)

```text
Using <<<image_1>>> as the exact same [location] — same [materials, landmarks and light logic] —
generate a NEW [reverse view / close-up / top view / oblique view].
Do not inherit its camera angle, framing or composition.
CAMERA: [relation to the reference camera]. At [height], looking [direction]. [Negative range.]
FRAMING: [subject] fills [amount]. Keep [1–3 landmarks]. [Excluded objects] fall outside the frame.
CONTINUITY: preserve the exact design, materials, wear, state and placement relationships.
This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.
[Parent's MASTER GEOMETRY · LIGHT LOCK · palette · era lock · finish — verbatim]
```

## 틀 3 — LOCKED EDIT (같은 사진, 한 가지)

```text
Edit <<<image_1>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon
line and perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same
photograph with one change only.
CHANGE — [TARGET AND LOCATION]: [ROTATE / STATE / ADD / REMOVE formula].
PRESERVE EXACTLY: [camera · architecture · every unnamed object · light · grade]
ONLY CHANGE: [same]. Everything else remains 100% identical.
```
