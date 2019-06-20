# Problem Link: https://www.hackerrank.com/challenges/s10-quartiles/problem
# -------------------------------------------------------------------------


n= int(input())
x = sorted(map(int, input().split(' ')))

def median(x):
    if len(x) % 2 != 0:
        return x[len(x)//2]
    else:
        return (x[len(x)//2] + x[len(x)//2 - 1]) / 2

Q1 = median(x[:len(x)//2])
Q2 = median(x)
Q3 = median(x[-(len(x) // 2):])

print(int(Q1), int(Q2), int(Q3), sep='\n')