/*

Problem Link: https://www.hackerrank.com/challenges/js10-loops/problem
----------------------------------------------------------------------

*/


// Solution: 
/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
var i;

function vowelsAndConsonants(s) {
    for (i = 0; i < s.length; i++) {
        if (s[i] == "a" || s[i] == "e" || s[i] == "i" || s[i] == "o" || s[i] == "u") {
            console.log(s[i]);
        }
    }

    for (i = 0; i < s.length; i++) {
        if (s[i] == "b" || s[i] == "c" || s[i] == "d" || s[i] == "f" || s[i] == "g" || s[i] == "h" || s[i] == "j" || s[i] == "k" || s[i] == "l" || s[i] == "m" || s[i] == "n" || s[i] == "p" || s[i] == "q" || s[i] == "r" || s[i] == "s" || s[i] == "t" || s[i] == "v" || s[i] == "w" || s[i] == "x" || s[i] == "y" || s[i] == "z") {
            console.log(s[i]);
        }
    }
}

