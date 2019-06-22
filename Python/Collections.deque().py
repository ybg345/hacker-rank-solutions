# Problem Link: https://www.hackerrank.com/challenges/py-collections-deque/problem
# --------------------------------------------------------------------------------


from collections import deque
n = int(input())
d = deque()
for i in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'append':
        d.append(command[1])
    if command[0] == 'appendleft':
        d.appendleft(command[1])
    if command[0] == 'pop':
        d.pop()
    if command[0] == 'popleft':
        d.popleft()
print(*d, sep=' ')