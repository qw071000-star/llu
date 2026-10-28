# 맹검 시험 기록

키트를 모르는 서브에이전트(플레이어)가 시험 작품 「빈 정류장」에서 Claude 역할을 했다. 다른 서브에이전트(채점자)가 그 결과를 키트 규칙으로 채점했다.

## 회차

| 회차 | 폴더 | 키트 판(커밋) | 플레이어 모델 | 체인 |
|---|---|---|---|---|
| 1차 | `r1/` | `01aeb5a` (결함 수정 전) | 이 세션과 같은 모델(Opus) | C01~C19 |
| 2차 | `r2/` | `e01c78e` (결함 약 35건 수정 후) | Opus | C01 C04 C06 C08 C10 C12 C18 |
| 소넷 | `sonnet/` | `e01c78e` | Sonnet | C02 C08 C10 C12 C13 C14 C17 C18 |
| 소넷 2 (정리된 키트) | `sonnet2/` | `c4aa989`, C17·C18은 `81de8f1` | Sonnet | C02 C08 C10 C12 C13 C14 C17 C18 (+ `C18-before-fix`: "됐어" 회귀 기록) |

## 체인 폴더 안

| 파일 | 내용 |
|---|---|
| `out/turnN.md` | 플레이어의 채팅 답 (맨 아래 `=== 메타 ===`: 연 파일, 부른 도구, 고친 정본) |
| `out/turn0.md` | 미리 넣어 둔 앞 대화 (C17, C18) |
| `project/` | 플레이어가 고친 뒤의 정본 |
| `changes.diff` | 시작 정본 대비 바뀐 내용 |
| `sim/higgsfield.md` | Higgsfield 시뮬레이션 결과표 (실제 Higgsfield는 부르지 않았다) |
| `CLAUDE.md`, `SKILLS-INDEX.md`, `PLAYER-RULES.md` | 플레이어가 받은 환경 |

- 키트 사본(`.claude/`)은 위 커밋의 `kit/`와 같아서 뺐다.
- 실행 폴더의 git 저장소(`.git/`)도 뺐다.

## 그 밖의 파일

- `transcripts/`: 서브에이전트 대화 전체(jsonl, gzip). 이름은 `회차_역할_체인_모델`이다.
  - 사용자 이메일 주소는 `[email]`로 가렸다.
- `../agents.tsv`: 에이전트 ID와 체인, 역할, 모델, 보낸 사용자 메시지.
- 채점 결과: `../results/`(1차 `C01.md`…, 2차 `r2-*.md`, 소넷 `sonnet-*.md`, 소넷 2 `sonnet2-*.md`).
- 진행 방법: `../player-rules.md`, `../grader-rules.md`, `../scenarios.md`, `../make_run.sh`.

## 다시 보관하기

```bash
python3 tests/agent-eval/archive_records.py ~/.claude/projects/<세션>/<id>/subagents
```
