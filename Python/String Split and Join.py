# Problem Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# ----------------------------------------------------------------------------------------


def split_and_join(line):
    a = line
    a = a.split(" ")
    
    a = "-".join(a)
    return a