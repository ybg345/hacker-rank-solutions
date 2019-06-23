# Problem Link: https://www.hackerrank.com/challenges/collections-counter/problem
# -------------------------------------------------------------------------------


from collections import Counter

n_shoes = int(input())
sample_size = Counter(map(int, input().split()))
n_customers = int(input())

money_earned = 0
for i in range(n_customers): 
    size, price = map(int, input().split())
    if sample_size[size]:
        money_earned += price
        sample_size[size] -=1
print(money_earned)