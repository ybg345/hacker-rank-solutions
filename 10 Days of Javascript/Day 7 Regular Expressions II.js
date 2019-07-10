/*

Problem Link: https://www.hackerrank.com/challenges/js10-regexp-2/problem
-------------------------------------------------------------------------

*/


// Solution: 
function regexVar() {
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts with 'Mr.', 'Mrs.', 'Ms.', 'Dr.', or 'Er.', 
     * followed by one or more letters.
     */
    var re;
    re = /^(Mr|Mrs|Ms|Dr|Er)\.[A-Za-z]+$/;
    
    
    return re;
}