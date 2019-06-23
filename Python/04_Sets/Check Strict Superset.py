# Problem Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# -----------------------------------------------------------------------------------


a = set(map(int, input().split()))
n = int(input())
lis = []
for i in range(n):
    b = set(map(int, input().split()))
    lis.append(list(b))

result = True
# Result will stay True, unless we find a set to whom A is not a superset.
for i in lis:
    if not a.issuperset(i):
        result = False
print(result)
