# Problem Link: https://www.hackerrank.com/challenges/zipped/problem
# ------------------------------------------------------------------


st_number, subject = map(int, input().split())
number = []

for i in range(subject):
    number.append(map(float, input().split()))
for j in zip(*number):
    print(sum(j)/subject)