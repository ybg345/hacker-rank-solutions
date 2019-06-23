# Problem Link: https://www.hackerrank.com/challenges/asian-population/problem
# ----------------------------------------------------------------------------


SELECT SUM(CITY.POPULATION) FROM CITY INNER JOIN COUNTRY 
WHERE CITY.COUNTRYCode = COUNTRY.Code AND COUNTRY.CONTINENT="Asia";