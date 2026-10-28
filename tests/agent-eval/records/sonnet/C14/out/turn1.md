[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-2-2)

**시작 보고**
- 판단: "2-2" = 컷 세션, 영상 프롬프트. "2-1 표정 유지"는 OK 카드 기준 요청이다.
- 읽은 것: 정본 3개, 2-1 영상 OK 카드, 2-2 시작 이미지 OK 카드, 컷 목록의 앞뒤 줄(2-1, 3-1). 2-2 폴더는 `[진행]`이고 승인된 시작 이미지 `job-ff-2-2` 하나뿐, 영상은 아직 없습니다. 2-2 컷 카드가 없어서 정본에서 초안(v0)을 만들었습니다(`project/cuts/2-2.md`).
- 지금 할 일: 영상 프롬프트에 비어 있는 칸을 채운 뒤 씁니다. 아래 질문에 답해 주세요. 프롬프트는 그다음에 위험 목록과 함께 보여 드리겠습니다.

**2-1에서 가져오는 것: 표정만** (2-1 영상 카드의 `CHARACTER_ACTING` 할아버지 줄, 글자 그대로)
```text
GRANDPA: waits without hoping. Between stillness and quiet resignation; a sigh or a frown = failed take, a smile = failed take. His eyes stay on the empty road on the tree side with slow, heavy blinks.
He never looks at the camera.
```
- 입 움직임 금지 줄(`AUDIO`의 no lip movement, Forbidden의 `GRANDPA moving his lips`)도 같이 옮깁니다.
- 바꾼 단어는 없습니다. 시작 이미지(ff-2-2)도 시선이 감나무 쪽 빈 길이라 그대로 맞습니다.
- 가져오지 않는 것: 2-1의 카메라·렌즈·위치 문장. 2-1은 길 건너 와이드(63°)이고 2-2는 85mm 클로즈업(29°)이라 시작 이미지를 따릅니다. 2-1의 동작(엄지 한 번)도 가져오지 않습니다. 이 컷은 쓰다듬기입니다.

**정본에서 채운 칸** (묻지 않음)
기본값으로 씀: 8초 · 고정 카메라 · 480p · 효과음만 · Seedance 2.5 · 16:9. 저장 `fld-2-2`. 참조 3개(시작 이미지, `char_grandpa_autumn_v1`, `prop_doctor_bag_v1`). 카메라·인물 시작 자세·빛은 ff-2-2 카드에서 가져옵니다.

**미리 보는 위험 → 막는 문장**
1. 클로즈업이라 한숨·찡그림·미소가 크게 보임 → 위 `failed take` 문장
2. 입이 달싹임 → no lip movement 줄
3. 2m 거리에서 카메라를 봄 → `He never looks at the camera.`
4. 쓰다듬다가 걸쇠를 건드려 가방이 열림 → 가방 전환 0번, Required에 "닫힘"
5. 손이 빠르게 문지르거나 커짐, 손가락 왜곡 → 느리고 고른 속도, QUALITY 줄
6. 카메라가 밀고 들어옴 → 완전 고정 문장

**확인할 것** (제안값이 괜찮으면 "그대로", 바꿀 것만 답해 주세요)
1. 쓰다듬는 동작과 타이밍: 제안 — 0:00–0:03 이미 쓰다듬는 중이던 손이 가죽 위를 한 번 천천히 쓸고 멈춤 / 0:03–0:06 시선은 길, 느린 깜박임 / 0:06–0:08 두 손이 가방 위에 쉼. (이유: ff-2-2가 쓰다듬는 도중이고, 사건 수를 하나로 두면 표정이 흔들리지 않습니다.)
2. 끝 상태: 제안 — 같은 자리, 두 손 가방 위, 시선 길. (이유: 3-1 첫 프레임이 두 손 가방 위, 닫힘입니다.)
3. 화면 속 배경: 제가 ff-2-2 이미지를 눈으로 확인하지 못했습니다. 그의 뒤와 좌우로 보이는 것(콘크리트 벽? 벤치? 왼쪽 가장자리 감나무 가지?)을 알려 주세요. 제안 — 뒤는 정류장 벽, 왼쪽 가장자리에 감나무 쪽. 보이지 않는 것은 `LOCATION_MAP`에 쓰지 않겠습니다.
4. 렌즈 관찰 결과: 제안 — "할아버지와 가방만 선명 / 배경은 압축되고 흐림 / 얼굴과 가방이 화면을 채움"(85mm = 29°).

(컷 카드 `project/cuts/2-2.md`에 제안값 표시로 적어 두었습니다. 생성은 하지 않았습니다.)

=== 메타 ===
- 연 파일(순서대로): PLAYER-RULES.md, CLAUDE.md, .claude/instructions.md, SKILLS-INDEX.md, project/decisions.md, project/shot-list.md, project/asset-registry.md, project/ok-cuts.md(목록과 `2-1 영상`·`2-2 시작 이미지` 카드 절만), .claude/skills/production-session/SKILL.md, .claude/skills/production-session/ok-reuse.md, sim/higgsfield.md, .claude/skills/video-prompt/SKILL.md, .claude/skills/video-prompt/live-action.md, .claude/skills/production-session/cut-card.md, .claude/skills/higgsfield-generation/SKILL.md, .claude/skills/acting/SKILL.md, project/cuts/3-1.md(형식 참고용으로 앞부분만, 규칙상 읽지 않았어야 할 다른 컷 카드)
- 부른 [TOOL]: list_folders(project_id=prj-sim-0001), list_project_assets(folder_id=fld-2-2)
- 고친 정본 파일: project/cuts/2-2.md (새로 만든 v0 컷 카드)
- 검사 스크립트(check_prompt.py): 프롬프트를 아직 보이지 않아서 실행하지 않음
