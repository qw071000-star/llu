[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-3-4)

3-4 컷 세션으로 시작합니다.
- 판단: "3-4 퍼스트 프레임" = 컷 번호가 있는 작업이라 컷 세션입니다. 컷 카드가 없어 정본에서 초안(v0)을 만들었습니다(`project/cuts/3-4.md`).
- 읽은 것: decisions, shot-list(3-3·3-4·3-5 줄과 연속성 표), asset-registry, 3-3 카드, 퍼스트 프레임 규칙. Higgsfield `fld-3-4 [대기]`는 비어 있고 승인·거절도 0입니다. 3-4는 아직 OK나 핸드오프가 없습니다.
- 지금 할 일: 프롬프트만 씁니다. 생성은 하지 않습니다. 아래 빈 칸이 있어 먼저 묻습니다.

프롬프트를 쓰기 전에 확인할 것이 5개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요.

1. 모드·카메라: 제안 — 새 시점(DERIVED VIEW). 길 쪽 벤치 정면 약 2.5m, 눈높이 약 1.5m, 북쪽을 보는 허리 위 미디엄, 35mm 렌즈, 삼각대 고정. (이유: LC-001-V1은 길 건너편에서 본 원경이라 무릎 위 가방과 손이 보이지 않습니다. 정본에 3-4 카메라가 없습니다.)
2. 0:00 할아버지: 제안 — 벤치 가운데에 앉아 무릎 위 닫힌 가방에 두 손을 얹고, 시선은 가방 걸쇠. 열기 직전의 정지 상태. (이유: 연속성 표의 2-1·3-1과 같은 자세, 3-3→3-4 이음새 "닫힘 유지". 가방은 0:00에 닫혀 있어야 합니다.)
3. 인원: 제안 — 할아버지 1명만 보입니다. 손녀는 화면 밖. (이유: 컷 목록의 3-4 인물은 CH-001·PR-001뿐입니다. 3-3의 손녀가 어디로 가는지는 정본에 없습니다.)
4. 새 시점의 화면 대응: 제안 — 화면 왼쪽 = 서쪽(감나무, 석양 키 라이트 쪽), 화면 오른쪽 = 동쪽(시간표 기둥, 가장자리에 걸쳐 글씨는 읽히지 않게). (이유: 에셋 대장에는 V1의 대응만 있고 이 시점 것은 없습니다. 빛 방향이 서쪽이라 왼쪽이 밝은 면이 됩니다.)
5. 룩 문장: 제안 — 틀의 PALETTE·ERA LOCK 자리에 decisions §3의 `Live-action film look; natural skin tones, restrained saturation.`와 "1990년대 초 늦가을 한국 시골 정류장, 현대 물건·글자 없음"을 씁니다. (이유: 대장에 PALETTE·ERA LOCK 문장이 없습니다.)

이미 정해진 값은 묻지 않습니다: GPT Image 2.5 · 1k · 16:9 · 1장 · 저장 `fld-3-4` · 참조 3장(`loc_busstop_road_v1`, `char_grandpa_autumn_v1`, `prop_doctor_bag_v1`) · 의상·가방·LIGHT LOCK 고정 문장.

답을 받으면 실패 위험 목록(시간표 글씨가 읽힘, 가방이 미리 열림, 손녀·제3의 인물 등장, 가방이 각진 상자로 변함 등)과 막는 문장, 프롬프트를 함께 보여 드립니다.

=== 메타 ===
연 파일(순서대로): PLAYER-RULES.md, CLAUDE.md, .claude/instructions.md, SKILLS-INDEX.md, project/decisions.md, project/asset-registry.md, project/shot-list.md, .claude/skills/production-session/SKILL.md, .claude/skills/image-prompt/SKILL.md, .claude/skills/image-prompt/first-frame.md, sim/higgsfield.md, .claude/skills/production-session/cut-card.md, .claude/skills/higgsfield-generation/SKILL.md, project/cuts/3-3.md(이웃 컷 카드), project/ok-cuts.md(제목 목록만 grep), .claude/skills/video-prompt/SKILL.md(앞 60줄)
부른 [TOOL]: list_folders(project_id=prj-sim-0001), list_project_assets(folder_id=fld-3-4) (생성 도구는 부르지 않음)
고친 정본 파일: project/cuts/3-4.md (신규, 컷 카드 v0 초안). 다른 정본은 고치지 않음
