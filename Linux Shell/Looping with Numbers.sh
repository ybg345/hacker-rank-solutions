# Problem Link: https://www.hackerrank.com/challenges/bash-tutorials---looping-with-numbers/problem
# -------------------------------------------------------------------------------------------------


n="1"
while [[ $n -le 50 ]]
do
    echo "$n"
    ((n++))
done