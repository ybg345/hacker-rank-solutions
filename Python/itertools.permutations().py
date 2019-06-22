# Problem Link: https://www.hackerrank.com/challenges/itertools-permutations/problem
# ----------------------------------------------------------------------------------


from itertools import permutations

u_input = list(map(str, input().split()))
s = sorted(u_input[0])
n = int(u_input[1])

p = list(permutations(s, n))
for i in p:
    print(*i, sep='')