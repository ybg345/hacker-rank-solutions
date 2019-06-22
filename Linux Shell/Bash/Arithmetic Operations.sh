# Problem Link: https://www.hackerrank.com/challenges/bash-tutorials---arithmetic-operations/problem
# --------------------------------------------------------------------------------------------------


read expr
printf "%.3f" $(echo $expr | bc -l)