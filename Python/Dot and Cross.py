# Problem Link: https://www.hackerrank.com/challenges/np-dot-and-cross/problem
# ----------------------------------------------------------------------------


import numpy as np
n = int(input())
a = []
b = []
for i in range(n):
    arr = list(map(int, input().split()))
    a.append(arr)
for i in range(n):
    arr = list(map(int, input().split()))
    b.append(arr)

A = np.array(a)
B = np.array(b)
print(np.dot(A, B))