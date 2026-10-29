# Fixes by symptom - find and use only the matching row

**Information needed:** the job of the wrong result, that job's prompt (OK ledger card or `get_project_asset_prompt`), the symptom as the user stated it (verbatim).
- If the symptom is vague ("이상해", it looks off), ask which interval and which character. Show two or three candidates from the table and let them choose.
- Speed, added motion, stars, speed of a person's action ("너무 빠르다", too fast), walk age, and several actions use the matching row of the `SKILL.md` §0 "vague phrases" table. The table below covers all other symptoms.
- Show the line to change as "전 → 후" and get confirmation (instruction 3). For an approved cut, first ask whether to replace it with a new take (the same take cannot be reproduced).

| Symptom | Fix |
|---|---|
| Starts with an empty frame and the character walks in | Character in place from the first frame, mid-action. Write the entrance as "already walking" |
| An environment event such as a door opening looks awkward | Remove that event and keep one state for the whole shot |
| Head/upper body whips around | Body-part order and seconds: `head → shoulders → feet over three seconds; turning within one second = failed take`. If only the head turns, write only the order `eyes → head` |
| A character who should not speak moves their mouth | Remove the attempt to speak itself: `[Person] does not say a single word: no attempt to speak, no parted lips, no mouthing.` If the prompt already has a weak sentence such as `no lip movement`, replace it with this sentence instead of adding. Express hesitation with breath, swallowing, hands |
| Head turns and then turns back | `From then until the end [his] eyes and head stay on [her]. Turning back = forbidden` |
| Another character reacts | Lock that character's gaze, head, hands: `does not react in any way, never looks at [him]` |
| A prop switches hands, grows, or goes elsewhere | Attach the prop element and state the hand (screen side + object), not put down, size = start image. If two objects of the same kind exist, distinguish them by name |
| The reference photo's face, colour, or lighting bleeds in | Remove that photo, and use an empty location image made in that composition as the location reference |
| Something wrong is reflected in a mirror/glass | State what is reflected and what is not reflected together |
| The sun appears as a flat disc | Write it as light that bleeds without an outline. No disc or rim; the lower part dissolves in horizon haze |
| Small repeating objects (flock of birds) smear | "Keep the same size and position, moving at the same speed as the camera". If that still fails, make it separately as overlay material |
| The camera goes straight to the centre instead of the designated point | Change to "tracking shot following the subject". Write the zoom amount as half of what is wanted |
| Acting is too big or expressionless | Close both ends of the emotional range with `failed take` |
| Background characters freeze or all move at once | Headcount + one different task each. Unnamed people are faceless silhouettes |
