# Art-style image (watercolour, illustration)

## Required information

| Required information | Template slot |
|---|---|
| Medium, technique, paper, aspect ratio | first line |
| Technique base image and auxiliary images (job, order) | `Reference images` |
| Colour base image (job) | last of `Reference images` |
| Viewpoint/angle, placement per third-zone, number of people | `Scene` |
| Time, the screen side the sun comes from and the object on that side, shadow direction, colour range | `Light` |
| Surface treatment | `Style` |
| Period-appropriate objects/materials, buildings/clothes to match other cuts | `Look of the place` |
| Crop band, occlusion zones | `Composition` |
| Things that must not appear because they do not fit the era | last line |

## Rules

- **If the surface reads as stone pattern or tile,** specify a wide brush range: `large, smooth, softly mottled plaster washes laid with a wide wet brush`
- **For "디테일만 올려" (only raise the detail),** insert only one reference and write "only refine the brushstrokes of the surfaces that exist". Leave vegetation, light, brightness and composition as they are.
- **For a local edit that moves or erases only part, direct editing (pixel compositing) is faster and cheaper.** Record "모델 생성 아님" (not model-generated) on the edited version.
- **When filling a narrow screen:** shrink the image into the centre of the canvas and have only the surroundings painted (`The central painting stays exactly as it is … paint only the empty margins`).

## Template (틀) — art-style scene (technique reference + colour reference)

```text
A [medium and technique] painting on [paper], [aspect ratio], of the following scene.
Reference images: the first is [base cut] and sets the painting style above all ([technique]); the
[second to Nth] are further style paintings of the same kind. Take only technique, brushwork and paper
texture from these, never their subjects, colors or composition. The [last] is [colour cut]: take only
its colors, light and mood, never its landscape and never its direction of light.
Scene: [viewpoint and angle; zones by thirds; people few and well apart].
Light: [time; the sun comes from screen [left/right], the [object] side; shadow direction; colour range].
Style: [surface handling]; soft lost edges, no outlines.
Look of the place: [period-accurate objects and materials; same buildings and clothing as other cuts].
Composition: [crop band; occlusion zone holds only minor details].
Not a photograph, 3D render, game art or detailed digital illustration; no pen outlines, vignette, text,
border, [period-wrong items].
```
