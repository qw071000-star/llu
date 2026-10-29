# real3-C04 인물 시트 의상 수정 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real2: PASS 2)
| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`character-edit.md`(character.md 안 엶) + ok-cuts CH-001 카드(`job-ch001`) 열람. 3항목(새 의상 색·재질·길이·여밈 / 없앨 옛 항목·목둘레 / 새 상태 요소 `char_grandpa_winter_v1` 여부 + 이 컷만인지) 제안값+이유. 신규 재작성 아님. |
| 2 | PASS | 틀 1: `Edit reference image 1 …` / CHANGE / REMOVE COMPLETELY(olive work jacket) / PRESERVE EXACTLY(HEADLESS `not an injury`, IDENTITY) / ONLY CHANGE(목둘레 포함). 얼굴 재묘사 없음, 참조 1. 사용자가 안 정한 토글·후드·주머니는 "제안값"으로 알리고 카드에 `(제안값)` 예고. 생성 안 함("보낼까요?"). |
검사기(`--kind image --refs 1`): `OK — image 프롬프트 2611자, 걸린 항목 없음`
추가 발견: 1턴 제안(노치 칼라·숯갈색)이 2턴 사용자 답(남색 더플)과 달라져 상세를 새로 정함 — 규칙 4 "답 하나로 제안이 바뀌면 바꿔 쓰고 알린다"대로. 검사 파일을 `out/ch001-winter-prompt.txt`에 남김(RUN/tmp 아님, 경미).
키트 결함: 없음.
총평: 규칙대로.
