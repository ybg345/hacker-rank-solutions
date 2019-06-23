# Problem Link: https://www.hackerrank.com/challenges/py-set-add/problem
# ----------------------------------------------------------------------


a = int(input())
country = set()
for i in range(a):
    name = input().strip()
    country.add(name)

print(len(country))