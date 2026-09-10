# Engineering highlights

This project combines image processing, data engineering, transactional storage and decision modeling around a real operational problem.

## Data integrity over convenient shortcuts

The system rejects several tempting shortcuts:

- same title across different platforms;
- standard edition vs. budget/reissue edition;
- disc-only vs. complete-copy valuation;
- retail asking price vs. seller proceeds;
- research timestamp vs. actual transaction date;
- closed case vs. confirmed disc presence.

The result is deliberately conservative. A missing answer is preferable to a convincing answer built from incompatible evidence.

## Idempotent ingestion

Store visits and market imports are designed so a second identical run is a no-op. This matters because live research is often repeated while debugging, and duplicate evidence would silently skew medians and confidence.

## Protected history

Major write phases are preceded by database backups. Validators can compare protected historical rows before and after migrations so an unrelated schema change cannot silently mutate old observations.

## Deterministic operational layer

Once evidence is accepted, the shopping layer is deterministic. It can answer:

- current modeled profit and ROI;
- maximum acquisition price for a target decision class;
- how much price headroom remains;
- whether a lower price can fix the decision;
- whether a non-price blocker still prevents purchase readiness.

This separation makes the system easier to test than a single opaque scoring function.

## Field feedback changed the architecture

The strongest design improvements came from actual store use: title/price association errors, duplicated photos, hidden price labels, missing physical contents and condition notes all forced the data model to become more explicit.
