# real5-C06 새 소품 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real4: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL + prop.md. 7항목(시트 필요 / 사진 속 모습 / 틀 재질·흔적 / 크기 13×18cm+손바닥 / 무게 / 나오면 안 되는 재질 / 상태·손) 제안값+이유, PR-002. 모델·1k·`fld-props`는 기본값 줄 |
| 2 | PASS | 소품 틀: 회색 무배경, `no hands, no people`, `Avoid:` 줄, 사진 속 인물은 `Except:`로 설명. 블록 밖 모드·참조 0·GPT Image 2.5·1k·16:9·`fld-props`. 에셋 대장 PR-002 초안을 "확정 후 등록"으로 보임. 위험 5줄. 생성 안 함 |

검사기: `--kind image --refs 0`: `OK — image 프롬프트 1157자, 걸린 항목 없음`

추가 발견: `project/cuts/3-4.md` 새 카드(v1)를 만들어 PR-002 답을 적음. 지침 4번("답은 컷 카드에 적는다")대로이나, prop.md·production-session §1은 확정 전 에셋 답을 에셋 대장 `초안(제안값)` 줄에 두라고 함. 사용자가 시킨 일은 소품 프롬프트까지였음.

키트 결함: `.claude/instructions.md` 규칙 4 마지막 불릿("답은 컷 카드에 적는다")과 `production-session/SKILL.md` §1 표(asset-registry 초안(제안값) 줄)가 에셋 질문에서 충돌. 고칠 곳: 지침 규칙 4에 "에셋(인물·장소·소품) 질문의 답은 에셋 대장 초안 줄, 컷 질문의 답만 컷 카드" 한 구절.

총평: 프롬프트·질문은 정확. 기록 위치만 키트 모순.

G1: 모든 턴 tools가 Bash/Write/Edit/Grep뿐, `mcp__` 호출 없음, `generate_*` 없음.
