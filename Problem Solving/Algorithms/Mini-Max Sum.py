# Problem Link: https://www.hackerrank.com/challenges/mini-max-sum/problem
# ------------------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    l = len(arr)
    a = arr.sort()
    li1 = arr[1: l+1]
    li2 = arr[:l-1]
    s1 = sum(li1)
    s2 = sum(li2)
    print(s2, s1)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
