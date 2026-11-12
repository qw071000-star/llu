# Character views

Midjourney does not reliably keep a headless three-panel layout. Make a character as **separate images**: close-up portrait first, then front full body, rear full body (and a profile if cuts need it).

## Required information

| Information | Template slot |
|---|---|
| Age, origin, skin, face structure, eyes, brows, nose, mouth, neutral expression | IDENTITY sentence |
| Outfit head to foot, colours, fabric, what is absent | WARDROBE sentence |
| Hair (length, texture, parting, colour) | HAIR clause |
| Build and height (as a look: slim, lanky; Midjourney does not keep numbers) | body clause |
| Backdrop and light | default: plain light-grey seamless backdrop, soft even daylight like an ID photo |
| Approved face image link (for the 2nd and 3rd view) | `--oref` |

## Order and templates

1. **Close-up portrait** (the reference for everything else):

```text
Close-up portrait of [IDENTITY sentence], [HAIR clause], neutral expression, plain light-grey seamless backdrop, soft even daylight like an ID photo, fine natural skin texture, 85mm --ar [aspect] --v [version] --stylize [value]
```

2. **Front full body**, then 3. **rear full body** (the user pastes the approved portrait link):

```text
Full-body photo from the front of [IDENTITY short], [WARDROBE sentence], [HAIR clause], standing straight, arms relaxed, hands empty, plain light-grey seamless backdrop, soft even daylight --oref [portrait link] --ow [value] --ar [aspect] --v [version]
```

For the rear view write `from behind, back of the hair visible`; do not ask for the face.

## Record

When confirmed, write into the registry: the IDENTITY and WARDROBE `MJ 문장` (≤ 40 words each), the three image links, the version and parameters, and the sides actually seen (a mole, a parting). Put only the WARDROBE sentence into later prompts, letter for letter.

## Editing a confirmed character

Derive only from the confirmed version; never a derivative of a derivative; never delete the confirmed version. Outfit or hair change = a new state asset (`char_<인물>_<상태>_v1`) made with the approved portrait as `--oref` and the changed clause only. Changing age: add the markers (wrinkles, skin, hair colour, posture) and keep the face structure words.

## Frequent accidents

| Symptom | Fix |
|---|---|
| Face drifts between views | lower `--stylize`, raise `--ow`, keep the portrait link; one change |
| A mark appears on the other side | write the side seen into the registry; do not fight it |
| Outfit changes | repeat the WARDROBE sentence letter for letter; shorten the rest |
| Extra people or props | `--no people, props` |
| Plastic skin | add `fine natural skin texture, matte` and lower `--stylize` |
