# Problem Link: https://www.hackerrank.com/challenges/30-binary-numbers/problem
# -----------------------------------------------------------------------------


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    b = str(bin(n))[2:]
    sep = b.split('0')
    l = [len(i) for i in sep]
    ans = max(l)
    print(ans)
