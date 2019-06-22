# Problem Link: https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
# -----------------------------------------------------------------------------


import numpy
size = tuple(map(int, input().split()))
print(numpy.zeros(size, dtype=int))
print(numpy.ones(size, dtype=int))