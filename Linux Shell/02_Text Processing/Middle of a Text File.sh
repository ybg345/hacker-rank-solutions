# Problem Link: https://www.hackerrank.com/challenges/text-processing-in-linux---the-middle-of-a-text-file/problem
# ----------------------------------------------------------------------------------------------------------------


head -n 22 | tail -n 11
# First it will grab the first 22 lines. Then from these 22 lines it will perform tail operation.



# This solution is also good:
# cut -d$'\n' -f12-22