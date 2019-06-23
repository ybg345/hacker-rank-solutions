# Problem Link: https://www.hackerrank.com/challenges/average-population-of-each-continent/problem
# ------------------------------------------------------------------------------------------------


SELECT COUNTRY.Continent, FLOOR(AVG(CITY.Population)) FROM COUNTRY INNER JOIN CITY WHERE
CITY.CountryCode = COUNTRY.Code GROUP BY COUNTRY.Continent;