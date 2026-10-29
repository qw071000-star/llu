# real8-C37 — 고해상도 ("1080p로")

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `rerender.md`·`video-prompt/SKILL.md`·`higgsfield-generation/SKILL.md`(크레딧) 엶. "draft였다면 `draft_job_id`로 올립니다 / 아니거나 기한 지났으면 채택본 첨부 재렌더", 승인 10-24 + 7일 = 10-31, "1080p 견적 없음 → `get_cost`로 먼저, 지금은 알 수 없음", "보내" 요청. 생성 없음, 바꾸는 것은 해상도 하나. 경미: draft면 새 프롬프트가 필요 없는데 비draft용 프롬프트를 미리 냄 |

검사기(내 실행, `--kind video --refs 3 --seconds 8`): `OK — video 프롬프트 1081자, 걸린 항목 없음`. `--refs 3`은 7회차 결함 수정(`rerender.md` 끝줄 "태그 수, 원본 영상은 세지 않는다")대로. 답의 "참조 3"과 일치.
추가 발견: `tmp/` 파일 삭제 확인.
키트 결함: `project/ok-cuts.md:16` 목록 "모델 · 설정"(`Seedance 2.5 · 480p · 8초`)과 카드(:141 부근)에 draft 여부 칸이 없어(7회차 결함 그대로) 플레이어가 draft인지 사용자에게 되물음. `rerender.md:5`는 "확인용은 draft로 보내 둔다"고만 적음. 고칠 것: OK 대장 "모델 · 설정"에 `draft` 표기를 넣고 `higgsfield-generation` §4 기록 규칙에 한 줄.
7회차 대비: PASS 유지.
총평: PASS 1 / 부분 0 / FAIL 0.
