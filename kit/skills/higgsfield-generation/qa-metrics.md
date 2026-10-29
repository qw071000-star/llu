# Numeric QA — only when the user wants analysis

Use numbers to find causes. Even if the numbers pass, if the user says "비어 보인다" (looks empty), that statement is the verdict.

| Metric | How to measure | Reference value |
|---|---|---|
| Overall/zone brightness | 0-1 mean | Set a target range per cut for the work. Color/brightness comparison and matching between approved cuts: `color-continuity` |
| Element position | Screen % (from top, width) | Whether it is inside the crop band / occlusion zone |
| Edge ratio | Ratio of edge pixels | Watercolor 2-8%. 13% or more means over-dense texture |
| Structure match | SSIM against the reference image | 0.9 or more for a "keep as is" edit |
| Highlights | Ratio of near-white pixels | Watercolor 0.1% or less |
| Camera motion | Cumulative zoom/shift via optical flow | Compare with the requested amount |
| Speed uniformity | Change per second | Must be constant |
| Texture jitter | Difference between consecutive frames | Elements must not suddenly appear or vanish |

**What to check when comparing with other cuts**
- Do viewpoint and composition overlap?
- Does light direction or brightness jump?
- Does prop state carry over?
- Does the last frame connect to the next cut's first frame?
