# Problem Link: https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-2/problem
# -------------------------------------------------------------------------------------------------------


uniq -c | tr -s " " | cut -c2-

#  tr -s " " will replace the leading spaces into one space, then 
# "cut -c2-" will cut from the next space to the end. 