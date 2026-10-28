[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-3-4)

- 판단: 3-4 컷 세션으로 시작합니다(할아버지가 무릎 위 가방을 여는 컷). 할 일은 퍼스트 프레임 프롬프트 작성이고, 생성은 하지 않습니다.
- 읽은 것: 컷 목록 3-3~3-5 줄, 이음새·연속성 표의 3-4 행, decisions, 에셋 대장(CH-001, PR-001, LC-001, 폴더)을 읽었습니다. Higgsfield 폴더 `3-4 [대기]`(`fld-3-4`)는 결과물이 0개이고, 3-4의 OK 카드와 핸드오프는 없습니다. 컷 카드가 없어서 정본으로 초안 v0을 만들었습니다(`project/cuts/3-4.md`).
- 지금 할 일: 카메라와 할아버지 0:00 상태가 정본에 없습니다. 이것만 확인하면 바로 프롬프트를 쓰겠습니다.

정본 값을 그대로 씁니다: GPT Image 2.5 · 1k(확인용) · 16:9 · 1장 · 저장 `fld-3-4` · 화면 인원 정확히 1명(할아버지만, 컷 목록 기준) · 가방 닫힘(이음새 3-3→3-4) · 빛은 LC-001 LIGHT LOCK(서쪽 낮은 석양).

프롬프트를 쓰기 전에 확인할 것이 6개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요. 바꿀 것만 답하셔도 됩니다.

[카메라]
1. 모드: 제안 — LC-001-V1을 기준으로 한 새 시점(DERIVED VIEW). 이유: V1은 길 건너에서 찍은 전경이라 무릎 위 가방과 손이 너무 작게 나옵니다. 3-4 장소 뷰 칸도 비어 있습니다.
2. 위치·높이·방향·크기: 제안 — 벤치 정면 약 2.5m 길가에서, 앉은 사람 눈높이(약 1.1m)로 북쪽을 봅니다. 미디엄 샷(머리~무릎, 가방 전체)이고 고정입니다. 이유: V1과 같은 축이라 좌우(왼쪽 감나무, 오른쪽 시간표)가 뒤집히지 않습니다. 2-2의 미디엄 클로즈업, 3-5의 손 클로즈업과도 크기가 겹치지 않습니다.
3. 렌즈: 제안 — 35mm 필름 카메라, 50mm(대각 약 47°), 심도 중간, 초점은 얼굴~가방. 이유: 표정과 손을 한 화면에 선명하게 담고, 필름 룩(§3)에 맞습니다.

[인물 — 할아버지]
4. 벤치 자리: 제안 — 3-1과 같은 자리로 하고, 3-1 시작 이미지 OK 카드에서 할아버지 위치 블록만 가져옵니다. 이유: 같은 장면 안에서 자리가 튀지 않습니다. 원치 않으시면 벤치 가운데, 등은 뒷벽에서 약 10cm로 하겠습니다.
5. 0:00 자세·손: 제안 — 등을 조금 굽히고 앉아, 닫힌 가방(폭 약 40cm, 무릎 폭)을 무릎에 올리고 두 손을 그 위에 얹습니다. 시간표에 가까운 손의 손가락은 놋쇠 걸쇠에 막 닿아 있습니다. 이유: 연속성 표의 "무릎 위·닫힘"을 이어받고, 곧 여는 동작의 시작 상태가 됩니다.
6. 시선: 제안 — 무릎 위 가방과 손을 내려다보고, 카메라는 보지 않습니다. 이유: 절제 연기(§5, 감정은 손과 시선으로)입니다. 3-2 옛 시도가 카메라를 봐서 폐기된 실패도 막습니다.

=== 메타 ===
연 파일(순서대로):
1. PLAYER-RULES.md
2. CLAUDE.md
3. .claude/instructions.md
4. SKILLS-INDEX.md
5. project/shot-list.md
6. project/decisions.md
7. project/asset-registry.md
8. .claude/skills/production-session/SKILL.md
9. .claude/skills/production-session/cut-card.md
10. .claude/skills/image-prompt/SKILL.md
11. .claude/skills/image-prompt/first-frame.md
12. sim/higgsfield.md
13. project/ok-cuts.md (제목 줄만 검색, 3-4 카드 없음 확인) · project/log/ (목록만, 3-4 핸드오프 없음)
14. .claude/skills/video-prompt/SKILL.md (§0 정보 점검표 — first-frame.md가 가리킴)
부른 [TOOL]:
- list_folders(project_id=prj-sim-0001) → 3-4 [대기] fld-3-4 (ok fld-3-4-ok / ng fld-3-4-ng)
- list_project_assets(folder_id=fld-3-4) → 검토 대기 0 · 승인 0 · 거절 0
고친 정본 파일:
- project/cuts/3-4.md (새로 만듦: 컷 카드 초안 v0, 미정 칸은 제안값으로 표시)
