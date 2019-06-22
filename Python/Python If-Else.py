# Problem Link: https://www.hackerrank.com/challenges/py-if-else/problem
# ----------------------------------------------------------------------


#!/bin/python3

N = int(input())

if N in range(1, 101): 
    if N % 2 != 0:
        print("Weird")
    else:
        if 2 <= N <= 5: 
            print("Not Weird")
        elif 6 <=N <= 20:
            print("Weird")
        elif N > 20:
            print("Not Weird")
        