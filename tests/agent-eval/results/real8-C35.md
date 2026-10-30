# real8 C35

**PASS 2 / 부분 0 / FAIL 0** (real7 PASS 0/부분 1/FAIL 1 → 상승)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt/SKILL.md` §0 표만(`fixes.md` 안 열림); '2-1은 승인된 컷 … 새 테이크로 만들고 승인본은 그대로' 질문; 어느 동작(엄지 vs 깜빡임) 후보; 기존 구간 0:04–0:08(4초)을 세어 '엄지 구간 4초 → 5초, 시작을 1초 앞당깁니다. 사건 수는 그대로'; 길이 8초는 decisions 확정이라 안 늘림(§0 '시작을 앞당기거나 길이를 늘리는 안을 제안값'으로 제시) |
| 2 | PASS | 전 `0:04–0:08` → 후 `0:03–0:08 — … taking the full 5 seconds. The thumb stroke finished in under 4 seconds = failed take.`(후 구간이 더 길고 N−1=4 ✓), 앞 구간 `0:00–0:04` → `0:00–0:03`, 나머지 14블록은 OK 카드 그대로; 위험 4개; 카드 2-1 v0에 `(제안값)`; 생성 안 보냄 |

## 검사기
내 재구성 실행(OK 카드 `job-v-2-1` 프롬프트에 위 전 → 후 적용) `--kind video --refs 3 --seconds 8 --must-include grandpa+bag+light`: `OK — video 프롬프트 4197자, 걸린 항목 없음` (플레이어 보고 4,197자와 일치).

## 추가 발견
G1(mcp 호출·생성) 위반 없음, RUN 밖 읽기 없음. T1에 `production-session/SKILL.md`도 엶(컷 세션 시작, 허용). 빈 `tmp/` 없음(삭제 확인).

## 키트 결함
없음(real7 지적 `video-prompt/SKILL.md` 사람 동작 속도 줄이 `[기존보다 긴 구간]` 일반형 + '먼저 기존 구간 초를 센다'로 고쳐져 해소).

## 총평
'천천히' 방향 정확, 7회차 결함 수정 효과 확인.
