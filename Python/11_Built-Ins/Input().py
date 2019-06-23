# Problem Link: https://www.hackerrank.com/challenges/input/problem
# -----------------------------------------------------------------


# x, k = map(int, input().split())
# p = input()
# if lambda x: p == k:
#     print('True')
# else:
#     print('False')

x, k = map(int, input().split())
p = eval(input())
if p == k:
    print('True')
else:
    print('False')

# The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.