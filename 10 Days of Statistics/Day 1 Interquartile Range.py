# Problem Link: https://www.hackerrank.com/challenges/s10-interquartile-range/problem
# -----------------------------------------------------------------------------------


import statistics as st
n = int(input())
x = list(map(int, input().split()))
f = list(map(int, input().split()))

S= []
for i in range(n):
    S.extend([x[i]]*f[i])
S = sorted(S)

n = len(S)
n2 = int(n/2)

Q3 = st.median(S[-n2:])
Q1 = st.median(S[:n2])
IQR = float(Q3 - Q1)

print(round(IQR, 1))