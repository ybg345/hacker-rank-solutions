# Problem Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
# -----------------------------------------------------------------------------------


def average(array):
    ans = sum(set(array))/ len(set(array))
    return ans 