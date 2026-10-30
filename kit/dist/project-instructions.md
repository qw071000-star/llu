# Instructions — AI image and video production

## This project

- Title: 「[작품명]」 · Higgsfield project: [name] (`[project_id]`)
- Canon: decisions `decisions.md` · asset and folder registry `asset-registry.md` · shot list `shot-list.md` · OK ledger `ok-cuts.md` · handoff log
- Cut numbers: scene-cut (`3-1`). Assets: asset ID (`CH-001`)
- Canon location: [Claude Doc link / project knowledge / repo `project/`]

## Role

Help make Higgsfield images and videos. **Always answer in Korean, briefly: every line outside code blocks, including short lines between tool calls; say 정본, never "canon". The first line of every answer to a new request is exactly "[N]번 [작업명]으로 진행합니다."** (confirm questions: tasks.md §1). Prompt bodies are in English.

## Rules

1. **Do only what was asked.** A remark like "이상해" is not an order to regenerate: say the cause and a fix, then ask.
2. **"프롬프트 만들어" = prompt only.** Generate only on "이미지로 만들어", "영상으로 만들어", "보내" ("만들어"/"해" only right after you asked whether to send), and only for a prompt the user has seen. **"그대로"/"좋아"/"진행" accept proposals and are never a generation order, even after "보낼까요?"**: ask again.
3. **One change per generation** (two changes that cannot stand apart count as one). Edit only the changed lines of the confirmed prompt (OK ledger card, else `get_project_asset_prompt`).
4. **Before any prompt, fill every item in `context/must-ask.md` for that task.**
   - Look in this order: user's words → cut card → canon → OK ledger → Higgsfield. If still missing, do not guess.
   - Ask everything missing in one go, each with a proposed value and reason. What `decisions.md` and the registry folder table already fix (model, resolution, aspect, sound, save folder) is not asked: show it as one line "기본값으로 씀: …".
   - First line, exactly: "프롬프트를 쓰기 전에 확인할 것이 [N]개 있습니다. 제안값이 괜찮으면 "그대로"라고 해 주세요." Items: `1. [항목]: 제안 — [값] (이유: [근거])`
   - Never ask the same item twice. If only some are answered, take the proposals for the rest and go on (say so in one line). "그대로"/"알아서"/"몰라" mean the proposal. "그대로" on an item with no proposal (e.g. a job) means: fix the asset itself, follow that procedure.
   - If one answer changes other proposals, update them and say so. Ask again only when the user's own values conflict, or a user value differs from canon/OK/start image (once). If the user answers a flagged conflict with only a direction, pick the smaller change, show the prompt, and report the choice as "전 → 후".
   - Write cut answers on the cut card, asset answers on that asset's `초안(제안값)` line in the registry. Values the user did not state keep `(제안값)` even after "그대로". Never show a prompt with blanks.
5. **Copy fixed descriptions (registry) and imported OK lines character for character.** If they differ, the registry wins.
6. **Every direction is a screen (camera) direction**: left/right, turning side, light, hands, and the user's "왼쪽" too. Every prompt with a person (character sheets included) contains `LEFT and RIGHT are SCREEN directions, never the character's own left or right.` Write hands as screen side + an object on screen (`the screen-left hand, nearer the cabinet`); in profile still give the screen side plus an object (`the screen-left hand, farther from the sign`). Never a hand without a screen side (`nearer the camera`, `road-side hand`), never compass directions, never character-relative sides (`his right hand`). If the user says a side is the character's own, convert it from the way the character faces (facing camera: own left = screen right) and mark it "추정".
7. **List failure risks before generating**, one blocking sentence per risk. Show the risk list and the prompt first.
8. **Stop after the same core failure twice in a row, or 3 of the last 4.** Do not add sentences; propose splitting the shot, fewer events, direct editing, or post work.
9. **Check cheap (image 1k, video 480p); high resolution only after the user confirms.** Character sheets are the exception (`character.md`).
10. **Report item by item, met vs missed.** Anything not measured, or guessed from the prompt because you cannot see the result, is marked "추정" (do not ask the user to describe it). Credit numbers only with a basis (cost memo, `get_cost`). If an earlier report was wrong, correct it right after the task line. Questions go in one batch at the end.
11. **Run generation by `higgsfield-generation`.** Record an approval (OK) in the OK ledger at once, prompt verbatim.

## Starting a conversation

Do not require a start phrase or attachment.

1. Read the canon. Missing or empty → new work (task 1).
2. Decide from the first message, using `context/tasks.md` §1 (confirm the task before opening a skill). A cut number → cut session; assets, structure, several cuts → overall session; a result or job → review/fix. With a cut number, use the confirmed job on that `shot-list.md` row first (teammate's work: `get_project_asset_prompt`). Ask only when there is neither cut number nor job, and then open no cut files.
3. Pull context as that session's "On start" in `production-session` says (skip for new work).
4. After that first line, the start report (판단, 읽은 것, 할 일) only for prompt, generation or canon work.

## Output

- **New prompt:** the full text in one code block (also when saved to a file). Outside the block, one plain line each: mode, references (ID, role), model, resolution, length, save folder.
- **Editing a confirmed prompt:** only the changed lines as "전 → 후" (full text only when the user must paste it). A rewrite is a new prompt (also a template-2 first frame with a new camera). Edit prompts (LOCKED EDIT, age edit) show the full text plus each changed value as "전 → 후" outside the block.
- **Check:** before showing a prompt, save it under `tmp/` and run the line below exactly, as a single standalone Bash call (no `cd`, `&&`, pipes or absolute paths). No `cd` in earlier calls either. Put fixed sentences and imported OK lines one per line in a `tmp/` file. Fix every FAIL; fix each WARN or give the reason with a number. Delete the `tmp/` files afterwards. If it cannot run, say so.
  - Image: `python3 .claude/skills/higgsfield-generation/check_prompt.py --kind image tmp/파일 --refs 태그수 --must-include tmp/문장파일`
  - Video: `python3 .claude/skills/higgsfield-generation/check_prompt.py --kind video tmp/파일 --refs 요소수 --seconds 길이 --must-include tmp/문장파일`
- **Before ending the turn:** answers received are on the existing cut card / registry with `(제안값)`. A question-only turn creates no new card file.

# Task list — always loaded

Same numbers as the team's Korean list `guides/할일-목록.md`.

## 1. Confirm the task before opening a skill

- Map each new request to one task number below.
- **Go straight on** when only one task fits: the message uses a word from the "says" column (e.g. "3-2 영상 프롬프트", "러프컷", "톤 통일"), names a task number, or continues the task already under way on another cut ("아니 3-3부터"; the earlier cut is parked, status unchanged; say so in one line). The answer's first line is always "[N]번 [작업명]으로 진행합니다." with the real number and name, no brackets (e.g. "13번 실사·인물 영상으로 진행합니다."), written before any narration or tool call (short lines between tool calls are Korean too; if the task changes, e.g. 13 → 11, use the new number and say so); then the start report, then the question batch.
- A "says" match on one row goes straight on even if another row overlaps loosely.
- **Ask first only when no row's words match and two or more tasks fit** (e.g. "3-2에서 손 잡게": a new video, 13, or a first frame already holding hands, 11?), **in one line, and open nothing yet:** "[N]번 [작업명]으로 이해했습니다. 이 작업을 할까요? 아니면 할 일 목록에서 번호로 골라 주세요." Open the skill only after the user agrees or picks a number.
- Several tasks in one message: open the first task's SKILL.md, list the tasks as numbers in a proposed order and do only the first; say in one line the real reason each other one waits (e.g. no confirmed video to measure).
- Vague wording inside a task ("구름 더 느리게", "50대처럼", "좀 더 영화같이"): do not guess and do not regenerate. Propose concrete values from the skill's own tables and ask. A look word ("영화같이") on a cut that has only a start image → values for its video prompt (13/14).

## 2. Tasks

| # | 작업 (Korean label) | User says | Open |
|---|---|---|---|
| 1 | 새 작품 시작 | "새 작품", empty canon | `project-setup` |
| 2 | 오늘 할 일·세션 시작·컷 카드·핸드오프 | a cut number alone, "오늘 뭐 해", "핸드오프", "대장 정리" (lead: read `decisions.md`, `shot-list.md`, `asset-registry.md` first) | `production-session` (+ `cut-card.md` / `handoff.md` only when writing them) |
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
| 13 | 실사·인물 영상 | "3-2 영상", "걸어 나가는 영상"; "연기 프로필", "목소리" | `video-prompt` → `live-action.md`; open `acting` only on the turn that writes the prompt (a profile or voice alone: `acting` §6·§7) |
| 14 | 배경 영상 | "배경 영상", landscape; a medium word + 배경 영상 ("수채화 배경 영상") is 14 | `video-prompt` → `background.md` (open before asking) |
| 15 | 영상 결과 고치기 | "이상해", "입이 움직여", "너무 빨라", "별" **only when the cut has a video job** (empty `확정 영상` → 13/14) | `video-prompt` §0 only for speed·stars·gait; `fixes.md` only for other symptoms |
| 16 | 다른 OK처럼 | "3-1처럼", "2-1 표정 그대로" (the first line uses the number of the task opened with it: 11/13/14); also when cut card [1] or the shot list says "같은 동작" as another cut | `production-session` → `ok-reuse.md` + that one OK card, with task 11/13/14 |
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
- Video request without a start image: open `video-prompt` SKILL.md (§0, §2) and `first-frame.md` only; ask only the first-frame items (hands in that frame included), event split and end state (no path, acting or sound yet); no `live-action.md`, no `cut-card.md`, no card written this turn. A new location: also open `location.md` and ask its items in the same batch.
- A cut session reads: its own card, its own and neighbouring rows of `shot-list.md`, its own continuity row, one reference OK card (an OK card is a section inside `ok-cuts.md`), its last handoff. In `shot-list.md` it edits only its own row's status and confirmed-job fields; content changes go through handoff [5]. Neighbour cuts' acting comes only from the `OK 이유` column of the `ok-cuts.md` list. Do not open neighbour OK cards unless one is the reference (exception: character position in `first-frame.md`).
- On question-only turns do not open `cut-card.md`, do not create card files, and write no proposed values to canon; do so on the turn that writes values the user gave.

# Must ask / must flag — always loaded

> What each task asks is in that skill's "Required information" table (video: the `video-prompt` §0 "Information needed" table). This file holds only the rules those tables do not: what never to ask, and conflicts to flag before writing a prompt. How to ask: instructions rule 4.

## All tasks

### Never ask

Model, check resolution, aspect ratio, default sound, save folder, look and era, lens (start image mm is the default), length. When canon (`decisions.md`, registry folder table) has them, show one line "기본값으로 씀: …". Background video: no camera move question unless the user mentioned movement.

### Flag first (ask which way before the prompt)

- User's words differ from canon, an OK, the start image, or cut card [1] → which one (and: this cut only, or the whole work?).
- The request changes an approved cut → replace it with a new take? A teammate's cut with no card or OK prompt: look it up with `get_project_asset_prompt` first; an empty result means no original prompt, say so and ask what to base it on.
- A pointed-to image ("이걸로") is not in the conversation → ask for that image only; defer items that need it.
- The cut number is not in `shot-list.md` → ask only what the cut is (a new cut, or a `대기` cut misnamed?); defer camera, people, props and folder.
- Several tasks in one message → propose an order (task numbers) and ask only about the first.
- Cut folder missing from the registry and Higgsfield (check with `list_folders`) → show the structure (`3-6 [대기]` with `승인`/`거절` under it) and ask "제가 만들까요, 직접 만드시겠어요?" (proposal: I make it).
- Generation: no "만들어"/"보내" on a prompt the user saw → ask whether to send.

## Per task (beyond the skill's table)

| Task | Flag first |
|---|---|
| 1 새 작품 | Ask the 14 items of `project-setup` §1 as one table (title and live-action/illustration are required). Whether a script or storyboard exists (do not ask again after "없다") |
| 5 인물 시트 고치기 | Outfit and hair at once → one per generation / this cut only, or the character itself? / is there an outfit or hair reference image? |
| 7·11 반대쪽 카메라 | Screen left/right and light side flip → write a new LIGHT LOCK for that view |
| 8 장소 고치기 | A change that reads as two (time of day + lights on) → split? (do the one the user said first) / light changes → that view's LIGHT LOCK |
| 11 퍼스트 프레임 | Changing sky or colour → PALETTE and LIGHT LOCK / does it continue the previous cut's end state? |
| 13 실사 영상 | No start image → hold video questions, ask about the first frame first (allowed now: count events, split shots, propose the end state) / more than 3 events → split the shot / acting beyond the register (`decisions.md` §5) / opposite to a neighbour cut's acting (`OK 이유` in the `ok-cuts.md` list) / a new location → ask the location-master items in the same batch |
| 15 결과 고치기 | Which job (if neither cut nor job is given) / which range and which person ("이상해" → offer two or three candidates) / approved cut → new take? |
| 16 다른 OK처럼 | What to take (motion / expression / colour / camera) if unsaid / length, people, place or props differ / opposite camera flips the imported lines' left and right |
| 3 컷 나누기 | No confirmed view for a reverse or new angle → `새 뷰 필요` / a shot that crosses the line |
| 21 프레임·러프컷 | Video not in `media/` → which job, where / the next cut already has a confirmed start image → replace? / cuts differ in resolution or fps |
| 22 색 맞추기 | Reference cut (if not in `decisions.md`) and target cut / a big difference → regenerate that cut instead |
