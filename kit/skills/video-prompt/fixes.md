# Fixes by symptom - find and use only the matching row

**Information needed:** the job of the wrong result, that job's prompt (OK ledger card or `get_project_asset_prompt`), the symptom as the user stated it (verbatim).
- If the symptom is vague ("이상해", it looks off), ask which interval and which character. Show two or three candidates from the table and let them choose.
- Speed, added motion, stars, speed of a person's action ("너무 빠르다", too fast), walk age, and several actions use the matching row of the `SKILL.md` §0 "vague phrases" table. The table below covers all other symptoms.
- Show the line to change as "전 → 후" and get confirmation (instructions rule 3). For an approved cut, first ask whether to replace it with a new take (the same take cannot be reproduced).

| Symptom | Fix |
|---|---|
| Starts with an empty frame and the character walks in | Character in place from the first frame, mid-action. Write the entrance as "already walking" |
| An environment event such as a door opening looks awkward | Remove that event and keep one state for the whole shot |
| Head/upper body whips around | Body-part order and seconds: `head → shoulders → feet over three seconds; turning within one second = failed take`. If only the head turns, write only the order `eyes → head` |
| A character who should not speak moves their mouth | Remove the attempt to speak itself: `[Person] does not say a single word: no attempt to speak, no parted lips, no mouthing.` If the prompt already has a weak sentence such as `no lip movement`, replace it with this sentence instead of adding. Express hesitation with breath, swallowing, hands |
| Head turns and then turns back | `From then until the end [his] eyes and head stay on [her]. Turning back = forbidden` |
| Another character reacts | Lock that character's gaze, head, hands: `does not react in any way, never looks at [him]` |
| A prop switches hands, grows, or goes elsewhere | Attach the prop element and state the hand (screen side + object), not put down, size = start image. If two objects of the same kind exist, distinguish them by name |
| The reference photo's face, colour, or lighting bleeds in | Remove that photo; replace it as in `image-prompt` §2 (storyboard/monitor photos) |
| Something wrong is reflected in a mirror/glass | State what is reflected and what is not reflected together |
| The sun appears as a flat disc | Write it as light that bleeds without an outline. No disc or rim; the lower part dissolves in horizon haze |
| Small repeating objects (flock of birds) smear | "Keep the same size and position, moving at the same speed as the camera". If that still fails, make it separately as overlay material |
| The camera goes straight to the centre instead of the designated point | Change to "tracking shot following the subject". Write the zoom amount as half of what is wanted |
| Acting is too big or expressionless | Close both ends of the emotional range with `failed take` |
| Background characters freeze or all move at once | Headcount + one different task each. Unnamed people are faceless silhouettes |

**관찰 (community sources, 2026-11; not yet seen in our own generations: promote to a rule after two cases of our own).** Same use as above: change only the matching line, show "전 → 후".

| Symptom | Fix |
|---|---|
| (관찰) Comes out as slow motion you did not ask for | Give the pace a number or a physical referent and make the action fit the clip, not the clip the action: `He walks at a steady pace, one footfall roughly every 0.55 seconds. Constant speed, no slow motion, no speed ramp.` Retiming in the edit (about 115%) before a cut often beats regenerating |
| (관찰) Looks like a slideshow: a photo with a zoom, nothing happens | The prompt describes a picture, not an event. Write at least two motion layers (body, cloth or hair, environment) and one weight shift: `His coat hem lifts and drops in gusts. He shifts his weight onto the screen-left foot and lowers his chin.` If the start image is a rigid symmetrical pose, rebuild it mid-gesture (`image-prompt` → `first-frame.md`) |
| (관찰) The mouth does not match the line | One speaker, one line of about six words or fewer, mouth clearly visible, clip 4 seconds or less. For a longer line, turn the speaker three-quarters away or show the listener, and place the line in the edit as voice-over. Treat generated room sound as a scratch track |
| (관찰) Head cut off, subject too small, wrong crop | State the frame as geography: `eyes on the upper third line, about 10% headroom, subject on the screen-left third, hands inside the frame.` Make the start image at the delivery aspect and size; never crop a 16:9 image into 9:16 |
| (관찰) A visible jump where an extended clip joins | Do not repeat the original prompt in the extension. Write a continuation that names the state in progress (`she is mid-step, right foot forward, weight still transferring; complete that step and take one more; do not reset her pose`). Or stop extending: two designed shots on a cut beat one extended shot with a seam. Hide a seam with a 0.5 s cutaway or a short dissolve |
| (관찰) A prop vanishes or changes after being covered, small, or leaving the frame | State it for the whole clip: `the cream paper envelope, one corner creased, stays flat in the lower right of frame for the entire shot, never covered, never leaving frame.` Name it with the same two or three nouns every time (colour, material, one edge condition). Keep a handled prop to 4 seconds or less. Put the occlusion on a cut: clip A ends with the hand over it, clip B opens uncovered |
