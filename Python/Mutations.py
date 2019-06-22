# Problem Link: https://www.hackerrank.com/challenges/python-mutations/problem
# ----------------------------------------------------------------------------


def mutate_string(string, position, character):
    s = string
    p = position
    c = character
    l = list(s)
    l[p] = c
    l = "".join(l)
    return l