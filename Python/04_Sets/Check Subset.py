# Problem Link: https://www.hackerrank.com/challenges/py-check-subset/problem
# ---------------------------------------------------------------------------


n = int(input())

for i in range(n):
    nsa = int(input())
    a = set(map(int, input().split()))
    
    nsb = int(input())
    b = set(map(int, input().split()))
    
    if a.issubset(b):
        print('True')
    else:
        print('False')