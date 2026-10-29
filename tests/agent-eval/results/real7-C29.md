# real7 C29

**PASS 2 / 부분 0 / FAIL 0** (real6 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 사건 4개(일어남·듦·돌아섬·나감) 계산 → 샷 A/B 분리 제안; '"왼쪽"은 화면 왼쪽(감나무 쪽)'; 나가기는 끝 프레임 상태('몸 절반이 화면 왼쪽 밖, 이미 걷는 중'); 시작 이미지 없음 → 퍼스트 프레임부터, 연기·타이밍 보류; `video-prompt` SKILL+`first-frame.md`만(`live-action.md` 안 열림); `[TOOL] list_folders`; 프롬프트·생성 없음 |
| 2 | PASS | (시나리오에 없는 '그대로' 턴 → 프롬프트 턴으로 채점) 제안 7번 '제가 만든다' 수락 → `[TOOL] create_folder` 3줄(sim 규칙대로 `fld-2-3`…); 컷 카드 v0; 샷 A 퍼스트 프레임 틀 1 LOCKED EDIT(WARDROBE·PROP·LIGHT LOCK 글자 그대로, `Exactly one person`); 위험 목록; 생성 보내지 않음 |

## 검사기
내 실행 `--kind image --refs 3 --must-include grandpa+bag+light`: `OK — image 프롬프트 2028자, 걸린 항목 없음`.

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 폴더 생성은 제안값 수락 범위(생성 아님). 임시 파일을 RUN 밖 scratchpad에 둠(경미).

## 키트 결함
없음.

## 총평
분해·화면 기준·퍼스트 프레임 우선 모두 충족.
