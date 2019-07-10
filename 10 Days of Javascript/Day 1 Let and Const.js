/*

Problem Link: https://www.hackerrank.com/challenges/js10-let-and-const/problem
------------------------------------------------------------------------------

*/


// Solution: 
/*
Variable Declaration Keywords:
------------------------------
# var: (Global or Local Scope)
We use the var keyword to declare variables. The scope of a variable declared using this keyword is within the context wherever it was declared. 

For variables declared outside any function, this means they are globally available throughout the program. For variables declared within a function, this means they are only available within the function itself.

# let: (Local Scope)
We use the let keyword to declare variables that are limited in scope to the block, statement, or expression in which they are used.

# const: (only read-only, cann't reassign it)
We use the const keyword to create a read-only reference to a value, meaning the value referenced by this variable cannot be reassigned.

*/


function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    const PI = Math.PI;
    let r;
    r = readLine();
    let area, perimeter;
    // Print the area of the circle:
    area = PI * r ** 2;
    console.log(area);
    // Print the perimeter of the circle:
    perimeter = 2 * PI * r;
    console.log(perimeter);
}