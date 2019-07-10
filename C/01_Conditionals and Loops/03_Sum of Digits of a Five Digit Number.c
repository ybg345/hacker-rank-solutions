/* 
	https://www.hackerrank.com/challenges/sum-of-digits-of-a-five-digit-number/problem
	----------------------------------------------------------------------------------
*/


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);

    //Complete the code to calculate the sum of the five digits on n.
    int i, last_digit, sum = 0;
    for (i = 1; i<= 5; i++) {
        last_digit = n % 10;
        // printf("%d\n", last_digit);
        sum += last_digit;
        n = n / 10;
    }

    printf("%d", sum);
    return 0;
}