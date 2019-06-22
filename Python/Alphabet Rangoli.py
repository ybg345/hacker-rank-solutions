# Problem Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# ----------------------------------------------------------------------------


def print_rangoli(size):
    import string 
    myStr = string.ascii_lowercase[0:size]
    for i in range(size-1,-size,-1):
        x = abs(i)
        word = '-'.join(myStr[size-1: x: -1] + myStr[x: size])
        print ("--"*x + word + "--"*x)