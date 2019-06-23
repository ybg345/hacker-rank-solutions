# Problem Link: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
# ----------------------------------------------------------------------------------


import re

m = re.findall(r'(?i)(?<=[^aeiou])[aeiou]{2,}(?=[^aeiou])', input())

if len(m) > 0:
    print(*m, sep = '\n')
else:
    print('-1')

    
# (?i) is for making case insensitive


#  Lookbehind:     
    # (?<=[expression])[pattern]  #positive lookbehind
    # (?<![expression])[pattern]  #negative lookbehind
    


# (?=...) -> It is called lookahead assertion
# eg. 
# Matches if ... matches next, but doesn’t consume any of the string. 
# This is called a lookahead assertion. For example, Isaac (?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.



# (?<=...) -> It is called Positive Lookbehind
# eg.
# Matches if the current position in the string is preceded by a match for ... that ends at the current position. 
# This is called a positive lookbehind assertion. (?<=abc)def will find a match in abcdef, 
# since the lookbehind will back up 3 characters and check if the contained pattern matches.


# References:
#     https://www.hackerrank.com/challenges/re-findall-re-finditer/forum/comments/88272