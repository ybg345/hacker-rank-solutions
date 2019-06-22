# Problem Link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# --------------------------------------------------------------------------------


from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())

for i in range(1,n+1):
    d[input()].append(str(i))
#print(d) --> defaultdict(<class 'list'>, {'a': [1, 2, 4], 'b': [3, 5]})

word_list2 = list()  # empty list
for i in range(m):
    word_list2.append(input())
# word_list2 = ['a', 'b']   

for i in word_list2:    
    if i in d:
        print(*d[i])
    else:
        print(-1)