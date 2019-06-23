# Problem Link: https://www.hackerrank.com/challenges/exceptions/problem
# ----------------------------------------------------------------------


n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as z:
        print("Error Code:",z)
    except ValueError as v:
        print("Error Code:",v)