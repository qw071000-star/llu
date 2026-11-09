---
name: edit-planning
description: Plans the cut sequence of a scene or whole film: whether each cut earns its place, cut lengths against a target runtime, seam checks between separately generated clips, and why each cut is where it is. Use for "편집 계획", "컷 몇 개로", "리듬", "페이싱", "이 컷 빼도 돼?", "이음새 점검". Proposals only; does not generate or assemble files.
---

# Edit planning

Sits after `shot-design` (scene geometry and coverage) and again after clips exist. `shot-design` decides where the camera goes; this skill decides which cuts stay, how long each lives and how neighbours join. File work (last frames, rough cut) is `assembly` (Claude Code). Cut cards are `production-session`'s job and prompts are `video-prompt`'s.

## 1. Required information (one batch with proposals, instructions rule 4)

| Information | From |
|---|---|
| Scope (one scene or the whole film) and target runtime | user; `decisions.md` §1 |
| Tempo: contemplative (long holds) / conventional / tightening | user; propose from the work's tone |
| The anchor moment: the one beat that may hold longest | user; propose from the script |
| Cuts already approved (job, length) and each cut's dialogue line | `shot-list.md`, OK ledger |

## 2. The cut test (every cut)

A cut stays only if it does at least one of three jobs: **changes emotion**, **advances action**, **raises pressure**. Write the job in one phrase per cut. "A beautiful establishing shot" is not a job. If no job is clear, ask the user what the cut is for; never invent story. A cut with no job: propose deleting or merging it. An approved cut is never removed by Claude: ask first.

## 3. Length distribution (not all equal)

Starting values from one community source (2026-11 research), not verified here. A single test of the user's own footage beats this table.

1. `N = runtime / average cut length`, whole number. Average by tempo: contemplative 8–15 s, conventional 5–12 s, tightening 3–6 s. The cut length in `decisions.md` is the default.
2. One **anchor** cut at 1.5–3× the average (at most 15 s per cut, `shot-design`), one **shortest** cut at about half the average and not below the model's minimum duration.
3. The rest: more short cuts than long ones, so the median sits below the average. Reconcile to the runtime ±1 s by trimming cuts near the average, never the anchor. A dialogue line needs 2–4 seconds.

## 4. Generated length versus cut length

A cut is shorter than the clip that made it. With a start image the head of a clip is fixed (`video-prompt` §2 "Chaining"), so budget a **tail handle** only: start at 1.5 s, 2.5 s for performance or dialogue, then confirm with one test. If cut + handle exceeds the model's maximum clip length, the clip length is the limit: read it from `decisions.md` or ask `models_explore`, never guess, and shorten the cut or split it. Many short cuts each pay a handle: before proposing a fast tempo, quote the credits (instructions rule 10) and show the generated seconds next to the finished seconds.

## 5. Seam check (each neighbouring pair)

A hard cut between two separately generated clips holds when A's last frame and B's first frame **match five things and break one on purpose**:

1. subject position on screen (within about 15% of the frame width)
2. direction of travel
3. light direction and level (key from the same side)
4. state: costume, prop position, what is in which hand
5. eyeline side
6. **break shot size** by two sizes on the same axis, or one size plus an angle change of at least 30°

Fill items 1–5 per seam from the continuity table and cut cards [5] [6] as `✔` `✘` or `?`. Claude cannot see the frames, so a judgement from text is marked "추정"; the real frames come from `assembly` (Claude Code) or the user's eyes. For a failed seam choose the cheapest: **fix in the edit** (colour, retime) → **cover it** (an insert or cutaway, an empty frame, a short dissolve of a few frames) → **regenerate** B from A's last frame. Show the credits before proposing a regeneration.

## 6. Why each cut is there

Name one reason per seam: **on action** (about a third into the movement in A; B resumes a little later), **on look** (after the eyeline settles), **on sound**, **on idea**, **on emptiness** (the shot has nothing left to give), **on impact**. If no name fits, the cut is arbitrary: reconsider it.

## 7. Output

```text
편집 계획 — [장면/전체] · 목표 [분:초] · 템포 [관조/보통/긴장]

| 컷 | 길이 | 이 컷의 일 | 자르는 동기 | 이음새 위치·방향·빛·상태·시선 | 생성 길이(꼬리 포함) |
|---|---|---|---|---|---|
| 3-1 | 8초 | [감정/행동/압력 + 한 구절] | [동기] | ✔ ✔ ✔ ✘ ? | 9.5초 |

앵커: [컷] · 가장 짧은 컷: [컷] · 합계 [ ]초 (목표와 차이 [ ]초) · 생성 합계 [ ]초
빼거나 합칠 컷: [컷 — 이유] (승인 컷은 묻고 결정)
고칠 이음새: [A → B — 편집 / 가리기 / 재생성, 예상 크레딧]
```

## 8. Rules

- **Proposals only** until the user says "확정" or "그대로". Then give the `shot-list.md` lines to change (length and time columns, new cuts as `대기`) and let `production-session` §1 say who edits.
- The numbers above are starting values. When the user's test shows a better value, put it in handoff [3] so the lead writes it into `decisions.md` §7.
- Do not write cut cards or prompts. Each cut's content goes to `production-session` and `video-prompt`.
