# Problem Link: https://www.hackerrank.com/challenges/30-review-loop/problem
# --------------------------------------------------------------------------


n = int(input())
for i in range(n):
    a = input()
    print(a[::2], a[1::2])
