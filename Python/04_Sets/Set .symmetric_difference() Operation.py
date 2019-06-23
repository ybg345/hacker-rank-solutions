# Problem Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# -------------------------------------------------------------------------------------------------


n1 = int(input())
English = set(map(int, input().split()))

n2 = int(input())
French = set(map(int, input().split()))

symmetric_difference_set = English.symmetric_difference(French)

print(len(symmetric_difference_set))