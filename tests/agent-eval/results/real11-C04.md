# real11-C04 인물 시트 의상 수정 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt` SKILL + `character-edit.md` + OK 대장 CH-001 카드(`job-ch001`) 기준. 코트 색·재질·길이·여밈·내복 유지·목선, 새 상태 `char_grandpa_winter_v1` 여부, 참조 이미지 유무를 제안값+이유로 3개 한 묶음. 늦가을 설정과의 계절 확인도 언급. 신규 제작 아님. (라벨 오류: "4번 인물 시트 고치기" — tasks.md에서는 5번) |
| 2 | 부분 | 틀 1 전문: `Edit reference image 1`, CHANGE / REMOVE COMPLETELY(올리브 재킷·가슴 덮개 주머니·납작 단추) / PRESERVE EXACTLY(`HEADLESS … not an injury`, 얼굴은 보존만) / ONLY CHANGE, 목둘레 3곳 있음, 참조 1개. **감점(G6):** 블록 밖 해상도가 "시트 수정 기준은 `character.md`를 열어 확인해야 해서 아직 정하지 않았습니다"로 비어 있음. `character-edit.md`에는 해상도 규칙이 없고 `character.md` §Spec에만 있음 |

검사기: `check_prompt.py --kind image C04_t2 --refs 1` → `OK — image 프롬프트 2652자, 걸린 항목 없음`
추가 발견: 사용자가 안 답한 2·3번을 제안값으로 처리하고 한 줄로 알림(규칙 4 부합). CH-001 아래에 `초안(제안값)` 기록(diff 확인). REMOVE 목록과 LEFT 줄 `no …` 목록(올리브 재킷·덮개 주머니·납작 단추) 일치.
키트 결함: `kit/skills/image-prompt/character-edit.md` (Rules 부근, 줄 1~3 직후)에 해상도·모델 줄이 없다. 고침: "Resolution: sheet edits are made at 2k from the start (same as `character.md` Spec); model = work default" 한 줄 추가.
총평: 내용은 정확, 해상도 한 줄만 키트 공백 때문에 비었다.
