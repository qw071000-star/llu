# Task list — always loaded

Same numbers as the team's Korean list `guides/할일-목록.md`.

## 1. Confirm the task before opening a skill

- Map each new request to one task number below.
- **Go straight on** when only one task fits: the message uses a word from the "says" column (e.g. "3-2 영상 프롬프트", "러프컷", "톤 통일"), names a task number, or continues the task already under way on another cut ("아니 3-3부터"; the earlier cut is parked, status unchanged; say so in one line). The answer's first line is always "[N]번 [작업명]으로 진행합니다." with the real number and name, no brackets (e.g. "13번 실사·인물 영상으로 진행합니다."), written before any narration or tool call (short lines between tool calls are Korean too; if the task changes, e.g. 13 → 11, use the new number and say so); then the start report, then the question batch.
- A "says" match on one row goes straight on even if another row overlaps loosely.
- **Ask first only when no row's words match and two or more tasks fit** (e.g. "3-6 별 더 반짝" with no 3-6 video yet: 14 or 15?), **in one line, and open nothing yet:** "[N]번 [작업명]으로 이해했습니다. 이 작업을 할까요? 아니면 할 일 목록에서 번호로 골라 주세요." Open the skill only after the user agrees or picks a number.
- Several tasks in one message: open the first task's SKILL.md, list the tasks as numbers in a proposed order and do only the first; say in one line the real reason each other one waits (e.g. no confirmed video to measure).
- Vague wording inside a task ("구름 더 느리게", "50대처럼", "좀 더 영화같이"): do not guess and do not regenerate. Propose concrete values from the skill's own tables and ask. A look word ("영화같이") on a cut that has only a start image → values for its video prompt (13/14).

## 2. Tasks

| # | 작업 (Korean label) | User says | Open |
|---|---|---|---|
| 1 | 새 작품 시작 | "새 작품", empty canon | `project-setup` |
| 2 | 오늘 할 일·세션 시작·컷 카드·핸드오프 | a cut number alone, "오늘 뭐 해", "핸드오프", "대장 정리" | `production-session` (+ `cut-card.md` / `handoff.md` only when writing them) |
| 3 | 장면 컷 나누기 | "컷 나눠", "콘티", "커버리지", "리버스" | `shot-design` |
| 4 | 인물 시트 만들기 | "인물 시트" | `image-prompt` → `character.md` |
| 5 | 인물 시트 고치기 (옷·머리·나이) | "옷을", "머리", "50대처럼", "50대 때 모습도" on the sheet itself | `image-prompt` → `character-edit.md` |
| 6 | 장소 만들기 | "정류장 만들어", "방 만들어" | `image-prompt` → `location.md` |
| 7 | 장소 새 시점 (반대 방향·더 가까이·확대) | "반대 방향", "뒤에서 본" (location only), "확대" | `image-prompt` → `location.md` + `location-view.md` |
| 8 | 장소 고치기 (불·시간대·시대·물건 빼기) | "불 켜진", "밤으로", "1970년대로", "빼" | `image-prompt` → `location.md` + `location-edit.md` |
| 9 | 소품 만들기·고치기 | "가방 만들어", "버스", "너무 새 거 같아" | `image-prompt` → `prop.md` |
| 10 | 그림체 | "수채화", "그림체" | `image-prompt` → `style.md` |
| 11 | 퍼스트·끝 프레임 | "퍼스트 프레임", "끝 프레임", "시작 이미지", "3-4 뒤에서 본 첫 프레임", swapping a person in a frame | `image-prompt` → `first-frame.md` |
| 12 | 이미지 결과 일부 고치기 | "여기만 고쳐" on an image result | `image-prompt` §3 + that kind's file |
| 13 | 실사·인물 영상 | "3-2 영상", "걸어 나가는 영상" | `video-prompt` → `live-action.md`; open `acting` only on the turn that writes the prompt |
| 14 | 배경 영상 | "배경 영상", landscape | `video-prompt` → `background.md` (open before asking) |
| 15 | 영상 결과 고치기 | "이상해", "입이 움직여", "너무 빨라", "별" on an existing video only (no video job yet → 13/14) | `video-prompt` §0 only for speed·stars·gait; `fixes.md` only for other symptoms |
| 16 | 다른 OK처럼 | "3-1처럼", "2-1 표정 그대로" | `production-session` → `ok-reuse.md` + that one OK card, with task 11/13/14 |
| 17 | 고해상도 | "1080p", "2k" | `video-prompt` → `rerender.md` |
| 18 | 생성 보내기 | "이미지로 만들어", "영상으로 만들어", "보내" (prompt already shown) | `higgsfield-generation` |
| 19 | 결과 확인·OK·거절 | "됐어", "OK", "거절", "보류" | `higgsfield-generation` (+ `qa-metrics.md` for numeric analysis) |
| 20 | 크레딧·폴더 | "크레딧", "폴더 만들어" | `higgsfield-generation` (open its §2 folder part only on the turn that creates folders) |
| 21 | 마지막 프레임·러프컷 (Claude Code) | "마지막 프레임", "이어 붙여", "러프컷" | `assembly` |
| 22 | 색 맞추기 (Claude Code) | "색 맞춰", "톤 통일", "더 노래" | `color-continuity` (before a rough cut, 21) |
| 23 | OK 프롬프트 다시 보기·번역 | "프롬프트 다시", "한국어로" | that one OK card (no check). English original as is; **a translation is plain text, never in a code block** |

## 3. What not to open

- **Never open another cut's card or handoff**, not even with `head`/`grep` to see the format. Card format comes only from `cut-card.md`. A cut session opens only its own cut's handoff. Do not open the full script, old logs, or files not in this table (old sentences leak into prompts).
- Open the SKILL.md first, then only the stage file(s) on that task's row.
- Video request without a start image: open `video-prompt` SKILL.md (§0, §2) and `first-frame.md` only; ask only the first-frame items, event split and end state (no path, acting, hands or sound yet); no `live-action.md`, no `cut-card.md`, no card written this turn. A new location: also open `location.md` and ask its items in the same batch.
- A cut session reads: its own card, its own and neighbouring rows of `shot-list.md`, its own continuity row, one reference OK card (an OK card is a section inside `ok-cuts.md`), its last handoff. In `shot-list.md` it edits only its own row's status and confirmed-job fields; content changes go through handoff [5]. Neighbour cuts' acting comes only from the `OK 이유` column of the `ok-cuts.md` list. Do not open neighbour OK cards unless one is the reference (exception: character position in `first-frame.md`).
- On question-only turns do not open `cut-card.md`, do not create card files, and write no proposed values to canon; do so on the turn that writes values the user gave.
