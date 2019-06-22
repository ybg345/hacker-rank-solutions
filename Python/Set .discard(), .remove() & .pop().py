# Problem Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# -------------------------------------------------------------------------------------


n = int(input())
s = set(map(int, input().split()))
command_no = int(input())

for i in range(command_no):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    if command[0] == 'remove':
        try:
            s.remove(int(command[1]))
        except KeyError:
            pass 
    if command[0] == 'discard':
        s.discard(int(command[1]))

ans = sum(s)
print(ans)