# real6-C11 배경 영상 1-1 (+C26 4~6턴) (6턴) — PASS 6 / 부분 0 / FAIL 0 (real5: PASS 6)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | video-prompt SKILL + background.md. 움직일 것(구름만, 이동 ≈3%) / Keep 2항목. 카메라·길이·소리·폴더·시작 이미지 `job-ff-1-1`은 "기본값으로 씀". 감나무에 잎 없음을 미리 알림 |
| 2 | PASS | 감나무 잎(시작 이미지에 없음)과 10초·무음(정본 8초·소리 효과음, 1-2가 0:08 시작)이 정본과 부딪친다고 프롬프트 전에 한 번 묻고, 이 컷만/작품 전체도 물음 |
| 3 | PASS | Camera / Motion / Keep / Silent 네 문단. 움직임은 %(4%, 3%). 끝 상태·페이드 없음. 맨가지·감만 흔들림("No leaves appear on the tree."). 카드 1-1 작성(제안값 표시). 생성 안 함 |
| 4 | PASS | 구름 3% → 1.5%, `Motion` 첫 문장만 "전 → 후"로 보임, 다른 문단 그대로. 검사 재실행. 거의 정지로 보일 수 있다는 경고 |
| 5 | PASS | 풀 추가로 움직임이 4개(푸시인, 구름, 가지·감, 풀)라 3개 한도 초과를 알리고 하나 빼기를 제안(감나무 가지 제안). 시나리오가 허용한 경로(프롬프트 미작성) |
| 6 | PASS | 별: 시작 이미지에 없고 노을 하늘이라 충돌, 작고 반복되는 요소는 모델이 못 지킨다고 알림, 후반 오버레이 제안(모호한 말 표 50줄과 일치). 앞 질문(하나 빼기) 되살림. 생성 안 함 |

검사기: 3턴 프롬프트 `--kind video --seconds 10 --refs 0` → 플레이어 실행 `OK — 1014자`, 4턴 수정본 `OK — 1016자`(스크립트 파일과 동일 확인). 내가 `light.lines`를 `--must-include`에 넣으면 FAIL이 뜨나, `background.md` 틀의 Keep이 "the light from screen [left/right], the [object] side"로 풀어 쓰는 구조라 고정 문장 검사가 맞지 않는 것(검사기 오탐/기대 부적합, 플레이어 FAIL 아님).
추가 발견: Motion에 "lit orange from below"(이미지 속 묘사 일부) 포함은 경미. 플레이어 임시 파일은 harness scratchpad에만 둠.
키트 결함: 없음. (참고: `testbed/grade/light.lines`를 배경 4문단 체인에 쓰지 않도록 scenarios C11 검사 줄이 이미 `--seconds 10`만 요구함.)
총평: PASS 6 유지.
