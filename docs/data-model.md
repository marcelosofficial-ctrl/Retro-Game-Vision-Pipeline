# Data model

The production schema is larger, but the core model centers on four entities.

| Entity | Represents | Key reason it is separate |
| --- | --- | --- |
| `canonical_item` | Product identity | Many physical copies and market rows can share one identity |
| `physical_observation` | One exact copy seen in the world | Store, price, condition and evidence belong to the copy, not the title |
| `market_observation` | One value/evidence point | Sold, active, retail, buyback and guide evidence must remain distinguishable |
| `evidence_asset` | Source image/document | Claims need stable lineage and duplicate detection |

## Canonical item

Typical fields include canonical title, Japanese/English aliases, platform, region and release/edition identity.

## Physical observation

One exact item seen in the world. It preserves store, city, observed price, visit/date precision, edition/completeness notes, condition and evidence lineage.

Two copies of the same title at two stores are two physical observations.

## Market observation

One evidence point used to understand resale value. Evidence types remain distinct: sold listing, active ask, retail ask, dealer buyback offer and price guide.

A retail asking price is not seller proceeds. A dealer buyback is not a sold marketplace comp.

## Evidence asset

A source object with stable lineage, typically content-hashed so duplicate uploads can be detected without creating duplicate physical observations.
