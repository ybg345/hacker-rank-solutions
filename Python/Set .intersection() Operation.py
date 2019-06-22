# Problem Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# -----------------------------------------------------------------------------------------


n1 = int(input())
English = set(map(int, input().split()))

n2 = int(input())
French = set(map(int, input().split()))

union_set = English.intersection(French)

print(len(union_set))