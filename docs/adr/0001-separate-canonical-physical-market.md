# ADR 0001: Separate canonical items, physical observations and market observations

**Status:** Accepted

## Context

A title can be seen multiple times, at different stores, with different prices and physical condition. The same title also has many market observations from different sources and evidence types.

Collapsing those records makes it impossible to answer whether a decision applies to this exact store copy.

## Decision

Model canonical identity, physical sightings and market evidence as separate entities linked by stable IDs.

## Consequences

This preserves store/date/price history, supports multiple physical copies, enables provenance and copy-specific condition, and prevents a market comp from becoming a physical-stock claim. The cost is more joins and explicit resolution steps.
