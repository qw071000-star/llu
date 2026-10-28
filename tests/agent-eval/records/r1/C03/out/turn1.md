[TOOL] list_folders(project_id=prj-sim-0001)
[TOOL] list_project_assets(folder_id=fld-chars)

이 요청은 에셋 작업(CH-003 버스 기사 인물 시트, 신규)이라 총괄 세션으로 시작합니다.
읽은 것: decisions·asset-registry·shot-list, OK 대장의 CH-001·CH-002 카드, Higgsfield `00 에셋/인물`(`fld-chars`). 이 폴더에 기사 시트는 아직 없습니다(0건).
할 일: 시트의 빈 칸 6개를 먼저 확인받겠습니다. 그다음 위험 목록과 프롬프트를 보여 드리고, 생성은 지시하실 때 합니다.

**이미 정해진 것 (다시 묻지 않음)**
- 모델·해상도: GPT Image 2.5, 확인은 1k, 확정 뒤 2k (decisions §2)
- 형식: 16:9 한 장을 3분할한 시트(목 아래 정면 / 후면 전신 / 가슴 위 클로즈업), 장 수 1
- 저장: 「빈 정류장」/00 에셋/인물 `fld-chars`
- 모드·참조: 신규, 참조 없음 (CH-001·CH-002와 같은 방식)
- 배경·조명: 따뜻한 회색 무지 배경에 약간 위에서 비추는 정면 소프트 키. CH-001·CH-002 시트와 같습니다.
- 공통 제약: 1990년대 초 늦가을 시골. 글자·로고·현대 물건은 금지입니다 (decisions §3·§7).

빈 칸이 남아 있어서 프롬프트도 생성도 아직 하지 않았습니다.

프롬프트를 쓰기 전에 확인할 것이 6개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요. 바꿀 것만 답하셔도 됩니다.

1. 나이·얼굴: 제안 — 50대 초반 한국 남자. 볕에 그을린 피부, 각진 턱, 홑꺼풀의 가는 눈, 짙은 눈썹, 굳게 다문 입에 무표정 (이유: 90년대 초 시골 군내버스 기사로 자연스럽습니다. 할아버지(70대 초)·손녀(10살)와 나이대가 겹치지 않습니다)
2. 체형·자세: 제안 — 보통 키에 다부진 몸. 오래 운전해 어깨가 약간 앞으로 둥글고 배가 조금 나왔습니다 (이유: 마르고 굽은 할아버지와 실루엣이 구분됩니다)
3. 의상: 제안 — 짙은 남색 작업 점퍼(지퍼는 가슴까지, 뚜껑 달린 가슴 주머니 둘) → 안에 연하늘색 칼라 셔츠 → 회색 면바지 → 낡은 검은 가죽 단화. 명찰·회사 배지·글자는 넣지 않습니다 (이유: 그 시대 늦가을 근무복입니다. 글자 금지(§7)라 명찰은 뺍니다. 할아버지의 올리브색·손녀의 노란색과 겹치지 않습니다)
4. 직업 소품: 제안 — 없음. 모자·흰 면장갑·손목시계를 모두 뺍니다 (이유: 시트 틀은 직업 소품을 요청할 때만 넣고, 두 손을 비워 둡니다. 흰 면장갑을 원하시면 의상 항목에 넣겠습니다)
5. 헤어: 제안 — 짧은 검은 머리에 옆머리만 조금 희끗합니다. 왼쪽 가르마에 뒷머리는 짧게 쳐 올리고, 윤기 없는 자연 마감입니다 (이유: 그 시대 중년 남자에게 흔한 머리입니다. 할아버지의 회색 스포츠머리와도 구분됩니다)
6. 등장 컷·대사: 제안 — 지금은 시트만 만듭니다. 기사가 나오는 컷과 대사 여부가 정해지면 그때 연기 프로필·목소리를 에셋 대장에 채웁니다 (이유: 컷 목록 1-1~3-6에 기사가 나오는 컷이 아직 없고, 이 두 칸은 시트 이미지에 영향이 없습니다)

=== 메타 ===
연 파일(순서대로):
1. PLAYER-RULES.md
2. CLAUDE.md
3. .claude/instructions.md
4. SKILLS-INDEX.md (같은 명령에서 out/·project/ 폴더 목록과 RUN 파일 목록도 확인 — out/turn0.md 없음)
5. project/decisions.md
6. project/asset-registry.md
7. project/shot-list.md
8. .claude/skills/production-session/SKILL.md
9. .claude/skills/image-prompt/SKILL.md
10. .claude/skills/image-prompt/character.md
11. .claude/skills/higgsfield-generation/SKILL.md
12. sim/higgsfield.md
13. project/ok-cuts.md — 제목 목록만 검색한 뒤 `### CH-001 인물` 절(28–57행)만 읽음
14. project/ok-cuts.md — `### CH-002 인물` 절(59–89행)에서 job·모델·BACKGROUND·한계 줄만 확인

부른 [TOOL]:
- list_folders(project_id=prj-sim-0001) → 00 에셋 `fld-assets` / 인물 `fld-chars` 있음
- list_project_assets(folder_id=fld-chars) → 검토 대기 0, 승인 0, 거절 0 (기사 시트 없음)

고친 정본 파일: 없음 (답을 받은 뒤 asset-registry.md CH-003 칸에 기록할 예정)
