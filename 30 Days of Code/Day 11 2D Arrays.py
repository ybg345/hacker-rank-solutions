# Problem Link: https://www.hackerrank.com/challenges/30-2d-arrays/problem
# ------------------------------------------------------------------------


#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


if __name__ == '__main__':
    arr = []
    
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    hourglasses, line = [], []
    for i in range(4):
        for j in range(4):
            line = [sum(arr[i][j:j+3]), arr[i+1][j+1], sum(arr[i+2][j:j+3])]
            hourglasses.append(sum(line))
    print(max(hourglasses))


# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

# 1 1 1   1 1 0   1 0 0   0 0 0
#   1       0       0       0
# 1 1 1   1 1 0   1 0 0   0 0 0

# 0 1 0   1 0 0   0 0 0   0 0 0
#   1       1       0       0
# 0 0 2   0 2 4   2 4 4   4 4 0

# 1 1 1   1 1 0   1 0 0   0 0 0
#   0       2       4       4
# 0 0 0   0 0 2   0 2 0   2 0 0

# 0 0 2   0 2 4   2 4 4   4 4 0
#   0       0       2       0
# 0 0 1   0 1 2   1 2 4   2 4 0


# ----------------------------- Explanation by MoonCWang ------------------------
# arr = [[1, 1, 1, 0, 0, 0],
# [0, 1, 0, 0, 0, 0],
# [1, 1, 1, 0, 0, 0],
# [0, 9, 2, -4, -4, 0],
# [0, 0, 0, -2, 0, 0],
# [0, 0, -1, -2, -4, 0]]


# hr_gls, line = [], []
# for i in range(4):
#     print("-----------------")
#     for j in range(4):
#         print("For Hourglass")
#         print ("%s %s %s" % (arr[i][j], arr[i][j+1], arr[i][j+2]))
#         print ("  %s  " % arr[i+1][j+1])
#         print ("%s %s %s" % (arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]))
        
#         print ("-----------")
#         line = [sum(arr[i][j:j+3]), arr[i+1][j+1], sum(arr[i+2][j:j+3])]
#         print ("getting first hourglass sum for  %s, %s, %s" % (arr[i][j], arr[i][j+1], arr[i][j+2]))
#         print ("sum(arr[%s][%s:%s]) = %s" % (i, j, j+3, sum(arr[i][j:j+3])))
#         print("----")
#         print ("getting middle value of %s" % arr[i+1][j+1])
#         print ("aka arr[%s][%s]" % (i+1, j+1))
#         print("----")
#         print( "getting last hourglass row of %s, %s, %s" % (arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]))
#         print ("sum(arr[%s][%s:%s]) = %s" % (i+2, j, j+3, sum(arr[i+2][j:j+3])))
#         print("----")
#         print ("Hourglass summation %s" % line)
#         print("-------------------")
#         print("-------------------")
#         print("-------------------")
        
#         hr_gls.append(sum(line))
# print(max(hr_gls))