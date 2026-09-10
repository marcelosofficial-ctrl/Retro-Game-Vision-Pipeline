# ADR 0002: Reject incompatible comps instead of normalizing them away

**Status:** Accepted

## Context

Collector pricing is often edition- and completeness-sensitive. A high-value complete copy can make a cheap disc-only copy look profitable if rows are pooled by title alone.

## Decision

Compatibility is an explicit gate before valuation. Platform, region, edition and completeness can reject a market row entirely.

## Consequences

The system sometimes returns `RESEARCH` when a looser scraper could produce a number. That is intentional. Missing evidence is preferable to false precision.
