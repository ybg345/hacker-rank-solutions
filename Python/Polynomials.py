# Problem Link: https://www.hackerrank.com/challenges/np-polynomials/problem
# --------------------------------------------------------------------------


import numpy as np

Polynomial = list(map(float, input().split()))
value_at = float(input())
print(np.polyval(Polynomial, value_at))