# Problem Link: https://www.hackerrank.com/challenges/the-report/problem
# ----------------------------------------------------------------------


SELECT (CASE WHEN GRADE>=8 THEN NAME ELSE NULL END), GRADE, MARKS FROM STUDENTS, GRADES
WHERE MARKS BETWEEN MIN_MARK AND MAX_MARK 
ORDER BY GRADE DESC, NAME ASC


-- SYNTAX FOR USING 'IF' IN PLACE OF CASE: 
--  "IF(GRADE >= 8, NAME, NULL)""