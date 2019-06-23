# Problem Link: https://www.hackerrank.com/challenges/placements/problem
# ----------------------------------------------------------------------


SELECT S.NAME FROM STUDENTS S INNER JOIN FRIENDS F 
ON S.ID=F.ID INNER JOIN PACKAGES P 
ON P.ID=S.ID INNER JOIN PACKAGES P1 
ON P1.ID=F.FRIEND_ID 
WHERE (P1.SALARY-P.SALARY)>0 ORDER BY P1.SALARY;

-- Here, we are making a table like the last table having all the column of the first 3 table using inner join. 
-- p1 is denoting friend and p is denoting student. 