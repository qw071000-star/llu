# real4-C04 인물 시트 의상 수정 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real3: PASS 2)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | image-prompt SKILL+character-edit.md(character.md 안 엶)+ok-cuts CH-001 카드. 5항목(새 의상 / 코트 색·재단 / 없앨 옛 항목·목둘레 / 참조 이미지 없음 / 새 상태 `char_grandpa_winter_v1`·컷 번호). 신규 재작성 아님 |
| 2 | PASS | `Edit reference image 1: change only the character's outfit…` / CHANGE / REMOVE COMPLETELY(olive work jacket, 목둘레) / PRESERVE EXACTLY(HEADLESS not an injury, IDENTITY) / ONLY CHANGE. 얼굴 재묘사 없음, 참조 1. 사용자 안 정한 토글·후드를 "제안값에서 바뀐 것"으로 전→후 알림. 위험 5줄. 생성 안 함 |
검사기(`--kind image --refs 1`): `OK — image 프롬프트 2846자, 걸린 항목 없음`
추가 발견: 프롬프트 파일을 `out/ch001_winter_prompt.txt`에 남김(RUN/tmp 아님, 경미).
키트 결함: 없음.
총평: 규칙대로.
