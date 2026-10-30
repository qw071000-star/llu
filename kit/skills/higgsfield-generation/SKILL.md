---
name: higgsfield-generation
description: Use when generating images or video with Higgsfield or organizing the results. Covers pre-generation checks, the save project/folder, ending the turn after sending, checking results, approve (OK)/reject/hold marking and the OK ledger entry, resolution stages, and credit logging and questions. Users say "좋아", "이걸로", "거절", "다시 만들어", "됐어", "크레딧 얼마나 썼어".
---

# Higgsfield generation operations

## 1. Pre-generation checks (send only if all are yes)

1. Did the user instruct this generation?
2. Is the `folder_id` to save to decided (§2)?
3. Is the resolution a check-quality one? Send Seedance 2.5 video with `draft: true` (480p; costs the same as a non-draft 480p). The 1080p final of the same take is `video-prompt` → `rerender.md`.
4. Credits basis: if the `decisions.md` §2 cost memo has this model, resolution and length, use it; otherwise get a quote with `get_cost: true` before sending (write the call). **Never cite a quote you did not get in this conversation.**
5. Did it pass `check_prompt.py` in this skill's folder (command and procedure: see instructions "Check")? The command must match the allow pattern in `.claude/settings.json` character for character to run without approval; in the Claude app only the path changes to that skill folder.

## 2. Save location

**Lookup order:** `asset-registry.md` folder table (the row the cut card `[2]` points to) → ask the user.

**Pass `folder_id` on every generation.**
- Without it, the result is saved outside the project and cannot be tracked.
- Do not rely on the project auto-create setting (`get_preferences`).

**When there is no folder:** show the structure below adapted to the work and ask who will create it (the question sentence is in must-ask "All tasks").

```
「작품명」 (Higgsfield 프로젝트)
├─ 00 에셋 / 인물 · 장소 · 소품 · 그림체     ← 확정된 공통 에셋
├─ 1-1 [진행]                               ← 새 결과물 = 검토 대기
│   ├─ 승인
│   └─ 거절
├─ 1-2 [대기]
└─ 99 시험·보관                              ← 시험 생성, 교체된 옛 승인본
```

- A cut folder name starts with the cut number (scene-cut), and the trailing status matches the cut list. Create it with the cut list status as is (`3-6 [대기]`), and change it to `[진행]` when sending the first generation. If there are many scenes, add one more level, like `장면 3 / 3-1 [진행] / 승인·거절`.
- **When Claude creates them:** use `create_folder` to create the cut folder and the `승인` and `거절` inside it.
  - On a timeout, check with `list_folders` whether it was created before creating again.
- **When the user creates them:** give the exact names, and when done, find the ID with `search_folders`.
- **Recording:** write the new folder ID in the folder table (Claude Code) or the "정본 갱신" block (Claude app).

## 3. Send the request and end the turn

Polling status repeatedly reprocesses the whole conversation each time. Leave the waiting to the user.

**Sending**
- To make one, use `generate_image` or `generate_video` with `count: 1`. The widget shows progress.
- Send several with `generate_*_batch` only when the user instructed them at once, and keep the list of job IDs.

**After sending, write in this format and stop.** If an earlier answer had an error, first write one line `정정: …` above the format.

```
보냈습니다.
- [컷] [무엇] · [모델] · [해상도·길이] · job `[전체 job ID]` · 약 [N] 크레딧
- 저장: 「작품」/[폴더]
- 바꾼 것: [전 → 후] (다시 만들 때만)
- 볼 점: [지시 항목 2~3개]
완성되면 알려 주세요. 분석이나 개선점, 다른 컷과의 비교가 필요하면 말씀해 주세요.
```

**Credit logging:** every time you send (no new quote → use the earlier recorded value for the same setting and name that basis), write `job — 보냄 — 약 N 크레딧` in cut card [11] and raise the counts in the cut list 생성/크레딧 cell (`이미지 n / 영상 n · 약 N 크레딧`). If the `decisions.md` §2 cost memo has that setting, use its value; otherwise use the `get_cost` quote. If neither exists, write `알 수 없음` instead of a number (instructions rule 10). Also attach the basis (cost memo / get_cost) to the credits in the after-sending format.

**Do not**
- Do not repeat `jobs_wait` or status polling.
- Do not resend the same request, even after a send timeout (double billing).
- Do not add other generations while waiting.

**When the user says "됐어" (it's done)**
1. Query only that job, once.
   - For a single job, use `job_display` or `jobs_wait` (`timeout_seconds: 0`).
   - For a batch, call `jobs_wait` (0) once, then `show_generation_by_ids` once.
2. If it is not done yet, write "아직 진행 중입니다. 완성되면 알려 주세요." and stop.
3. If it is done, change the cut folder and cut list status to `검토`, mark ✔/✘ per instructed item (3-5 lines), and ask "승인할까요, 거절할까요?". For items only visible on screen, write "봐 주세요".
4. Numeric measurement, cause analysis and comparison with other cuts only when the user wants them (`qa-metrics.md`).

**When the user says "기다렸다가 봐 줘" (wait and look):** for images, use `jobs_wait` (15 seconds) up to 4 times. Do not wait for video.

## 4. Status marking

| User says | Status | Do |
|---|---|---|
| "좋아", "이걸로", "픽스", "확정", "OK" | 승인 | Move to the `승인` folder and write the OK record right away (below) |
| "별로", "아니야", "버려", "거절" | 거절 | Move to the `거절` folder; state a one-line reason + cause + fix. Do not regenerate |
| A remark like "이상해", "왜 이래" | No change | State cause and fix, and ask whether to reject. For video, take the fix from that symptom's line in `video-prompt` → `fixes.md` |
| "다시 만들어" | Previous one rejected | For video, show the one thing to change as "전 → 후" from that symptom's line in `video-prompt` → `fixes.md`, and generate after confirmation. If the immediately preceding answer already showed 전 → 후 and asked "이걸로 다시 만들까요?", then "다시 만들어" is that confirmation. For "그대로 다시" (again as is), send without changing anything |
| "나중에", "일단 둬" | 보류 | Leave in the cut folder and note it in cut card [11]. Also set the cut folder name and cut list status to `보류` |
| A new approved version appears | Superseded | Move the old approved version to `99 시험·보관`, and move the old OK card to the log |

- **How to move:** find that job's `placement_id` with `list_project_assets` (cut folder), and move with `move_project_asset`.
- **Cut status:**
  - Stages are `대기` → `진행` → `검토` → `승인`, and can become `보류` midway.
  - `진행`: generation sent or work underway. `검토`: a finished result awaiting a verdict. If rejected, revert to `진행` on the spot.
  - Change the end of the cut folder name (`3-1 [승인]`) with `rename_folder`, and write the same in `shot-list.md`.
  - The canon is `shot-list.md`.
- **Reject log:** leave the reject reason in cut card [11] as `job — 거절 — 이유`. The next attempt's risk list comes from here.

**OK record (at the moment of approval, never deferred to the next conversation)**
1. Write a list line and a card in the OK ledger (`ok-cuts.md`). The format is in that file.
2. Copy the prompt exactly as sent, character for character. Lookup order:
   1. What was sent in this conversation
   2. `get_project_asset_prompt` (that job)
   3. Ask the user to paste it (it is in the result detail on the Higgsfield web)
   - Never rewrite it from memory. For results made by another account, option 2 returns empty, so the card is the only copy teammates can see.
3. For a job sent with `draft: true`, write `draft 예 · 만료일` in the list's "모델 · 설정" and the card's draft line (otherwise `draft 아니오`). The 1080p finalization picks its `rerender.md` route from this marking.
4. Fix the cut list's `확정 job` cell. For an asset, also fix the asset registry's `확정 job` and fixed description text (the session that edits: `production-session` §1).

## 5. Post-production

**Do not leave to the model; hand off to post:**
- Exact travel distance
- Exact entrance/exit timing
- Fine jitter of small, dark elements
- Star twinkle
- Paths of small repeated objects (bird flocks, etc.)
- Dissolves, color matching

## 6. Resolution and credits

**Resolution**
- Follow the single high-resolution method in `video-prompt` → `rerender.md`.
- Upscaling erases watercolor/film texture. Ask before using it.

**Credits**
- **If asked "크레딧 얼마나 썼어"**, answer from the cut list 생성/크레딧 cell. Handoff [2] opens only cuts whose cell is empty. Answer only recorded cells and `알 수 없음` (cuts with no record). Unit-price estimates only when the user wants them, after actually calling `get_cost`, labeled `추정`. If the cost memo is empty, say there is no unit price, and do not fill it in without a `get_cost` quote.
- If video for the same cut exceeds 10 generations in one day, stop and re-decide the approach with the user.
