3-3 영상 프롬프트입니다. 렌즈는 시작 이미지 그대로(대각 약 47°)로 정했고, 나머지는 "알아서"로 받아 제안값을 썼습니다. 컷 카드 3-3에 기록했습니다. 아직 생성하지 않았습니다.

```text
[SCENE_CONTEXT]
Early 1990s, late autumn. A rural Korean bus stop at dusk. A ten-year-old girl stands at the timetable sign beside the shelter. In this clip she reads the printed times one more time, lowers her hand, and turns slowly away from the sign toward the shelter.

[ACTIVE_REFERENCES]
<<<ff_3-3_v1>>> START IMAGE: the exact frame at 0:00. The camera position, lens, framing, composition, the shelter, the timetable sign, the light, colour and brightness, and the position and pose of the girl at 0:00 are exactly this image. The video begins from this image and continues from it without any cut, jump or reframing.
<<<char_girl_raincoat_v1>>> GIRL (about ten). A Korean girl of about ten with a round face, straight black hair in a low ponytail and a slim build. A yellow raincoat over a navy school uniform, white knee socks and red rain boots. Face, hair, body type and wardrobe 100% match this reference.
REFERENCE AUTHORITY: the start image has sole authority over camera, framing, the location, light, colour and the 0:00 position. The character reference has authority only over the girl's face, hair, body and clothes.

[LOCATION_MAP]
LEFT and RIGHT are SCREEN directions. Places are named by the objects on screen.
The end of the corrugated-tin-roofed shelter is at the LEFT edge. The painted metal timetable sign on its pole is on the RIGHT, and the girl stands beside it, an arm's length from the pole. The road is in the FOREGROUND; harvested paddies and low hills lie behind.

[FIRST_FRAME_AND_SPATIAL_BLOCKING]
(Scope: FIRST_FRAME only.)
- GIRL: at the timetable sign, an arm's length from its pole, in three-quarter back view facing the sign, mid-reading, the hand nearer the sign raised to the printed times, the other arm relaxed at her side.
- TIMETABLE SIGN: on its pole at RIGHT; the printed times are not legible.
Exactly 1 person is visible.

[FORMAT_MODE]
Live action. A single continuous take from 0:00 to 0:08. No cuts. 8 seconds. All movement is slow and even.

[OPTICS]
Diagonal field of view about 47°. The girl and the timetable sign fill the right half of the frame / the end of the shelter sits at the left edge / the road edge and the paddies behind are all visible, without strong compression. The girl, the sign and the shelter end are sharp; the far hills are slightly soft.

[CAMERA]
Standing eye level at the near edge of the road, opposite the timetable sign, facing north. Fixed and completely locked from 0:00 to 0:08. No pan, no tilt, no zoom, no push-in, no reframing.

[ACTION_TIMING]
0:00–0:03 — The girl reads the timetable again. The fingertip of the hand nearer the sign moves once along the printed times and rests on one row. Her eyes stay on the sign.
0:03–0:04 — The hand comes down slowly to her side. Her eyes stay on the sign.
0:04–0:07 — Her eyes leave the sign a beat before her head; then head, shoulders and feet turn in that order toward the shelter at LEFT over three seconds. She turns on the spot.
0:07–0:08 — She stands facing LEFT toward the shelter, still. The lowered hand rests on the hem of her raincoat. The shot ends with her standing still, eyes on the shelter, not on the camera.

[CHARACTER_ACTING]
GIRL: wants to be sure there is no bus left, then accepts it and turns back toward the shelter. Her hands are busy: the fingertip traces the row once, then the fingers close around the raincoat hem. Naturalistic eye life: micro-saccades, the gaze drifting and settling rather than locking, realistic blink rate, live wet catchlights, the eyes reaching the target a beat before the head turns. Range: between composed and quietly deflated; a crying face, a big sigh or a drooped head = failed take; no reaction at all is also a failed take. Head → shoulders → feet over three seconds; turning within one second = failed take. At the end she does not startle; she simply stops. Nobody looks at the camera.

[PHYSICS]
motion_owner = CHARACTER: the girl's raised hand lowers once; her body turns on the spot; the raincoat follows her turn lightly.
motion_owner = PROP: none; the timetable sign stays still.
motion_owner = CAMERA: none
motion_owner = ENVIRONMENT: none

[LIGHTING]
Low dusk sun from the west, the persimmon-tree side, is the only key; the shelter's single fluorescent tube is off. In this view the west is screen LEFT.

[AUDIO]
No dialogue. The girl does not say a single word: no attempt to speak, no parted lips, no mouthing. Sound effects only: faint evening wind, a soft rustle of the raincoat, a quiet scuff of rubber boots on gravel during the turn. No music.

[STYLE]
Live-action film look; natural skin tones, restrained saturation.

[QUALITY]
Facial features clear; skin and fabric textures natural. No distortion of face or fingers.

[REQUIRED_AND_FORBIDDEN_CONSTRAINTS]
Required:
- Exactly 1 person is visible. (ENTIRE_SHOT)
- The turn takes three seconds, head → shoulders → feet. (INTERVAL 0:04–0:07)
- She faces LEFT toward the shelter, eyes not on the camera. (FINAL_FRAME)
Forbidden:
- No legible text on the timetable sign; the printed times stay unreadable. (ENTIRE_SHOT)
- No walking away; no step out of her place. (ENTIRE_SHOT)
- No second person, no vehicle. (ENTIRE_SHOT)
- Subtitles, watermarks, logos. (ENTIRE_SHOT)
```

- 모드: 영상, image-to-video (실사 15블록)
- 참조(붙일 순서): 1 시작 이미지 `job-ff-3-3` (`<<<ff_3-3_v1>>>`, 구도·빛 권한) · 2 `char_girl_raincoat_v1` (`<<<char_girl_raincoat_v1>>>`, 얼굴·의상만). 장소 참조는 붙이지 않습니다(카드 [7]).
- 모델: Seedance 2.5 · 해상도: 480p 확인 · 길이: 8초 · 16:9 · 소리: 효과음만(대사 없음)
- 저장 폴더: 「빈 정류장」/ 3-3 (`fld-3-3`)

**실패 위험과 막는 문장** (프롬프트에 한 줄씩 넣었습니다)
| 위험 | 막는 문장 (위치) |
|---|---|
| 몸이 휙 돈다 | `Head → shoulders → feet over three seconds; turning within one second = failed take` (CHARACTER_ACTING, REQUIRED) |
| 시선이 카메라로 간다 | `Nobody looks at the camera`, 끝 시선은 정류장 쪽 (CHARACTER_ACTING, REQUIRED) |
| 시간표 글씨가 읽힌다(§7) | `No legible text on the timetable sign` (FORBIDDEN) |
| 말하지 않는데 입이 움직인다 | `does not say a single word: no attempt to speak, no parted lips, no mouthing` (AUDIO) |
| 카메라가 움직이거나 구도가 바뀐다 | `No pan, no tilt, no zoom, no push-in, no reframing` (CAMERA) |
| 걸어 나가거나 다른 인물이 들어온다 | `No walking away; no step out of her place` · `Exactly 1 person is visible` (FORBIDDEN, REQUIRED) |

위 위험은 이 컷에서 실제로 난 실패가 아니라 예상입니다(3-3 영상은 아직 생성한 적이 없습니다).

**검사 결과:** 검사 스크립트 통과(FAIL 0, 참조 수 2 일치, 고정 문장 3개 글자 그대로 포함, 8초). WARN 1개: 길이 5,233자. 15블록 틀의 고정 문장(START IMAGE, REFERENCE AUTHORITY)이 차지하는 분량이라 그대로 두었습니다.

**알아 둘 것**
- 사용자가 말한 "망원"은 승인된 시작 이미지(50mm)와 맞지 않아 시작 이미지를 따랐습니다. 망원이 꼭 필요하면 시작 이미지부터 새로 만들어야 합니다.
- OPTICS의 관찰 결과 3개(손녀와 시간표가 오른쪽 절반 / 정류장 끝이 왼쪽 가장자리 / 배경 논이 보임)는 시작 이미지의 프롬프트 기준이라 이미지를 직접 보고 확인한 것은 아닙니다(추정). 이미지와 다르면 알려 주세요.
- 3-2의 끝 상태는 알 수 없어(영상 없음) 이음새는 의상·빛·시간표 위치만 맞췄습니다.

**다음 선택지:** "생성해"라고 하시면 확인용으로 480p 8초 1개를 `fld-3-3`에 보냅니다(처음 쓰는 설정이면 먼저 견적을 봅니다). 고칠 곳이 있으면 바뀐 줄만 "전 → 후"로 보여 드립니다.

=== 메타 ===
연 파일(순서대로):
- RUN/out/turn1.md, RUN/out/turn2.md (이미 오간 내용)
- RUN/project/cuts/3-3.md
- RUN/.claude/skills/higgsfield-generation/check_prompt.py (검사 스크립트 사용법·규칙 확인)
- RUN/tmp/3-3_video_v1.txt, RUN/tmp/3-3_fixed.txt (작성한 프롬프트와 고정 문장 목록)
부른 [TOOL]: 없음 (생성하지 않음)
고친 정본 파일:
- RUN/project/cuts/3-3.md ([4] 렌즈를 대각 약 47°로 확정, 사용자 답 기록)
- 임시 파일: RUN/tmp/3-3_video_v1.txt, RUN/tmp/3-3_fixed.txt
