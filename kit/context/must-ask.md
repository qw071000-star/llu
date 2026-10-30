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
