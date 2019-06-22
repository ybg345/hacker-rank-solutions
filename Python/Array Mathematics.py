# Problem Link: https://www.hackerrank.com/challenges/np-array-mathematics/problem
# --------------------------------------------------------------------------------


import numpy
n, m = map(int, input().split())
A = []
B = []
for i in range(n):
    a = list(map(int, input().split()))
    A.append(a)
for i in range(n):
    b = list(map(int, input().split()))
    B.append(b)

A = numpy.reshape(A, (n,m))
B = numpy.reshape(B, (n,m))
print((A+B))
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)