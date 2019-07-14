/*

Problem Link: https://www.hackerrank.com/challenges/js10-arrows/problem
-----------------------------------------------------------------------

*/


// Solution: 
/*
 * Modify and return the array so that all even elements are doubled and all odd elements are tripled.
 * 
 * Parameter(s):
 * nums: An array of numbers.
 */

function modifyArray(nums) {
    const newNums = nums.map(s => (s%2==0) ? s*2 : s*3)
    return newNums;
}