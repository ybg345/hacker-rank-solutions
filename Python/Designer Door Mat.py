# Problem Link: https://www.hackerrank.com/challenges/designer-door-mat/problem
# -----------------------------------------------------------------------------


import math
n, m = map(int,input().split()) #taking input

string = '.|.'              #Pattern to print in loop
f = math.floor(n/2)         #taking floor value since we loop through floor value in both the loop

# Printing UPPER pattern above 'WELCOME'
for i in range(1, f+1):
    print((string*(2*i-1)).center(m, '-'))

#Pring only 'WELCOME' with pattern
print('WELCOME'.center(m,'-'))

# Printing LOWER pattern above 'WELCOME'
for i in range(1, f+1):
    print((string*(n-2*i)).center(m, '-'))