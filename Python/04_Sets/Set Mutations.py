# Problem Link: https://www.hackerrank.com/challenges/py-set-mutations/problem
# ----------------------------------------------------------------------------


na = int(input())
A = set(map(int, input().split()))
no_test_set = int(input())

for i in range(no_test_set):
    operation = list(map(str, input().split()))
    B = set(map(int, input().split()))

    if operation[0] == 'intersection_update':
        A.intersection_update(B)
    if operation[0] == 'update':
        A.update(B)
    if operation[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    if operation[0] == 'difference_update':
        A.difference_update(B)
print(sum(A))