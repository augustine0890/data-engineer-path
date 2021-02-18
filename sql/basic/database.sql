SELECT employee_id, first_name, title
FROM employee;

SELECT first_name, title, employee_id
FROM employee;

/* select specific columns from a table */
SELECT first_name, last_name, birthdate, phone, email
FROM employee;

/* display all columns */
SELECT * FROM genre;

SELECT country, name, version
FROM apps;

SELECT company_name FROM companies;

SELECT net_worth, ceo
FROM companies;

SELECT *
FROM invoice_line
LIMIT 10;

SELECT DISTINCT unit_price
FROM invoice_line;

SELECT invoice_id, track_id
FROM invoice_line
LIMIT 3;

SELECT *
FROM artist
LIMIT 5;

-- Get the first five rows from genre
SELECT *
FROM genre
LIMIT 5;

SELECT customer_id, first_name, last_name, email 
FROM customer 
LIMIT 5;

SELECT city, state, country, postal_code
  FROM employee
 LIMIT 20;