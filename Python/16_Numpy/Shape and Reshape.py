# Problem Link: https://www.hackerrank.com/challenges/np-shape-reshape/problem
# ----------------------------------------------------------------------------


import numpy as np
np_arr = np.array(list(map(int, input().split())))
converted_array = np.reshape(np_arr, (3, 3))
print(converted_array)