# Problem Link: https://www.hackerrank.com/challenges/np-concatenate/problem
# --------------------------------------------------------------------------


import numpy as np
n, m, p = map(int, input().split())
arr_1 = []
arr_2 = []

for i in range(n):
    a = list(map(int, input().split()))
    arr_1.append(a)
for j in range(m):
    b = list(map(int, input().split()))
    arr_2.append(b)

np_arr1 = np.reshape(arr_1, (n, p))
np_arr2 = np.reshape(arr_2, (m, p))
print(np.concatenate((np_arr1, np_arr2), axis = 0))