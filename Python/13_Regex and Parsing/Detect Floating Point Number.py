# Problem Link: https://www.hackerrank.com/challenges/introduction-to-regex/problem
# ---------------------------------------------------------------------------------


import re
n = int(input())
for i in range(n):
    s = input()
    print(bool(re.search(r"^[+-]?[0-9]*\.[0-9]+$",s)))

# 4.0O0
# -1.00
# +4.54

# ? - Matches 0 or 1 occurrence of preceding expression.
# * - Matches 0 or more occurrences of preceding expression.
# + - Matches 1 or more occurrence of preceding expression.