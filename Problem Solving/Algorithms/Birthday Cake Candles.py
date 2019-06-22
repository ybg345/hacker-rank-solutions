# Problem Link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# ---------------------------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    a = sorted(ar, reverse=True)
    max = a[0]
    count = 0
    for i in a:    
        if i == max: 
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
