# Problem Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem
# --------------------------------------------------------------------------------


k = int(input())
room_number = list(map(int, input().split()))

from collections import Counter
count = Counter(room_number)

for k, v in count.items():
    if v == 1:
        print(k)