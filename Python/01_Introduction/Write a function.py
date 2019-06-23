# Problem Link: https://www.hackerrank.com/challenges/write-a-function/problem
# ----------------------------------------------------------------------------


def is_leap(year):
    leap = False
    if year in range(1900, 10**5+1):
        if (year % 4 == 0) and (year % 100 !=0) or (year % 400 == 0):
            leap = True 
        else: 
            leap = False 
    
    return leap