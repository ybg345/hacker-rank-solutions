# Problem Link: https://www.hackerrank.com/challenges/python-tuples/problem
# --------------------------------------------------------------------------


n = int(input())
integer_list = map(int, input().split())
z = tuple(integer_list)
x = hash(z)
print(x)