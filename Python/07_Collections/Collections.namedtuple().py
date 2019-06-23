# Problem Link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# -------------------------------------------------------------------------------------


from collections import namedtuple
n = int(input())
fields = input().split()

total = 0
for i in range(n):
    students = namedtuple('students', fields)
    fields_input_row_wise = input().split()
    x = students(*fields_input_row_wise)
    total += float(x.MARKS)
print('{:.2f}'.format(total/n))

# 5
# ID         MARKS      NAME       CLASS     
# 1          97         Raymond    7         
# 2          50         Steven     4         
# 3          91         Adrian     9         
# 4          72         Stewart    5         
# 5          80         Peter      6  