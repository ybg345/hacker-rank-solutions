# Problem Link: https://www.hackerrank.com/challenges/bash-tutorials-filter-an-array-with-patterns/problem
# --------------------------------------------------------------------------------------------------------


readarray names
echo ${names[@]/*[aA]*/}