# real6-C14 "표정은 2-1처럼, 2-2 영상" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real5: PASS 2)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `[TOOL] list_project_assets(fld-2-2)`. ok-reuse + OK 대장 2-1 영상·2-2 시작 이미지. "표정 그대로"를 2-1 `CHARACTER_ACTING` GRANDPA 줄로 읽고 카메라·렌즈는 안 가져옴. 일·타이밍(쓰다듬기 2번)·끝 상태·대사·연기 5항목 제안값+이유. 렌즈 85mm는 기본값 |
| 2 | PASS | `GRANDPA: waits without hoping. Between stillness and quiet resignation; a sigh or a frown = failed take, a smile = failed take. …` 글자 그대로(acting_2-1.lines 일치) + 손 문장 추가. 손은 `screen-left hand, nearer the tree`. 입 잠금을 표준으로 올림(알림). 위험 목록. 생성 안 함 |

검사기: `check_prompt --kind video --refs 3 --seconds 8 --must-include grandpa+bag+light+acting_2-1` → `OK — video 프롬프트 5106자, 걸린 항목 없음`
추가 발견: 프롬프트·고정 문장 파일을 `project/log/`에, 카드 `project/cuts/2-2.md`를 만듦(카드는 기록이라 허용, log 파일은 경미).
키트 결함: 없음.
총평: PASS 2 유지.
