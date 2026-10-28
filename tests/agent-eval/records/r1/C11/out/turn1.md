[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-1-1)

- **판단:** 1-1 컷 세션입니다. 인물이 없는 배경 영상이라 4문단 형식(Camera / Motion / Keep / 소리)으로 씁니다.
- **읽은 것:** 컷 목록 1-1 줄(진행, 시작 이미지 `job-ff-1-1`), 확정 사항, 에셋 대장(LC-001·폴더), OK 대장「1-1 시작 이미지」, Higgsfield 1-1 폴더(`1-1 [진행]` · 검토 대기 0 · 승인 `job-ff-1-1` · 거절 1). 1-1 핸드오프는 없습니다. 컷 카드가 없어서 정본으로 `project/cuts/1-1.md` v1을 만들었습니다.
- **지금 할 일:** 빈 칸 2개를 먼저 여쭙니다. 답을 받으면 위험 목록과 프롬프트를 보여 드리고, 생성은 그다음에 합니다.

**정본에서 채운 것**
- 시작 이미지: `job-ff-1-1` (OK 이유 "하늘 색 좋아")
- 모델·설정: Seedance 2.5 · 확인용 480p · 8초 · 16:9 (확정 사항 기본값). 길이는 배경 스킬 권장(10~15초)보다 짧지만 확정 사항의 컷당 8초를 따릅니다.
- 저장: 「빈 정류장」/1-1 [진행] `fld-1-1`
- 카메라: 고정. 확정 사항 §4의 기본값을 씁니다.
- 유지할 것: 실사 필름 룩, 정류장·양철 지붕·시간표 기둥·감나무·길·논·낮은 산의 형태, 화면 왼쪽(서쪽)의 낮은 해, 꺼진 형광등
- 소리: 효과음만 넣습니다(확정 사항 §2). 배경 스킬의 기본값은 무음이지만 정본을 따릅니다.

**예상 위험** (프롬프트에 위험마다 막는 문장을 한 줄씩 넣습니다)
1. 사람·차·동물이 나타남
2. 해가 지면서 빛 방향이나 밝기가 바뀜, 형광등이 켜짐
3. 정류장·감나무 형태가 녹거나 변형됨, 시간표에 글자가 생김
4. 고정 카메라가 흘러가거나 줌이 들어감

---

프롬프트를 쓰기 전에 확인할 것이 2개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요.
1. **움직일 것:** 구름은 화면 오른쪽으로 아주 천천히 흐르게 하고(8초 동안 화면 폭의 약 2%), 논 그루터기와 길가 마른 풀은 약한 바람에 살짝 흔들리게 하는 것을 제안합니다. 해·빛·감나무는 움직이지 않습니다.
   (이유: 8초에 움직임이 둘이면 서두르는 느낌이 나지 않습니다. 해가 지는 움직임을 넣으면 빛이 바뀌어 시작 이미지와 어긋날 위험이 큽니다.)
2. **효과음:** 마른 들판을 스치는 약한 바람 소리 하나만 넣고, 대사와 음악은 넣지 않는 것을 제안합니다.
   (이유: 화면에서 소리를 낼 것은 바람뿐입니다. 새나 차 소리를 넣으면 화면에 없는 소리가 됩니다.)

기본값으로 정한 것(카메라 고정, 8초, 480p)도 바꾸고 싶으면 그것만 말씀해 주세요.

=== 메타 ===
연 파일(순서대로):
1. PLAYER-RULES.md
2. CLAUDE.md
3. .claude/instructions.md
4. SKILLS-INDEX.md (같은 명령으로 out/ 폴더와 RUN 파일 이름 목록도 확인. out/turn0.md 없음)
5. .claude/skills/production-session/SKILL.md
6. project/shot-list.md
7. project/decisions.md
8. project/asset-registry.md
9. .claude/skills/production-session/cut-card.md
10. project/ok-cuts.md — 제목 줄(`^##`)만 검색한 뒤「### 1-1 시작 이미지」절(115–137행)만 읽음
11. sim/higgsfield.md
12. .claude/skills/video-prompt/SKILL.md
13. .claude/skills/higgsfield-generation/SKILL.md
14. .claude/skills/video-prompt/background.md
(project/log/는 1-1 핸드오프가 없어서 열지 않음. 다른 컷 카드는 열지 않음)

부른 [TOOL]:
- list_folders(project_id=prj-sim-0001) → 1-1 [진행] `fld-1-1` (승인 `fld-1-1-ok`, 거절 `fld-1-1-ng`)
- list_project_assets(folder_id=fld-1-1) → 검토 대기 0 · 승인 `job-ff-1-1` · 거절 1

고친 정본 파일:
- project/cuts/1-1.md (새로 만듦 · 컷 카드 v1. [4] 카메라 고정(기본값), [6] 움직일 것과 [3] 효과음 내용은 "미정(질문 중)")
