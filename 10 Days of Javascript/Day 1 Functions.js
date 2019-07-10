/*

Problem Link: https://www.hackerrank.com/challenges/js10-function/problem
-------------------------------------------------------------------------

*/


// Solution: 
function factorial(n) {
    if (n > 1) {
        return n * factorial(n - 1);
    }

    return 1;   //Returns 1 if n <= 1
}





/*
    By default, functions return the value undefined; to return any other value, the function must have a return statement that consists of the return keyword followed by the value to be returned (this can be a literal value, a variable, or even a call to a function).

# Unnamed Function Expression:
    The main difference between a function expression and a function statement is the function name, which can be omitted from a function expression to create an anonymous function. Function expressions are often used as Immediately Invoked Function Expressions (IIFEs), which run as soon as they're defined.
        var square = function(x) {
            return x * x;
        };

# Named Function Expression:
    See Example from: https://www.hackerrank.com/challenges/js10-function/topics

# Recursion:
    This is an extremely important algorithmic concept that involves splitting a problem into two parts: a base case and a recursive case. The problem is divided into smaller subproblems which are then solved recursively until such time as they are small enough and meet some base case; once the base case is met, the solutions for each subproblem are combined and their result is the answer to the entire problem.

    It's important to note that any task that can be accomplished recursively can also be performed iteratively (i.e., through a sequence of repeatable steps).

    Typically, we use recursion when each recursive call significantly reduces the size of the problem (e.g., if we can halve the dataset during each recursive call).

*/