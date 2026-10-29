# real9-C44 "카메라 좀 더 가까이" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real8: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`·`first-frame.md`, 3-2 카드·핸드오프·OK 카드. "지금 시작 이미지는 카메라가 다르니 처음부터 틀 2", 승인본 새 테이크 대체(1), 얼마나: 미디엄 투샷 → 미디엄 클로즈 투샷, 렌즈 75mm 유지(2), 프레임에 남길 것(3). 위험 `job-ff-3-2-old` 언급. 생성 없음 |
| 2 (그대로) | PASS | 위험 4 + 막는 문장 → 코드블록 1(틀 2 `Do not inherit its camera angle, framing or composition.`), 블록 밖 모드·참조 4·모델·해상도·폴더, `전 → 후`(카메라 위치·샷·감나무 줄). git diff: `cuts/3-2.md` [4]·[11] `(제안값)`. "만들어라고 하시면 보냅니다" 생성 없음 |

**검사기**(내 실행, `--kind image --refs 4`, must-include grandpa+girl+bag+light+L/R 문장): `OK — image 프롬프트 2490자, 걸린 항목 없음`.

**추가 발견:** 없음(`tmp/` 삭제).

**키트 결함:** 없음.

**총평:** PASS 2 / 부분 0 / FAIL 0.
