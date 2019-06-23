# Problem Link: https://www.hackerrank.com/challenges/draw-the-triangle-2/problem
# -------------------------------------------------------------------------------


set @number = 0;
select repeat('* ', @number := @number + 1) 
from information_schema.tables limit 20;