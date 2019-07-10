/*

Problem Link: https://www.hackerrank.com/challenges/js10-regexp-1/problem
-------------------------------------------------------------------------

*/


// Solution: 
function regexVar() {
    var re;
    re = /^([aeiou])[a-z]+\1$/;

    return re;
}


// Enclosing '[aeiou]' within parenthesis i.e. like ([aeiou]) means we are creating a group. 

/*

We can refer a group by calling it's position number. We have only one group in the regular expression. So we can refer the group by \1.

i.e. '\1' refers to - what was matched in the first set of parentheses i.e. the first group.

For example, 
If our regular expression is like this - /^([aeiou])[a-z]([0-9])+\1$/, then
- ([aeiou]) creates the first group and we can access it by \1.
- ([0-9]) creates the second group and we can access it byy \2.

*/


