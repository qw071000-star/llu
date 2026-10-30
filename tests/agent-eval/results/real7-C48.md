# real7-C48 — 화면 밖으로 나가기

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `production-session`·`video-prompt` SKILL·`live-action.md`, 3-3 카드·OK 카드. `acting` 안 엶. 사건 3개 한도(확인·돌아서기·나가기), 나가는 쪽 제안 "화면 왼쪽(정류장 끝, 벤치 쪽)" + 이유(3-4는 할아버지만), 마지막 프레임 "몸 절반이 프레임 밖, 이미 걷는 중", 카드 [1] "돌아선다"와 다름 → (제안값)으로 고치고 핸드오프 [5]로 확인, 컷 목록은 총괄 몫. `[TOOL] list_folders`/`list_project_assets` 줄 기록. 생성 없음 |
| 2 (그대로, 프롬프트 턴) | PASS | `acting/SKILL.md` 엶. 코드블록 1(15블록 전문), 블록 밖 모드·참조 2·모델·해상도·길이·소리·폴더, 위험 5, FINAL_FRAME 몸 절반 프레임 밖, Required `screen-left … only`, 연기 양 끝 `a blank face = failed take, a crumpling face … = failed take`, 손 `the screen-right hand, nearer the sign`. 카드 `cuts/3-3.md` [1]·[3]~[6] `(제안값)` 기록(git diff). SCENE_CONTEXT에서 6회차의 "grandfather out of frame" 암시 사라짐. 생성 없음 |

검사기(내 실행, `--kind video --refs 2 --seconds 8`, must-include girl+light): `OK — video 프롬프트 5074자, 걸린 항목 없음`.
추가 발견: 프롬프트 초안과 `3-3_must_include.txt`를 `project/log/`에 남김(C47과 같음).
키트 결함: 임시 파일 위치 규칙 없음(C44).
6회차 대비: PASS 2 유지.
총평: PASS 2 / 부분 0 / FAIL 0.
