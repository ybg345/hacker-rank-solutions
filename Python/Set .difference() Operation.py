# Problem Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# ---------------------------------------------------------------------------------------


n1 = int(input())
English = set(map(int, input().split()))

n2 = int(input())
French = set(map(int, input().split()))

union_set = English.difference(French)

print(len(union_set))