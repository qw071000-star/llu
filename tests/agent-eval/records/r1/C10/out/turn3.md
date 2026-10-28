렌즈는 시작 이미지 그대로(대각 약 34°) 두었고, 나머지 7개는 제안값으로 썼습니다. 컷 카드 [4]~[7]과 [10]에 기록했고, 제안값으로 정한 칸에는 `제안값`이라고 표시했습니다.

**위험 → 막는 문장**
1. 휙 돌아섬 → `Head → shoulders → feet over three seconds; turning within one second = failed take.`
2. 돌아서면서 카메라를 봄 → `Nobody looks at the camera.` (끝에 향하는 쪽은 화면 왼쪽)
3. 대사가 없는데 입이 움직임(Seedance는 소리가 기본으로 켜짐) → `no attempt to speak, no lip movement`
4. 시간표에서 걸어 나감 → `The girl stays at the timetable sign, an arm's length from its pole; no step away.`
5. 시간표 글씨가 읽힘(§7) → `The printed times stay unreadable.`
6. 정류장 쪽으로 돌 때 다른 사람이 생김 → `Exactly 1 person is visible.` + `the bench inside it is out of frame`
7. 울상이나 한숨, 또는 무표정 → `Between matter-of-fact and quietly worried; … = failed take`
8. 0:00에서 화면이 튀거나 카메라가 움직임 → START IMAGE 문장 + `Fixed and completely locked from 0:00 to 0:08.`

- 모드: 시작 이미지에서 영상으로(image-to-video), 실사 15블록
- 시작 이미지: `job-ff-3-3`(`<<<ff_3-3_v1>>>`)이 0:00 프레임·카메라·빛을 정함 · 끝 이미지는 쓰지 않음
- 붙일 요소: 1 `char_girl_raincoat_v1`(얼굴·머리·의상만)
- 모델: Seedance 2.5 · 확인 480p · 8초 · 16:9
- 소리: 효과음만(바람, 마른 풀, 돌아설 때 장화 소리 한 번). 대사와 음악은 없음
- 저장: `fld-3-3` (3-3 [진행])
- 검사 스크립트: 통과(4,993자, 걸린 항목 없음)

```text
[SCENE_CONTEXT]
Early 1990s, late autumn, a rural bus stop in Korea at dusk. A ten-year-old girl is reading the timetable sign beside the shelter. She checks the printed times once more, stops, and turns away toward the shelter.

[ACTIVE_REFERENCES]
<<<ff_3-3_v1>>> START IMAGE: the exact frame at 0:00. The camera position, lens, framing, composition, the shelter, the timetable sign, the light, colour and brightness, and the girl's position and pose at 0:00 are exactly this image. The video continues from this image without any cut, jump or reframing.
<<<char_girl_raincoat_v1>>> GIRL (about ten). A yellow raincoat over a navy school uniform, white knee socks and red rain boots. Face, hair, body type and wardrobe 100% match this reference.
REFERENCE AUTHORITY: the start image has sole authority over camera, framing, the location, light, colour and the 0:00 position. The character reference has authority only over her face, hair, body and clothes. Do not take the background, lighting, pose or panel layout from the character reference.

[LOCATION_MAP]
LEFT and RIGHT are SCREEN directions. Places are named by the objects on screen.
LEFT EDGE: the end of the concrete shelter; the bench inside it is out of frame. RIGHT HALF: the painted metal timetable sign on its pole, with the girl in front of it. BACKGROUND: harvested rice paddies stretching to low hills. The low sun is off screen LEFT.

[FIRST_FRAME_AND_SPATIAL_BLOCKING]
(Scope: FIRST_FRAME only.)
- GIRL: at the timetable sign, an arm's length from its pole, facing the sign in three-quarter back view, mid-reading, the hand nearer the sign raised to the printed times.
Exactly 1 person is visible.

[FORMAT_MODE]
Live action. A single continuous take from 0:00 to 0:08. No cuts. 8 seconds.
All movement is slow and even; nothing accelerates suddenly.

[OPTICS]
Diagonal field of view about 34°, the same as the start image. The girl and the sign fill the right half of the frame / the end of the shelter stays at the left edge / the paddies and hills behind are slightly soft. The girl and the sign stay sharp; no focus pull.

[CAMERA]
From the near edge of the road at standing eye level, opposite the timetable sign, looking north. Fixed and completely locked from 0:00 to 0:08. No pan, no tilt, no zoom, no push-in, no reframing.

[ACTION_TIMING]
0:00–0:03 — the fingertip of the hand nearer the sign slides slowly down one column of printed times, once.
0:03–0:04 — the finger stops on one line; she does not startle, simply stops. The hand lowers and closes on the hem of her raincoat.
0:04–0:07 — she turns on the same spot toward screen LEFT, toward the shelter: eyes first, then head, shoulders and feet, over three seconds.
0:07–0:08 — she stands still in profile facing screen LEFT, the hand still holding her raincoat hem, her gaze low on the ground toward the shelter. The shot ends with her in this pose, the timetable sign behind her.

[CHARACTER_ACTING]
GIRL: Character acting as GIRL. Ten, quick, practical. Hides worry by doing something with her hands. She searches the printed times for a bus that may still come. Continuous naturalistic eye life: micro-saccades and gaze targeting, the gaze drifting and settling rather than locking, realistic blink rate tied to state, live wet catchlights, the eyes reaching the target a beat before the head turns. Between matter-of-fact and quietly worried; a tearful face or a visible sigh = failed take, a blank, empty face = failed take. Head → shoulders → feet over three seconds; turning within one second = failed take. Nobody looks at the camera.

[PHYSICS]
motion_owner = CHARACTER: the girl only. The raincoat swings slightly with the turn and settles; her rain boots pivot on the same spot.
motion_owner = PROP: none.
motion_owner = CAMERA: none.
motion_owner = ENVIRONMENT: a faint breeze in the dry paddy stubble; nothing else moves.

[LIGHTING]
Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. In this view the west is screen LEFT. The light does not change during the shot.

[AUDIO]
GIRL does not say a single word; no attempt to speak, no lip movement. Sound effects: a faint wind, dry grass rustling, one soft scuff of her rubber rain boots as she turns. No music.

[STYLE]
Live-action film look; natural skin tones, restrained saturation.

[QUALITY]
Facial features clear; skin and fabric textures natural. No distortion of her face or fingers.

[REQUIRED_AND_FORBIDDEN_CONSTRAINTS]
Required:
- Exactly 1 person is visible. (ENTIRE_SHOT)
- The girl stays at the timetable sign, an arm's length from its pole; no step away. (ENTIRE_SHOT)
- The printed times stay unreadable. (ENTIRE_SHOT)
- The turn takes three seconds: eyes, head, shoulders, feet. (INTERVAL 0:04–0:07)
- She ends in profile facing screen LEFT, the timetable sign behind her. (FINAL_FRAME)
Forbidden:
- Subtitles, text, watermarks, logos. (ENTIRE_SHOT)
- Anything more recent than the early 1990s. (ENTIRE_SHOT)
```

- 3-4 카드가 아직 없어서 이음새 값(손녀의 끝 자세)을 이웃 카드에는 적지 못했습니다. 핸드오프 때 총괄에 올리겠습니다.
- 다음: 이대로 480p 확인 생성을 지시하시거나, 바꿀 줄을 말씀해 주세요. 생성은 지시하실 때만 합니다.

=== 메타 ===
연 파일(순서대로):
1. .claude/skills/higgsfield-generation/SKILL.md (§1의 프롬프트 자동 검사 방법을 보려고)
2. .claude/skills/higgsfield-generation/check_prompt.py (`--help`와 검사만 실행, 내용은 읽지 않음. 1차 5,548자 WARN → 겹치는 문장을 줄여 4,993자로 통과)
3. project/cuts/3-3.md (다시 읽고 수정)
- 작업용 사본: /tmp/claude-0/-home-user/dca0a83f-e443-5698-9f4c-755968d364fc/scratchpad/c10/prompt_3-3_v1.txt (프롬프트), must.txt (고정 설명문 3줄)
- 그 밖에는 1·2턴에서 읽은 내용(OK 대장 "3-3 시작 이미지", 에셋 대장 CH-002·LC-001, decisions §1~§7, live-action.md, acting/SKILL.md)을 썼습니다.

부른 [TOOL]: 없음 (생성 지시가 없어 보내지 않음)

고친 정본 파일:
- project/cuts/3-3.md
  - [4] `[고정/움직임]` → `고정(§4 기본값)`. 렌즈는 "확인 중" → `시작 이미지 그대로, 대각 약 34°` (사용자 답) + 관찰 결과 (제안값)
  - [5] 끝(마지막 프레임)·동선·시선을 채움, 연기 줄을 추가함 (제안값)
  - [6] 타이밍·이음새를 채움 (제안값)
  - [7] `끝 프레임 없음 (제안값)`을 추가함
  - [10] 예상 위험 7개와 막는 문장을 적음
