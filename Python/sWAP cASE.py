# Problem Link: https://www.hackerrank.com/challenges/swap-case/problem
# ---------------------------------------------------------------------


def swap_case(s):
    strs = s
    new = ""
    for i in strs:
        if i.isupper():
            new += i.lower()
        else:
            new += i.upper()
    return new