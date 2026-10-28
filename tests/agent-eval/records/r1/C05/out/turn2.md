반영했습니다. 카메라는 벤치 높이·미디엄 와이드(사용자 답)이고, 나머지는 제안값입니다. 에셋 대장 LC-001 뷰 표에 `LC-001-V2` 줄로 기록했습니다(상태: 진행).

**실패 위험 → 막는 문장**
1. 좌우 반전(V1을 뒤집어 감나무가 왼쪽에 옴) → `not a horizontal mirror of the reference` + `In this view the east is screen LEFT and the west is screen RIGHT…`
2. V1 구도를 물려받음(다시 길에서 정류장을 보는 그림) → `Do not inherit its camera angle, framing or composition.` + `PRIORITY: the CAMERA and FRAMING blocks below override the reference.`
3. 고정문에 있는 벤치·북쪽 논이 화면에 들어옴 → `The bench, the back wall and the paddies and hills north of the shelter are behind the camera and fall outside the frame.`
4. 낮은 카메라라 위로 꺾인 앙각이 됨 → `The camera is level, not tilted up; the horizon sits near the middle of the frame.`
5. 빛 방향이 틀리거나 해가 화면에 들어옴 → `The sun itself is out of frame beyond screen RIGHT; long shadows fall toward screen LEFT.`
6. 역광 노출(안은 새까맣고 밖은 하얗게 날아감) → `Exposure holds detail both in the shaded shelter interior and in the dusk-lit road outside; nothing is blown out.`
7. 시간표 글씨가 읽힘 → `showing only its plain painted back` + `No legible text anywhere.`
8. GPT Image 2.5가 3D 렌더 질감으로 감 → 앞쪽에 `A real 35mm film photograph, not a 3D render.`

- 모드: DERIVED VIEW (새 시점, 반대 방향)
- 참조: image_1 = `job-lc001v1` (LC-001-V1). 같은 장소로서 지리·재질·랜드마크·빛 방향만 가져오고, 카메라·구도는 가져오지 않음
- 모델: GPT Image 2.5
- 해상도: 1k 확인용 · 16:9
- 장 수: 1
- 저장: 00 에셋 / 장소 `fld-locs`

```text
Using <<<image_1>>> as the exact same rural bus stop — same materials, landmarks and light logic —
generate a NEW reverse view. A real 35mm film photograph, not a 3D render.
Do not inherit its camera angle, framing or composition.
PRIORITY: the CAMERA and FRAMING blocks below override the reference.
CAMERA: the reverse of the reference camera. Inside the shelter, just in front of the wooden bench at the centre of the back wall, at the height of the bench seat (about 45 cm above the concrete floor), looking south straight out through the open front toward the road. Medium wide shot, tripod-locked. The camera is level, not tilted up; the horizon sits near the middle of the frame.
FRAMING: the shelter's open front fills most of the frame like a picture frame: the corrugated tin roof edge along the top, the ends of the two concrete side walls at the left and right edges, the concrete floor slab at the bottom. Through it, the empty two-lane road crosses the frame left to right, and beyond the road harvested rice paddies with straw stubble stretch flat to a distant line of low hills. Keep the timetable sign's pole just beyond the east wall at screen LEFT, showing only its plain painted back, and the bare persimmon branches at the screen-RIGHT edge. The bench, the back wall and the paddies and hills north of the shelter are behind the camera and fall outside the frame.
THE DOMINANT ELEMENT: the empty road seen through the shelter's open front, with low dusk light raking in from screen RIGHT across the asphalt.
CONTINUITY: preserve the exact design, materials, wear, state and placement relationships.
This is a newly observed direction of the same physical room, not a horizontal mirror of the reference.
MASTER GEOMETRY (as seen from the road, looking north): A concrete bus shelter with a corrugated tin roof stands at the centre, its open front facing the road. A wooden bench runs along its back wall. A painted metal timetable sign stands on a pole at the east side of the shelter. A bare persimmon tree stands at the west side. Harvested rice paddies stretch behind it to low hills.
LIGHT LOCK: Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off.
Nothing else: no other buildings, no cars, no people, no legible text.
Empty deserted bus stop, still air.
Palette of roughly 80% dry ochre and grey concrete — 15% deep blue dusk sky — 5% persimmon orange.
Real material truth: rough cast concrete with rain streaks, rusted tin ridges, cracked asphalt at the road edge.
In this view the east is screen LEFT and the west is screen RIGHT: the timetable sign is at screen LEFT and the persimmon tree at screen RIGHT. The sun itself is out of frame beyond screen RIGHT; long shadows fall toward screen LEFT. Exposure holds detail both in the shaded shelter interior and in the dusk-lit road outside; nothing is blown out.
Image finish: ARRI Alexa Mini, 35mm lens, Kodak Vision3 250D. Era lock: late autumn, early 1990s, rural South Korea. Nothing more recent anywhere in frame. Hand-lettered signage, text not legible. No legible text anywhere.
```

**점검**
- 검사 스크립트: 통과(image, 참조 1, 걸린 항목 없음).
- 고정문: MASTER GEOMETRY · LIGHT LOCK · Nothing else는 에셋 대장과 글자까지 같습니다. 팔레트·마감·시대 잠금은 V1 카드 그대로입니다.
- V1과 다른 줄은 하나입니다. Real material truth의 `a bench worn pale where people sit` → `cracked asphalt at the road edge`로 바꿨습니다. 벤치가 화면 밖에 있어서, 남겨 두면 벤치를 화면 안으로 끌어올 위험이 있습니다.

**확인할 것**
1. "벤치 높이"는 벤치 앉는 판의 높이(바닥에서 약 45cm)로 넣었습니다. 앉은 사람 눈높이(약 1.1m)를 뜻하셨으면 CAMERA 줄 하나만 바꾸겠습니다.
2. 이대로 1k 한 장 보낼까요?

=== 메타 ===
연 파일(순서대로, 이번 턴):
1. RUN/.claude/skills/higgsfield-generation/check_prompt.py — 열지 않고 실행만 함(`--help` 1회, 검사 2회: `--kind image --refs 1 --must-include`)
2. RUN/project/asset-registry.md — 89–93행(LC-001 뷰 표, 고치기 위해)
- 그 밖에 스크래치 폴더에 검사용 파일 2개(프롬프트, 고정문 목록)를 씀. RUN 밖의 파일은 읽지 않음.

부른 [TOOL]: 없음(생성 지시 전이라 보내지 않음)

고친 정본 파일:
- RUN/project/asset-registry.md — LC-001 뷰 표에 `LC-001-V2` 줄 추가, 그 아래 정보 점검 답 한 줄 추가(사용자 답/제안값 구분, 저장 `fld-locs`, 확정 시 요소 이름)
