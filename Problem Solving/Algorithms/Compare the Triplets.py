# Problem Link: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# --------------------------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    suma = 0
    sumb = 0
    # summ = [suma, sumb]
    for i in range(len(a)): 
        if a[i] > b [i]:
            suma +=1
            print(suma)
        elif a[i] < b[i]:
            sumb +=1
            print(sumb)
        # elif a[i] == b[i]:
        #     return summ 
        #     print(summ)
    return [suma, sumb]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
