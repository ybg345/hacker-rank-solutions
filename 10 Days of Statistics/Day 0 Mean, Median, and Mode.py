# Problem Link: https://www.hackerrank.com/challenges/s10-basic-statistics/problem
# ----------------------------------------------------------------------------------


n = int(input())
numbers = sorted(list(map(int,input().split())))

mean = sum(numbers)/n
print(mean)

def median(x):
    if len(x) % 2 != 0:
        return x[len(x)//2]
    else:
        return (x[len(x)//2] + x[len(x)//2 - 1]) / 2
print(median(numbers))

# from collections import Counter
# Mode = sorted(sorted(Counter(numbers).items()), key = lambda x: x[1], reverse = True)[0][0]
# print(Mode)

import numpy as np
from scipy import stats
print(int(stats.mode(numbers)[0]))