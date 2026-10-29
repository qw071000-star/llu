# real13-C06 새 소품 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real11: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | `image-prompt`+`prop.md`. 7개 질문(시트 여부 / 재질·흔적 / 크기 18×23cm / 무게 / 나오면 안 되는 것 / 사진 속 모습 / 3-4 변경 "화면 오른쪽 손(시간표 쪽)") 모두 제안·이유. PR-002 매김, 컷 카드 파일 안 만듦. 감점: 첫 줄이 "**시작 보고**"라 "[9]번 소품 만들기로 진행합니다." 없음 |
| 2 | PASS | 소품 틀: 회색 무배경, `no hands, no people`, `Avoid: plastic, glossy new varnish, flowers, ribbons, brand logos, text, watermarks`, 크기 cm. registry PR-002 `초안(제안값)` 고정 설명문 기록(diff). 3-4 답을 `cuts/3-4.md`에 새로 기록(값을 쓰는 턴이라 허용, 이 턴에 `cut-card.md` 엶). shot-list 안 건드림, 변경은 핸드오프 [5]로 제안. 위험 5줄, "이미지를 보낼까요?" |

검사기: `--kind image --refs 0` → `OK — image 프롬프트 824자, 걸린 항목 없음`
추가 발견: t1이 질문 턴인데 registry에 PR-002 임시 행을 미리 기록(답을 받기 전 제안값 기록). `kit/instructions.md` "Before ending the turn"은 받은 답만 기록하라고 함.
키트 결함: 첫 줄 누락(C01과 같은 원인). `instructions.md` "Before ending the turn"에 "질문만 있는 턴에는 registry도 쓰지 않는다" 한 줄 필요(통합 후 `prop.md` 규칙과 중복 없이 한 곳으로).
총평: 내용 PASS, t1 형식 부분.
