# Problem Link: https://www.hackerrank.com/challenges/earnings-of-employees/problem
# ---------------------------------------------------------------------------------


SELECT MONTHS*SALARY, COUNT(*) FROM EMPLOYEE GROUP BY MONTHS*SALARY DESC LIMIT 1;

-- count(*) counts the total number of rows based on codtition of group by. 
-- group by , groups based on the condition (Here, descending order based on months*salary)
-- limit 1, we use it to display the first row only. 
