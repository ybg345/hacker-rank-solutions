/*

Problem Link: https://www.hackerrank.com/challenges/js10-arrays/problem
-----------------------------------------------------------------------

*/


// Solution: 

function getSecondLargest(nums) {
    // Sort in ascending lexicographical order using a compare function
    // for compare arrow function it would be, nums.sort((x, y) => x > y);
    var sorted_nums = nums.sort(function (x, y) { return x > y; });
    var last = sorted_nums[sorted_nums.length - 1];     //last element of sorted array. 
  
    for (let i of sorted_nums) {
        while (sorted_nums[i] == last) {
            sorted_nums.pop();    // removing last element from array as long as it equals to current maximum.
        }
    }

    return sorted_nums[sorted_nums.length - 1];   //returning the current maximum element after removing previous maximum.
}
