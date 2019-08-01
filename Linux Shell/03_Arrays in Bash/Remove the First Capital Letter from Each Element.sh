# Problem Link: https://www.hackerrank.com/challenges/bash-tutorials-remove-the-first-capital-letter-from-each-array-element/problem
# ----------------------------------------------------------------------------------------------------------------------------------


names=($(cat))                  #Another way of reading array is - readarray [array_name]
echo ${names[@]/[A-Z]/.}