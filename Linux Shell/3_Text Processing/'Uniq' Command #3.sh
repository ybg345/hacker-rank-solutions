# Problem Link: https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-3/problem
# -------------------------------------------------------------------------------------------------------


uniq -c -i | tr -s " " | cut -c2-


# Some tips:
    # - avoid comparing first N characters (using the -s option) 
    # - ignore variations in case between lines (the -i option) 
    # - avoid comparing the first N fields using the -f option. 
