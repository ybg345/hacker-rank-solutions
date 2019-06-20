# Problem Link: https://www.hackerrank.com/challenges/s10-weighted-mean/problem
# -----------------------------------------------------------------------------


n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))
weighted_mean = 0

for i in range(n):
    weighted_mean += (x[i] * w[i])/sum(w)
print(round(weighted_mean,1))