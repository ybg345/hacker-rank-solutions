# Problem Link: https://www.hackerrank.com/challenges/bash-tutorials-slice-an-array/problem
# -----------------------------------------------------------------------------------------


names=($(cat))                  # Reading list as array
echo ${names[@]:3:5}


# Here we extract 5 elements starting from the position 3 from an array called "names".