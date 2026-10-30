# real8 C32

**PASS 2 / 부분 0 / FAIL 0** (real7 PASS 2 유지)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | '"오른손"이 지금 시간표 짚는 손과 겹칩니다. 화면 기준으로 읽으면 화면 오른쪽 손'; 승인 컷 새 테이크 대체 질문; 적용 범위(3-2 연결) 질문; 우산 재질·크기(80cm)·금지(비닐·로고)·시트 여부 제안값; `her right hand` 없음; `first-frame.md`+카드·핸드오프(3-1)만 |
| 2 | PASS | '손녀가 시간표를 향해 서 있으므로 손녀의 오른손은 화면 오른쪽 손(추정)' (등지면 화면 오른쪽 ✓); 충돌이 남아 더 작은 변경안(팔뚝에 걸기)을 고르고 '전 "쥐고 늘어뜨림" → 후 "화면 오른쪽 팔뚝에 손잡이를 걸어"'로 알림, 쥐게 하려면 손을 바꿔야 한다는 대안 제시; 프롬프트에 `the screen-right hand, nearer the sign`, `screen-right forearm, nearer the sign`; WARDROBE·PROP·LIGHT LOCK 글자 그대로; PR-002 `(제안값)` |

## 검사기
내 실행 `--kind image --refs 4 --must-include grandpa+girl+bag+light`: `OK — image 프롬프트 2960자, 걸린 항목 없음`.

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. T1에서 `image-prompt/SKILL.md`를 열지 않고 `first-frame.md`만 열었으나 T2에서 SKILL.md를 엶(경미). 우산을 '들게' 해 달라는 요청을 팔뚝 걸기로 바꾼 것은 지침 4번(더 작은 변경안)에 부합. `tmp/` 삭제 확인.

## 키트 결함
없음.

## 총평
손 방향 변환·정정 규칙대로.
