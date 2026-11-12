# Shared-account operation

Applies when `decisions.md` §7 says `운영 방식: 공용 계정`: one Claude account and one Midjourney account used by several people in turns. Docs edits and Midjourney jobs all show the same account, so **nothing records who did what unless the canon does**. Just follow these rules.

1. **Who.** The user's first message names them (`나는 지수`). If missing, ask once per conversation. The name goes into: the cut list `담당` cell, the handoff header, the OK card `승인` line.
2. **Claim before work.** Read the cut's `상태` and `담당` first. If another name holds the cut in `진행` or `검토`, say so in one line and ask before working on it. If the cell is empty or the user's own, write the user's name in `담당`.
3. **Writes.** The lead is named in `decisions.md` §7 `총괄:` (ask once if missing). `decisions.md` and `asset-registry.md` are lead-only: if the speaker is not the lead, do not edit them or show an edit block for them; put the request in handoff [5] for the lead. A cut session writes its own row (`담당`, `상태`, confirmed links), its own card, OK cards, handoffs.
4. **OK cards are append-only.** Never edit an approved card or its prompt. A correction is a new line under that card: `정정(날짜 · 이름): [무엇을 → 무엇으로 · 이유]`. A replacement is a new take: new card; the old card goes to the log. Before writing any card, find its title (`3-1 스틸`, `3-1 영상`); if it exists, ask: correction or new take?
5. **Start image and clip are saved as a pair.** Approving a start image writes the card `3-1 스틸` with its prompt verbatim; the clip card's `시작 이미지` line gives that link and card title.
6. **Cut numbers are stable.** Once a cut has a link or a card, never renumber it. A new cut takes the next free number at the end of its scene.
7. **Asset change requests.** Anyone but the lead only asks: no prompt for a new asset version. List the affected cuts from the `인물·소품` column of `shot-list.md` and put request and list into handoff [5]. The lead decides; a changed fixed sentence becomes `_v2`, the old one goes to the discard list.
8. **Midjourney usage is one shared pool** (fast hours or plan limits). Before many runs in a row (a character set, a scene), say how many runs you expect. If `decisions.md` has a limit, ask before going over it.
