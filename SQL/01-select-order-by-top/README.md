# SELECT, ORDER BY and TOP

Exercises on sorting and limiting rows in SQL Server.

## Source
Exercises based on Baraa's SQL course.
Database used: [https://academy.datawithbaraa.com/l/digital_download/930511/sql-course-materials]

## What I learned
- SQL Server has no `LIMIT`; it uses `TOP` or `OFFSET ... FETCH`.
- `NULL` comes first in `ORDER BY ... ASC`.
- Comparing with `NULL` requires `IS NULL` / `IS NOT NULL`, never `=` or `!=`.
- `TOP` itself does not work per groups;
- `WITH TIES` only matters when there is a tie at the `TOP` boundary.