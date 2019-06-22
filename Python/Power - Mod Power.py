# Problem Link: https://www.hackerrank.com/challenges/python-power-mod-power/problem
# ----------------------------------------------------------------------------------


a = float(input())
b = float(input())
m = int(input())

p = int(pow(a,b))
pp = pow(int(a),int(b),m)
print(p)
print(pp)