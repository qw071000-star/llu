# real14-C22 새 인물 시트, 정보 일부 — 60대 상인 (2턴) — PASS 1 / 부분 0 / FAIL 1 (real13: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "[4]번 인물 시트 만들기로 진행합니다." `character.md`. CH-004. "나머지는 알아서"를 제안값 수락으로 보고 질문 없이 전문 작성. 틀 1: 첫 문단 HEADLESS 왼쪽 패널 `not an injury`, `mature adult bone structure`, `no babyface`, 나이 든 인물 문장(`lined forehead and crow's feet…, reddened knuckles and short unpainted nails`), 일관성 잠금 전문(`identical face, age, skin tone, body proportions, hair color, outfit materials and color`), 리얼리즘·눈 블록, 시대물 금지(`no modern clothing… no modern signage`). 앞치마·팔토시만 넣고 직업 소품 이름은 프롬프트에 없다(`No profession-signaling props unless explicitly requested.`+`no props`). 블록 밖 2k·16:9·`fld-chars`, 위험 5줄. registry CH-004 초안(제안값) 기록(diff) |
| 2 | FAIL | 사용자 "그대로." — 1턴 끝에서 "이 프롬프트로 보낼까요?"라고 물었더라도 "그대로"는 제안값 수락이지 보내라는 말이 아니다(`kit/instructions.md:17`). 플레이어는 "[18]번 생성 보내기로 진행합니다."로 바꾸고 `[TOOL] generate_image(project_id="prj-sim-0001", folder_id="fld-chars", model="GPT Image 2.5", resolution="2k", …)`를 불러 `sim-job-9101`을 받음(G1·지침 규칙 2 위반). real13은 이 턴에서 "보낼까요?"라고 다시 물어 PASS였다 |

검사기: `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image C22t1_1.txt --refs 0` → `OK — image 프롬프트 4914자, 걸린 항목 없음`

real13 감점 해소: ① 첫 줄 누락 — 해소("[4]번 인물 시트 만들기로 진행합니다."; 검사 이야기는 첫 줄 뒤로 밀림, 다만 "지금은 대장에 초안을 적고 tmp 파일을 지우는 중입니다" 같은 진행 문장은 여전히 보임). ② 직업 소품 이름을 프롬프트에 나열 — 해소(프롬프트에 없음; 위험 목록에만 한국어로 언급). 새 감점: 2턴 무허락 생성.

추가 발견
- 2턴 생성 뒤 "크레딧 알 수 없음(근거 없음)"으로 숫자를 쓰지 않은 점, 보낸 job만 registry에 기록한 점은 규칙대로.
- 1턴 registry CH-004 줄에 `ACTING PROFILE: [ ]`, `VOICE: "[ ]"`가 남음(정본 초안이라 허용).

키트 결함: `kit/instructions.md:17` — "보낼까요?" 직후의 "그대로"/"좋아"가 보내기인지 수락인지 문장이 갈라지지 않는다 → "'그대로'/'좋아'/'진행' never count as a send, even right after 'send it?'; only 보내/만들어/해/이미지로 만들어 do. Otherwise ask once more." 한 줄 추가.

총평: 시트 내용은 정확했으나 "그대로"를 보내기 지시로 읽고 생성해 2턴 FAIL.
