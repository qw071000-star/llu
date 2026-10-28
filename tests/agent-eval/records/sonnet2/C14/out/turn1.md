프롬프트를 쓰기 전에 확인할 것이 5개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요.

컷 2-2 카드가 없어서 컷 목록·결정 사항·OK 대장으로 초안(v0)을 만들었습니다 (`project/cuts/2-2.md`). 2-1 영상 OK 카드를 열어 표정 줄을 확인했습니다. 시작 이미지 `job-ff-2-2`는 승인 상태이고 영상 시도는 아직 없습니다.

**2-1에서 가져오는 것 (표정):** 2-1 영상의 할아버지 `CHARACTER_ACTING` 줄 ("waits without hoping", 한숨·찌푸림·미소는 실패 테이크, 느리고 무거운 깜빡임, 카메라를 보지 않음)과 "입술 움직임 금지" 줄을 글자 그대로 옮깁니다. 바뀌는 건 이 컷의 눈 대상 문장뿐이고, 그건 "전 → 후"로 보이겠습니다. 2-1의 낙엽 속도 한계는 이 컷과 무관해서 가져오지 않습니다.

**기본값으로 씀:** 8초 · 16:9 · 고정 카메라(삼각대) · Seedance 2.5 480p · 효과음만 · 렌즈 85mm = 대각 약 29° (시작 이미지 기준). 카메라와 렌즈는 2-1(63°)이 아니라 2-2 시작 이미지를 따릅니다. 표정만 2-1에서 옵니다.

[동작]
1. 쓰다듬기: 제안 — 0:00–0:03 시작 이미지에서 이미 쓰다듬는 중인, 나무 쪽 손(the hand nearer the tree)이 가죽 위를 천천히 한 번 더 쓸고 멈춤 / 0:03–0:08 두 손이 가방 위에 얹혀 정지 (이유: 사건 1개. 2-1에서 엄지 한 번 움직임이 통했고, 반복 쓰다듬기는 속도가 붙거나 가방이 들릴 위험이 있음)
2. 시선: 제안 — 0:00–0:08 내내 나무 쪽 빈 길, 가방도 카메라도 보지 않음 (이유: 2-1의 "기대 안 하는 얼굴"은 시선이 한 점에 머무는 데서 나옴)
3. 끝 상태: 제안 — 같은 자리, 두 손이 가방 위에 얹힌 채 눈은 길, 가방은 닫힘 (이유: 2-1 끝과 같고, 연속성 표의 3-1 시작이 "두 손을 위에")

[카메라·환경]
4. 85mm 관찰 결과 3개: 제안 — 배경 벽이 압축되고 흐림 / 얼굴과 가방 걸쇠만 선명 / 카메라가 물리적으로 멂 (이유: 미디엄 클로즈업 프레임)
5. 환경 움직임: 제안 — 없음 (이유: 머리부터 가방까지만 담는 프레임이라 감나무가 안 들어옴. 2-1의 낙엽 문장은 뺌)

**미리 보는 위험 (생성 전, 막는 문장은 프롬프트에 넣습니다):**
- 입술이 달싹임 → `GRANDPA moving his lips` Forbidden (2-1에서 가져옴)
- 한숨·찌푸림·미소로 표정이 변함 → 범위 문장 "a sigh or a frown = failed take, a smile = failed take" (2-1에서 가져옴)
- 쓰다듬기가 반복되거나 가방이 들리거나 열림 → "한 번만", `never lifted, never opened`
- 시선이 카메라나 가방으로 감 → 눈 대상 문장과 `He never looks at the camera`

**추정:** 시작 이미지 속 얼굴이 2-1의 표정과 맞는지는 이미지를 볼 수 없어 승인 프롬프트("calm and heavy-lidded")로 짐작한 것입니다. 영상은 시작 이미지에서 출발하니, 0:00 얼굴이 다르면 문장만으로는 못 바꿉니다. 결과를 보고 판단해 주세요.

[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-2-2)

=== 메타 ===
연 파일(순서대로): PLAYER-RULES.md, CLAUDE.md, .claude/instructions.md, SKILLS-INDEX.md, .claude/skills/production-session/SKILL.md, project/shot-list.md, project/decisions.md, .claude/skills/production-session/ok-reuse.md, .claude/skills/production-session/cut-card.md, project/ok-cuts.md (목록, 2-1 영상 카드, 2-2 시작 이미지 카드), .claude/skills/video-prompt/SKILL.md, .claude/skills/video-prompt/live-action.md, project/asset-registry.md, sim/higgsfield.md, .claude/skills/higgsfield-generation/SKILL.md
부른 [TOOL]: list_folders(project_id=prj-sim-0001), list_project_assets(folder_id=fld-2-2) (결과는 sim 표에서 확인: 2-2 [진행], 승인 job-ff-2-2, 거절 0, 검토 대기 0)
고친 정본 파일: project/cuts/2-2.md (새로 만든 초안 v0)
