# Problem Link: https://www.hackerrank.com/challenges/np-eye-and-identity/problem
# ------------------------------------------------------------------------------


import numpy
row, column = map(int, input().split())
numpy.set_printoptions(sign=' ')
print(numpy.eye(row, column, k=0))