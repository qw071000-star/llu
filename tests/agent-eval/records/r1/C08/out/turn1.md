[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-3-4)

- **판단:** 3-4 퍼스트 프레임 요청 → 3-4 컷 세션입니다.
- **읽은 것:** 정본 3종의 3-4 줄, OK 대장 목차(3-4 카드 없음), 로그(3-4 핸드오프 없음), Higgsfield `fld-3-4` [대기]·결과물 0. 컷 카드가 없어서 정본으로 `project/cuts/3-4.md` v1을 만들었습니다.
- **지금 할 일:** 카메라와 0:00 자세가 정본에 비어 있습니다(컷 목록의 3-4 장소 뷰가 "—"). 아래 4개를 확인하면 프롬프트와 위험 목록을 같이 드립니다.

**정본에서 채운 값**
- GPT Image 2.5 · 확인 1k · 16:9 · 1장 · 저장 `fld-3-4`
- 참조 순서: ① LC-001-V1 `job-lc001v1` 장소 ② CH-001 `char_grandpa_autumn_v1` 얼굴·머리·의상만 ③ PR-001 `prop_doctor_bag_v1` 모양·재질·상태만
- 화면에 1명(CH-001만) · 가방은 0:00에 닫힘, 무릎 위, 폭 약 40cm · 빛은 서쪽의 낮은 해질녘 해 하나

프롬프트를 쓰기 전에 확인할 것이 4개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요. 바꿀 것만 답해 주세요.

1. **카메라·모드:** 제안 — LC-001-V1 기준 새 시점(틀 2)입니다. 정류장 앞 길 쪽에서 북쪽 벤치를 봅니다. 앉은 할아버지 눈높이(약 1.1m), 약 2m 거리, 미디엄 샷(머리~무릎, 가방 전체), 삼각대 고정입니다. 35mm 필름 카메라·50mm 렌즈·Kodak 250D로 쓰고, 화면 왼쪽이 서쪽(감나무, 빛 쪽)입니다.
   (이유: LC-001-V1은 길 건너 와이드라 40cm 가방이 읽히지 않습니다. 3-5가 손 클로즈업이라 3-4는 미디엄으로 둬야 겹치지 않습니다. 기본은 고정·아이레벨입니다.)
2. **할아버지 자리:** 제안 — 벤치 가운데에 앉고, 등은 뒷벽에서 약 20cm, 두 발은 바닥에 둡니다.
   (이유: 위치는 앵커·거리·접촉으로 써야 지켜집니다. 3-1과 같은 자리로 하려면 "3-1처럼"이라고 해 주세요. 그 OK 카드에서 가져오겠습니다.)
3. **0:00 손:** 제안 — 닫힌 가방 위에 두 손을 얹고, 오른손 손가락이 놋쇠 걸쇠에 걸친 상태(열기 직전)입니다.
   (이유: 3-3→3-4 이음새에서 0:00은 닫힘입니다. 2-1·3-1의 "두 손을 위에"와 이어지고, 0:00은 동작 도중이어야 합니다.)
4. **시선:** 제안 — 걸쇠를 내려다봅니다. 카메라는 보지 않습니다.
   (이유: 연기 레지스터는 절제이고 감정은 손과 시선으로 냅니다. 카메라 응시는 폐기된 `job-ff-3-2-old`의 거절 이유였습니다.)

답은 컷 카드에 기록합니다. 생성은 지시하실 때만 합니다.

=== 메타 ===
연 파일(순서대로):
1. PLAYER-RULES.md
2. CLAUDE.md
3. .claude/instructions.md
4. SKILLS-INDEX.md
5. project/decisions.md
6. project/shot-list.md
7. project/asset-registry.md
8. .claude/skills/production-session/SKILL.md
9. .claude/skills/production-session/cut-card.md
10. project/log/ (목록만 — 3-4 핸드오프 없음)
11. project/ok-cuts.md (제목 줄만 검색 — 3-4 카드 없음, 본문 안 읽음)
12. .claude/skills/image-prompt/SKILL.md
13. .claude/skills/image-prompt/first-frame.md
14. sim/higgsfield.md

부른 [TOOL]:
- list_folders(project_id=prj-sim-0001) → 3-4 [대기] `fld-3-4` (승인 `fld-3-4-ok`, 거절 `fld-3-4-ng`)
- list_project_assets(folder_id=fld-3-4) → 검토 대기 0 · 승인 0 · 거절 0

고친 정본 파일:
- project/cuts/3-4.md (새로 만듦, v1. 미정 칸은 제안값과 함께 "[미정·질문 중]"으로 표시)
