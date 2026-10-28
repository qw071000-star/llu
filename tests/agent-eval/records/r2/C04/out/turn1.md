- 판단: 에셋(CH-001 할아버지 시트) 의상 수정 → 총괄 세션, 기존 시트를 편집하는 작업(틀 2, 의상 하나만 바꿈)입니다.
- 읽은 것: decisions.md, asset-registry.md(CH-001 고정 문장·폴더), shot-list.md, OK 대장 CH-001 카드(`job-ch001` 프롬프트), Higgsfield 폴더 목록(`00 에셋 / 인물` `fld-chars` 있음).
- 할 일: 아래 4가지만 정하면 편집 프롬프트와 실패 위험 목록을 먼저 보여 드립니다. 아직 생성하지 않았습니다.

[TOOL] list_folders(project_id=prj-sim-0001)

**정본과 걸리는 점:** 지금 CH-001 의상(올리브 작업 재킷)은 승인된 1-2·2-1·3-1 영상과 2-2·3-2·3-3 첫 프레임에 이미 들어가 있습니다. 작품 설정도 "늦가을"(decisions §3)입니다. 기존 의상을 겨울 코트로 **대체하면** 이 승인 컷들을 다시 만들어야 합니다.

프롬프트를 쓰기 전에 확인할 것이 4개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요.

1. 용도: 제안: **추가 상태(파생)**. 기존 시트는 그대로 두고 겨울 코트 시트를 새 요소 `char_grandpa_wintercoat_v1`로 만들고, 쓸 컷은 따로 정합니다. (이유: 승인 컷 연속성 유지. 대체를 원하시면 v2로 바꾸고 옛 시트는 폐기 목록으로 옮기며, 다시 만들 컷 목록을 따로 정리하겠습니다.)
2. 바꾸는 범위: 제안: **올리브 작업 재킷만 코트로 바꾸고**, 크림 니트 조끼, 흰 셔츠, 다크 그레이 울 바지, 갈색 가죽 구두는 유지합니다. (이유: "의상만"이라는 말과 한 번에 하나만 바꾸는 원칙에 따름. 옛 재킷은 모든 패널에서 완전히 지웁니다.)
3. 코트 모양: 제안: **낡은 차콜 그레이 울 오버코트, 무릎 길이, 싱글 여밈, 어두운 단추 3개를 모두 채움, 평범한 노치드 칼라, 덮개 달린 허리 주머니 2개, 로고·무늬 없음.** (이유: 1990년대 초 시골 노인 차림. 절제된 채도에 맞고, 다크 그레이 바지와도 어울립니다.)
4. 목도리·모자·장갑: 제안: **없음.** (이유: 의상 하나만 바꿉니다. 모자는 헤어를, 장갑은 손 연기(§5 "감정은 손으로")를 가립니다.)

기본 설정은 아래와 같습니다. 바꿀 것만 답해 주세요.
- 모드: 편집(LOCKED, 시트 구조·얼굴 보존). 참조 1장은 `job-ch001`(얼굴·체형·시트 구조 기준)입니다.
- 모델: GPT Image 2.5 · 확인용 1k · 16:9 · 1장 (확정 뒤에만 2k)
- 저장: 「빈 정류장」/00 에셋/인물 (`fld-chars`)

=== 메타 ===
연 파일(순서대로):
1. PLAYER-RULES.md
2. CLAUDE.md
3. .claude/instructions.md
4. SKILLS-INDEX.md
5. project/decisions.md
6. project/asset-registry.md
7. project/shot-list.md
8. .claude/skills/image-prompt/SKILL.md
9. .claude/skills/image-prompt/character.md
10. .claude/skills/higgsfield-generation/SKILL.md
11. project/ok-cuts.md (제목 목록과 목록 표, `### CH-001 인물` 카드만)
12. sim/higgsfield.md

부른 [TOOL]:
- list_folders(project_id=prj-sim-0001) → `00 에셋` 아래 인물 `fld-chars` 있음

고친 정본 파일: 없음(아직 사용자 답이 없어 기록할 값이 없음)

참고: SKILLS-INDEX에 있는 production-session 스킬은 RUN/.claude/skills/ 아래에 폴더가 없어 열지 못했습니다.
