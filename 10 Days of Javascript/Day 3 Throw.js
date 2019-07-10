/*

Problem Link: https://www.hackerrank.com/challenges/js10-throw/problem
----------------------------------------------------------------------

*/


// Solution: 
function isPositive(a) {
    if (a > 0) {
        return "YES";
    }

    else if (a == 0) {
        throw new Error("Zero Error");
    }
    
    else if (a < 0) {
        throw new Error("Negative Error");
    }
}
