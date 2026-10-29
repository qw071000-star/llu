# High-resolution re-render

Do not generate anew. Regenerating yields a different take.

**Before sending:** get the 1080p quote with `[TOOL] get_cost` (`higgsfield-generation` §1), tell the user the number with its basis, and confirm once.

- **For Seedance 2.5, send review versions as `draft: true` (480p).** On approval, within 7 days make the 1080p final from `draft_job_id`. The same take is upscaled as is. A review version costs the same as a non-draft 480p.
- If it was not a draft or the deadline has passed, attach the adopted take as the source video using the template below, and re-render with the same elements and the same voices.

## Information needed

| Information needed | Place in the template |
|---|---|
| Adopted take job (OK ledger card), source resolution, target resolution | `SOURCE VIDEO`, `RESOLUTION` |
| Shot composition of the source: cuts, lengths, lines | Shot summary |
| Elements attached to the source and their order, voice files | `ACTIVE REFERENCES` |
| The source's STYLE and QUALITY sentences | `STYLE / QUALITY` |
| Whether the user instructed a final-resolution generation | Pre-generation check |

## Template

```text
SOURCE VIDEO: the attached video is the take to reproduce. [Shot-by-shot summary]. Every cut,
duration, line and sound stays the same.
RESOLUTION: the source is [480p/720p]; only resolution and detail differ.
ACTIVE REFERENCES: [same elements, same order, same voice files as the source].
STYLE / QUALITY: [same]. No digital sharpening.
Required: same number, order and length of shots as the source; any difference = failed take.
```

The check's `--refs` is the number of `<<<>>>` tags in the prompt. The attached source video is not counted.
