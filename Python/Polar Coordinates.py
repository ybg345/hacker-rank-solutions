# Problem Link: https://www.hackerrank.com/challenges/polar-coordinates/problem
# -----------------------------------------------------------------------------


import cmath

z = complex(input())
print(*cmath.polar(z), sep='\n')