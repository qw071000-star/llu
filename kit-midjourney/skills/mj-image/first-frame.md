# Still frame / start frame

A still for a cut, or the first image of a short clip (`mj-video`). It is the 0:00 state of the clip, not a thumbnail moment.

## Required information

| Information | Template slot |
|---|---|
| The cut's place view link and its LIGHT LOCK clause | place clause |
| For each character: the approved portrait link and the WARDROBE sentence | `--oref`, wardrobe clause |
| Prop: position, state, who holds it, size | prop clause |
| Camera: position by objects on screen, height, distance, shot size | camera clause |
| Each person's position, action, gaze, hands (screen side + object) | blocking clause |
| Number of visible people | `exactly one person` etc. |

## Two steps when character and place are both needed

Midjourney does not reliably combine a character reference and a place reference in one run. Propose **two steps** (one change each): 1) the place with the camera of this cut (master link as image prompt), 2) the character placed in it (the place image as image prompt, the portrait as `--oref`). Judge the result; when the combination fails twice, rule 7: composite by hand or use Midjourney's editor for the person only.

```text
[Shot size] of [person by IDENTITY short] [position by objects], [action], [gaze], [WARDROBE sentence], in [place clause with LIGHT LOCK], [camera], photorealistic --oref [portrait link] --ar [aspect] --v [version]
```

The WARDROBE sentence appears once per visible person, letter for letter.
