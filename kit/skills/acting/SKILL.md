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

**Play only what the character knows right now,** and believe the situation fully (no winking at the audience). Tears or anger need a trigger and a cost (restraint, then a crack). Menace comes ordinarily, without warning. A strong event leaves a trace into the next beat; no instant recovery.

**Do not act the subtext.** When a character speaks false text while pursuing the real objective, it leaks on its own. Markers: answers that are too short, asking the same thing again, sudden topic changes, a joke at the wrong moment.

## 2. Decide per scene

1. **Objective:** what they want from this person right now (a verb). Write as `[상대]에게/에게서 + 동사` ([other person] + to/from + verb). Examples: speaker `[상대]에게서 사과를 받아 낸다` (extracts an apology from [other]), listener `[상대]에게 괜찮다고 믿게 한다` (makes [other] believe it's fine). Something aimed at oneself, like "내색하지 않기" (not showing it), is not an objective.
2. **Obstacle and cost:** what blocks it, what is lost on failure.
3. **Tactic:** change it when it fails.
4. **Beats:** change 2-4 times per scene. A change shows as behaviour (pause, posture, tempo, gaze).
   - A gaze shift, a pause, a breath, a posture change are beats, not events. Leave the event count (`video-prompt` §2 "Event count") as it is and write beats as tactic changes within the same action. A 6-second cut needs only 2 beats.
   - Count and write down the event count and the beat count separately.

## 3. Body

- **Fix four body states.** Centre of weight (high = confidence/status / low = fatigue/submission), tempo (fast and jagged = anxious / slow and economical = controlled), openness (open shoulders, open hands / crossed arms, lowered head), breathing (high and fast = panic / low and slow = controlled). **Breathing is the most honest indicator.**
- **Give the hands a job (business).** While speaking, the hands do real work. How someone counts money says more than words.
- **The moment of stopping what they were doing is the strongest accent.** When stopping, add `does not startle; simply stops`.
- **Change in distance = change in beat.** Within 0.5 m intimate, 0.5-1.2 m trust, 1.2-3.5 m business/guarded, beyond 3.5 m alienation. Write who closes it and who breaks it.
- **Status lives in the body.** High: a still head, slow movement, a pause before answering. Low: fussing, self-touch, broken speech. **A status rupture** (a superior showing fear for one second) is the most interesting.
- **Name the walk.** `"[name] walk" — [step size, arm swing]`. The name fixes the movement.
- **Wear accumulates.** A character who is worn down across the story is not reset between scenes.
- The physical order of actions goes in `ACTION_TIMING`; the texture of the acting goes in `CHARACTER_ACTING` (no wardrobe, camera or colour there).

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
| A pause reads as being startled | `does not startle; simply stops` / `the action carries through and only the eyes stay on it` |
| Reaction too big or absent | `If [the reaction] is strong, it is a failed take; if there is no reaction at all, it is also a failed take.` |
