[TOOL] get_project_asset_prompt(job=job-lc001v1)

반영했습니다. 카메라는 LC-001-V1과 똑같이, 나머지는 제안대로 확정입니다(컷 카드 3-4 v0.1에 기록).

달라진 점: 카메라가 V1과 같아서 새 시점(DERIVED VIEW) 대신 V1 사진 위에 인물·소품만 더하는 LOCKED EDIT 틀을 씁니다. 화면 대응은 V1의 것(왼쪽 = 서쪽 감나무, 오른쪽 = 동쪽 시간표)을 그대로 씁니다.

**실패 위험 → 막는 문장**
1. 시간표 글씨가 읽힘 → `The timetable lettering stays hand-painted and illegible; no legible text anywhere.`
2. 가방이 미리 열림 → `closed, clasp fastened, lid flat on top`
3. 가방이 각진 상자로 변함 → `soft worn leather that sags slightly, not a rigid box`
4. 손녀·다른 인물 등장 → `Exactly 1 person is visible.`
5. 할아버지가 카메라를 봄(3-2에서 폐기된 사유) → `eyes down on the bag, not looking at the camera`
6. 모델이 다시 구도를 잡음 → LOCKED EDIT 여는 문장과 PRESERVE EXACTLY
7. 고정 문장 충돌: PR-001 설명문의 "손잡이에 매달려 있다"가 무릎 위 가방과 부딪칩니다. 문장은 고치지 않고 뒤에 `Except:` 한 줄을 붙였습니다. 총괄에 올릴 것으로 기록했습니다.

**프롬프트**
```text
Edit <<<loc_busstop_road_v1>>> WITHOUT reframing: camera position, camera height, angle, lens, framing, horizon line and perspective are LOCKED — zero reframing, zero recentering, zero zoom — this is the same photograph with one change only.
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions.
CHANGE — ADD THE PERSON AND THE PROP at existing anchors:
- An old man sits at the centre of the wooden bench along the shelter's back wall, his back against the wall, knees together. He is mid-pause, just before opening the bag: head slightly bowed, eyes down on the bag, not looking at the camera. Both hands rest on top of the closed bag, fingertips near the brass clasp, not touching it.
- The bag rests on his knees, as wide as his knees, about 40 cm wide, closed, clasp fastened, lid flat on top. Except: here the bag rests on his knees and does not hang from its handles.
REFERENCE AUTHORITY:
- <<<loc_busstop_road_v1>>> is the exact same photograph. It controls the place, the camera, the light and every object already in it.
- <<<char_grandpa_autumn_v1>>> controls only the old man's face, hair and wardrobe. Same face, same bone structure, same hair, same wardrobe.
- <<<prop_doctor_bag_v1>>> controls only the bag's shape, material and state; its size is as described above.
DO NOT TRANSFER: the character sheets' backdrop, studio lighting, pose or framing.
WARDROBE: A faded olive work jacket over a cream knit vest and a white collared shirt, dark grey wool trousers, scuffed brown leather shoes.
PROP: A worn brown leather doctor's bag with a brass clasp, about 40 cm wide, hanging heavy from its handles.
PRESERVE EXACTLY: camera and perspective · every object already in the place, including the persimmon tree and its fruit, the timetable sign and the bench · Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. In this view the west is screen LEFT. · shadows, exposure, grade, grain
ONLY CHANGE: the person and the prop are added exactly as described. Everything else remains 100% identical.
The bag is soft worn leather that sags slightly, not a rigid box. The timetable lettering stays hand-painted and illegible; no legible text anywhere. Nothing modern in frame.
Exactly 1 person is visible.
```
- 모드: 신규가 아니라 편집(LOCKED EDIT, 카메라 유지)
- 참조(붙이는 순서): 1 `loc_busstop_road_v1`(LC-001-V1, 같은 사진) · 2 `char_grandpa_autumn_v1`(얼굴·머리·의상만) · 3 `prop_doctor_bag_v1`(모양·재질·상태만)
- 모델: GPT Image 2.5 · 해상도 1k(확인용) · 16:9 · 1장
- 저장 폴더: 「빈 정류장」 / 3-4, `fld-3-4`
- 검사: 검사 스크립트 통과(참조 3개, 고정 문장 4줄 포함, 걸린 항목 없음)

주의 하나: 카메라가 V1과 같은 와이드라 할아버지와 가방이 화면에서 작습니다. 이 컷은 가방을 여는 손이 핵심이니, 영상에서 손동작이 잘 안 보이면 그때 샷 크기를 다시 상의하겠습니다.

아직 생성하지 않았습니다. 생성하려면 "생성해"라고 지시해 주세요. 3-4 컷 폴더가 `[대기]`라서 보낼 때 `[진행]`으로 바꿉니다.

=== 메타 ===
연 파일(순서대로): project/ok-cuts.md(목록 1~25줄, LC-001-V1 카드 90~114줄), .claude/skills/higgsfield-generation/check_prompt.py(앞 60줄), tmp/ff-3-4.txt, tmp/fixed-3-4.txt(내가 쓴 임시 파일), project/cuts/3-4.md
부른 [TOOL]: get_project_asset_prompt(job=job-lc001v1) (생성 도구는 부르지 않음)
고친 정본 파일: project/cuts/3-4.md (카메라·모드·시선·참조·고정 설명문·위험 줄을 v0.1로 갱신). 임시: tmp/ff-3-4.txt, tmp/fixed-3-4.txt
