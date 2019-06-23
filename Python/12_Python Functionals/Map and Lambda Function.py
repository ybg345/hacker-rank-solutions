# Problem Link: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
# -------------------------------------------------------------------------------------


cube = lambda x: x**3

def fibonacci(n):
    f0 = 0
    f1 = 1
    fibo = [f0, f1]
    for i in range(2, n):
        s = f0 + f1
        f0 = f1
        f1 = s
        fibo.append(s)
    return fibo[0:n]




#Another Solution:
#-----------------

cube = lambda x: x**3

def fibonacci(n):
    f0 = 0
    f1 = 1
    fibo = [f0, f1]
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    for i in range(2, n):
        s = f0 + f1
        f0 = f1
        f1 = s
        fibo.append(s)
    return fibo
