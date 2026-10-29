---
name: acting
description: Use when newly writing CHARACTER_ACTING for an AI live-action video cut in which a character acts, or when building a recurring character's master profile and voice sentence. Fixing the acting of a video already made is video-prompt's fixes.md.
---

# Character acting

## 1. Principles

**Acting is behaviour under pressure, not a display of emotion.** Do not write emotion. Write objective and action.

| Do not write | Write |
|---|---|
| Emotion adjectives | A verb aimed at the other person |
| An empty face waiting for its line | A reaction that starts before the other person finishes speaking |
| Gestures that mimic the dialogue | Hands doing real work |
| An acting face (eyebrows, frowning) | A thinking face. It reads in the eyes first |

**Do not act the subtext.** When a character speaks false text while pursuing the real objective, it leaks on its own. Markers: answers that are too short, asking the same thing again, sudden topic changes, a joke at the wrong moment.

## 2. Decide per scene

1. **Objective:** what they want from this person right now (a verb). Write as `[상대]에게/에게서 + 동사` ([other person] + to/from + verb). Examples: speaker `[상대]에게서 사과를 받아 낸다` (extracts an apology from [other]), listener `[상대]에게 괜찮다고 믿게 한다` (makes [other] believe it's fine). Something aimed at oneself, like "내색하지 않기" (not showing it), is not an objective.
2. **Obstacle and cost:** what blocks it, what is lost on failure.
3. **Tactic:** change it when it fails.
4. **Beats:** change 2-4 times per scene. A change shows as behaviour (pause, posture, tempo, gaze).
   - An event is an action that changes the state of a body or object (grip, release, stand, turn, walk, line of dialogue). A gaze shift, a pause, a breath are beats.
   - A beat is not an event. Leave the per-generation event count (1-3, `video-prompt` §2) as it is, and write beats as tactic changes within the same action (gaze shift, pause, posture). A 6-second cut needs only 2 beats.

## 3. Body

- **Fix four body states.** Centre of weight (high = confidence/status / low = fatigue/submission), tempo (fast and jagged = anxious / slow and economical = controlled), openness (open shoulders, open hands / crossed arms, lowered head), breathing (high and fast = panic / low and slow = controlled). **Breathing is the most honest indicator.**
- **Give the hands a job (business).** While speaking, the hands do real work. How someone counts money says more than words.
- **The moment of stopping what they were doing is the strongest accent.** When stopping, add `does not startle; simply stops`.
- **Change in distance = change in beat.** Within 0.5 m intimate, 0.5-1.2 m trust, 1.2-3.5 m business/guarded, beyond 3.5 m alienation. Write who closes it and who breaks it.
- **Status lives in the body.** High: a still head, slow movement, a pause before answering. Low: fussing, self-touch, broken speech. **A status rupture** (a superior showing fear for one second) is the most interesting.
- **Name the walk.** `"[name] walk" — [step size, arm swing]`. The name fixes the movement.
- **Wear accumulates.** A character who is worn down across the story is not reset between scenes.
- The physical order of actions goes in `ACTION_TIMING`; the texture of the acting goes in `CHARACTER_ACTING`.

## 4. Listening and speaking

- **Thought before speech.** A slight pause before answering a hard question. An instant answer at constant speed is a memorised line.
- **The moment of assessment.** After something important (news, a threat, an insult) there is time to digest it. A gaze that loses focus for 1-2 seconds.
- **Contagion from the other person.** Tempo and volume change in response to them.
- **The scariest words, the quietest.** A pause is an event, not a hole. Use one only when something is happening inside.
- **Real speech has debris.** Interruptions, repetition, unfinished sentences. Overlap is normal, but keep the key words clean.

## 5. Eyes

```text
continuous naturalistic eye life: micro-saccades and gaze targeting, the gaze drifting and settling
rather than locking, realistic blink rate tied to state, live wet catchlights, the eyes reaching
the target a beat before the head turns
```

- Put only the physics of the eyes (moisture, catchlights) in the character sheet. Put the eyes' character (whether they give first or avoid) in the cut prompt.

## 6. Master profile (recurring characters)

One English paragraph of 150-220 words, only observable things. Keep it in the asset registry.

```text
Character acting as [NAME]. [age, build, posture]. [psychological engine, one clause].
Vocal profile: [range, accent, pace, change under pressure]. Key physical habits and tics: [tic + trigger;
stress tic + trigger; what is hidden; the mask and what breaks it]. Eye life: [§5]. Walking style:
["name" + description]. However, when [trigger], [change]. [The one thing that softens them].
```

- Attach a trigger to every tic. A tic without a trigger is decoration.
- At least one `However, when …` crack is required. Only one thing that softens them.
- Do not include wardrobe, camera, or colour.

**Rewrite it for the scene (do not paste).**
- Write only the characters in the frame.
- The invariant core is the same in every scene: identity, voice, signature tics, eye life, the emotional through-line.
- Choose according to the scene's posture, actions and beats. Do not delete an impossible action; convert it to another outlet. Energy is constant, the outlet changes.
- One flowing paragraph without bullets. If using reference tags, start the paragraph with the character tag.

## 7. The voice is fixed

Make one sentence per character and paste it verbatim whenever there is dialogue.

```text
"A [age]-year-old [origin/accent]. [timbre, range]; [pace, delivery]; [change under pressure]."
```

## 8. Register and ensemble

- Set per work, in `decisions.md`, "acting used / acting not used". The tighter the shot, the less the movement. A close-up is eyes and thought only.
- **Group reactions come as a wave.** One person first, the second half a beat later, the third does not catch on. Before a threat everyone stops. Movement has a motive.

## 9. Sentences in use

| Problem | Sentence |
|---|---|
| Emotion overflows or is switched off | `between [A] and [B]; [extreme 1] = failed take, [extreme 2] = failed take` |
| The whole body (down to the feet) whips around | `head → shoulders → feet over three seconds; turning within one second = failed take` |
| Mouth of a character who should not speak | `[Person] does not say a single word: no attempt to speak, no parted lips, no mouthing.` Write hesitation with breath, swallowing, hands |
| A pause reads as being startled | `does not startle; simply stops` / `the action carries through and only the eyes stay on it` |
| Reaction too big or absent | `If [the reaction] is strong, it is a failed take; if there is no reaction at all, it is also a failed take.` |

## 10. Bad acting -> fix

| Symptom | Fix |
|---|---|
| Plays the ending from the first second | Write only what the character knows right now |
| One tone all the way through | Give a new tactic verb at each beat |
| Tears/anger without a trigger | Ladder of restraint -> crack. Emotion has a cost |
| Body at odds with the character's history | Fix centre of weight, tempo, wear |
| A character who talks in written language | Put interruptions and repetition into the speech |
| A "menacing" pause before violence | Menace comes ordinarily, without warning |
| Silence in which nothing happens | Fill it with assessment or a hand task, or cut it |
| A crowd reacts identically | Stagger it as a wave and vary the intensity |
| Instant recovery after a strong event | Leave a trace into the next beat |
| Acting that winks at the audience | Fully believe the situation |

## 11. Pre-send check

- [ ] Does every character in frame have an objective as a verb aimed at the other person, and an obstacle?
- [ ] Do beat changes show as behaviour (pause, posture, tempo, gaze)? Is there one action per character in `ACTION_TIMING`?
- [ ] Did you count and write down the event count (per verb) and the beat count (gaze, pause, posture) separately?
- [ ] Does the reaction start mid-way through the other person's line? Is there a moment of assessment?
- [ ] Does every character have a hand task? Did you write the body state (including breathing)?
- [ ] Did you write the eye life? Did you close both ends of the emotional range as failed take?
- [ ] If there is dialogue, did you paste the voice sentence verbatim? Did you lock the mouth of characters who do not speak?
- [ ] Is there no wardrobe, camera, or colour inside the acting? Did it stay within the work's register?
- [ ] If your own rating is "objective visible but one tone" (diligent), rewrite it
