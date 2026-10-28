# 장소

## 규칙

**장소는 작품의 자산이다.** 새 축이 필요하면 프롬프트로 카메라를 돌리지 말고 뷰를 하나 더 확정한다. 뷰는 축이 바뀔 때만 늘린다.

**계보:** `MASTER`에서 다음으로 갈라진다.
- `VIEW`: 카메라 변경, DERIVED
- `PROP`: 소품 확대
- `STATE`: 빛·점유·소품 상태, LOCKED
- `FIX`: 오류 제거, LOCKED

승인된 자식만 다음 부모가 된다. 형제 뷰는 부모 프롬프트에서 CAMERA·전중후경만 바꾼다.

**쓰는 법**
- **시대는 물건·재질·글자·마감으로 쓴다. 색으로 쓰지 않는다.** 과거와 현재는 필름 그레인 유무로 가른다.
- **시대·고증은 자료로 확인한다.** 의도한 시대 착오라면 그렇다고 기록한다.
- **장비명(카메라·렌즈·필름 스톡)은 정지 이미지에만 쓴다.** 영상에는 화각(도)을 쓴다.
- **축이 긴 공간은 소실점 위치를 직접 쓴다.**
- **같은 종류 물건이 둘 이상이면 이름과 위치로 구분한다.**
- **문장을 다른 장소로 옮기면 광원·재질·가구 명사를 한 줄씩 검사한다.**
- **모양이 자꾸 틀리는 물건은 화면에 보이는 모양으로 쓴다:** `reads as a TALL NARROW RECTANGLE`
- **군중은 얼굴 없이 쓴다:** `seen from behind … no faces visible anywhere`
- **반대 방향 뷰에는 이 문장을 붙인다:** `This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.`
- **사물 편집(LOCKED)은 네 공식 중 하나로 쓴다.**
  - ROTATE: 제자리 회전, 위치 잠금
  - STATE: 상태만 변경, 형태 잠금
  - ADD: 기존 앵커에 추가
  - REMOVE: 드러날 표면을 지정하고 `no residual shadow, indentation, fragment or duplicate`
  - 켠 광원이 번지면: `lit but does NOT glow: no halo, no bloom`

**기록:** 확정되면 에셋 대장에 적는다.
- MASTER GEOMETRY (3~4문장)
- LIGHT LOCK (한 문장)
- `Nothing else` 목록
- 뷰 계보

## 틀 1 — 마스터 (빈 공간)

```text
[Using <<<A>>> as the same building's material register, generate a NEW / Generate] [SPACE].
CAMERA: [shot size], camera at [height and position], looking [direction].
THE DOMINANT ELEMENT: [the one thing seen first].
SPATIAL GEOGRAPHY (as seen from [camera position]; LEFT and RIGHT are SCREEN directions):
At the FAR END, [ ]. The RIGHT wall [ ]. At the LEFT, [ ]. [Floor, ceiling, openings.]
Nothing else: no [ ].
Empty deserted [space], still air.
Palette of roughly 80% [ ] — 15% [ ] — 5% [ ].
Real material truth: [ ]. Real aged surfaces: [wear and where it is].
[Light logic, one sentence.]
[Image finish: camera body, lens, film stock.] [Era lock: season, year, place. Nothing more recent
anywhere in frame.] No legible text anywhere.
```

## 틀 2 — DERIVED VIEW (새 시점)

```text
Using <<<image_1>>> as the exact same [location] — same materials, landmarks and light logic —
generate a NEW [reverse view / close-up / top view / oblique view].
Do not inherit its camera angle, framing or composition.
CAMERA: [relation to the reference camera]. At [height], looking [direction].
FRAMING: [subject] fills [amount]. Keep [1–3 landmarks]. [Excluded objects] fall outside the frame.
CONTINUITY: preserve the exact design, materials, wear, state and placement relationships.
This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.
[Parent's MASTER GEOMETRY · LIGHT LOCK · palette · era lock · finish — verbatim]
```

## 틀 3 — LOCKED EDIT (같은 사진, 한 가지)

```text
[LOCKED EDIT 여는 문장 — SKILL.md §1]
CHANGE — [TARGET AND LOCATION]: [ROTATE / STATE / ADD / REMOVE].
PRESERVE EXACTLY: [camera · architecture · every unnamed object · light · grade]
ONLY CHANGE: [same]. Everything else remains 100% identical.
```
