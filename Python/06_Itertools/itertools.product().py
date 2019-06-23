# Problem Link: https://www.hackerrank.com/challenges/itertools-product/problem
# -----------------------------------------------------------------------------


from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = list(product(a,b))
print(*c, sep=' ')     

# The star symbol is called a "splat" operator in python. 
# The way it works is separates each item in the tuple as individuals.

# sep=' ' is optional. If we want to seperate tuples something other than space, it that case it is necessary. 