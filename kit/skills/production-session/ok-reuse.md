# Using another OK as the basis — "3-1처럼 3-2"

## 1. Find it

1. Find that number in the OK ledger list.
   - If there are several kinds (start image and video), choose with "Which OK" in the table below. If still ambiguous, ask with a proposal.
2. Open only that card's prompt. An OK card is a section inside `ok-cuts.md`.
   - Open the card first even **before proposing** to bring in an OK (do not propose from the list's `OK 이유` alone).
3. If there is no card, first create it from the confirmed job in the cut list. The order for finding the prompt is the same as the OK record in `higgsfield-generation` §4. Do not guess and rewrite the prompt by looking at the result.
4. Do not use superseded old OKs. If the user points to an old one, confirm which one they mean.

## 2. What to bring

| User says | Which OK | Where to take from the video prompt | Where to take from the image prompt |
|---|---|---|---|
| motion, action, movement, path, speed (모션, 동작, 움직임, 동선, 속도) | video | `ACTION_TIMING`, `PHYSICS`, speed sentences | — (for images, only the mid-action pose) |
| camera, angle, composition, lens (카메라, 앵글, 구도, 렌즈) | video or start image | `CAMERA`, `OPTICS`, the camera line of `LOCATION_MAP` | CAMERA, FRAMING lines |
| colour, texture, tone, look, grain (색감, 질감, 톤, 룩, 그레인) | start image or video | `STYLE`, `QUALITY`, the colour sentences of `LIGHTING` | palette, material/finish, grade lines |
| light (빛) | OK of the same location | `LIGHTING` | LIGHT LOCK line |
| expression, acting, emotion (표정, 연기, 감정) | video (acting) or image (expression) | that person's line in `CHARACTER_ACTING`, the acting-range sentence | that person's expression/gaze phrase |
| voice, speech style (목소리, 말투) | video | that person's voice sentence in `AUDIO` | — |
| prop state (소품 상태) | OK of the previous cut | the prop line in `PHYSICS` | PROP line |
| number only ("3-1처럼") | — | Ask what to bring. Propose: motion. Camera too only if the two cuts share the same location view and direction | Ask. Propose: colour. Composition too only for the same view |

- **"3-1 카드처럼 써" is about format.** Write with the `cut-card.md` template; do not bring in the OK.

**When attaching an OK image as a reference** — narrow its authority to that element and list the rest under `DO NOT TRANSFER`. For the tag `<<<OK>>>`, use the OK card's element name as is.

| What is brought | Authority sentence |
|---|---|
| colour/texture | `<<<OK>>> controls only colour, grade, contrast and texture. Never take its subjects, composition, people or light direction.` |
| expression | `<<<OK>>> controls only [PERSON]'s facial expression and gaze. Identity, hair and wardrobe come from <<<CHAR>>>.` |

- **If first-frame template 1 (LOCKED) applies,** colour comes from that location view. Follow "다른 OK의 색감을 가져올 때" in `image-prompt` → `first-frame.md`.
- **If the OK prompt has no colour/texture sentence,** that colour came from a reference image. Do not invent a sentence; attach that OK image as a colour reference.
- **Composition does not follow through a reference.** Bring the camera/composition sentences (coordinates), or use the same location view as LOCKED.
- **Motion is not carried by image references.** Bring the sentences. Attach that OK video and narrow it to `motion only` only when the tool accepts video references.

## 3. How to carry it over

1. **In a brought line, change only** the names, objects, and time ranges that differ in this cut. If something must be added, do not split that line or insert into the middle; write it as a new sentence after the period (do not join with `;` or `,`). Exception: if the brought line's mouth lock is weaker than `[Person] does not say a single word: no attempt to speak, no parted lips, no mouthing.`, raise it to this sentence. Leave remaining sentences as they are. Put the whole brought line in the `--must-include` file.
2. **Show changed words as "before → after".**
3. **Fill the other fields as usual with the information checklist.** A brought element does not substitute for other fields.
4. **Bring the risks tied to the brought element too.** Carry over the OK card's "위험 → 막는 문장" together with the Required/Forbidden lines of the OK prompt that concern the brought action or person. The same action produces the same failure. If the card has no "위험" line, carry over only the prompt's Required/Forbidden.
5. **If it conflicts with this cut** (must-ask), ask with a proposal: length → the stretched or shortened range; number of people, location, props → the name/object to change. If the camera direction is opposite, swap the screen sides in the brought line (hand, turning side, light) to fit this view (`image-prompt` → `location.md` "Writing directions").
6. **Do not write cut numbers in the prompt body** ("as in shot 3-1" means nothing to the model). Write the content directly.
7. **If an OK image is attached, match the reference count to the tag count.**

## 4. Recording

- **Cut card [7]:** `가져온 OK: 3-1 영상 — 모션(ACTION_TIMING, PHYSICS)`
- **Standards spanning several cuts:** "색감은 앞으로 전부 3-1처럼" (from now on, all colour like 3-1) is written in `decisions.md` §3 as a standard.
