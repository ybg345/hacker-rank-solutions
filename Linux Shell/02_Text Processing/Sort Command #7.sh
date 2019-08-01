# Problem Link: https://www.hackerrank.com/challenges/text-processing-sort-7/problem
# ------------------------------------------------------------------------------------


sort -t'|' -k2 -n -r

#  The -t option helps specify the delimiting character depending on the file format.
#     -t $'\t' for a tab delimited file    
#     -t',' for a comma delimited file    
#     -t'|' for a pipe delimited file