# real11-C14 "표정은 2-1처럼, 2-2 영상" (2턴) — PASS 1 / 부분 1 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | `ok-reuse.md`·2-1 영상 카드·2-2 시작 이미지 카드. `[TOOL] list_project_assets(folder_id=fld-2-2)`. 가져올 것(표정 줄 `CHARACTER_ACTING`+입 잠금)을 밝히고 동작/타이밍·끝 프레임·시선·시작 이미지 요소 이름을 제안값+이유로 4개. **감점 2:** ① 질문 턴에 `acting` SKILL을 열었음(reads에 `acting/SKILL.md`; `live-action.md:3` "Do not open `acting` in a question turn", 또 연기를 새로 쓰지 않고 2-1 줄을 가져오는 작업이라 필요 없음 — G8). ② `cut-card.md`를 열어 `project/cuts/2-2.md` 신설(tasks.md §3) |
| 2 | PASS | 15블록 전문. `CHARACTER_ACTING` 할아버지 줄이 2-1 줄 글자 그대로(`acting_2-1.lines` 통과). 입 잠금은 2-1이 약해 올리고 "전 → 후" 표시. 시작 이미지=`ff_2-2_v1`, 참조 3 = 태그 3. 검사 WARN 1개(손의 화면 쪽 없음)를 고쳐 다시 돌림. 위험 5줄, "ff_2-2_v1 실제 이름 미확인" 알림 |

검사기: `--kind video C14_t2 --refs 3 --seconds 8 --must-include grandpa+bag+light+acting_2-1` → `OK — video 프롬프트 4594자, 걸린 항목 없음`
추가 발견: 시작 이미지 요소 이름을 사용자에게 묻는 항목(4번)을 만듦 — OK 대장·카드에서 알 수 있는 값이라 불필요한 질문에 가까움(경미).
키트 결함: 1턴의 `acting` 개방은 플레이어 실수이나, `kit/context/tasks.md` 13행("open `acting` only on the turn that writes the prompt")과 `video-prompt/SKILL.md:10`·`live-action.md:3`에 같은 말이 흩어져 있다. 카드 신설은 C11 키트 모순 참고.
총평: 가져온 표정 줄은 완벽. 질문 턴의 불필요한 `acting` 개방과 카드 신설로 1턴 부분.
