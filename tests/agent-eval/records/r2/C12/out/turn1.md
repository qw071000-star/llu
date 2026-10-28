- 판단: 3-2 컷 세션 · 3-2 영상 프롬프트, 모션은 3-1 영상 OK(`job-v-3-1`)를 기준으로 합니다.
- 읽은 것: 3-2 컷 카드, 컷 목록(3-1~3-3 줄), 확정 사항, OK 대장(3-1 영상 · 3-2 시작 이미지 카드), 3-2 마지막 핸드오프, Higgsfield 3-2 폴더(`3-2 [진행]`, 검토 대기 0 · 승인 `job-ff-3-2` · 거절 1)
- 지금 할 일: 3-1 모션 블록을 그대로 옮기고, 빈 칸 4개만 확인받은 뒤 전문을 보여 드립니다.

[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-3-2)

**3-1 영상에서 가져오는 것 (모션: ACTION_TIMING · PHYSICS · 속도 문장, 글자 그대로)**
- 바꾼 단어: 없음. 인물(GIRL·GRANDPA), 물건(sign·bench·bag·brass clasp), 길이(8초)와 구간이 3-2와 같습니다.
- 속도 문장(FORMAT_MODE): `All movement is slow and even; nothing accelerates suddenly.`

```text
[ACTION_TIMING]
0:00–0:03 — GIRL keeps reading, the hand nearer the sign sliding down the times; GRANDPA sits still, eyes on the road.
0:03–0:05 — GIRL turns toward the bench, eyes first, then head, then shoulders, about 1.5 s, and says the line in AUDIO once.
0:05–0:08 — GRANDPA lowers his eyes to the bag and his thumb rests on the brass clasp; GIRL takes one small step toward the bench and stops. The shot ends with GIRL facing the bench and GRANDPA looking down at the bag.

[PHYSICS]
motion_owner = CHARACTER: the girl's turn and one step; the grandpa's eyes and thumb.
motion_owner = PROP: the bag stays on his lap, closed and heavy; never lifted, never opened.
motion_owner = CAMERA: none.
motion_owner = ENVIRONMENT: none.
```

**알림 — 렌즈:** 컷 카드는 대각 35°인데, 승인된 시작 이미지(`job-ff-3-2`)는 75mm로 만들어져 약 32°입니다. 시작 이미지를 따라 32°로 쓰고, 카드도 고쳤습니다.

**실패 위험 → 막는 문장**
1. 누군가 카메라를 봄 (3-2 시작 이미지에서 실제로 남, `job-ff-3-2-old`) → `Nobody looks at the camera.`
2. 할아버지 입이 움직임 (3-1 모션에서 함께 가져옴) → Forbidden `GRANDPA moving his lips or speaking (ENTIRE_SHOT)` + `GRANDPA does not say a single word: no attempt to speak, no parted lips, no mouthing.`
3. 대사가 두 번 나옴 → Required `The line is spoken exactly once, by the girl (INTERVAL 0:03–0:05)`
4. 가방이 열리거나 들림 → Required `The bag stays closed on his lap (ENTIRE_SHOT)`
5. 가까운 화각에서 카메라가 밀거나 다시 잡음 → CAMERA `completely locked from 0:00 to 0:08. No pan, no tilt, no zoom, no push-in, no reframing.`

기본값으로 씀: Seedance 2.5 · 8초 · 16:9 · 확인 480p · 고정 카메라(길 건너 벤치 가운데 맞은편, 앉은 눈높이, 북쪽) · 소리 켬(대사 "할아버지, 막차 갔대." 한 번, 손녀 목소리 문장은 에셋 대장 그대로) · 룩은 확정 STYLE 문장 · 저장 `fld-3-2`
참조(붙이는 순서): 1 ff_3-2_v1 — 시작 이미지(`job-ff-3-2`) · 2 char_grandpa_autumn_v1 · 3 char_girl_raincoat_v1 · 4 prop_doctor_bag_v1

프롬프트를 쓰기 전에 확인할 것이 4개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요. 바꿀 것만 답해 주시면 됩니다.

[렌즈]
1. 관찰 결과·심도: 제안 — `The bench and the timetable sign fill the frame side by side / the paddies behind are compressed and soft / the camera is physically far away.` 두 사람 모두 선명, 배경만 흐림, 초점 이동 없음. (이유: 승인된 시작 이미지 프롬프트의 75mm · "paddies compressed and soft"와 같게)

[인물]
2. 연기(CHARACTER_ACTING): 제안 — 3-1 영상의 두 사람 연기 줄을 그대로 쓰고, 마지막 줄만 `Neither of them looks at the camera.` → `Nobody looks at the camera.`로 바꿈. (이유: 같은 순간을 섞어 편집하므로 연기가 다르면 튑니다. 카메라 응시를 막는 문장은 하나로 통일) — "모션"만 말씀하셔서 연기는 따로 여쭙니다.
3. 동선에서 지나가지 않는 구역: 제안 — `GRANDPA stays on the bench. GIRL stays between the sign and the bench and never steps into the road.` (이유: 3-1과 같은 제한. 한 걸음이 길 쪽으로 새지 않게)

[이음새]
4. 마지막 프레임 = 다음 컷(3-3) 첫 프레임과 맞출 상태: 제안 — 3-1 끝과 같게(손녀는 벤치를 보고 한 걸음 다가선 자리, 할아버지는 가방을 내려다봄, 가방 닫힘). (이유: 3-2는 3-1과 섞여 쓰이므로 3-3은 둘 중 어느 끝에서도 이어져야 합니다)

답을 주시면 컷 카드에 기록하고 15블록 전문(검사 스크립트 통과본)을 보여 드립니다. 생성은 지시하실 때만 합니다.

=== 메타 ===
연 파일(순서대로):
1. PLAYER-RULES.md
2. CLAUDE.md
3. .claude/instructions.md
4. SKILLS-INDEX.md (+ RUN 파일 목록 확인)
5. project/decisions.md
6. project/shot-list.md
7. project/cuts/3-2.md
8. .claude/skills/production-session/SKILL.md
9. .claude/skills/production-session/ok-reuse.md
10. project/ok-cuts.md — 제목 목록(grep), 목록 표, "### 3-1 영상" 절, "### 3-2 시작 이미지" 절만
11. project/log/3-2_handoff_2026-10-27.md
12. .claude/skills/video-prompt/SKILL.md
13. .claude/skills/video-prompt/live-action.md
14. .claude/skills/acting/SKILL.md
15. .claude/skills/higgsfield-generation/SKILL.md
16. sim/higgsfield.md
17. project/asset-registry.md

부른 [TOOL]:
- list_folders(project_id=prj-sim-0001) → 3-2 [진행] `fld-3-2` (승인 `fld-3-2-ok`, 거절 `fld-3-2-ng`)
- list_project_assets(folder_id=fld-3-2) → 검토 대기 0 · 승인 `job-ff-3-2` · 거절 1 (`job-ff-3-2-old`)

고친 정본 파일:
- project/cuts/3-2.md — [4] 렌즈 35° → 약 32°(시작 이미지 우선), [5] 끝·동선·시선(3-1 모션), [6] 타이밍(3-1 모션), [7] 가져온 OK: 3-1 영상 — 모션, [10] 3-1 모션에서 가져온 위험 3줄 추가

검사 스크립트: 프롬프트 전문을 아직 보이지 않아 돌리지 않음(전문을 보일 때 `--kind video --refs 4`로 실행 예정).
