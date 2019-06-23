# Problem Link: https://www.hackerrank.com/challenges/np-inner-and-outer/problem
# ------------------------------------------------------------------------------


import numpy as np
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = np.array(a)
B = np.array(b)

print(np.inner(A, B))
print(np.outer(A, B))