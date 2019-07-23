# Problem Link: https://www.hackerrank.com/challenges/bash-tutorials---compute-the-average/problem
# ------------------------------------------------------------------------------------------------


read n
readarray num

sum=0
for (( i=0; i<n; i++ ))
do
    sum=$(($sum+${num[i]}))
done

printf "%.3f" $(echo "scale=10; $sum / $n" | bc -l) 



# "bc -l" is required to print the exact numbers after decimal place. Otherwise only using bc will print three 0 after decimal. 
