# Task list — always loaded

## 1. Confirm the task before opening a skill

- Map each new request to one task number below.
- **Go straight on** when only one task fits: the message uses a word from the "says" column, names a task number, or continues the task already under way. The answer's first line is always "[N]번 [작업명]으로 진행합니다." with the real number and name, no brackets, 으로/로 by the last syllable, written before any narration; then the start report, then the question batch.
- **Ask first only when no row's words match and two or more tasks fit**, in one line, and open nothing yet: "[N]번 [작업명]으로 이해했습니다. 이 작업을 할까요? 아니면 할 일 목록에서 번호로 골라 주세요." Open the skill only after the user agrees or picks a number.
- Several tasks in one message: open the first task's SKILL.md, list the tasks as numbers in a proposed order and do only the first.
- Vague wording ("좀 더 영화같이", "더 귀엽게"): do not guess. Propose concrete values from the skill's tables and ask.

## 2. Tasks

| # | 작업 | User says | Open |
|---|---|---|---|
| 1 | 새 작품 시작 | "새 작품", empty canon | `mj-setup` |
| 2 | 오늘 할 일·세션 시작·컷 카드·핸드오프 | a cut number alone, "오늘 뭐 해", "핸드오프", "대장 정리" | `mj-production` (+ `cut-card.md` / `handoff.md` only when writing them; `shared-account.md` if 공용 계정) |
| 3 | 장면 컷 나누기 | "컷 나눠", "콘티", "커버리지", "리버스" | `mj-shots` |
| 4 | 인물 만들기 | "인물 만들어", "인물 시트", "캐릭터" | `mj-image` → `character.md` |
| 5 | 인물 고치기 (옷·머리·나이) | "옷을", "머리", "50대처럼" on an approved character | `mj-image` → `character.md` (editing) |
| 6 | 장소 만들기 | "정류장 만들어", "방 만들어" | `mj-image` → `location.md` |
| 7 | 장소 새 시점 | "반대 방향", "뒤에서 본", "더 가까이" | `mj-image` → `location.md` (new view) |
| 8 | 소품 | "가방 만들어", "소품" | `mj-image` → `prop.md` |
| 9 | 그림체 | "그림체", "스타일 레퍼런스", "sref" | `mj-image` SKILL §4 |
| 10 | 스틸 컷·퍼스트 프레임 | "3-4 이미지 만들어", "퍼스트 프레임", "시작 이미지" | `mj-image` → `first-frame.md` |
| 11 | 결과 판정·OK·거절 | "됐어", "OK", "거절", "보류", a pasted image or link | `mj-production` §4 (OK record) |
| 12 | 짧은 영상 (이미지→영상) | "영상으로", "움직이게", "애니메이트" | `mj-video` |
| 13 | 다른 OK처럼 | "3-1처럼", "2-1 표정 그대로" | `mj-production` §5 + that one OK card |
| 14 | 프롬프트 고치기 (결과가 마음에 안 들 때) | "마음에 안 들어", "여기만 바꿔", "더 ~하게", "이상해", a pasted image with a complaint | `mj-image` §7 (images) or `mj-video` §3 (clips), then the stage file of that asset |
| 15 | OK 프롬프트 다시 보기·번역 | "프롬프트 다시", "한국어로" | that one OK card. English original as is; **a translation is plain text, never in a code block** |

## 3. What not to open

- **Never open another cut's card or handoff**, not even to see the format. Card format comes only from `cut-card.md`. A cut session opens only its own cut's handoff.
- Open the SKILL.md first, then only the stage file(s) on that task's row.
- A cut session reads: its own card, its own and neighbouring rows of `shot-list.md`, one reference OK card, its last handoff. In `shot-list.md` it edits only its own row's `담당`, status and confirmed-link fields; content changes go through handoff [5].
- On question-only turns do not open `cut-card.md`, do not create card files, and write no proposed values to canon.
