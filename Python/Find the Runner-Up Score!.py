# Problem Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# ------------------------------------------------------------------------------------------------


n = int(input())
arr = list(map(int, input().split()))
m = max(arr)

while(max(arr)==m):
    arr.remove(max(arr))
print(max(arr))