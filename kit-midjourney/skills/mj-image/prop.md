# Props

## Required information

| Information | Template slot |
|---|---|
| Object, material, shape, wear | description sentence (material, shape, size, signs of use only) |
| Size in cm and against a body part | size clause |
| Materials that must not appear | `--no` |
| State changes in the story, who holds it in which hand (screen side + object) | registry `상태 머신`, not the sentence |

## Rules

- A prop whose state, hand or size changes is its own asset (`_v1`, `_v2`). The sentence holds material, shape, size and signs of use only: no open/closed, no hand.
- Size is set in the scene: a studio prop image throws the size off. State the size in the clause (`about 40 cm wide, the width of an adult's lap`) and check it again in the still frame.
- If no image is needed (a distant light), propose writing it as a clause in the cut prompt.

```text
[Object, material, shape, wear], about [N] cm [against a body part], on a plain neutral surface, soft even daylight, sharp focus --no logos, text --ar 1:1 --v [version]
```

Record the link and the sentence; later cuts copy the sentence and attach the link as a reference only when the prop must look identical.
