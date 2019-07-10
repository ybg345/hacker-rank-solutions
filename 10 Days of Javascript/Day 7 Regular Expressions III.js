/*

Problem Link: https://www.hackerrank.com/challenges/js10-regexp-3/problem
-------------------------------------------------------------------------

*/


// Solution: 
function regexVar() {
    var re;
    re = /[0-9]+/g;

    return re;
}



/* 
My comments:
-----------
- I am using flag 'g' which denotes 'global flag'. 
- For searching using global flag:
    - 102, 1948948 will give output as:      [102, 1948948]
    - 1948948 and 1.3 will give output as:   [1948948, 1, 3]
    - 1.3 will give output as:               [1, 3]

- General Syntax (for Regex with Flag) is: /regex_pattern/flags

*/