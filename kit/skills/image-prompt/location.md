# 장소

처음 만드는 빈 공간 마스터는 틀 1, 같은 건물의 안 보이던 공간은 틀 1-B.

## 필요한 정보

| 필요한 정보 | 틀의 자리 |
|---|---|
| 장소 정체성(시대, 지역, 용도) | 첫 줄 `[SPACE]` |
| 같은 건물의 새 공간이면: 참조 job, 공통 재료·창호·조명 규칙, 공간의 기능과 동선 | 틀 1-B 첫 줄, `FUNCTION`, `CONTINUITY` |
| 카메라 위치·높이·방향, 샷 크기 | `CAMERA` |
| 처음 보이는 지배 요소 | `THE DOMINANT ELEMENT` |
| 방향별 벽·개구부·바닥·천장, 소실점(축이 긴 공간) | `SPATIAL GEOGRAPHY` |
| 없어야 할 것 | `Nothing else` |
| 팔레트 비율, 재질, 사용 흔적과 위치 | 팔레트, `Real material truth`, `Real aged surfaces` |
| 광원, 이 뷰에서 빛이 오는 화면 쪽과 그쪽 물건, 시간대 | 빛 문장 (LIGHT LOCK) |
| 이미지 마감(카메라·렌즈·필름) | `Image finish` |
| 시대 잠금(계절·연도·장소) | `Era lock` |
| 간판·가격표처럼 글자가 있는가 | 무문자 줄 |
| 새 시점·편집이면: 그 파일의 표 | `location-view.md` / `location-edit.md` |

## 규칙

**장소는 작품의 자산이다.** 새 축이 필요하면 컷 프롬프트로 카메라를 돌리지 말고 뷰를 하나 더 확정한다. 예외: 그 축을 한 컷만 쓰면 퍼스트 프레임 틀 2(`first-frame.md`).
- 새 뷰를 여는 것: 180° 반대, 아이레벨 → 부감, 문턱 너머.
- 새 뷰가 아닌 것: 같은 방향에서 가깝게·넓게, 인물 위치만 다름.

**계보:** `MASTER`에서 다음으로 갈라진다.
- `CLEAN`: 구조·배치만 정리한 판, LOCKED
- `VIEW`: 카메라 변경, DERIVED
- `PROP`: 소품 확대, DERIVED
- `STATE`: 빛·점유·소품 상태, LOCKED. 카메라 변경이 섞이면 STATE가 아니라 VIEW다
- `FIX`: 오류 제거, LOCKED

승인된 자식만 다음 부모가 된다. 폐기한 변형에서 파생하지 않는다. 자식끼리 물리지 않는다. 형제 뷰는 부모 프롬프트에서 CAMERA·FRAMING(전·중·후경)만 바꾸고 나머지는 글자까지 같게 둔다.

**방향 쓰기 (지침 6번: 모두 화면 기준)**
- MASTER GEOMETRY에는 기준 시점을 괄호로 먼저 적는다: `(directions as seen from [camera position], looking at [what])`.
- LIGHT LOCK은 그 뷰의 화면 쪽 + 그쪽 물건으로 쓴다: `Low dusk sun from screen left, the [object] side, is the only key.` 물건 이름이 있어서 뷰가 바뀌어도 같은 빛이 된다.
- LIGHT LOCK은 뷰마다 하나다. 반대 방향 뷰는 좌우를 뒤집어 그 뷰의 LIGHT LOCK을 새로 쓰고(`from screen right, the [object] side`), 에셋 대장의 그 뷰 줄에 적는다.

**쓰는 법**
- **시대는 물건·재질·글자·마감으로 쓴다. 색으로 쓰지 않는다.** 과거와 현재는 필름 그레인 유무로 가른다.
- **시대·고증은 자료로 확인한다.** 의도한 시대 착오라면 그렇다고 기록한다.
- **장비명(카메라·렌즈·필름 스톡)은 정지 이미지에만 쓴다.** 영상에는 화각(도)을 쓴다.
- **축이 긴 공간(복도·플랫폼·통로)은 소실점 위치를 직접 쓰고 `Rule of thirds`를 뺀다.** 일점 투시와 3분할은 부딪친다.
- **빈 공간 레퍼런스판만** 사선(`the room read at an angle, not square-on`)과 `Rule of thirds composition.`을 쓴다. 실제 컷과 퍼스트 프레임은 컷의 앵글을 따른다.
- **`no people`보다 `Empty deserted [space], still air.`가 세다.** 인물 없이 크기를 주려면 `A person standing here would be small in all this space.`(좁으면 `would fill most of the room`).
- **같은 종류 물건이 둘 이상이면 이름과 위치로 구분한다.**
- **문장을 다른 장소로 옮기면 광원·재질·가구 명사를 한 줄씩 검사한다.** 형제판 규칙은 같은 장소 안에서만 성립한다.
- **모양이 자꾸 틀리는 물건은 화면에 보이는 모양으로 쓴다:** `reads as a TALL NARROW RECTANGLE`
- **이름 없는 군중은 얼굴 없이 쓴다:** `seen from behind … no faces visible anywhere, dissolving into darkness toward the edges`. 대본에 이름이 있는 인물에는 쓰지 않는다.
- **켠 광원이 번지면:** `lit but does NOT glow: no halo, no bloom, no light spilling onto [surfaces]`
- **글자:** `[Hand-lettered signage], text not legible. No legible text anywhere.` 실제 문구를 따옴표로 넣지 않는다. 넣으면 모델이 쓰려고 한다.

**기록:** 확정되면 에셋 대장에 적는다. MASTER GEOMETRY는 승인 전에는 컷 프롬프트에 넣지 않는다.
- MASTER GEOMETRY (3~4문장, 기준 시점 포함. 미터·높이는 근거가 있을 때만)
- 뷰마다 LIGHT LOCK (한 문장, 화면 쪽 + 물건)
- PALETTE, ERA LOCK, FINISH (각 한 문장)
- 뷰마다 렌즈(mm = °)
- `Nothing else` 목록
- 뷰 계보 (부모, 유형)

## 틀 1 — 마스터 (빈 공간)

```text
Generate [SPACE].
CAMERA: [shot size], camera at [height and position], looking [direction][, the room read at an angle,
not square-on / for a long axis: strict one-point perspective, the vanishing point at (position)].
THE DOMINANT ELEMENT: [the one thing seen first, ideally the light source].
SPATIAL GEOGRAPHY (directions as seen from [camera position], looking [direction]; LEFT and RIGHT are
SCREEN directions, never the character's own left or right):
At the FAR END, [ ]. The RIGHT wall [ ]. At the LEFT, [ ]. [Floor, ceiling, openings.]
Nothing else: no [ ].
Empty deserted [space], still air.
Palette of roughly 80% [ ] — 15% [ ] — 5% [ ].
Real material truth: [ ]. Real aged surfaces: [wear and where it is].
[Light logic, one sentence: the light comes from screen [left/right], the [object] side.]
[Image finish: camera body, lens, film stock.] [Era lock: season, year, place. Nothing more recent
anywhere in frame.] No legible text anywhere.
[Reference plate only, not for a long axis: Rule of thirds composition.]
```

## 틀 1-B — 같은 건물의 새 공간 (새 MASTER)

참조에서 공통으로 반복되는 것만 건물 규칙으로 잠근다. 재료군, 문·창·창틀의 언어, 조명 방식·색온도, 시대, 관리 상태가 그것이다. 참조에 없는 평면을 사실처럼 주장하지 않는다. 영구 구조와 동선을 먼저, 기능 가구를 다음에 쓴다.

```text
Using [<<<A>>>, <<<B>>>] as the same building's material and architectural register — [floor], [wall],
[window / frame], [door] and [lighting rule] — generate a NEW [SPACE] belonging to the same [BUILDING TYPE].
Do not copy the reference rooms' camera, framing, furniture or layout.
CAMERA: [as 틀 1].
THE DOMINANT ELEMENT: [ ].
SPATIAL GEOGRAPHY (directions as seen from [camera position]; LEFT and RIGHT are SCREEN directions, never the character's own left or right):
At the FAR END, [ ]. The RIGHT wall [ ]. At the LEFT, [ ]. [Floor, ceiling, openings and circulation.]
FUNCTION: [required landmarks, furniture and fixtures], arranged for [real use], with a clear entry,
circulation path and working zone. Nothing else: no [ ].
CONTINUITY: use the same [materials, frame profiles, door language, lighting temperature and
maintenance level] as the references.
LIGHT: [sources, falloff]. [Light logic, one sentence: the light comes from screen [left/right], the [object] side.]
Empty deserted [space], still air.
[Palette · material truth · finish · era lock as 틀 1]
```

**교정**
- 참조 방의 가구가 복사됨 → `Transfer only the building-wide material and architectural language. Do not copy the reference room's furniture, layout or camera.`
- 같은 건물로 안 보임 → `Repeat the same [floor material], [glass-frame profile], [door language] and [light rule] as the references.`
- 기능 없는 전시장처럼 나옴 → `Arrange the permanent openings and required fixtures for the real operation of [function], with a clear entry, circulation path and working zone.`
