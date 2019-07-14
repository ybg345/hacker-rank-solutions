/*

Problem Link: https://www.hackerrank.com/challenges/js10-class/problem
----------------------------------------------------------------------

*/


// Solution: 

/*
 * Implement a Polygon class with the following properties:
 * 1. A constructor that takes an array of integer side lengths.
 * 2. A 'perimeter' method that returns the sum of the Polygon's side lengths.
 */

class Polygon {
    constructor(input_array) {
        this.first = input_array[0];
        this.second = input_array[1];
        this.third = input_array[2];
        this.fourth = input_array[3];
        this.fifth = input_array[4] || 0;  //setting default value to 0 if fifth side's length is not provided.  
    };
    
    perimeter() {
        return (this.first + this.second + this.third + this.fourth + this.fifth); 
    }
};