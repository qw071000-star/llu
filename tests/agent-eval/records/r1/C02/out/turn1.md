[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-3-2)

- 판단: "3-2" → 3-2 컷 세션입니다. 지난 핸드오프(10-27)의 다음 할 일 "3-2 영상 프롬프트"부터 이어 갑니다.
- 읽은 것: 3-2 컷 카드, 컷 목록 3-2 줄·이음새 표, 확정 사항, 에셋 대장(CH-001·CH-002·LC-001·PR-001·3-2 폴더), OK 대장 "3-2 시작 이미지", 3-2 핸드오프, Higgsfield 3-2 폴더.
- 지금 할 일: 영상 프롬프트를 쓰기 전에 빈칸 5개를 확인합니다(아래).

**현재 상태**
- Higgsfield `3-2 [진행]`(`fld-3-2`): 컷 목록 상태 `진행`과 같습니다. 검토 대기 0 · 승인 `job-ff-3-2`(시작 이미지) · 거절 1 `job-ff-3-2-old`(할아버지 카메라 응시).
- 영상은 아직 없습니다.

**정해져 있어 묻지 않는 것:** Seedance 2.5 · 확인 480p · 8초 · 16:9 · 소리 켬(대사) · 저장 `fld-3-2` · 시작 이미지 `job-ff-3-2` · 카메라 길 건너편 벤치 가운데 맞은편, 앉은 눈높이, 북쪽, 고정 · 빛 서쪽(감나무 쪽) 낮은 석양 하나 · 가방 무릎 위 닫힘 유지 · 실사 필름 룩 · 절제 연기 · 막는 문장 "Nobody looks at the camera".

프롬프트를 쓰기 전에 확인할 것이 5개 있습니다. 제안값이 괜찮으면 "그대로"라고 하시고, 바꿀 것만 답해 주세요.

[동작 기준]
1. 동작·타이밍·대사·시선·연기를 3-1 영상 OK(`job-v-3-1`)와 같게 할까요? 제안 — 예. OK 대장 "3-1 영상" 카드에서 ACTION_TIMING, AUDIO 대사 줄, 시선, CHARACTER_ACTING을 글자 그대로 가져오고 카메라·렌즈·시작 이미지 줄만 3-2 것으로 바꿉니다. (이유: 카드 완료 조건과 컷 목록 이음새가 "3-1과 같은 동작·타이밍"이고, 편집에서 3-1과 섞어 씁니다.) 아니라면 끝 위치·동선·시선·타이밍·대사를 따로 제안해 여쭙겠습니다.

[카메라]
2. 렌즈 화각: 카드는 대각 35°인데, 확정 시작 이미지 프롬프트는 "75mm lens"(Alexa Mini)로 보냈습니다. 대각 약 20–25°에 해당합니다(계산 추정). 제안 — 시작 이미지 쪽, 대각 약 25°로 카드를 맞춥니다. (이유: 영상은 시작 이미지 화면에서 출발합니다. 수치가 어긋나면 0:00 뒤에 화면을 다시 잡을 위험이 있습니다.)
3. 관찰 결과 3개 + 심도: 제안 — 벤치와 시간표가 나란히 화면을 채운다 / 뒤 논은 압축되고 흐리다 / 카메라는 길 건너 멀리 있다 · 두 사람 모두 선명, 초점 이동 없음. (이유: 시작 이미지 CAMERA 문장과 같은 화면입니다.)

[이음새]
4. 끝 프레임 이미지: 제안 — 안 씀. (이유: 고정 카메라이고 꼭 도착해야 할 구도가 없습니다. 끝 상태는 타이밍 블록으로 고정합니다.)
5. 다음 컷(3-3) 첫 프레임과 맞출 것: 제안 — 없음. (이유: 컷 목록 이음새 표에 3-2→3-3 항목이 없습니다.)

답을 주시면 컷 카드에 기록하고, 위험 목록과 프롬프트를 먼저 보여 드립니다. 생성은 그다음에 지시하실 때만 합니다.

=== 메타 ===
연 파일(순서대로):
1. PLAYER-RULES.md
2. CLAUDE.md
3. .claude/instructions.md
4. SKILLS-INDEX.md
5. .claude/skills/production-session/SKILL.md
6. (줄 수만 확인: project/*.md, project/cuts/*.md, project/log/*.md, sim/higgsfield.md — wc -l, 내용은 안 읽음)
7. project/cuts/3-2.md
8. project/shot-list.md — 머리말(1–8줄), 3-2 줄, 이음새·소품 연속성 표(20–35줄)만
9. project/decisions.md
10. project/log/3-2_handoff_2026-10-27.md
11. project/ok-cuts.md — 제목 목록(grep), 머리말·목록(1–25줄), "### 3-2 시작 이미지" 절(360–390줄)만
12. sim/higgsfield.md
13. .claude/skills/video-prompt/SKILL.md
14. project/asset-registry.md — 관련 줄 grep 후 머리말·폴더(1–12줄), 3-2 폴더 줄, CH-001·CH-002(38–65줄), LC-001·PR-001(79–104줄)만
15. .claude/skills/video-prompt/live-action.md

부른 [TOOL]:
- list_folders(project_id=prj-sim-0001) → 3-2 [진행] fld-3-2 (승인 fld-3-2-ok, 거절 fld-3-2-ng)
- list_project_assets(folder_id=fld-3-2) → 검토 대기 0 · 승인 job-ff-3-2 · 거절 1 (job-ff-3-2-old)

고친 정본 파일: 없음
