# Problem Link: https://www.hackerrank.com/challenges/itertools-combinations/problem
# ----------------------------------------------------------------------------------


from itertools import combinations

u_input = list(map(str, input().split()))
s = sorted(u_input[0])
n = int(u_input[1])

for i in range(1, n+1):
    p = list(combinations(s, i))
    for j in p:
        print(*j, sep='')