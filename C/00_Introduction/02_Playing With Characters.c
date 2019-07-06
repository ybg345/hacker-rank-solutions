// https://www.hackerrank.com/challenges/playing-with-characters/problem
// ---------------------------------------------------------------------


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch, s[100], c[100];

    scanf("%c", &ch);   
    scanf("%s", &s);
    scanf("\n");
    scanf("%[^\n]%*c", c);

    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", c);
}