# Problem Link: https://www.hackerrank.com/challenges/bash-tutorials-count-the-number-of-elements-in-an-array/problem
# -------------------------------------------------------------------------------------------------------------------


names=($(cat))
echo ${#names[@]}