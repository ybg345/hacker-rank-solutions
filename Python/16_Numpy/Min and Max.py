# Problem Link: https://www.hackerrank.com/challenges/np-min-and-max/problem
# --------------------------------------------------------------------------


import numpy
A = []
n, m = map(int, input().split())
for i in range(n):
    a = list(map(int, input().split()))
    A.append(a)
A = numpy.reshape(A, (n, m))
min_1 = numpy.min(A, axis = 1)
ans = numpy.max(min_1)
print(ans)