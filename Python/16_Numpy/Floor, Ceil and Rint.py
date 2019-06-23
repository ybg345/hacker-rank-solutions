# Problem Link: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
# -------------------------------------------------------------------------------


import numpy
A = numpy.array(list(map(float, input().split())))
numpy.set_printoptions(sign=' ')
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))