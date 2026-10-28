[TOOL] list_folders(project_id=prj-sim-0001)

- 판단: 에셋 수정(CH-001 할아버지 시트, 의상 한 가지)이라 총괄 세션으로 봅니다. 얼굴·패널 구조는 그대로 두고 의상만 바꾸는 편집(기준 `job-ch001`)으로 합니다.
- 읽은 것: decisions · shot-list · asset-registry, OK 대장 CH-001 카드, 인물 시트·생성 스킬, Higgsfield 폴더 목록(00 에셋/인물 `fld-chars` 있음).
- 지금 할 일: 아래 질문이 정해지면 위험 목록과 프롬프트를 먼저 보여 드립니다. 아직 생성하지 않았습니다.

**걸리는 점:** 지금 의상(올리브 작업 재킷)이 이미 승인된 컷에 들어가 있습니다.
- 승인 영상: 1-2(지수 님 작업), 2-1, 3-1
- OK 시작 이미지: 2-2, 3-2 (컷 카드 3-1·3-2의 고정 문장도 이 재킷)
- 1-2부터 끝까지 한 저녁의 연속 장면이라, 컷마다 옷이 다르면 편집에서 튑니다.

**그대로 쓸 값 (바꿀 것만 답해 주세요):** 편집 · 참조 1 = `job-ch001`(얼굴·패널 구조·배경 보존) · GPT Image 2.5 · 1k 확인 · 16:9 · 1장 · 저장 00 에셋/인물 `fld-chars`

프롬프트를 쓰기 전에 확인할 것이 4개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요. 1번은 골라 주셔야 합니다.
1. 적용 범위: 정본·승인 컷과 다르니 어느 쪽을 따를지 골라 주세요.
   - A. 교체: CH-001 의상을 겨울 코트로 바꿉니다(고정 문장 v2, 요소 `char_grandpa_winter_v1`, 옛 시트는 폐기 목록으로). 위 승인·OK 5건을 다시 만들어야 이어집니다.
   - B. 파생: 지금 시트와 승인 컷은 그대로 두고 겨울 코트 상태만 따로 만듭니다(`char_grandpa_winter_v1`). 이 경우 쓸 컷을 알려 주세요.
2. 코트: 제안 — 무릎 길이의 낡은 차콜 그레이 울 오버코트, 외줄 단추 3개를 모두 채움, 노치드 칼라, 양옆 플랩 주머니 (이유: 90년대 초 시골 노인의 겨울 외출복. 무릎 위 갈색 가죽 가방과 색이 섞이지 않음. 패딩·로고 같은 현대물은 §7 금지)
3. 나머지 옷: 제안 — 겉옷(올리브 작업 재킷)만 코트로 바꾸고, 크림 니트 조끼·흰 셔츠·짙은 회색 울바지·낡은 갈색 가죽 구두는 그대로 (이유: 한 번에 한 가지만 바꿈. 셔츠 깃만 코트 깃 안쪽에 보임)
4. 목도리·모자·장갑: 제안 — 없음 (이유: 모자는 머리를 가려 헤어까지 바뀜. 장갑은 손 연기(§5 "감정은 손으로")를 가림)

=== 메타 ===
연 파일(순서대로):
1. PLAYER-RULES.md
2. CLAUDE.md
3. .claude/instructions.md
4. SKILLS-INDEX.md (같은 호출에서 RUN 파일 목록 확인, out/에 turn0.md 없음 확인)
5. project/decisions.md
6. project/asset-registry.md
7. project/shot-list.md
8. .claude/skills/production-session/SKILL.md
9. .claude/skills/image-prompt/SKILL.md
10. .claude/skills/image-prompt/character.md
11. .claude/skills/higgsfield-generation/SKILL.md
12. project/ok-cuts.md (제목 목록으로 찾은 뒤 1–58줄만: 머리말·목록·`### CH-001 인물` 카드)
13. sim/higgsfield.md
14. project/log/*.md, project/cuts/*.md (통째로 열지 않고 의상·CH-001·총괄 키워드 줄만 grep)

부른 [TOOL]:
- list_folders(project_id=prj-sim-0001) → 00 에셋 `fld-assets` 아래 인물 `fld-chars` 있음

고친 정본 파일: 없음 (확정된 답이 없어 기록할 것 없음)
