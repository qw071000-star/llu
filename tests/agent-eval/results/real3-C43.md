# real3-C43 — 연기 지적 ("걸음이 너무 젊어")
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | `video-prompt/SKILL.md`(§0)만 열람, `fixes.md` 안 엶. 걸음 줄 제안은 §0 그대로: `"Grandfather walk" — short, careful steps; arms hang close…; feet barely lifted, soles shuffling…; weight … A brisk, springy, long-stride walk = failed take.`, 승인 컷 대체 질문, 재생성 아님. 미달: 1-2가 팀원 작업이라 원 프롬프트가 없다는 것(`get_project_asset_prompt` → 빈 문자열)을 확인하지 않고 "어느 job입니까? job ID를 알려 주세요"라고 사용자에게 되묻고 컷 목록·1-2 줄도 안 엶. 2회차는 [TOOL]로 빈 프롬프트를 알리고 기준을 물었음 |
검사기: 프롬프트 코드블록 없음(한 줄 제안문), 해당 없음.
2회차 대비: PASS → 부분(회귀).
키트 결함: `instructions.md` "대화를 시작할 때" 2번이 "컷 번호 → 컷 세션"과 "결과물·job → job이 대화에 없으면 묻고 컷 파일은 열지 않는다"를 함께 두어, 컷 번호가 있는 결과 지적("1-2에서 …")에서 플레이어가 컷 목록의 job 칸을 안 보고 사용자에게 되묻는다 → "컷 번호가 있으면 컷 목록 그 줄의 확정 job을 먼저 찾아 쓰고(팀원 작업이면 `get_project_asset_prompt` 확인), 컷 번호도 job도 없을 때만 묻는다" 추가.
총평: PASS 0 / 부분 1 / FAIL 0.
