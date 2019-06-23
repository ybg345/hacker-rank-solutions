# Problem Link: https://www.hackerrank.com/challenges/np-linear-algebra/problem
# ----------------------------------------------------------------------------


import numpy as np

n = int(input())
arr = []

for i in range(n):
    a = list(map(float, input().split()))
    arr.append(a)
    
np.set_printoptions(legacy='1.13')
print(np.linalg.det(arr))




#Another Solution:
#----------------

import numpy as np
np.set_printoptions(legacy='1.13')
n = int(input())
arr = []

for i in range(n):
    a = list(map(float, input().split()))
    arr.append(a)

A = np.array(arr)
print(np.linalg.det(A))