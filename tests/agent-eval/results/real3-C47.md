# real3-C47 — 두 인물 접촉 ("손 잡게")

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | 연 것: production-session, video-prompt SKILL·live-action.md, ok-reuse.md, OK 대장(3-1 영상). `acting` 안 엶. [TOOL] 2줄(list_folders 등, sim 근거, 실제 mcp 아님). 질문 6개: 카드 [1] "3-1과 같은 동작"과 다름, 사건 4개→대사 빼기, "손녀 화면 왼쪽 손 → 할아버지 화면 오른쪽 손(가방 위)", 3-3 이음새 충돌, 시선, 연기 양 끝(절제). 가방 위 손과의 겹침 짚음. 경미: 질문 턴에 카드 [1]을 먼저 고침 |
| 2 ("그대로", 프롬프트 턴) | PASS | `acting/SKILL.md` 열고 15블록. 위험 8개, 블록 밖 모드·참조 4·모델·해상도·길이·소리·폴더. 손은 `screen-left hand, nearer the persimmon tree` / `screen-right hand, nearer the sign`. 3-1에서 가져온 줄은 바꾼 부분을 전→후로 보임. 검사기 3회 실행. WARN 길이는 6,443자와 줄인 양을 적음 |

검사기(`--kind video --refs 4 --seconds 8 --must-include bag,girl,grandpa,light`, 채점자 재실행):
```
WARN  길이 6443자. 5,500자 이하가 안전했다. 남기려면 이 숫자를 그대로 적고 이유를 쓴다
— FAIL 0 · WARN 1 · 6443자
```
(3-1 motion 줄까지 must-include에 넣으면 FAIL 3이지만, 새 사건 때문에 의도적으로 바꾼 줄이고 전→후로 보였으므로 플레이어 처리가 맞다.)

2회차 대비: PASS 2 유지(검사 결과 6,115→6,443자, 같은 WARN).

키트 결함: 없음. 경미: 사건 4개일 때 WARN 이유 칸에 "약 400자를 뺐다"만 적고 "무엇을 더 못 줄이는지"는 적음(예시 형식 `live-action.md:31`과 거의 같음).

총평: PASS 2 / 부분 0 / FAIL 0 (2회차와 동일).
