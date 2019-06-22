# Problem Link: https://www.hackerrank.com/challenges/re-start-re-end/problem
# ---------------------------------------------------------------------------


import re

s, k = input(), input()
i = 0
m = re.search(k, s)
if m:
    while m != None:
        print('({}, {})'.format(m.start() + i, m.end() + i - 1))
        i += m.start() + 1
        m = re.search(k, s[i:])
        
else:
    print("(-1, -1)")