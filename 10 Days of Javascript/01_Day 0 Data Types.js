/*

Problem Link: https://www.hackerrank.com/challenges/js10-data-types/problem
---------------------------------------------------------------------------

*/


// Solution: 
function performOperation(secondInteger, secondDecimal, secondString) {

    const firstInteger = 4;
    const firstDecimal = 4.0;
    const firstString = 'HackerRank ';

    
    console.log(firstInteger + parseInt(secondInteger));
    console.log(firstDecimal + parseFloat(secondDecimal));
    console.log(firstString + secondString);
}