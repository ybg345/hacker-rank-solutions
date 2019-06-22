# Problem Link: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
# ------------------------------------------------------------------------------------


import numpy as np
n, m = map(int, input().split())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
np_arr = np.array(arr)
print(np.transpose(np_arr))
print(np_arr.flatten())