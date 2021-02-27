-- Using if/then logic
SELECT CASE
    WHEN rank <= 10 THEN 'Top 10'
    WHEN rank <= 20 THEN 'Top 20'
    ELSE NULL
    END AS rank_category
FROM recent_grads;

SELECT CASE
   WHEN Sample_size < 200 THEN 'Small'
   WHEN Sample_size < 1000 THEN 'Medium'
   ELSE 'Large'
   END AS Sample_category
FROM recent_grads;

SELECT Major, Sample_size,
    CASE
    WHEN Sample_size < 200 THEN 'Small'
    WHEN Sample_size < 1000 THEN 'Medium'
    ELSE 'Large'
    END AS Sample_category
FROM recent_grads;

-- Summary statistic by a unique value in a row
SELECT Major_category, SUM(Employed)
    FROM recent_grads
GROUP BY Major_category;

SELECT Major_category, SUM(Total) AS Total_graduates
    FROM recent_grads
GROUP BY Major_category;

SELECT Major_category, AVG(ShareWomen) AS Average_women
    FROM recent_grads
GROUP BY Major_category;

SELECT Major_category,
    SUM(Employed), AVG(Employed), MAX(Employed) - MIN(Employed) as range_employed
FROM recent_grads
GROUP BY Major_category;

SELECT Major_category,
    SUM(Women) AS Total_women,
    AVG(ShareWomen) AS Mean_women,
    SUM(Total)*AVG(ShareWomen) AS Estimate_women
FROM recent_grads
GROUP BY Major_category;

SELECT Major_category, Sample_category,
       AVG(ShareWomen) AS Mean_women,
       SUM(Total) AS Total_graduates
FROM new_grads
GROUP BY Major_category, Sample_category;

-- Filtering results after aggregation
SELECT Major_category,
    AVG(Low_wage_jobs)/AVG(Total) AS Share_low_wage
FROM new_grads
GROUP BY Major_category
HAVING Share_low_wage > 0.1

-- Rounding a column to four decimal places
SELECT Major_category, ROUND(ShareWomen, 4) AS Rounded_women
FROM new_grads
LIMIT 10;

SELECT Major_category, ROUND(AVG(College_jobs)/AVG(Total), 3) AS Share_degree_jobs
FROM new_grads
GROUP BY Major_category
HAVING Share_degree_jobs < 0.3;

-- Convert, "casting" a column to a float type
SELECT CAST(Women AS Float) / CAST(Total AS Float) AS women_ratio
FROM new_grads
LIMIT 5;

SELECT Major_category,
    SUM(CAST(Women AS Float)) / SUM(CAST(Total AS Float)) AS SW
FROM new_grads
GROUP BY Major_category
ORDER BY SW;