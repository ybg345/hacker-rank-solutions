/*

Problem Link: https://www.hackerrank.com/challenges/js10-objects/problem
------------------------------------------------------------------------

*/


// Solution: 

function Rectangle(a, b) {
    this.length = a;
    this.width = b;

    this.perimeter = 2 * (this.length + this.width);
    this.area = this.length * this.width;
}