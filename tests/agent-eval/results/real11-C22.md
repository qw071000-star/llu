# real11-C22 새 인물 시트, 정보 일부 — 60대 상인 (2턴) — PASS 1 / 부분 1 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | 부분 | `character.md`를 엶. CH-004 매김, "알아서"라 제안값으로 채워 바로 전문 제시(허용). 틀 1: 성숙한 골격·나이 든 인물 문장(`lined forehead and crow's feet …, reddened knuckles and short unpainted nails`), 일관성 잠금, 리얼리즘·눈 블록, 왼쪽 패널 A(HEADLESS … not an injury), 앞치마·팔토시만 넣고 직업 소품은 `no basket, no knife, no fish, no bag`로 금지, 시대 금지 줄, 2k·16:9·`fld-chars`. 생성 안 함. **감점(G7):** 프롬프트를 보이기 전에 검사를 돌리지 못했다고 밝힘("작업 폴더가 `project/`로 바뀌어 …경로를 못 찾음"). 원인은 플레이어가 앞서 `cd …/project && cat …`을 한 것(셸 cwd가 이어짐). 그대로 보여 주고 "확인할 것: 대사 있나요?"를 덧붙임 |
| 2 | PASS | "그대로"를 생성 지시로 읽지 않음("보내려면 '이미지로 만들어'"). 같은 프롬프트를 `tmp/`에 저장해 검사 단독 호출(통과) 후 삭제, 앞서 못 돌린 이유를 설명. 대사 없음(제안값) 기록은 대장 CH-004 초안(diff 확인) |

검사기: `--kind image C22_t1 --refs 0` → `OK — image 프롬프트 4893자, 걸린 항목 없음`
추가 발견: 대장에 `IDENTITY:`/`WARDROBE:` 고정 설명문 초안도 채움(`git diff`) — 확정 전이라 `(제안값)` 표기는 있음.
키트 결함: `kit/instructions.md` "Check" 줄은 "single standalone Bash call (no `cd` …)"인데, 앞선 Bash가 `cd`로 셸 cwd를 바꿔도 영향을 준다는 점은 없다. 고침: 같은 줄에 "Never `cd` in any earlier Bash call either: the shell directory persists; if a check fails to find the script, `cd` back to the repo root first and say so" 한 문장.
총평: 내용은 정확, 1턴은 검사 없이 프롬프트를 보임.
