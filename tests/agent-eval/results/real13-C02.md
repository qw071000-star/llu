# real13-C02 "3-2"만 (1턴) — PASS 0 / 부분 1 / FAIL 0 (real11: PASS 0 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 시작 문구 요구 없음. `[TOOL] list_folders(project_id=prj-sim-0001)`·`list_project_assets(folder_id=fld-3-2)`, 3줄 시작 보고(판단·읽은 것·Higgsfield 현황), 4개 질문(3-1에서 가져올 범위 / 끝 상태·동선·시선 / 대사 / 3-3 이음새). 렌즈는 안 묻고 "알림: 카드 35°와 시작 이미지 75mm(32°)가 다릅니다. 시작 이미지를 따릅니다." 3-1 카드는 제안 근거로만 열음, 이웃 컷 카드 안 엶, 질문 턴 카드 파일 없음. 감점: 답이 `[TOOL]` 줄과 "**시작 보고**"로 시작, "[2]번 오늘 할 일·세션 시작으로 진행합니다." 없음 |

검사기: 프롬프트 없음.
추가 발견: `video-prompt/SKILL.md`를 시작 시 열음(`production-session` On start 범위, 허용).
키트 결함: 첫 줄 규칙 누락 — C01과 같은 원인(`kit/instructions.md:41`). 컷 번호만 오면 "시작 보고"가 먼저 떠올라 `tasks.md` 2번 행 라벨 문장을 건너뜀 → `tasks.md` 2번 행 "a cut number alone" 옆에 "line 1 still `[2]번 …으로 진행합니다.`" 추가.
총평: 내용은 정확, 형식 첫 줄만 누락.
