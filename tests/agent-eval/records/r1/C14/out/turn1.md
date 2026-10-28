[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-2-2)

- 판단: 2-2 컷 세션으로, 영상 프롬프트를 씁니다(생성은 하지 않음). 표정 기준은 OK 대장의 `2-1 영상`(job-v-2-1) 카드입니다.
- 읽은 것: 정본의 2-2 줄, CH-001, PR-001, 폴더 / OK 대장의 `2-2 시작 이미지`(job-ff-2-2)·`2-1 영상` 카드 / Higgsfield `2-2 [진행]` 폴더(승인 job-ff-2-2 1개, 검토 대기·거절 0). 2-2 핸드오프와 컷 카드가 없어서 정본을 바탕으로 컷 카드를 만들었습니다(`project/cuts/2-2.md`).
- 지금 할 일: 프롬프트의 빈 칸 7개를 아래에서 확인한 뒤 전문을 쓰겠습니다.

**이미 정해진 것 (묻지 않음)**
- 형식: Seedance 2.5 · 8초 · 16:9 · 확인 480p · 효과음만(대사 없음) · 저장 `fld-2-2`
- 참조(붙일 순서): 1 시작 이미지 `job-ff-2-2`(카메라·구도·빛·0:00 위치) / 2 `char_grandpa_autumn_v1`(얼굴·머리·몸·옷만) / 3 `prop_doctor_bag_v1`(재질·모양·상태만)
- 카메라: 시작 이미지와 같은 자리, 삼각대 완전 고정(기본값으로 씀)
- 빛·룩: 서쪽(감나무 쪽)의 낮은 해가 유일한 키, 형광등 꺼짐 / STYLE은 확정 문장 그대로
- 가방: 닫힌 채 무릎 위, 끝까지 열리지 않음(3-4에서 열림)

**2-1에서 가져올 표정 블록**: 2-1 영상 `CHARACTER_ACTING`의 GRANDPA 줄을 글자 그대로 옮깁니다. 같은 인물이 같은 길을 보므로 바꾼 단어는 없습니다.
```text
GRANDPA: waits without hoping. Between stillness and quiet resignation; a sigh or a frown = failed take, a smile = failed take. His eyes stay on the empty road on the tree side with slow, heavy blinks.
He never looks at the camera.
```
2-1 결과물은 참조로 붙이지 않습니다. 붙이면 2-1의 넓은 구도가 섞일 수 있어서, 표정은 문장으로만 옮깁니다.

**꼽아 둔 위험 → 막는 문장 (프롬프트에 한 줄씩 넣음)**
1. 쓰다듬다가 걸쇠를 만지거나 가방이 열림 → 손은 가죽만 쓸고, 가방 상태는 한 번도 바뀌지 않음
2. 클로즈업이라 입이 달싹임 → 말하지 않음 문장(no parted lips, no mouthing)
3. 표정이 한숨·찌푸림·미소로 바뀜 → 위 블록의 실패 정의
4. 손이 빨라지거나 같은 동작이 반복됨 → 횟수를 정하고 느린 속도 문장을 넣음
5. 카메라가 밀고 들어감 → 완전 고정 문장
6. 손가락 왜곡 → QUALITY 문장

프롬프트를 쓰기 전에 확인할 것이 7개 있습니다. 바꿀 것만 답해 주세요. 제안값이 괜찮으면 "그대로"라고 해 주세요.

[렌즈]
1. 화각: 제안은 대각 약 29°입니다. 머리부터 무릎 위 가방까지 한 화면에 들어오고, 뒤 정류장 벽은 압축돼 부드럽게 흐리며, 할아버지와 가방만 선명합니다. 초점은 옮기지 않습니다.
   - 이유: 시작 이미지가 85mm 미디엄 클로즈업입니다. 이미지를 실제로 재지 못해 화각은 추정입니다.
   - 거리: 시작 이미지 프롬프트의 "약 2 m"는 85mm로 머리부터 무릎까지 담기 어려운 거리입니다. 그래서 영상 프롬프트에는 거리 숫자를 쓰지 않습니다.

[인물]
2. 시선: 0:00–0:08 내내 감나무 쪽 빈 길을 보고, 가방은 내려다보지 않는 것을 제안합니다.
   - 이유: 시작 이미지와 2-1 표정 블록 모두 길을 봅니다. 가방을 보게 하면 가져온 블록의 시선 줄을 바꿔야 합니다.
3. 쓰다듬기: 감나무에 가까운 손이 0:00–0:05에 가죽을 천천히 두 번 쓸고 멈추는 것을 제안합니다. 다른 손은 계속 가방 위에 둡니다.
   - 이유: 시작 이미지에서 그 손이 쓰다듬는 중입니다. 동작을 하나로 줄여 표정을 지킵니다.
4. 끝(0:05–0:08, 마지막 프레임): 두 손 모두 닫힌 가방 위에 두고, 길을 보는 채로 끝나는 것을 제안합니다.
   - 이유: 다음 컷 3-1의 첫 상태가 "무릎 위, 두 손을 위에"입니다.

[소리·배경·형식]
5. 효과음: 먼 들판의 바람과 가죽을 쓰는 아주 작은 소리를 넣고, 음악은 넣지 않는 것을 제안합니다.
   - 이유: 대사 없는 컷은 효과음만 씁니다. 바람 소리가 2-1과 이어집니다.
6. 배경 움직임: 없음을 제안합니다.
   - 이유: 뒤가 정류장 뒷벽이라 움직일 것이 거의 없습니다. 2-1에서 생긴 낙엽 속도 문제도 피할 수 있습니다.
7. 끝 프레임 이미지: 쓰지 않는 것을 제안합니다.
   - 이유: 꼭 도착해야 할 구도가 없고, 끝 상태는 문장으로 고정합니다.

=== 메타 ===
연 파일(순서대로):
1. PLAYER-RULES.md
2. CLAUDE.md (시스템 지침으로 로드됨)
3. .claude/instructions.md (시스템 지침으로 로드됨)
4. SKILLS-INDEX.md
5. (폴더 목록 확인: out/에 turn0.md 없음, project/cuts/에 2-2 카드 없음, project/log/에 2-2 핸드오프 없음)
6. project/decisions.md
7. project/shot-list.md
8. .claude/skills/production-session/SKILL.md
9. .claude/skills/production-session/ok-reuse.md
10. .claude/skills/production-session/cut-card.md
11. project/asset-registry.md: 헤더, 폴더 표, CH-001, LC-001, PR-001 절만
12. sim/higgsfield.md
13. project/ok-cuts.md: 제목 목록, 목록 표(1–27행), `### 2-1 영상` 절, `### 2-2 시작 이미지` 절만
14. .claude/skills/video-prompt/SKILL.md
15. .claude/skills/video-prompt/live-action.md
16. .claude/skills/acting/SKILL.md
17. project/asset-registry.md: 이름 규칙(29–37행)

부른 [TOOL]:
- list_folders(project_id=prj-sim-0001) → 2-2 [진행] `fld-2-2` (승인 `fld-2-2-ok`, 거절 `fld-2-2-ng`)
- list_project_assets(folder_id=fld-2-2) → 검토 대기 0 / 승인 `job-ff-2-2` / 거절 0

고친 정본 파일:
- project/cuts/2-2.md (새로 만듦. 정본에서 옮긴 값과 가져온 OK를 적고, 렌즈·시선·타이밍·끝 상태·효과음·환경·끝 프레임은 "질문 중"으로 둠. 2,990자)
