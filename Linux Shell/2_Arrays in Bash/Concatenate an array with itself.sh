# Problem Link: https://www.hackerrank.com/challenges/bash-tutorials-concatenate-an-array-with-itself/problem
# -----------------------------------------------------------------------------------------------------------


names=($(cat))
twiceConcat=("${names[@]}" "${names[@]}" "${names[@]}")
echo ${twiceConcat[@]}