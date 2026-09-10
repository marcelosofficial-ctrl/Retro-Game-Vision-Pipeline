# Vision and evidence pipeline

The image workflow is designed around a simple rule: **analysis may transform an image, but it must not erase where a claim came from.**

## Flow

1. Preserve the original store image.
2. Compute a stable content hash for duplicate detection.
3. Create derived crops or grid cells for analysis.
4. Run OCR / visual candidate extraction on the derived region.
5. Keep candidate text, confidence and spatial context separate from accepted identity.
6. Resolve the candidate to a canonical product only when platform/region/edition evidence is sufficient.
7. Create a physical observation that points back to the original evidence asset and image region.
8. Route ambiguous cases to review instead of forcing a title.

## Why spatial lineage matters

The earliest whole-shelf workflow could read a valid title and a valid price while still pairing the wrong two objects. That is more dangerous than an OCR miss because the output looks plausible.

The fix was architectural rather than cosmetic: original evidence, derived region, recognized candidate and accepted item identity became separate states. This makes it possible to audit exactly which pixels supported a store observation.

## Duplicate handling

Evidence assets are content-addressed. Uploading the same photo twice should not create duplicate physical copies. The public demo includes SHA-256 helpers and idempotence tests that illustrate this pattern without exposing the production image pipeline.
