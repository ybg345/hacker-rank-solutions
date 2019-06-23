# Problem Link: https://www.hackerrank.com/challenges/african-cities/problem
# --------------------------------------------------------------------------


SELECT CITY.NAME FROM CITY INNER JOIN COUNTRY WHERE
CITY.CountryCode = COUNTRY.Code AND COUNTRY.CONTINENT = "Africa";