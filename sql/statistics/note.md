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

## Summary Statistics
- General structure of a query
```sql
SELECT column(s)
  FROM some_table
 WHERE some_condition
 GROUP BY column(s)
HAVING some_condition
 ORDER BY column(s)
 LIMIT some_limit;
```
- `ORDER BY` executes after `GROUP BY`.
And the order in which SQL runs this is as follows:
```sql
FROM
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT
```
- The `GROUP BY` clause allows you to compute summary statistics by group
- The `HAVING` clause filters on the virtual column that `GROUP BY` generates.
- `WHERE` filters results before the aggregation, whereas `HAVING` filters after aggregation.
- The `ROUND` function rounds the results to the desired decimal place.
- To get float value, we can use the `CAST()` function to the transform the columns into `Float` type.
- We can the `CAST` function to convert numeric data into charecter string data.