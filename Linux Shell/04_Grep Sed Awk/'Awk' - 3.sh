# Problem Link: https://www.hackerrank.com/challenges/awk-3/problem
# -----------------------------------------------------------------


# Awk If Else If ladder Syntax:
    # if(conditional-expression1)
    #     action1;
    # else if(conditional-expression2)
    #     action2;
    # else if(conditional-expression3)
    #     action3;
    #     .
    #     .
    # else
    #     action n;

awk '{
    total = $2 + $3 + $4;
    avg = total/3;

    if (avg >= 80)
        print $1, $2, $3, $4, ":", "A";
    else if (avg >= 60 && avg < 80)
        print $1, $2, $3, $4, ":", "B";
    else if (avg >= 50 && avg < 60)
        print $1, $2, $3, $4, ":", "C";
    else
        print $1, $2, $3, $4, ":", "FAIL";
}' 