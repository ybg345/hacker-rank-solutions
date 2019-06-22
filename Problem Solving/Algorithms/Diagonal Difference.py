# Problem Link: https://www.hackerrank.com/challenges/diagonal-difference/problem
# -------------------------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    d1 = 0
    d2 = 0
    for i in range(n):
        d1 += int(arr[i][i])
        d2 += int(arr[i][n-i-1])
    d3 = abs(d1-d2)
    # print(d3)
    return d3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
