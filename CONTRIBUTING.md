# Contributing to Retro Game Vision

Thanks for taking the time to improve the public Retro Game Vision pipeline.

## Core design rules

Changes should preserve the principles that make the system trustworthy:

- canonical item identity, physical observations, market observations, and evidence assets remain separate concepts
- missing or unreadable data stays missing instead of being guessed
- compatibility checks happen before valuation
- evidence lineage and uncertainty are preserved
- repeated imports remain safe and idempotent
- public-demo code must not expose private field evidence, production scoring policy, credentials, or private source adapters

For larger changes, open an issue first so scope and data-model implications can be discussed before implementation.

## Validation

Run the same checks used by CI:

```bash
python -m pip install -e .
python -m pip check
python -m unittest discover -s tests -v
python scripts/prepublish_check.py
python -m retro_resale_pipeline.demo
```

A pull request should keep all of these checks green.

## Pull requests

Keep changes focused and explain:

1. the problem being solved
2. any schema, evidence-lineage, compatibility, or economics implications
3. how the change was tested
4. whether publication boundaries or private-data handling are affected

Behavior changes should include regression tests. Avoid bundling unrelated formatting or cleanup into the same pull request.

## Security and private evidence

Potential vulnerabilities should follow [SECURITY.md](SECURITY.md). Never attach real private store photos, marketplace credentials, private datasets, or sensitive source configuration to a public issue or pull request.