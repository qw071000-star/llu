[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-3-4)

- 판단 근거: 컷 번호(3-4)와 퍼스트 프레임 요청이라 컷 세션입니다. 3-4 컷 카드가 없어서 정본으로 초안(v0)을 `project/cuts/3-4.md`에 만들었습니다.
- 읽은 것: 확정 사항, 컷 목록(3-3·3-4·3-5 줄, 연속성 표), 에셋 대장(CH-001, PR-001, LC-001-V1), 직전 승인 시작 이미지(3-2) OK 카드. Higgsfield 3-4 폴더는 `[대기]`, 승인·거절·검토 대기 모두 0.
- 지금 할 일: 아래 5개를 확인한 뒤 프롬프트 한 장을 씁니다. 생성은 하지 않습니다.

프롬프트를 쓰기 전에 확인할 것이 5개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요.

1. 카메라와 모드: 제안 — 새 시점(DERIVED VIEW). 길 건너편, 벤치 감나무 쪽 절반 맞은편, 앉은 눈높이, 50mm 미디엄 샷. 할아버지와 무릎 위 가방이 프레임 중심 (이유: 컷 목록에 3-4 장소 뷰가 없고, 확정 뷰 LC-001-V1은 정류장 전체를 보는 35mm라 가방 여는 손이 작게 나옵니다. 3-2는 75mm 투샷, 3-3은 손녀 쪽 50mm라 겹치지 않고, 다음 3-5 손 클로즈업으로 이어집니다)
2. 할아버지 자리와 자세: 제안 — 벤치 감나무 쪽 절반, 등을 정류장 벽에 기댐, 가방은 무릎 위에 가로로 (이유: 연속성 표의 3-4 인물 자리가 "미정"이라, 같은 인물이 나온 직전 승인 시작 이미지인 3-2 카드의 BLOCKING을 가져왔습니다. 빛이 서쪽 감나무 쪽에서 오므로 화면 왼쪽입니다)
3. 0:00 시선: 제안 — 무릎 위 가방을 내려다봄 (이유: 3-2에서는 길을 봤지만 3-3에서 손녀가 돌아선 뒤 이 컷의 사건이 가방 열기입니다. 연기는 절제하고 감정은 시선과 손으로 간다는 확정 사항에 맞춥니다)
4. 0:00 손과 가방: 제안 — 가방은 닫힘(걸쇠 잠김, 컷 목록에 확정). 두 손은 가방 위에 놓고, 놋쇠 걸쇠는 손에 가리지 않게 보임 (이유: 영상에서 걸쇠를 풀어야 하므로 걸쇠가 시작 이미지에서 보여야 합니다. 손은 "오른손" 대신 물건 기준으로 씁니다)
5. 프레임 안 인원: 제안 — 할아버지 1명, 손녀는 프레임 밖 (이유: 컷 목록의 3-4 인물이 CH-001과 PR-001뿐입니다)

정본에 이미 있어서 묻지 않은 것: GPT Image 2.5 · 1k · 16:9 · 보이는 띠 전체, 저장 폴더 `fld-3-4`, 참조 3장(장소 `loc_busstop_road_v1`, 인물 `char_grandpa_autumn_v1`, 소품 `prop_doctor_bag_v1`), 의상·가방 고정 설명문, 빛 고정문, 가방 폭 약 40cm.

=== 메타 ===
연 파일(순서대로): PLAYER-RULES.md, CLAUDE.md, .claude/instructions.md, SKILLS-INDEX.md, .claude/skills/production-session/SKILL.md, project/decisions.md, project/shot-list.md, project/asset-registry.md, .claude/skills/production-session/cut-card.md, sim/higgsfield.md, .claude/skills/image-prompt/SKILL.md, .claude/skills/image-prompt/first-frame.md, project/ok-cuts.md (목록 + 3-2·3-3 시작 이미지 절; 3-3 절은 같은 범위에 걸려 함께 봄)
부른 [TOOL]: list_folders(project_id=prj-sim-0001), list_project_assets(folder_id=fld-3-4) → 3-4 [대기], 모두 0 (시뮬 표 "그 밖")
고친 정본 파일: project/cuts/3-4.md (새로 만든 초안 v0, 사용자가 정하지 않은 값에 (제안값))
