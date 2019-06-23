# Problem Link: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
# -------------------------------------------------------------------------------


import numpy as np
n, m = map(int, input().split())

array = []
for i in range(m):
    arr = list(map(int, input().split()))
    array.append(arr)

my_array = np.array(array)
np.set_printoptions(legacy='1.13')
print(np.mean(my_array, axis = 1))
print(np.var(my_array, axis = 0))
print(np.std(my_array))
