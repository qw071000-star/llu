# real13-C41 정본에 없는 장소의 복합 동작 — 옷장 앞에서 왼쪽으로 돌아 나가기 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real12-recheck: PASS 1 / 부분 1 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 첫 줄 "13번 실사·인물 영상으로 진행합니다." 시작 이미지·컷 번호가 없고 방은 정본에 없는 새 장소라며 "방 확정 → 첫 프레임 → 영상 프롬프트 순서". 사건을 동사마다 4개로 세고(옷장 열기·돌아서기·방문 열기·나가기) A/B 두 컷 분할을 제안값으로, 퇴장은 "마지막 프레임은 몸 절반이 프레임 밖, 문이 닫히는 중". "왼쪽"은 화면 왼쪽(방문은 화면 왼쪽 벽, 옷장은 화면 오른쪽 벽). 질문 2에서 카메라 위치를 먼저 정한 뒤 옷장·방문을 배치(real12의 모순 해소), 경첩과 열리는 방향을 물건 기준으로. 새 장소 질문을 같은 묶음에 포함. `video-prompt` SKILL·`first-frame.md`·`location.md`만 열었고 카드·프롬프트 없음 |
| 2 | PASS | "그대로" 뒤 바로 방 이미지(LC-002) 프롬프트. 두 번째 질문 묶음 없음. 경첩 기준을 서로 마주 보는 문 대신 `창에 가까운 쪽`으로 바꾼 것을 "전 → 후"로 알림(규칙 4 "update and say so"). `LEFT and RIGHT are SCREEN directions …`, `SPATIAL GEOGRAPHY (directions as seen from the camera position …)`, 화면 오른쪽 옷장·왼쪽 방문, `hinged on the edge nearer the window … opening away from the room`, LIGHT LOCK `from screen right, the wardrobe side`, `Nothing else`, 팔레트·재질·시대·무글자 줄. 블록 밖에 모드·참조·모델·해상도·폴더·위험 4개. 대장에 LC-002 `초안(제안값)`, 카드 `4-1.md` 신설(diff). 생성 안 함 |

검사기: `--kind image C41t2_1.txt --refs 0` → `OK — image 프롬프트 2119자, 걸린 항목 없음` (플레이어 첫 실행의 FAIL 1건은 고정 문장 분리로 해결)

추가 발견
- 대장에 `### LC-002 …(초안)` 소제목을 새로 만든 것은 확정 전 `초안(제안값)` 줄 규칙의 연장으로 허용.
- 방 이미지에 "child's room"이라고 용도를 지어 넣었다(손녀 방이라는 사용자 말은 없음, 사실상 추정). 경미.

키트 결함: 없음.

총평: real12의 두 문제(질문 안 모순, t2 질문 분할)가 모두 사라졌다.
