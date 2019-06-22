# Problem Link: https://www.hackerrank.com/challenges/capitalize/problem
# ----------------------------------------------------------------------


def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s
  

# Replace syntax:
#     string.replace(old, new)
# In this case: 
#     s.replace(old, old.capitalize())
