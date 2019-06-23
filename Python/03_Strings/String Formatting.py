# Problem Link: https://www.hackerrank.com/challenges/python-string-formatting/problem
# ------------------------------------------------------------------------------------


def print_formatted(number):
    for i in range(1, number+1):
        width = len(bin(number)[2:])
        d = i
        o = oct(i)[2:]
        h = hex(i)[2:].upper()
        b = bin(i)[2:]
        print('{} {} {} {}'.format(str(d).rjust(width, ' '), str(o).rjust(width, ' '), str(h).rjust(width, ' '), str(b).rjust(width, ' ')))
