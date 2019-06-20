# Problem Link: https://www.hackerrank.com/challenges/30-recursion/problem
# ------------------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n <= 1:
        return 1
    else:
        f = n*factorial(n-1)
        n-=1
        return f

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
