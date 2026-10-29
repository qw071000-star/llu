---
name: color-continuity
description: Measure color/brightness across approved cuts with ffmpeg and match them to a reference cut (Claude Code). Users say "색이 컷마다 달라", "3-2가 더 노래", "3-1이랑 색 맞춰", "밝기 맞춰", "톤 통일", "LUT". Does not grade or generate.
---

# Color matching between cuts

Done with `color.py` (ffmpeg/ffprobe) in Claude Code's Bash. Do not use MCP. Creative grading (making a new look) is out of scope.

## 1. When to use

- When color temperature, brightness or contrast jump between approved cuts (video or image)
- When matching cut tone before viewing the rough cut (`assembly`)

## 2. Reference cut

- The reference is one OK cut, chosen by the user (suggestion: read the `OK 이유` column of the `ok-cuts.md` list and propose the cut whose reason is "색감").
- Record the chosen reference on the `기준 색 컷` line of `decisions.md` §3 (canon edits: `production-session` §1). If it exists, do not ask.
- Cuts to match: every cut with a filled `확정 영상` field in `shot-list.md`, teammates' cuts included. If the user's range has fewer than 2, ask whether to add cuts outside it or wait.
- Files are `media/<cut number>.mp4` (`.png` for images). If missing, ask which job to put where.

## 3. Recipes

Run commands from the repo root exactly as written, one line at a time (one script per call: no `cd`, `&&`, `;` or pipes; same characters as the allow list). The script prints the ffmpeg command before running it.

| Task | Command |
|---|---|
| Measure | `python3 .claude/skills/color-continuity/color.py measure media/3-1.mp4 media/3-2.mp4` |
| Match | `python3 .claude/skills/color-continuity/color.py match media/3-1.mp4 media/3-2.mp4 media/color/3-2_match.mp4` |
| Comparison image | `python3 .claude/skills/color-continuity/color.py compare media/3-1.mp4 media/3-2.mp4 media/color/3-2_match.mp4 media/color/3-2_compare.png` |

- **What is measured:** the mean over about 5 evenly spaced frames. Y = brightness, U·V = color tilt (low U leans yellow, high V leans red), R·G·B, Y standard deviation = contrast. The difference from the first file (the reference) is output too.
- **How it matches:** `colorchannelmixer` (R·G·B gain) brings color, and `eq` (contrast/brightness) brings exposure, closer to the reference. Values are clamped to a safe range, and it reports when it clamps. After matching, run `measure` again and show with numbers that the difference shrank.
- **Comparison image:** middle frame, reference | original | matched.

## 4. Record · approval

- Show the matched file, comparison image, filter string used, and before/after numbers, and ask whether to use it. **Before approval, only propose.**
- On approval, leave the filter string as one line on that cut's card or in the `decisions.md` §3 look memo (under the `기준 색 컷` line) (`3-2: colorchannelmixer=… , eq=… (기준 3-1)`).
- Do not make LUT files. The filter string is that cut's first-pass matching record.

## 5. When to regenerate

If the difference is large (the script prints "차이가 크다" or "안전 범위로 잘랐다", or the time of day or light direction looks different), propose regenerating that cut instead of post correction. The places to fix are the LIGHT LOCK and PALETTE lines of `video-prompt` and `image-prompt`.

## 6. Do not

- Generate, upload to Higgsfield, or make a creative look
- **Never overwrite originals.** Outputs go only as new files in `media/color/`. The script refuses an output equal to the input and an output that already exists.
- If ffmpeg is missing or errors, show the script's Korean error as is.
