# real3-C10 영상, 일부만 답함 3-3 (3턴) — PASS 3 / 부분 0 / FAIL 0 (real2: PASS 3)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `production-session`+`video-prompt` SKILL+`live-action.md`+3-3 카드·shot-list·decisions·asset-registry·ok-cuts(3-3 시작 이미지) 열람, `[TOOL] list_project_assets(fld-3-3)`. 7항목(돌아서는 쪽 / 끝 상태 / 시선 / 타이밍 / 연기 양 끝 / 소리·대사 / 이음새) 제안값+이유. 렌즈·길이·카메라 고정·모델·폴더는 "기본값으로 씀"(렌즈 50mm=47°). `acting`은 질문 단계라 안 엶(routing.md 허용). 손은 "화면 오른쪽 손". |
| 2 | PASS | 대사 없음 반영. 망원(≈85mm)이 승인된 시작 이미지 50mm와 다르므로 A(50mm 유지)/B(새 시작 이미지) 한 번 질문 — instructions.md 4번 "사용자 값이 시작 이미지와 다를 때 한 번". 카드 [3]~[6] `(제안값)` 기록(Edit 3). 프롬프트는 3턴으로. |
| 3 | PASS | `acting/SKILL.md` 열람(프롬프트 쓰는 턴). 15블록 전문: OPTICS `Diagonal field of view about 47°` + 관찰 3개(mm 없음), 의상(girl)·LIGHT LOCK 글자 그대로, `Nobody looks at the camera`, 손 `the screen-right hand, nearer the sign`, 타이밍 0:00–0:04–0:05–0:08 연속, AUDIO 효과음만·대사 없음, 감정 양 끝 failed take. 카드 [1]~[6] `(제안값)` 기록. 검사 실행, 길이 5956→5435자로 줄여 OK. "알아서 해"를 생성 지시로 안 봄("이번에 처음 보여 드린 것"). 사건 수 정정(2→3). |
검사기(`--kind video --refs 2 --seconds 8 --must-include girl+light`): `OK — video 프롬프트 5435자, 걸린 항목 없음`
추가 발견: 없음. 2턴 재질문은 지침 4번 명시 예외라 "키트 모호" 아님.
키트 결함: 기대 오류 후보 — `scenarios.md` C10 2턴 기대("렌즈 망원 → 약 30°로 15블록 전문")는 `instructions.md:19`의 "사용자 값이 시작 이미지와 다를 때 한 번 묻는다"와 어긋남. 시나리오 2턴 문구에 "시작 이미지(50mm)와 달라 한 번 확인해도 PASS"를 넣어 정리할 것(키트 쪽 수정 불필요).
총평: real2와 동일, 규칙대로.
