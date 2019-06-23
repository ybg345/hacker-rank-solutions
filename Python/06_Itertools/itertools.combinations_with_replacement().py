# Problem Link: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
# ---------------------------------------------------------------------------------------------------


from itertools import combinations_with_replacement
u_input = list(map(str, input().split()))
s = sorted(u_input[0])
n = int(u_input[1])

p = list(combinations_with_replacement(s, n))
for i in p:
    print(*i, sep='')