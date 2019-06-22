# Problem Link: https://www.hackerrank.com/challenges/re-group-groups/problem
# ---------------------------------------------------------------------------


import re

S = input()
m = re.search(r'([a-zA-Z0-9])\1+', S)
try:
    print(m.group(1))
except:
    print('-1')
