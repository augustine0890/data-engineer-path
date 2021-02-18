# Basics of SQL
- Database: structure data just like a spreadsheet, by organizing data in different tables comprised of rows and columns.
- A database can store much more data more securely than a spreadsheet or a text file. In order to "ask" for data from the database we need to write queries.
- Column names are metadata.
- The semicolon indicates that we have reached the end of the query.

## Exploring Tables
- Most of the tables start with an ID column from 1 to the number of rows in the tables. This is called the identity column.
- `SELECT DISTINCT` to remove duplicate values in a column.
- SQL uses the following order of precedence:
    - `FROM`, `SELECT`/`SELECT DIST`, `LIMIT`.

## Coding Style
- Comments are readable messages in code that SQL ignores.
- Reserved words have a special function and shouldn't be used for anything else.