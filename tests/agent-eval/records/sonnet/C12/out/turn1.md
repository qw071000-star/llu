[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-3-2)

- 판단: 컷 번호(3-2)와 "3-1의 모션" → 3-2 컷 세션, 기준은 OK 대장 "3-1 영상"(`job-v-3-1`).
- 읽은 것: 3-2 컷 카드, 3-2 핸드오프, 컷 목록(3-1~3-3 줄·이음새), 결정 사항, 에셋 대장, OK 카드 `3-1 영상`·`3-2 시작 이미지`. Higgsfield 폴더 `3-2 [진행]`: 검토 대기 0, 승인 시작 이미지 `job-ff-3-2`, 거절 1.
- 지금 할 일: 3-1 모션을 가져와 3-2 영상 프롬프트를 쓴다. 아래 3개가 비어 있어 먼저 묻는다. 프롬프트는 답을 받은 뒤에 보입니다(생성은 하지 않습니다).

**3-1에서 그대로 가져온 것 (모션)** — 컷 카드 [5][6][7]에 적어 두었습니다.
- `ACTION_TIMING` 3구간: 0:00–0:03 손녀 읽기 / 0:03–0:05 눈→머리→어깨 약 1.5초로 돌아서며 대사 한 번 / 0:05–0:08 할아버지 시선 가방·엄지 걸쇠, 손녀 작은 한 걸음 후 정지
- `PHYSICS`: 손녀의 돌아섬과 한 걸음, 할아버지 눈과 엄지만 움직임. 가방은 닫힌 채 무릎 위. 카메라 고정
- 속도 문장 "All movement is slow and even…"
- 같이 가져오는 위험: 할아버지 입 움직임 → `no attempt to speak, no lip movement`, 대사 두 번 → `exactly once`, 할아버지가 손녀를 봄 → `He never looks at the girl`. 3-2 자체 위험: 카메라 응시 → `Nobody looks at the camera`
- 바뀌는 단어: 없음(인물·소품·길이 8초·대사 모두 같음). 번호는 본문에 쓰지 않습니다.
- 기본값으로 씀: 8초 · 고정 카메라 · 480p 확인 · 대사 소리 켬(바람, 음악 없음)

프롬프트를 쓰기 전에 확인할 것이 3개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요.

[카메라]
1. 화각: 컷 카드는 35°인데 승인된 시작 이미지는 75mm 렌즈로 만들었습니다(≈32°). 시작 이미지가 이기므로 제안 — 대각 약 32°. 관찰 결과 3개: 벤치와 시간표가 한 화면에 나란히 / 직선 유지 / 뒤 논밭은 눌려서 흐림. 심도: 배경만 흐린 얕은 심도, 초점 이동 없음 (이유: 시작 이미지 프롬프트의 문장 그대로). 3-1의 63°·깊은 초점은 카메라 요소라 가져오지 않았습니다.

[연기]
2. 연기 범위: 모션만 가져왔고 연기 문장은 따로 정합니다. 제안 — 3-1과 같게: 손녀는 걱정과 조급 사이(울음·장난스러운 톤 = 실패), 할아버지는 가만함과 조용한 체념 사이(한숨·찡그림, 무반응 = 실패). 이유: 같은 순간이고 §5 절제 연기에 맞음. 가까워진 만큼 눈과 손으로만 보이게 함.

[이음새]
3. 다음 컷 3-3 첫 프레임과 맞출 것: 3-3은 "손녀가 시간표를 한 번 더 보고 돌아선다"(손녀만)인데, 3-1 모션의 끝은 손녀가 벤치를 보고 서 있는 상태입니다. 제안 — 3-2는 3-1 끝 상태 그대로 끝내고, 시간표로 되돌아가는 동작은 3-3에서 처리(이유: 3-2에 사건을 더하면 3-1과 어긋나 편집에서 섞기 어려움). 3-3 시작 이미지의 손녀 위치는 아직 보지 않았으니, 3-2 끝 위치와 맞는지는 프롬프트 뒤에 확인하겠습니다. 이 방식이면 됩니까?

=== 메타 ===
연 파일(순서대로): PLAYER-RULES.md, CLAUDE.md, .claude/instructions.md, SKILLS-INDEX.md, .claude/skills/production-session/SKILL.md, .claude/skills/production-session/ok-reuse.md, project/decisions.md, project/shot-list.md, project/cuts/3-2.md, project/log/3-2_handoff_2026-10-27.md, project/ok-cuts.md(목록과 `### 3-1 영상`, `### 3-2 시작 이미지` 절), project/cuts/3-1.md, project/asset-registry.md, .claude/skills/video-prompt/SKILL.md, .claude/skills/video-prompt/live-action.md, .claude/skills/higgsfield-generation/SKILL.md, .claude/skills/acting/SKILL.md, sim/higgsfield.md
부른 [TOOL]: list_folders(project_id=prj-sim-0001), list_project_assets(folder_id=fld-3-2)
고친 정본 파일: project/cuts/3-2.md ([5] 끝·동선·시선, [6] 타이밍, [7] 가져온 OK 줄)
