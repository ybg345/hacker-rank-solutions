# Problem Link: https://www.hackerrank.com/challenges/symmetric-difference/problem
# --------------------------------------------------------------------------------


a = int(input())
m = set(map(int, input().split()))
b = int(input())
n = set(map(int, input().split()))

c = m.difference(n)
d = n.difference(m)
e = c.union(d)
print(*sorted(e), sep='\n')