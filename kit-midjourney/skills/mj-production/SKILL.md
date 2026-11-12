---
name: mj-production
description: Runs the lead (총괄) session and cut sessions for a Midjourney production. Use when starting a new conversation, issuing cut cards, writing handoffs, recording an approved result in the OK ledger, editing the canon, or basing a cut on another OK ("3-1처럼 3-2", "2-1 표정 유지"), and "됐어", "OK", "거절", "보류", "핸드오프".
---

# Lead session + cut session operation

Principle: **keep memory in documents; sessions are written to and thrown away.** A new conversation must be able to continue from the instructions, the canon and the cut card alone.

## 1. Canon and who writes it

| Canon | Lead session (총괄) | Cut session |
|---|---|---|
| `decisions.md` confirmed decisions | Edits | Does not edit. New rules go in handoff [3] |
| `asset-registry.md` asset ledger | Edits. Answers before confirmation go on that asset's `초안(제안값)` line | Nothing |
| `shot-list.md` cut list | Edits | Only its own row: `담당`, status, confirmed links |
| `ok-cuts.md` OK ledger | The session that approves adds the card in place | (same as left) |
| Cut card `cuts/<cut number>.md` | Issues it. Writes [1] [2] [3] [8] [9] | Writes [4]~[7] [10]~[12]. No card: build a draft (v0) from the canon using the `cut-card.md` template |
| Logs (handoffs, old prompts) | Append only | Append only |

- Edit only the relevant lines of a file. Never rewrite a canon document wholesale.
- Canon holds only what is currently valid; history and discarded items go to the log, never the same content in two documents.
- Do not touch canon another session is editing.
- `decisions.md` §7 `운영 방식: 공용 계정` → also `shared-account.md`.

## 2. Lead session

**On start:** read `decisions.md`, `shot-list.md`, `asset-registry.md` in that order; read the OK ledger only when needed; process received handoffs (§3). **Does:** decides sections, cut order, aspect, style reference, era; confirms shared assets; issues cut cards (`cut-card.md`). **Does not:** rerun one cut again and again, or change an approved result without asking.

## 3. Cut session and handoff

**On start:** read the cut card (none → draft), its row and the neighbours' rows, and its last handoff; continue from [6] next steps. If the cut was approved before, read its card in the OK ledger.

**Hand over to a new conversation when:** the cut is approved, or runs and judgements on the same cut exceed 8. Leave a handoff (`handoff.md`) in the log. **Lead receiving a handoff:** open the links to verify, check that the approved result has an OK card (if not, create it), check conflicts with confirmed decisions, then apply: `shot-list.md` (status, confirmed link), `asset-registry.md` (confirmed version, limits), `decisions.md` (new rules).

## 4. OK record (at the moment of approval, never deferred)

User says "좋아", "OK", "픽스", "확정" → approved. "별로", "거절" → rejected: one-line reason + cause + fix; do not make a new prompt without asking. "나중에" → held: note it in cut card [11].

1. Write a list line and a card in the OK ledger (`ok-cuts.md`). With `운영 방식: 공용 계정`, the `승인` line ends with the approver's name.
2. Copy the prompt exactly as the user ran it, parameter line included. If the user changed it, ask for the final text; never rewrite it from memory.
3. Fix the cut list's confirmed-link cell. For an asset, also the registry's confirmed link and fixed sentence (the session that edits: §1).
4. Start image and clip are a pair, each with its own card, each pointing to the other.
5. An approved card is never edited: a correction is one `정정(날짜 · 이름)` line under it, a replacement a new take.

## 5. Using another OK ("3-1처럼 3-2")

Open that one card first (never propose from the list's `OK 이유` alone). Ask what to take (look, expression, composition, light) if unsaid. Bring in only that part of the prompt and its parameters; keep the new cut's own fixed sentences. If sizes, people or places differ, say so first. Never use superseded OKs.

## 6. Reading and editing by canon location

| Canon location | Read | Edit · leave handoff |
|---|---|---|
| Claude Doc (recommended) | Only the needed tabs. Cut card: search its first line `받는 세션: 3-1`; OK card: title `3-1 스틸` | A cell: find its words as read (a teammate's edit then refuses, not overwritten). OK card + row, handoff: append |
| Project knowledge | Already in context; cut cards come pasted by the user | Claude cannot edit: output a "정본 갱신" block (changed lines only); the user replaces the files |
