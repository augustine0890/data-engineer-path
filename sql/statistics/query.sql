SELECT * FROM recent_grads;

-- Return the first five rows for 'recent_grads'
SELECT *
FROM recent_grads
LIMIT 5;

-- Returns only the 'Major' and 'ShareWomen'
SELECT Major, ShareWomen
FROM recent_grads;

-- Where 'ShareWomen' is less than 0.5
SELECT Major, ShareWomen
FROM recent_grads
WHERE ShareWomen < 0.5;

/* Where 'ShareWomen' is greater than 0.5
and 'Median' is greater than 50000*/
SELECT Major, Major_category, Median, ShareWomen
FROM recent_grads
WHERE ShareWomen > 0.5
AND Median > 50000;

/* 'Median' greater than 10,000 or more men than women*/
SELECT Major, Median, Unemployed
FROM recent_grads
WHERE Median >= 10000
OR Men > Women
LIMIT 20;

/*
Category of Engineering and either
The majority of the graduates were women
Or had an unemployment rate below 5.1%
*/
SELECT Major, Major_category, ShareWomen, Unemployment_rate
FROM recent_grads
WHERE (Major_category = 'Engineering')
AND (ShareWomen > 0.5 OR Unemployment_rate < 0.051);

SELECT Rank, Major, Major_category, ShareWomen, Unemployment_rate
FROM recent_grads
WHERE (Major_category = 'Engineering') 
AND (ShareWomen > 0.5 OR Unemployment_rate < 0.051)
ORDER BY Unemployment_rate DESC;

/*
'ShareWomen' is greater than 0.3 and 'Unemployment_rate' is less than .1
Descending order by the 'ShareWomen' column
*/

SELECT Major, ShareWomen, Unemployment_rate
FROM recent_grads
WHERE ShareWomen > 0.3
AND Unemployment_rate < 0.1
ORDER BY ShareWomen DESC

/*
Returns 'Engineering' or 'Physical Sciences' category
Ascending order of unemployment rate
*/
SELECT Major_category, Major, Unemployment_rate
FROM recent_grads
WHERE (Major_category = 'Engineering')
OR (Major_category = 'Physical Sciences')
ORDER BY Unemployment_rate;