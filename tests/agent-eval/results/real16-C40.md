# real16-C40 한 번에 여러 수정 ("이것저것 다") (2턴) — PASS 10 / 부분 0 / FAIL 0

> 채점: tests/agent-eval/grader-rules.md. 출력 `runs-real16/C40/out/turn*.md`, 메타 `turn*.meta.json`, 정본 diff, 기대 `scenarios.md`. G1: 모든 턴에서 `mcp__` 도구 호출 없음, RUN 밖 파일 읽기 없음, 시킨 적 없는 생성 없음(확인함).

## 턴별 판정

| 턴 | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 첫 줄·작업 번호 | PASS | `11번 퍼스트·끝 프레임으로 진행합니다.` |
| 1 | 세 변경을 나눠 순서 제안, 첫 번째만 | PASS | `한 번에 하나만 바꿀 수 있어서 첫 번째 것만 진행하고 … 1. 진행 순서: 제안 — 머리 풀기 → 장화 파란색 → 하늘 붉게`; 장화·하늘 값은 해당 차례에 묻는다고 미룸 |
| 1 | 장화(의상)가 정본 WARDROBE와 다름, 하늘이 PALETTE에 영향 | PASS | `장화: CH-002는 빨간 장화입니다`, `하늘: 장소 대장 PALETTE는 짙은 파랑 노을하늘 15%입니다` (LIGHT LOCK 언급은 미룸) |
| 1 | 이 컷만/인물 설정 변경 묻기, 승인 컷 새 테이크 | PASS | `3. 적용 범위: 제안 — 이 컷만 … Except: 한 줄만`, `2. 승인본 처리: … 새 테이크` |
| 1 | 생성 없음·질문 한 묶음 | PASS | 도구 0회, 질문 4개 |
| 2 | "머리부터 해"의 "해" ≠ 생성, 머리 하나만 | PASS | `"해"는 보내라는 말이 아니라서 프롬프트까지만 만듭니다`; `ONLY CHANGE: the girl's hair …` |
| 2 | LOCKED EDIT 표준 여는 문장·WARDROBE·LIGHT LOCK 글자 그대로 | PASS | `Edit <<<ff_3-3_v1>>> WITHOUT reframing …`, `WARDROBE: A yellow raincoat …`, LIGHT LOCK must-include 통과 |
| 2 | 정본과 다른 줄은 `Except:` 한 줄·전 → 후 | PASS | `Except: her hair is worn loose instead of in a low ponytail.`; `머리: 낮은 포니테일 → 끈 없이 풀어 내린 어깨 길이 생머리` (CH-002 시트의 shoulder-length와 일치) |
| 2 | G7 검사·위험 목록·카드 `(제안값)` | PASS | check 1587자 통과, diff 3-3.md [5]에 `(제안값)` |
| 2 | G1 생성 통제 | PASS | `이 프롬프트로 보낼까요? (1k 1장)` |

## 검사기 결과

- `python3 kit/skills/higgsfield-generation/check_prompt.py --kind image --refs 1 --must-include girl+light C40_turn2_b1.txt`
  - 결과: `OK — image 프롬프트 1587자, 걸린 항목 없음`

## 추가 발견

- 2턴 프롬프트에 first-frame.md 틀 1의 `FIRST FRAME of a film shot — the exact state at 0:00 of the video.` 줄이 없다(C30은 있음). 좌표 문장은 따로 넣음.

## 키트 결함

- `kit/skills/image-prompt/first-frame.md:45` 틀 1은 신규 추가용뿐이라, 승인된 첫 프레임을 한 가지만 고치는 편집(C30·C32·C40)의 모양이 플레이어마다 다르다. 수정: 편집용 변형 한 틀을 추가.

## 총평

세 변경을 순서대로 나누고 머리만 정확히 진행. 정본과의 차이를 모두 짚음.
