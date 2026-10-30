# real11-C02 "3-2"만 (1턴) — PASS 0 / 부분 1 / FAIL 0 (real9: PASS 1 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | 시작 문구 요구 없음. `[TOOL] list_folders(project_id=prj-sim-0001)` / `list_project_assets(folder_id=fld-3-2)`. 세 줄 보고(판단·읽은 것·할 일) 있음. 읽은 것: production-session SKILL, cuts/3-2, shot-list, 핸드오프, decisions, registry, ok-cuts, video-prompt SKILL(§0). 이웃 컷 카드 안 엶. 핸드오프의 "3-1과 같게"를 제안 1번으로 처리, 대사·3-3 이음새도 한 묶음(4개). "렌즈 알림: 카드 35°, 시작 이미지 75mm(32°) 우선" 알림도 있음. **감점:** 3번 "렌즈 관찰 결과·심도"를 질문 항목으로 올림("제안 — 벤치와 시간표가 한 화면에… 얕은 심도"). 기대는 "렌즈는 묻지 않는다(관찰 결과는 프롬프트 턴에 채운다)". 지침·must-ask는 렌즈를 never-ask로 둠 |

검사기: 프롬프트 없음.
추가 발견: 질문 턴에 카드 파일을 만들지 않음(적절). run의 `tasks.md` 사본은 현재 `kit/context/tasks.md`와 §1 "Go straight on / Ask first" 두 문단이 다른 구판이다(플레이어는 "[N]번 …으로 진행합니다" 줄을 쓰지 않음, 이번 턴은 영향 없음).
키트 결함: `kit/skills/video-prompt/SKILL.md` §0 표의 "Lens | Diagonal FOV, 3 observable results, depth of field" 행이 "Information needed"라서 묻는 항목으로 읽히고, `kit/context/must-ask.md` "Never ask … lens"와 부딪힌다. 고침: 표 행에 "(질문 금지: 시작 이미지 프롬프트에서 Claude가 채움)" 한 줄.
총평: 3-2 세션 시작은 정확. 렌즈 관찰 결과를 질문에 넣은 것만 흠.
