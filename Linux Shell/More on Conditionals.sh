# Problem Link: https://www.hackerrank.com/challenges/bash-tutorials---more-on-conditionals/problem
# -------------------------------------------------------------------------------------------------


read x
read y
read z

if [[ $x == $y && $y == $z ]]
then
    echo 'EQUILATERAL';
elif [[ $x == $y || $y == $z || $z == $x ]]
then
    echo 'ISOSCELES';
else
    echo 'SCALENE';
fi