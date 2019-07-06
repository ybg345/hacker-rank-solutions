// https://www.hackerrank.com/challenges/hello-world-c/problem
// -----------------------------------------------------------


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
	
    char s[100];
    scanf("%[^\n]%*c", &s);
  	
    printf("Hello, World!");
    printf("\n");
    printf("Welcome to C programming.");    
    return 0;
}