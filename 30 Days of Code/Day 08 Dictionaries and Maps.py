# Problem Link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# ------------------------------------------------------------------------------------


n = int(input())
phoneBook = {}

for i in range(n):
    name, phoneNumber = input().split(' ')
    phoneBook[name] = phoneNumber
    
while(True):
    try:
        n = input().strip()
        if n in phoneBook:
            print('{}={}'.format(n, phoneBook[n]))
        else:
            print('Not found')
    
    except EOFError:
        break 