# Problem Link: https://www.hackerrank.com/challenges/30-interfaces/problem
# -------------------------------------------------------------------------


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        self.DivSum = 0
        for i in range(1, n+1):
            if n % i == 0:
                self.DivSum += i   
        return self.DivSum