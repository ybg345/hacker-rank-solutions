# Problem Link: https://www.hackerrank.com/challenges/no-idea/problem
# -------------------------------------------------------------------


i = input().split(" ")
n = int(i[0])
m = int(i[1])

l=input().split(' ')
A=set(input().split(' '))
B=set(input().split(' '))
happiness=0

for i in l:
    if i in A:
        happiness+=1
    if i in B:
        happiness-=1
print(happiness)




#Another Solution:
#----------------
n,m=map(int,input().split())
l=input().split(' ')
A=set(input().split(' '))
B=set(input().split(' '))
happiness=0
for i in l:
    if i in A:
        happiness+=1
    if i in B:
        happiness-=1
        
print(happiness)