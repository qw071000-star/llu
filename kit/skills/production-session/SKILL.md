---
name: production-session
description: Runs the lead (총괄) session and cut sessions in AI video production. Use when starting a new conversation, creating or receiving cut cards, writing or applying handoffs, editing the canon, handing over to a new conversation, or basing a cut on another OK cut ("3-1처럼 3-2", "3-1의 색감으로", "2-1 표정 유지").
---

# Lead session + cut session operation

Principle: **keep memory in documents; sessions are written to and thrown away.** A new conversation must be able to continue from the instructions, the canon, and the cut card alone.

## 1. Canon and who writes it

| Canon | Lead session (총괄) | Cut session |
|---|---|---|
| `decisions.md` confirmed decisions | Edits | Does not edit. New rules go in handoff [3] |
| `asset-registry.md` asset/folder ledger | Edits. Answers before confirmation go on that asset's `초안(제안값)` line; the fixed-sentence field is filled after confirmation | New cut folder IDs only |
| `shot-list.md` cut list / continuity table | Edits | Only the two fields on its own line (`context/tasks.md` §3). The lead edits the `생성/크레딧` field from the handoff (§4) |
| `ok-cuts.md` OK ledger | The session that approves adds the card in place | (same as left) |
| Cut card `cuts/<cut number>.md` | Issues it. Writes [1] [2] [8] [9] | Writes [3]~[7] [10]~[12]. If [1] is empty, or the user gives a direction different from [1], edit it that turn as `(제안값)` and get confirmation through handoff [5]. If there is no card, build a draft (v0) from the canon using the `cut-card.md` template |
| Logs (handoffs, trial-and-error, old prompts) | Append only | Append only |

- Edit only the relevant lines of a file. Never rewrite a canon document wholesale.
- Canon holds only what is currently valid. Move history and discarded items to the log. Do not write the same content in two documents.
- Do not touch canon that another session is editing.
- A problem outside the cut session's scope is not fixed; write it under handoff [5] "총괄에 올릴 것". A fixed description sentence that conflicts with this cut goes there too.

## 2. Lead session

**On start:** read `decisions.md`, `shot-list.md`, `asset-registry.md` in that order. Read the OK ledger only when the list is needed. Process received handoffs (§4). Do not open the handoff of a cut whose `생성/크레딧` field is already filled.

**Does:** decides sections, cut order and length, aspect ratio, crop, masked zones, era, and art-style reference. Confirms shared assets. Decides the Higgsfield folder structure. Issues cut cards (`cut-card.md`).

**Does not:** repeatedly generate a single cut. Does not change results a cut session confirmed without asking.

## 3. Cut session

**On start Claude gathers** (instructions, "when starting a conversation").
1. Read the cut card. If none, build a draft from that cut's line and the continuity table in `shot-list.md`, the relevant asset/folder in `asset-registry.md`, and the relevant lines in `decisions.md` (`cut-card.md`). Even for a new cut, do not open neighboring cut cards or handoffs (routing §3).
2. Check current state in the Higgsfield cut folder (`list_folders`, `list_project_assets`): the state in the folder name, the number of results in the `승인` and `거절` folders, results awaiting review.
3. If that cut number has a last handoff, read it and continue from [6] next steps. If that step is a user confirmation, ask that confirmation together with the proposed values for the card's empty fields, in one go.
4. If that cut has ever received OK, read its card in the OK ledger.

**Hand over to a new conversation when:** the cut is approved, or generation/review round trips on the same cut exceed 8. When handing over, leave a handoff (`handoff.md`) in the log at the canon location (§5). The next conversation picks up by itself via 1~4 above.

## 4. When the lead receives a handoff

1. Open the job IDs directly in Higgsfield to verify. Check that the approved job exists as a card in the OK ledger. If not, create it (`higgsfield-generation` §4).
2. Check for conflicts with confirmed decisions or the asset ledger. Do not accept a change that weakens a requirement the user confirmed; ask instead.
3. Apply: `shot-list.md` (status, confirmed job, and add handoff [2] to the `생성/크레딧` field as `이미지 N / 영상 N · 약 N 크레딧`), `asset-registry.md` (confirmed version, limits), `decisions.md` (new rules).
4. If neighboring cuts are affected, fix their cards too (prop state, light, last-frame composition).

## 5. Reading and editing by canon location

| Canon location | Read | Edit · leave handoff |
|---|---|---|
| Claude Doc (recommended) | Read only the needed tabs with the Docs tool. Find the OK cut tab and cut card tab by title (`3-1 영상`, `3-1`) and read only that section | Put OK cards as sections in the OK cut tab, cut cards as sections in the cut card tab. Append handoffs to the log tab |
| Claude app project knowledge | Already in context. For cut cards, use what the user pasted into that cut's conversation | Claude cannot edit. Output a "정본 갱신" block (only the changed lines per file); the user replaces the files. OK cards are delivered in the same block. Output the handoff in the final reply |
| Repo `project/` | Open only needed files. Find `ok-cuts.md` by heading and open only that section | Write handoffs to `project/log/` |
