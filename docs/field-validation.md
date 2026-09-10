# Anonymized field validation

The production system is tested on real store visits, but this public case study intentionally omits store names, title names, source URLs and proprietary market details.

## Recent live batch

A recent visit supplied ten store-photo uploads.

### Ingestion result

- 10 uploads
- 9 unique evidence assets after byte-level duplicate detection
- 49 distinct physical copies
- 48 directly visible shelf prices
- 1 obscured price preserved as unknown
- 47 newly resolved canonical products
- 2 exact existing canonical products reused

### Market pass

Rather than researching every product equally, the pipeline prioritized items where market evidence could plausibly change a purchase decision.

- 55 compatible market observations added in the targeted pass
- import rerun inserted 0 duplicates
- SQLite integrity check: `ok`
- foreign-key violations: `0`

### Decision surface

The resulting live screen produced:

- 1 `BUY`
- 7 `MAYBE`
- 41 `RESEARCH`

A large `RESEARCH` count is intentional. It means the system did not manufacture strong decisions for products without sufficient compatible evidence.

## Physical-condition follow-up

A later condition-card review showed why title-level valuation is insufficient. Several apparently attractive products lost most of their modeled margin after visible disc scratches, manual damage, missing inserts and case damage were applied.

That field result validated the decision to model physical copies independently from canonical product value.
