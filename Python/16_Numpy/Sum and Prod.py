# Problem Link: https://www.hackerrank.com/challenges/np-sum-and-prod/problem
# ---------------------------------------------------------------------------


import numpy
n, m = map(int, input().split())
A = []
for i in range(n):
    a = list(map(int, input().split()))
    A.append(a)
A = numpy.reshape(A, (n, m))
s = numpy.sum(A, axis = 0)
print(numpy.prod(s))