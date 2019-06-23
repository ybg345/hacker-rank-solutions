# Problem Link: https://www.hackerrank.com/challenges/what-type-of-triangle/problem
# ---------------------------------------------------------------------------------


SELECT
CASE
    WHEN A+B>C THEN
        CASE 
            WHEN (A=B AND B=C) THEN 'Equilateral'
            WHEN (A=B OR B=C OR C=A) THEN 'Isosceles'
            WHEN (A!=B OR B!=C OR C!=A) THEN 'Scalene'
        END
    ELSE 'Not A Triangle' 
END 
FROM TRIANGLES; 


--------------------------------CASE SYNTAX IN MySQL:----------------------------------
-- SELECT [COLUMN NAMES]
-- CASE
--     WHEN [CONDITION 1 TRUE] THEN "Print something or do something"
--     WHEN [CONDITION 2 TRUE] THEN "Print something or do something"
--     ELSE "Print something or do something"
-- END
-- FROM [TABLE NAME]
    