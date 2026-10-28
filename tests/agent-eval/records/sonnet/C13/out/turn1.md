[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-3-5)

3-5 첫 프레임을 쓰기 전에 확인할 것이 6개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요. 일부만 답하셔도 됩니다.

**판단한 것**
- 3-5는 컷 카드가 없어서 정본으로 초안(`project/cuts/3-5.md`, v0)을 만들었습니다. 모르는 칸은 비워 두었습니다.
- "3-1처럼"은 OK 대장의 `3-1 시작 이미지`(job-ff-3-1, OK 이유 "색감, 질감")에서 가져옵니다. 영상 카드(`3-1 영상`)가 아니라 이미지 카드로 읽었습니다. 영상 쪽 색감을 뜻하셨다면 말씀해 주세요.
- 그 프롬프트에는 색·질감 문장이 따로 없습니다. 색은 장소 뷰(LC-001-V1)에서 왔고, 3-5는 카메라가 다릅니다. 그래서 문장을 지어내지 않고 3-1 이미지를 색 참조로 붙이고, 권한을 "색·콘트라스트·질감만"으로 좁히겠습니다. 구도·인물·빛 방향은 가져오지 않습니다.
- 정본에서 가져온 값은 다시 묻지 않습니다. GPT Image 2.5 · 1k · 16:9, 저장 `fld-3-5`, 빛은 서쪽 저녁 햇빛 하나(LIGHT LOCK), 가방은 열림(§6), 연기는 절제(§5)입니다.

**확인할 것**
1. 카메라: 제안 — 길 건너편 벤치 가운데 맞은편, 앉은 눈높이, 북쪽, 고정. 손과 가방 입구가 프레임을 채우는 클로즈업, 85mm. (이유: §4 기본이 고정·아이레벨이고, 3-2의 75mm 투샷보다 한 단계 더 가깝게 잡았습니다. 장소 뷰와 카메라가 달라 새 시점 방식으로 씁니다.)
2. 가방 안: 제안 — 내용물은 보이지 않게, 어두운 안감만. (이유: 안에 무엇이 있는지 정본에 없습니다. 정해지면 바로 반영합니다.)
3. 손: 제안 — 걸쇠가 열린 입구 가장자리 위에 한 손(가방 걸쇠에 가까운 손)이 멈춰 있고, 다른 손은 손잡이 쪽에 둡니다. 거칠고 마디 굵은 늙은 손에 올리브색 재킷 소매 끝이 보입니다. (이유: §5 "감정은 손과 시선으로". 동작이 아니라 멈춘 순간입니다.)
4. 얼굴: 제안 — 프레임 밖(손, 가방, 무릎, 조끼 일부만). (이유: 클로즈업이고 시선 문제를 피합니다. 이러면 얼굴 참조는 붙이지 않고 의상 문장만 씁니다.)
5. 이음새: 제안 — 3-4 끝의 열린 가방 상태에서 그대로 시작합니다. 3-4 카드가 아직 없어서 3-4 끝 구도는 비어 있습니다. 이 값은 총괄에 올릴 것으로 적겠습니다.
6. 이 컷의 영상 쪽도 같이 정할까요: 제안 — 지금은 첫 프레임만 정하고, 영상(길이·움직임)은 이 프레임이 승인된 뒤에 묻습니다. (이유: 한 번에 한 가지씩 확정합니다.)

답을 받으면 위험 목록과 프롬프트를 함께 보여 드리겠습니다. 생성은 그 뒤에 지시해 주실 때만 합니다.

=== 메타 ===
연 파일(순서대로):
- PLAYER-RULES.md, CLAUDE.md, .claude/instructions.md, SKILLS-INDEX.md
- project/decisions.md, asset-registry.md, shot-list.md, cuts/3-1.md, cuts/3-2.md, cuts/3-3.md, log/3-1_handoff_2026-10-26.md, log/3-2_handoff_2026-10-27.md
- sim/higgsfield.md
- .claude/skills/production-session/SKILL.md, production-session/ok-reuse.md, production-session/cut-card.md
- .claude/skills/image-prompt/SKILL.md, image-prompt/first-frame.md
- .claude/skills/higgsfield-generation/SKILL.md
- .claude/skills/video-prompt/SKILL.md (정보 점검표만)
- project/ok-cuts.md (목록, 3-1 시작 이미지 / LC-001-V1 / 3-2 시작 이미지 / 3-3 시작 이미지 카드)
부른 [TOOL]:
- [TOOL] list_folders(project_id=prj-sim-0001)  → 3-5 [대기], fld-3-5
- [TOOL] list_project_assets(folder_id=fld-3-5)  → 검토 대기 0 / 승인 0 / 거절 0
(생성 도구는 부르지 않음)
고친 정본 파일:
- project/cuts/3-5.md (새로 만듦, v0 초안. 빈 칸은 질문 답 후 채움)
