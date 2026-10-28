카메라를 LC-001-V1과 같게 했으니 틀 1(LOCKED EDIT + 인물·소품 추가)로 씁니다. 자리·손·시선은 제안값을 썼고, 컷 카드 [4]·[5]에 기록했습니다.

**실패 위험 → 막는 문장**
1. 인물을 넣다가 확대·재구도함 → `He is drawn at the true scale of the bench in this wide view; do not enlarge him or bring him closer.` (LOCKED 여는 문장과 함께)
2. 카메라를 봄(폐기된 `job-ff-3-2-old`의 거절 이유) → `He does not look at the camera.`
3. 고정 설명문의 "hanging heavy from its handles" 때문에 가방이 들림 → `The bag rests flat across his knees; it is not lifted or hanging.`
4. 0:00에 가방이 이미 열림 → `The bag is fully closed; the brass clasp is shut.`
5. 손녀나 행인이 나옴 → `Exactly 1 person is visible.`
6. 붙여 넣은 듯 빛·질감이 따로 놂(GPT Image의 3D 질감 포함) → `Grandpa and the bag sit inside this same photograph: lit only by the same dusk light from screen LEFT, with the same film grain and grade.`
7. 소품 요소를 3-1 프레임에서 잘라 만들어서 그 손·옷이 따라옴(추정) → DO NOT TRANSFER에 `any hands or clothing in it`
8. 시간표 글자가 읽히거나 현대 물건이 나옴 → `No legible text anywhere; the timetable sign stays unreadable. No modern objects.`
9. **문장으로 못 막는 위험:** 길 건너 와이드라 40cm 가방과 걸쇠 위 손가락이 작게 보여 여는 동작이 덜 읽힐 수 있습니다(추정). 1k 확인에서 보고, 부족하면 카메라를 다시 정할지 여쭙겠습니다.

에셋 대장의 `Nothing else` 줄은 넣지 않았습니다. 그 줄의 "no people"이 할아버지와 부딪치기 때문입니다. 대신 5·8번 문장을 넣었습니다.

- 모드: 틀 1 LOCKED EDIT + ADD (카메라 = LC-001-V1)
- 참조: ① `<<<LOC>>>` LC-001-V1 `job-lc001v1` — 같은 사진(장소·카메라·빛) ② `<<<CHAR>>>` CH-001 `char_grandpa_autumn_v1` — 얼굴·머리·의상만 ③ `<<<PROP>>>` PR-001 `prop_doctor_bag_v1` — 모양·재질·상태만
- 모델: GPT Image 2.5
- 해상도: 1k(확인용) · 16:9 · 1장
- 길이: 해당 없음(8초 영상의 0:00 이미지)
- 저장 폴더: `fld-3-4`

```text
Edit <<<LOC>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with one change only.
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions.
CHANGE — ADD THE PEOPLE AND PROPS at existing anchors:
- GRANDPA: seated at the centre of the wooden bench along the shelter's back wall, his back about 20 cm from the wall, both feet flat on the ground. Mid-gesture: both hands rest on top of the closed bag, the fingers of his right hand settled on the brass clasp, about to open it. He looks down at the clasp. He does not look at the camera. He is drawn at the true scale of the bench in this wide view; do not enlarge him or bring him closer.
- DOCTOR'S BAG: A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, hanging heavy from its handles. Here it lies across Grandpa's knees, as wide as his lap, its handles slack on top. The bag rests flat across his knees; it is not lifted or hanging. The bag is fully closed; the brass clasp is shut.
REFERENCE AUTHORITY:
- <<<LOC>>> is the exact same photograph. It controls the place, the camera, the light and every object already in it.
- <<<CHAR>>> controls only Grandpa's face, hair and wardrobe. Same face, same bone structure, same hair, same wardrobe.
- <<<PROP>>> controls only the doctor's bag's shape, material and state; its size is as described above.
DO NOT TRANSFER: the character sheets' backdrop, studio lighting, pose or framing; from <<<PROP>>>, its background, surface, camera angle or any hands or clothing in it.
WARDROBE: A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes.
PRESERVE EXACTLY: camera and perspective · every object already in the place · Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. In this view the west (persimmon tree) is screen LEFT and the east (timetable sign) is screen RIGHT. · shadows, exposure, grade, grain
Grandpa and the bag sit inside this same photograph: lit only by the same dusk light from screen LEFT, with the same film grain and grade.
No legible text anywhere; the timetable sign stays unreadable. No modern objects.
ONLY CHANGE: Grandpa and the doctor's bag are added exactly as described. Everything else remains 100% identical.
Exactly 1 person is visible.
```

생성은 지시하실 때 위 설정(1k 1장, `fld-3-4`)으로 보냅니다. 3-5 컷 카드가 아직 없어서, 같은 자리·손 값은 컷 카드에 "총괄에 올릴 것"으로 적어 두었습니다.

=== 메타 ===
연 파일(순서대로):
1. project/cuts/3-4.md (이 대화에서 만든 카드 — 고친 뒤 글자 수를 확인하려고 다시 엶)

부른 [TOOL]:
- 없음

고친 정본 파일:
- project/cuts/3-4.md — [4] 카메라를 LC-001-V1과 같게(틀 1, 사용자 답), 렌즈는 LC-001-V1을 따름 · [5] 시작 자리·손과 시선(제안값) · [6] 이음새에 3-5와 같은 자리를 "총괄에 올릴 것"으로 적음 · [7] LOC 권한을 "같은 사진"으로 · [10] 위험 2줄 추가 · 카드 버전 줄 단축(3천 자 제한)
