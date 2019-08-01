# Problem Link: https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals/problem
# --------------------------------------------------------------------------------------------------------------


read x 

if [[ $x == y || $x == Y ]];
then
    echo "YES"
elif [[ $x == n || $x == N ]];
then
    echo "NO"
fi