렌즈는 시작 이미지(50mm = 대각 약 47°) 그대로 두고, 나머지는 제안값으로 컷 카드에 적은 뒤 프롬프트를 썼습니다. 생성은 하지 않았습니다. 검사 스크립트는 통과했습니다(5,007자, 걸린 항목 없음).

**정정(제안값 하나):** 끝 자세 "시간표에서 반 걸음 떨어져" → "시작 위치 그대로". 동선이 "걸음 없음"이라 서로 맞지 않아서 맞췄습니다.

**위험 → 막는 문장**
1. 시선이 카메라로 향함 → `Nobody looks at the camera.` + Forbidden `GIRL looking at the camera`
2. 휙 돌아섬 → 3-1 영상에서 OK 받은 속도 문장(눈 → 머리 → 어깨, 약 1.5초) + `Turning within one second = failed take.`
3. 말 없는 입 움직임 → `GIRL does not say a single word: no attempt to speak, no parted lips, no mouthing.`
4. 걸어 나가거나 길로 나감 → `on the spot with no step` + `never steps into the road`
5. 구도가 바뀜 → 시작 이미지가 구도를 통제한다는 문장 + 카메라 고정 문장
6. 시간표 글씨가 읽힘 → Required `The print on the timetable stays illegible marks, not readable text.`
7. 감정 과잉이나 무반응 → `Between worry and resignation; tears, a sigh or a big gesture = failed take, no reaction at all = failed take.`
8. 얼굴 정체성(끝에서 얼굴이 보이고 CH-002는 주근깨가 약함) → `Face, hair, body type and wardrobe 100% match this reference.` 얼굴은 결과에서 확인합니다.

**3-1 영상에서 가져온 줄**(전 → 후)
- 구간 `0:03–0:05` → `0:04–0:06`
- 대사 `says the line in AUDIO once` → 삭제, 걸음 `one small step` → `on the spot with no step`
- 속도 문장 `All movement is slow and even; nothing accelerates suddenly.`은 그대로

```text
[SCENE_CONTEXT]
Late autumn, early 1990s, a rural bus stop at dusk. A girl checks the timetable sign one more time, finds nothing has changed, and turns away from it toward the bench. She says nothing.

[ACTIVE_REFERENCES]
<<<ff_3-3_v1>>> START IMAGE: the exact frame at 0:00. The camera position, lens, framing, composition, the end of the shelter, the timetable sign, the light, colour and brightness, and the position and pose of the girl at 0:00 are exactly this image. The video begins from this image and continues from it without any cut, jump or reframing.
<<<char_girl_raincoat_v1>>> GIRL (10). A yellow raincoat over a navy school uniform, white knee socks and red rain boots. Face, hair, body type and wardrobe 100% match this reference.
REFERENCE AUTHORITY: the start image has sole authority over camera, framing, the place, the light, colour and the 0:00 position. The character reference has authority only over face, hair, body and clothes. Do not take the background, lighting, pose or panel layout from the character reference.

[LOCATION_MAP]
LEFT and RIGHT are SCREEN directions. Places are named by the objects on screen.
LEFT EDGE: the end of the concrete shelter with its corrugated tin roof; the bench is behind it, out of frame. RIGHT HALF: the timetable sign on its pole, and the girl an arm's length from the pole. FOREGROUND: the empty edge of the road. BEHIND: harvested paddies to low hills.
In this view the west, the persimmon-tree side, is screen LEFT. GIRL stays where she stands and never steps into the road.

[FIRST_FRAME_AND_SPATIAL_BLOCKING]
(Scope: FIRST_FRAME only.)
- GIRL: standing at the timetable sign, an arm's length from its pole, facing the sign in three-quarter back view, mid-reading, the hand nearer the sign raised to the printed times, the other arm relaxed at her side.
Exactly 1 person is visible.

[FORMAT_MODE]
Live action. A single continuous take from 0:00 to 0:08. No cuts. 8 seconds.
All movement is slow and even; nothing accelerates suddenly.

[OPTICS]
Diagonal field of view about 47°. The girl and the timetable sign fill the right half of the frame / the end of the shelter sits at the left edge / the bench is out of frame. The girl is sharp and the far paddies are slightly soft.

[CAMERA]
Fixed on a tripod at standing eye level at the near edge of the road, opposite the timetable sign, looking north, at the same position as in the start image, completely locked from 0:00 to 0:08. No pan, no tilt, no zoom, no push-in, no reframing.

[ACTION_TIMING]
0:00–0:04 — GIRL keeps reading; the hand nearer the sign moves once down the printed times, then does not startle; simply stops and rests there.
0:04–0:06 — GIRL turns toward the bench, out of frame at screen LEFT, on the spot with no step: eyes first, then head, then shoulders, about 1.5 s, her feet pivoting last. The hand nearer the sign leaves the sign and lowers to her side.
0:06–0:08 — GIRL stands still where she began, her body turned toward screen LEFT in three-quarter front view, both hands at her sides, her eyes on the bench side out of frame. The shot ends with her standing like this.

[CHARACTER_ACTING]
GIRL: checks the times once more and accepts that nothing has changed; her hand does the checking. Her eyes leave the timetable a beat before her head turns: continuous naturalistic eye life, the gaze drifting and settling rather than locking, realistic blink rate, live wet catchlights. Between worry and resignation; tears, a sigh or a big gesture = failed take, no reaction at all = failed take. Turning within one second = failed take.
Nobody looks at the camera.

[PHYSICS]
motion_owner = CHARACTER: the girl's hand along the times, then her turn (eyes, head, shoulders, feet); no step.
motion_owner = PROP: none; the timetable sign and its pole stay fixed.
motion_owner = CAMERA: none.
motion_owner = ENVIRONMENT: none.

[LIGHTING]
Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. In this view the west is screen LEFT, so the light falls on the girl from screen LEFT.

[AUDIO]
No dialogue. GIRL does not say a single word: no attempt to speak, no parted lips, no mouthing. Distant wind over the paddies and the soft rustle of her raincoat as she turns. No music.

[STYLE]
Live-action film look; natural skin tones, restrained saturation.

[QUALITY]
Facial features clear; skin and fabric textures natural. No distortion of faces or fingers.

[REQUIRED_AND_FORBIDDEN_CONSTRAINTS]
Required:
- Exactly one person (ENTIRE_SHOT)
- The camera stays locked and the framing stays as in the start image (ENTIRE_SHOT)
- The turn happens once, toward screen LEFT, on the spot (INTERVAL 0:04–0:06)
- The print on the timetable stays illegible marks, not readable text (ENTIRE_SHOT)
- The girl ends turned toward screen LEFT, hands at her sides (FINAL_FRAME)
Forbidden:
- GIRL looking at the camera (ENTIRE_SHOT)
- GIRL moving her lips (ENTIRE_SHOT)
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
```

- 모드: image-to-video (시작 이미지 포함 참조 2개, 순서대로 1 `ff_3-3_v1` 시작 이미지 / 2 `char_girl_raincoat_v1` 인물)
- 모델: Seedance 2.5 · 해상도: 480p(확인용) · 길이: 8초 · 화면비 16:9 · 소리: 효과음만(대사 없음)
- 저장 폴더: `fld-3-3` (「빈 정류장」 / 3-3 [진행])
- 예상 비용: 약 40 크레딧 (3-1 영상과 같은 모델·해상도·길이)

이 프롬프트로 480p 한 번 생성할까요? "생성해"라고 하시면 보내겠습니다.

=== 메타 ===
연 파일(순서대로):
- .claude/skills/higgsfield-generation/SKILL.md
- .claude/skills/acting/SKILL.md
- .claude/skills/higgsfield-generation/check_prompt.py (사용법 확인과 실행)
- 앞 턴에 읽은 컷 카드 3-3, 영상 프롬프트 공통·live-action 파일, 확정 사항, 에셋 대장, OK 대장(3-1 영상 카드), ok-reuse.md를 다시 열지 않고 참고
부른 [TOOL]: 없음
고친 정본 파일: project/cuts/3-3.md ([4] 렌즈 확정, [5] 끝 자세, [6] 돌아섬 구간). 임시 파일: tmp/p33.txt, tmp/fixed33.txt
