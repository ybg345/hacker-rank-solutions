# Problem Link: https://www.hackerrank.com/challenges/awk-2/problem
# -----------------------------------------------------------------


# Basic Syntax: 
# awk '/search pattern1/ {Actions}

# if-else syntax:
    # Syntax:
    # if (conditional-expression)
    #     action1
    # else
    #     action2


awk '{ 
    if($2 >= 50 && $3 >= 50 && $4 >= 50) 
        print $1 " : " "Pass";
    else
        print $1 " : " "Fail";
    }'