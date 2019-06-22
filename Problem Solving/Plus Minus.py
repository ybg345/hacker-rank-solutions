# Problem Link: https://www.hackerrank.com/challenges/plus-minus/problem
# ----------------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    sump = 0
    sumn = 0
    sumz = 0
    for i in arr:
        if i > 0:
            sump += 1
        elif i < 0:
            sumn += 1
        else:
            sumz += 1
    print(sump/len(arr))
    print(sumn/len(arr))
    print(sumz/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
