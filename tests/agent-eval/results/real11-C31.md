# real11-C31 장소 시간대 바꾸기 — "밤으로, 형광등 켜진 걸로" (2턴) — PASS 1 / 부분 1 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

플레이어가 본 `.claude/context/tasks.md`는 "컷 번호/에셋 + 말이 있으면 바로, 아니면 먼저 확인" 구판이다(`[N]번 … 진행합니다` 줄이 아직 없는 판). 그래서 그 줄이 없는 것은 감점하지 않았다.

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`·`location.md`·`location-edit.md`만 읽음(`location-view.md` 안 열림). 한 줄 첫 문장 그대로 "프롬프트를 쓰기 전에 확인할 것이 3개 있습니다". 변경이 둘로 읽힘을 짚고 나눔: "두 번에 나눠 만듭니다. 1단계는 밤으로 바꾸기 … 형광등은 꺼진 채 … 1단계 결과는 아직 "불 켜진 밤"이 아닙니다"(`location-edit.md` Rules 1번 충족). 새 LIGHT LOCK 제안 `The shelter's single fluorescent tube, hanging under the roof above the bench, is the only key.`(광원 = 형광등, 물건 기준 위치 제안). 해 질 녘 문장 없음. 질문만, 생성 없음 |
| 2 | 부분 | 내용은 맞음: 1단계 LOCKED EDIT, `The low sun, its raking light … are gone. The shelter's single fluorescent tube stays off.`, PRESERVE에 `The unlit fluorescent tube`, 해 질 녘 LIGHT LOCK 문장 안 남김, `LEFT and RIGHT are SCREEN directions …`. 블록 밖 모드·참조·모델·1k·`fld-locs`, 위험 4개, 대장에 `초안(제안값)` 기록(diff `+초안(제안값) LC-001 밤 STATE …`), 생성 안 함. **빠진 것:** 지침 Output "Edit prompts … show the full text plus each changed value as 전 → 후"인데 블록 밖에 전 → 후 줄이 없음 |

## 검사기
- 내 실행 `--kind image --refs 1`(고정 문장 없음 — 빛이 바뀌는 편집이라 LIGHT LOCK 고정 문장은 넣지 않음): `OK — image 프롬프트 1544자, 걸린 항목 없음`
- 플레이어 실행: `check_prompt.py --kind image tmp/lc001-night-step1.txt --refs 1 --must-include tmp/lc001-must.txt` 단독 호출, 삭제까지 함.

## 추가 발견
- G1 위반 없음(mcp 호출 없음, RUN 밖 읽기 없음). 2턴에서 `ls`·`cat`을 쓰지 않고 정본 `asset-registry.md`만 고침.
- 1단계 프롬프트에 형광등 꺼짐 + 달·별 없음 → 거의 검은 이미지가 나올 위험을 스스로 짚음(좋음).

## 키트 결함
- `kit/instructions.md` Output "Editing a confirmed prompt" 줄(전 → 후)이 "Edit prompts (LOCKED EDIT, …)" 괄호 안에만 있어 눈에 띄지 않는다. 제안: `kit/skills/image-prompt/location-edit.md` Rules 끝에 "Show 전 → 후 for each changed value outside the block" 한 줄을 넣는다.

## 총평
시간대와 불 켜기를 나눠 1단계가 최종 모습이 아님을 알렸으나, 2턴에 전 → 후 줄이 빠졌다.
