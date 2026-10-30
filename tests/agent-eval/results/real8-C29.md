# real8 C29

**PASS 2 / 부분 0 / FAIL 0** (real7 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 사건 4개(일어나·들고·돌아서·나간다) 계산 → 샷 A/B 분리; '"왼쪽"은 화면 왼쪽, 곧 감나무 쪽'; 나가기는 B의 끝 상태; 시작 이미지 없음 → 퍼스트 프레임 먼저, 연기·타이밍 보류; `video-prompt` SKILL+`first-frame.md`만(`live-action.md` 안 열림); 3-1(0:40) 앉은 상태와의 충돌까지 짚음; 컷 폴더 2-3 구성안 질문; 프롬프트·생성 없음 |
| 2 | PASS | (시나리오에 없는 '그대로' → 프롬프트 턴) 폴더 `fld-2-3`·`-ok`·`-ng` 대장 반영, 컷 카드 v0, 샷 A 퍼스트 프레임 틀 1: WARDROBE·PROP·LIGHT LOCK 글자 그대로, `Exactly 1 person is visible.`, 화면 좌우 문장; 위험 목록; 이음새 2-3→3-1 표에 올림; 생성 안 보냄; `higgsfield-generation/SKILL.md`는 폴더를 만드는 턴이라 허용 |

## 검사기
내 실행 `--kind image --refs 3 --must-include grandpa+bag+light`: `OK — image 프롬프트 2005자, 걸린 항목 없음`.

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. 폴더 생성을 말하면서 `[TOOL] create_folder` 줄이 없음(sim 기록 규칙, 경미). `tmp/` 삭제 확인.

## 키트 결함
없음.

## 총평
분해·화면 기준·퍼스트 프레임 우선 충족.
