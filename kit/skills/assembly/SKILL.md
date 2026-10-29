---
name: assembly
description: Handle approved video with ffmpeg in Claude Code. Users say "마지막 프레임 뽑아", "다음 컷 시작 이미지로", "3초 프레임", "이어 붙여 봐", "러프컷", "컷 경계 비교"; also trimming and matching resolution. Does not generate.
---

# Rough-cut assembly · joining frames

Done with `assemble.py` (ffmpeg/ffprobe) in Claude Code's Bash. Do not use MCP. Grading and sound are out of scope.

## 1. When to use

- To extract the previous cut's last frame as a start-image candidate for the next cut
- To join approved cuts in order and check the flow (rough cut)
- To compare a cut boundary (previous cut end | next cut start) side by side

## 2. Inputs · outputs

- **Input:** the approved video job in the OK ledger (`ok-cuts.md`) and its local file. Assume the mp4 downloaded from Higgsfield sits in the repo's `media/` like `3-1.mp4`. If not, ask which job to put where (suggestion: `media/<cut number>.mp4`).
- **Output:** frames `media/frames/<cut>_last.png`, `<cut>_<sec>s.png`, `seam_<prev>_<next>.png`; rough cut `media/rough/rough_<date>.mp4`.

## 3. Recipes

Run commands from the repo root exactly as written, one line at a time (no cd or `&&`; same characters as the allow list). The script prints the ffmpeg command before running it.

| Task | Command |
|---|---|
| Last frame | `python3 .claude/skills/assembly/assemble.py lastframe media/3-1.mp4 media/frames/3-1_last.png` |
| Frame at a given time | `python3 .claude/skills/assembly/assemble.py frame media/3-1.mp4 2.5 media/frames/3-1_2.5s.png` |
| Join (rough cut) | `python3 .claude/skills/assembly/assemble.py concat media/rough/rough_1029.mp4 media/3-1.mp4 media/3-2.mp4` |
| Boundary comparison | `python3 .claude/skills/assembly/assemble.py seam media/3-1.mp4 media/3-2.mp4 media/frames/seam_3-1_3-2.png` |

- **Unifying resolution/fps:** `concat` does it. If they differ, it re-encodes to match the first video (letterbox if the aspect ratio differs) and prints what it changed. If they match, it does not re-encode.
- **Trim:** not in the script. `ffmpeg -ss 0.5 -to 4.0 -i media/3-1.mp4 -c:v libx264 -crf 18 -c:a aac media/rough/3-1_trim.mp4` (start and end in seconds). For rough-cut checking only; leave the original untouched.

## 4. Cautions

- **Never overwrite originals.** Outputs go only to `media/frames/` and `media/rough/`. The script refuses an output equal to the input and an output that already exists (use a new name).
- **Upload a frame to Higgsfield as a cut's start image only after user confirmation.** Show the extracted frame's path and the second it is from, and ask.
- **Do not generate.** If a seam looks off, only suggest which cut to fix, together with the boundary comparison image.
- **Rough-cut order is the `shot-list.md` order.** Skip cuts whose approved-video cell is empty and tell the user which were skipped.
- If ffmpeg is missing or errors, show the script's Korean error as is.
