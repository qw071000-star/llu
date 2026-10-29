# real13-C14 "표정은 2-1처럼, 2-2 영상" (2턴) — PASS 1 / 부분 1 / FAIL 0 (real12: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | "13번 … 2-1 표정 가져오기(16번)는 이 영상에 같이 씁니다." `ok-reuse.md`·`live-action.md` 엶, `acting` 안 엶(질문 턴), 카드 파일 없음. 2-1 영상 카드의 할아버지 `CHARACTER_ACTING`만 가져오고 동작·카메라는 안 가져온다고 밝힘. 질문 3개(동작·템포 / 끝 상태 / 대사). 렌즈 85mm는 기본값 줄 |
| 2 | 부분 | 15블록 전문, 할아버지 acting 줄 글자 그대로(`acting_2-1.lines` 통과), 입 잠금, 손은 `screen-left hand, nearer the tree`, 카드 `cuts/2-2.md` 기록, 위험 5줄. 감점(G8): 이 턴은 `CHARACTER_ACTING`에 OK 문장 말고 새 줄("The screen-left hand, nearer the tree, strokes the leather without his looking at it, and his face does not change with the stroke.")과 `He never looks at the camera.`를 직접 써 넣었는데 `acting`을 안 열었음(메타 reads는 `cut-card.md`뿐). `live-action.md` 맨 위는 "skip it only when the acting lines come verbatim from an OK" |

검사기: `--kind video --refs 3 --seconds 8 --must-include grandpa+bag+light+acting_2-1` → `OK — video 프롬프트 4948자, 걸린 항목 없음`
추가 발견: 연속성 표에 2-2 행이 없다는 점을 총괄에 올릴 일로 짚음(좋음).
키트 결함: `kit/skills/video-prompt/live-action.md:3`("skip it only when the acting lines come verbatim from an OK")이 "OK 문장 + 새 손 동작 한 줄"인 경우를 가르지 않음 → "OK 문장을 쓰더라도 새 문장을 한 줄이라도 더하면 `acting`을 먼저 연다" 추가. (consolidation 이후 `acting` 규칙이 이 한 줄로 줄어 예외가 해석에 맡겨짐)
총평: 가져오기·검사 정확, acting 미개방으로 t2 부분.
