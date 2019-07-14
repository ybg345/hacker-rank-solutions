/* 
	https://www.hackerrank.com/challenges/recursion-in-c/problem
	------------------------------------------------------------
*/


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.

int find_nth_term(int n, int a, int b, int c) {
  if (n==1) return a;
  if (n==2) return b;
  if (n==3) return c;

  if (n==4) return a + b + c;

  return find_nth_term(n-1, n-2, n-3, n-4);
  
}

int main() {
    int n, a, b, c;
  
    scanf("%d %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);
 
    printf("%d", ans); 
    return 0;
}
