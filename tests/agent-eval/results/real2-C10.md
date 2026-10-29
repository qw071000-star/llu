# real2-C10 영상, 일부만 답함 (3턴) — PASS 3 / 부분 0 / FAIL 0 (지난: 부분 2 / PASS 1)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `production-session`+`video-prompt` SKILL+`live-action.md`+decisions·asset-registry·ok-cuts(3-3 시작 이미지) 열람. `[TOOL] list_project_assets(fld-3-3)`. 7항목(대사, 사건 2개, 타이밍, 끝 상태·돌아서는 방향, 시선, 연기 양 끝, 이음새) 제안값+이유. 렌즈·길이·소리·카메라는 "기본값으로 씀: … 렌즈는 시작 이미지 50mm(약 47°)". 손 "화면 오른쪽 손(시간표 쪽)". `acting`은 질문 단계라 안 엶(routing.md 해당 줄이 허용). |
| 2 | PASS | 대사 없음 반영, 망원(85mm 약 29°)이 시작 이미지 50mm와 충돌함을 짚고 A(50mm 유지)/B(새 퍼스트 프레임) 질문. 나머지는 제안값으로 카드 `(제안값)` 기록(Edit 3). 시나리오 마지막 불릿("망원과 50mm 충돌 짚음은 PASS"), 지침 4번 "사용자 값이 시작 이미지와 다를 때 한 번 묻는다"와 일치. |
| 3 | PASS | `acting/SKILL.md` 열람. 15블록 전문. OPTICS "Diagonal field of view about 47°… / straight lines stay straight / no telephoto compression" (mm 없음), 손 "the screen-right hand, nearer the sign", 의상(girl)·LIGHT LOCK 글자 그대로, `Nobody looks at the camera.`, AUDIO 효과음만, 시간 구간 연속(0:00–0:04–0:07–0:08), 감정 양 끝 failed take. 카드 [1][3][4][5][6][10] `(제안값)` 기록. 검사기 실행, 5,531자 WARN을 `live-action.md:29` 절차대로 숫자+줄여 본 내용+이유 적어 유지. 생성 안 함("480p로 보낼까요?"). |
검사기(채점자, `--kind video --refs 2 --seconds 8 --must-include girl+light`): `WARN  길이 5531자. 5,500자 이하가 안전했다…` / `— FAIL 0 · WARN 1 · 5531자` → 키트가 허용하는 길이 WARN(이유 기재됨), FAIL 없음.
추가 발견: 없음. 핸드오프에 3-2·3-3 연속성 행 누락을 "적겠습니다"라 했으나 이번 턴엔 안 씀(시킨 적 없으니 문제 없음).
## 지난 회차 대비
- 1턴 부분(acting 미열람): `routing.md`가 "질문 단계는 must-ask로 충분"으로 명시 → 해결.
- 3턴 부분(손 방향 `the hand nearer the sign pole`): 이번엔 `screen-right hand, nearer the sign` → 해결.
- 검사기 미실행 → 실행.
- 2턴 재질문 모호: 지침 4번에 두 가지 예외가 명시되어 PASS로 정리됨.
## 키트 결함
없음.
총평: 지난 회차 지적 4건 모두 해소.
