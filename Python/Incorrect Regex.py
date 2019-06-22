# Problem Link: https://www.hackerrank.com/challenges/incorrect-regex/problem
# ---------------------------------------------------------------------------


import re
n = int(input())

for i in range(n):
    regex = input()
    try:
        x = re.compile(regex)
        print(bool(x))
    except:
        print('False')