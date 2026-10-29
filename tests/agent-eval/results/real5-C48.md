# real5-C48 — 화면 밖으로 나가기

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt`·`live-action.md`, 3-3 카드(자기 컷)·OK 대장. 4회차의 다른 컷 핸드오프 열람 없음. `acting` 안 엶. `[TOOL] list_folders/list_project_assets`, 카드 [1]·컷 목록 "돌아선다"와 방향이 다름을 짚음, 사건 3개, 나가는 쪽 "화면 왼쪽, 정류장 지붕 끝", 끝 상태 "몸 절반이 프레임 밖, 이미 걷는 중", 질문 7. 생성 없음 |
| 2 (그대로, 프롬프트 턴) | 부분 | `acting/SKILL.md` 엶(메타 기록 있음), 위험 7, 블록 밖 모드·참조 2·모델·해상도·길이·폴더, 카드 `(제안값)`, "만들어라고 하시면". 미달: G6 — 새 프롬프트 전문을 코드블록으로 보이지 않고 `out/3-3_video_prompt.txt`에만 쓰고 답에는 ACTION_TIMING만 보인 뒤 "전문을 붙여 드릴까요?"라고 되물음(`instructions.md` "출력": 새 프롬프트는 전문) |

검사기(내 실행, 파일 `out/3-3_video_prompt.txt`, `--kind video --refs 2 --seconds 8`, must-include girl+light): `OK — video 프롬프트 5462자, 걸린 항목 없음`. 내용: FINAL_FRAME `Half of her body is outside the LEFT edge, mid-stride`, 화면 기준 손, 1명. 내용 자체는 합격.
4회차 대비: PASS 1/부분 1 → 같음(회귀 항목이 바뀜: 핸드오프 열람 해소, 전문 미표시 발생).
추가 발견: 임시 파일이 아니라 프롬프트 산출물을 `out/`에 두어 답에서 대체함.
키트 결함: 없음(`instructions.md` "출력"이 분명). 필요하면 "파일로 저장해도 답에는 전문을 코드블록으로 낸다" 한 줄 추가.
총평: PASS 1 / 부분 1 / FAIL 0.
