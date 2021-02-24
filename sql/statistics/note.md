# Statistics with SQL
- A database is a data representation that lives on disk, and it can be required, accessed, and updated without using much memory.
- A database management system (DBMS) allows you to interact with a database. SQLite, Postgresql, and MySQL are the most popular databases in the world.

```sql
SELECT *
FROM some_table
WHERE some_condition
ORDER BY some_column
LIMIT some_limit;
```
- The `COUNT` clause can be used on any column while aggregate functions can only be used on numeric columns.
- We use summary statistics to summarize a set of observations.
- `NULL` is a special entity in SQL that exists to capture the concept of missing value.
- Concatenate strings by using the `||` operator.
- Most operators can be used with a mixture of constant values and columns