-- Lowest unemployment rate
SELECT MIN(Unemployment_rate)
FROM recent_grads;

-- Computes the sum of the `Total` column
SELECT SUM(Total)
FROM recent_grads;

-- Returns the number of majors that include mostly men
SELECT COUNT(Major)
FROM recent_grads
WHERE ShareWomen > 0.5;

-- Average of the 'Total' column, MIN of the 'Men', MAX of the 'Women'
SELECT AVG(Total), MIN(Men), MAX(Women)
FROM recent_grads;

SELECT 
    COUNT(*) AS 'Number of Majors', 
    MAX(Unemployment_rate) AS 'Highest Unemployment Rate'
FROM recent_grads;

SELECT 
    COUNT(DISTINCT(Major)) 'unique_majors', 
    COUNT(DISTINCT(Major_category)) 'unique_major_categories', 
    COUNT(DISTINCT(Major_code)) 'unique_major_codes'
FROM recent_grads;

SELECT 'Major: ' || LOWER(Major) AS 'Major',
    Total, Men, Women, Unemployment_rate,
    LENGTH(Major) AS Length_of_name
FROM recent_grads
ORDER BY Unemployment_rate DESC
LIMIT 3;

SELECT Major, Major_category, P75th - P25th AS quartile_spread
FROM recent_grads
ORDER BY quartile_spread
LIMIT 20;