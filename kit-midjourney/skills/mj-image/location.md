# Locations

## Required information

| Information | Template slot |
|---|---|
| Place identity, era, use | first clause |
| 2–4 landmarks and where they stand by screen side | landmark clause |
| Materials, wear, colour palette | material clause |
| Time of day, the light's screen side and the object on that side (LIGHT LOCK, one clause per view) | light clause |
| Camera: position, height, direction, shot size | camera clause |
| Empty or with people (default: empty) | `--no people` |

## Master view (new)

```text
[Place, era], [landmarks by screen side], [materials and wear], [palette], [time of day], [LIGHT LOCK clause], wide establishing view from [position, height], no people --no people, text --ar [aspect] --v [version]
```

Record: the `MJ 문장` for the place, the master link, and this view's LIGHT LOCK clause (`the low sun from screen left, the tree side`).

## New view

- **Same side, closer or wider:** use the master link as an image prompt (placed first) and change only the camera clause.
- **Opposite side:** screen left and right flip; landmarks and the light side swap. Write a new LIGHT LOCK clause for that view and say in the prompt `a new view of the same place seen from the opposite end`. The result is a new image, not a mirror: check the landmarks on both sides in the result.
- One view = one registry line (`LC-001-V2`). A view that needs the master but is missing → make the master first.

## Editing

Time of day, lights on/off, or removing an object = one change per run, written as "전 → 후" in the prompt words; keep the rest of the place sentence verbatim. A change that moves the camera is a new view, not an edit.

## Accidents

| Symptom | Fix |
|---|---|
| Place changes between views | keep the `MJ 문장` letter for letter; use the master link as image prompt |
| Light side flips | rewrite the light clause for that view; judge by the object named, not left/right |
| Invented signs or text | `--no text, signs` |
