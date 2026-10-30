# real11-C61 인물 기준 손 — "자기 왼손으로" (1턴) — PASS 0 / 부분 1 / FAIL 0 (real9: PASS 1 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | "13번 실사·인물 영상으로 진행합니다." 3줄 보고에 `[TOOL] list_folders(project_id=prj-sim-0001)`·`list_project_assets(folder_id=fld-2-2)` 근거(2-2 `[진행]`, 승인 폴더에 `job-ff-2-2`만). **핵심 충족:** "할아버지는 카메라를 마주 보고 앉아 있어서, '자기 왼손'은 화면 오른쪽 손입니다(추정)." 화면 쪽 + 물건으로 제안("화면 왼쪽 손(감나무 쪽 손)"), `his left hand`를 쓰지 않음. 사용자 말과 시작 이미지의 충돌도 짚음: "승인된 시작 이미지(`job-ff-2-2`)는 화면 왼쪽 손이 이미 가죽 위를 쓰다듬는 중 … 화면 오른쪽 손으로 하려면 시작 이미지를 새로 만들어 승인본을 교체"하며 선택을 물음(이 컷만). 2-2 카드가 없어 동작 구간·끝 상태·시선도 함께 물음(4개, 제안값+이유), 렌즈는 안 물음("85mm … 약 29°"). 프롬프트·생성·카드 파일 없음. **감점:** 질문만 하는 턴인데 `production-session/cut-card.md`를 열었다(메타 reads 마지막). `tasks.md` §3 "On question-only turns do not open `cut-card.md`" 위반. 카드 형식을 미리 보려는 것이었으나 파일은 만들지 않았다. 교체 비용 "약 4크레딧"은 shot-list 3-2 행(이미지 2장 약 8크레딧)에서 나온 근거가 있다 |

검사기: 프롬프트 없음.

추가 발견
- 제안값이 사용자 말과 반대(화면 왼쪽 손)인 점은 시작 이미지 우선 원칙에 따른 것이고, 사용자 말대로 갈 때의 비용까지 제시해 "추정"을 확인받는 형태다.
- 2번 동작 구간·3번 끝 상태는 1턴 질문으로 적절(카드 없음 규칙).

키트 결함: `kit/context/tasks.md:47`("question-only turns do not open cut-card.md")와 `kit/skills/production-session/SKILL.md:37`("If none, build a draft from … (`cut-card.md`)")이 겹쳐서, 카드가 없는 컷의 첫 응답에서 카드 형식을 미리 볼지 모호하다. 고침: production-session SKILL 37행에 "카드를 쓰는 턴에만 `cut-card.md`를 연다. 질문 턴에는 초안 항목을 머릿속에서만 만든다."

총평: 인물 기준 손 → 화면 기준 변환과 시작 이미지 충돌 알림은 훌륭. 질문 턴에 `cut-card.md`를 연 것만 규칙 위반.
