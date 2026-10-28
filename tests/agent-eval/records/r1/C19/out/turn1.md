[TOOL] list_folders(project_id="prj-sim-0001")

- **판단:** "3-6 퍼스트 프레임"이라 3-6 컷 세션으로 일합니다.
- **읽은 것:** decisions · shot-list(3-6: 대기, 장소 뷰·인물 없음) · 에셋 대장(LC-001, 폴더 표) · Higgsfield 폴더 목록. 3-6은 컷 카드·OK 카드·핸드오프·Higgsfield 폴더가 모두 없어서, 정본에서 컷 카드 초안 `project/cuts/3-6.md`를 만들었습니다.
- **지금 할 일:** 저장 폴더가 없고 빈 칸이 남아 있어서, 프롬프트를 아직 쓰지 않았고 생성도 보내지 않았습니다(폴더 없이는 생성하지 않습니다).

정본에서 채운 값: GPT Image 2.5 · 1k 확인용 · 16:9 · 1장 · 인원 0명 · LC-001 고정 설명문과 LIGHT LOCK은 글자 그대로 · 1990년대 초 늦가을 · 글자·현대 물건 금지.

프롬프트를 쓰기 전에 확인할 것이 6개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요.

1. **저장 폴더:** 3-6 폴더가 Higgsfield에도, 에셋 대장에도 없습니다. 제안: 아래처럼 제가 만듭니다.
   ```
   「빈 정류장」
   └─ 3-6 [대기]      ← 첫 생성을 보내면 [진행]으로 바꿈
       ├─ 승인
       └─ 거절
   ```
   제가 만들까요, 직접 만드시겠어요?
2. **버스 불빛을 생성할지 합성할지(decisions 미결 #1):** 제안: 생성. (이유: 지금 가정이 "생성"입니다. 합성으로 하면 퍼스트 프레임은 버스 없는 빈 길이 됩니다.)
3. **모드·카메라:** 제안: 새 시점(DERIVED VIEW)으로 만들고, `job-lc001v1`(LC-001-V1)을 같은 장소 참조로 붙입니다. 카메라는 정류장 동쪽 시간표 기둥에서 동쪽으로 약 3m 떨어진 길 북쪽 가장자리에 둡니다. 서서 눈높이(약 1.5m)로 길을 따라 동쪽 길 끝(낮은 산)을 봅니다. 삼각대 고정 와이드 샷, 50mm 상당(대각 약 47°), 길 끝까지 초점이 맞습니다. 화면 왼쪽은 북쪽(정류장 뒤 논), 오른쪽은 남쪽입니다. (이유: V1은 길 건너에서 정류장 정면을 보는 시점이라 "길 끝"이 화면에 없습니다. 동쪽을 보면 서쪽 해를 등져 불빛이 역광에 묻히지 않고, 시간표가 화면 밖이라 글자가 들어갈 위험도 없습니다.)
4. **길 남쪽(화면 오른쪽) 풍경:** 제안: 북쪽처럼 추수가 끝난 논과 낮은 산. (이유: 에셋 대장에는 길 남쪽 묘사가 없고 "no other buildings"만 있습니다.)
5. **0:00의 버스:** 제안: 길 끝 소실점 근처에 헤드라이트 두 점과 흐린 상자 모양 실루엣만 보입니다(화면 폭의 1/30 이하). 1990년대 초 시골 완행버스이고 글자·번호판은 읽히지 않습니다. 불빛은 주변을 비추지 않습니다. (이유: "다가오는" 컷의 0:00 상태입니다. 등장 타이밍은 모델에 맡기지 않습니다. LIGHT LOCK의 "only key"도 지킵니다.)
6. **고정 설명문과 충돌:** LC-001의 `Nothing else: no other buildings, no cars, no people, no legible text.`가 버스와 부딪칩니다. 제안: 문장은 글자 그대로 두고 바로 뒤에 `The only exception is the one distant bus described below.` 한 줄을 더합니다. 고정 설명문을 고칠지는 총괄에 올립니다. (이유: 컷 세션은 고정 설명문을 바꾸지 않습니다. 그대로 두면 버스가 지워질 수 있습니다.)

바꿀 것만 답해 주세요. 답을 받으면 위험 목록과 프롬프트를 먼저 보여 드리겠습니다. 보내라고 하시면 1k 1장으로 생성합니다.

=== 메타 ===
- 연 파일(순서대로): PLAYER-RULES.md → (RUN 파일 목록 조회) → CLAUDE.md → .claude/instructions.md → SKILLS-INDEX.md → .claude/skills/production-session/SKILL.md → project/decisions.md → project/shot-list.md → project/asset-registry.md → .claude/skills/production-session/cut-card.md → sim/higgsfield.md → .claude/skills/image-prompt/SKILL.md → .claude/skills/image-prompt/first-frame.md → .claude/skills/higgsfield-generation/SKILL.md → project/ok-cuts.md(제목 줄만 grep, 3-6 카드 없음) · project/log/, project/cuts/ (목록만, 3-6 핸드오프·카드 없음)
- 부른 [TOOL]: list_folders(project_id="prj-sim-0001") → 3-6 폴더 없음
- 고친 정본 파일: project/cuts/3-6.md (새로 만듦 · 컷 카드 초안 v0, 미정 칸은 [ ])
