# real9-C35 승인 영상 속도 — "너무 빨라, 천천히" 2-1 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt/SKILL.md`만 Read(`fixes.md`·`live-action.md` 안 열림; §0 "사람 동작 속도" 표 `kit/skills/video-prompt/SKILL.md:53` 사용). 승인 컷이라 "새 테이크로 만들고 `job-v-2-1`은 승인 상태로 둡니다" 질문. 어느 동작이 빠른지(엄지 vs 깜빡임) 후보 제시. 기존 구간 초를 셈: "기존 구간이 이미 4초라 같은 구간 안에서는 더 길게 쓸 수 없습니다" → 시작 앞당기기(4초 → 5초) 제안, 영상 길이를 늘리는 대안도 암시, `전 0:00–0:04 / 0:04–0:08 → 후 0:00–0:03 / 0:03–0:08`. 사건 수 그대로. 생성 없음 |
| 2 | PASS | "그대로"=수락. OK 카드 `job-v-2-1` 프롬프트에서 `[ACTION_TIMING]` 두 줄만 전 → 후: `0:03–0:08 — his thumbs move once … taking the full 5 seconds; … Thumb movement finished in under 4 seconds = failed take.`(N−1=4 규칙 충족). 나머지는 OK 카드 그대로. 위험 3개, 낙엽 속도 미해결과 "얼마나 느려질지는 추정" 명시. 카드 `project/cuts/2-1.md`에 `(제안값)` 기록. 생성 안 보냄 |

## 검사기
내 재구성(OK 카드 프롬프트에 위 전 → 후 적용) `--kind video --refs 3 --seconds 8 --must-include grandpa+bag+light`: `OK — video 프롬프트 4195자, 걸린 항목 없음` (플레이어 보고 4,195자와 일치)

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인.
- 확정 프롬프트 수정이라 전문 대신 바뀐 줄만 "전 → 후"로 보임(`kit/instructions.md:52` 규칙대로). 사용자가 붙여 넣어야 한다면 전문을 달라고 해야 하는데 "보낼까요?"로 끝나 문제 없음.
- 기존 승인 영상이 draft 예(만료 2026-10-31)인데 이번 턴에서 언급 없음 — 속도 수정에는 무관.

## 키트 결함
없음.

## 총평
§0 속도 줄(후 구간이 더 길고 N−1 failed take)을 정확히 적용.
