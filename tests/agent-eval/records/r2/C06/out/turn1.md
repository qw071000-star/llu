[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-props)
[TOOL] list_project_assets(folder_id=fld-3-4)

- 판단: 새 소품 에셋(PR-002 할머니 사진 액자)이라 총괄 세션으로 진행합니다.
- 읽은 것: decisions·shot-list·asset-registry, 소품·생성 스킬, Higgsfield 폴더(소품 폴더 `fld-props`와 3-4 폴더 `fld-3-4` 모두 비어 있음). OK 대장에 액자 카드는 없습니다.
- 지금 할 일: 소품 정보를 채운 뒤 위험 목록과 프롬프트를 먼저 보여 드립니다. 이번 답에서는 생성하지 않습니다.

정본에서 이미 정해진 값(묻지 않음):
- 모델 GPT Image 2.5 · 확인용 1k · 16:9 · 1장 (decisions §1·§2)
- 저장 `00 에셋 / 소품` `fld-props` (에셋 대장)
- 신규 생성 · 참조 없음 · 무배경 회색 스튜디오 소품 사진
- 1990년대 초 시골, 현대 물건·글자 금지 (decisions §3·§7)
- 가방 PR-001 폭 약 40cm (decisions §6)

프롬프트를 쓰기 전에 확인할 것이 6개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요. 바꿀 것만 답해 주셔도 됩니다.

1. 액자 재질·모양: 제안 — 짙은 갈색 나무 테, 앞에 유리, 뒤에 받침다리가 있는 세우는 액자 (이유: 90년대 초 시골 집에 흔하고, 플라스틱·아크릴은 현대 물건 금지에 걸림)
2. 크기: 제안 — 액자 약 15×20cm(사진 10×15cm), 할아버지 손바닥 하나 반 정도 (이유: 폭 40cm 가방에 눕혀 들어가고 한 손으로 꺼낼 수 있는 크기)
3. 사진 속 할머니: 제안 — 색이 바랜 컬러 사진, 60대 한국 여성의 상반신 정면, 짧은 파마머리, 옅은 미소 (이유: 90년대 초 사진관 사진의 흔한 모습). 영상에서 얼굴이 또렷이 보여야 하는지도 알려 주세요. 보여야 하면 할머니 얼굴을 따로 정해야 합니다.
4. 사용 흔적: 제안 — 테 모서리의 칠 벗겨짐, 유리의 잔 흠집, 사진 가장자리의 누런 변색 (이유: 오래 지닌 물건이라는 정서. 손때는 영상에서 손과 겹쳐도 무리가 없음)
5. 무게로 본 물성: 제안 — 가볍고 단단함, 휘지 않음, 유리가 저녁빛을 한 줄 반사 (이유: 나무와 유리 재질에서 나옴)
6. 이야기 속 상태와 3-4·3-5 반영: 제안 —
   - 상태 머신: 가방 안(안 보임) → 3-4에서 할아버지가 두 손으로 꺼내 무릎 위 가방에 기대 세움 (이유: "두 손"이면 좌우 손이 뒤집힐 위험이 없음)
   - 컷 목록 3-4 줄: "할아버지가 무릎 위 가방을 연다" → "할아버지가 무릎 위 가방을 열고 액자를 꺼낸다"
   - 3-5(열린 가방 위 손 클로즈업): 액자가 손에 있는지 함께 정해 주세요. 제안 — 액자를 든 손
   - 참고: 3-4가 8초 안에 사건 두 개(열기, 꺼내기)가 됩니다. 영상에서 실패가 잦으면 3-4와 3-5로 나누는 방법이 있습니다.

답을 주시면 에셋 대장의 PR-002 초안 줄과 컷 목록·연속성 표에 반영하고, 위험 목록과 프롬프트를 보여 드리겠습니다.

=== 메타 ===
연 파일(순서대로):
1. RUN/PLAYER-RULES.md
2. RUN/CLAUDE.md
3. RUN/.claude/instructions.md
4. RUN/SKILLS-INDEX.md
5. RUN/project/decisions.md
6. RUN/project/asset-registry.md
7. RUN/project/shot-list.md
8. RUN/.claude/skills/production-session/SKILL.md
9. RUN/.claude/skills/image-prompt/SKILL.md
10. RUN/.claude/skills/image-prompt/prop.md
11. RUN/.claude/skills/higgsfield-generation/SKILL.md
12. RUN/sim/higgsfield.md
13. RUN/project/ok-cuts.md (제목 줄과 "PR-002/액자" 검색만, 본문은 읽지 않음)

부른 [TOOL]:
- list_folders(project_id=prj-sim-0001) → fld-props 있음, fld-3-4 [대기] 있음
- list_project_assets(folder_id=fld-props) → 0
- list_project_assets(folder_id=fld-3-4) → 0

고친 정본 파일:
- RUN/project/asset-registry.md — 소품에 "PR-002 할머니 사진 액자 (확정 전)" 절 추가(사용자 말 + 제안값 표시, 고정 설명문 비움)
