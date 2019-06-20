# Problem Link: https://www.hackerrank.com/challenges/s10-standard-deviation/problem
# ----------------------------------------------------------------------------------


n = int(input())
numbers = list(map(int,input().split()))

mean = sum(numbers)/n
x = []

for i in numbers:
    d = (i - mean) * (i - mean)
    x.append(d)
# print(sum(x))
s = sum(x)
sd = (s/n) ** (1/2)
print(round(sd,1))