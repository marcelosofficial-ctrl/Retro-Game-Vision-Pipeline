# Development notes

The project was built iteratively against real field observations rather than as a one-off prototype.

A typical change cycle is:

1. identify a concrete failure mode from real data;
2. reduce it to a reproducible case;
3. encode the schema or rule change;
4. add a regression guard;
5. back up before writes;
6. make the change idempotent;
7. run SQLite foreign-key and integrity checks;
8. package a checkpoint;
9. extract that checkpoint into a fresh directory and validate it again.

This approach has been especially useful because most serious bugs are not syntax errors. They are semantic errors: the wrong price attached to the right title, the right title matched to the wrong edition, an old sale treated as fresh, or a closed case treated as proof that the disc exists.
