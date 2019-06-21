# Problem Link: https://www.hackerrank.com/challenges/30-inheritance/problem
# --------------------------------------------------------------------------


class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
    # we can write super().__init__ instead of using superclass name. 
        self.scores = scores

    def calculate(self):
        average = sum(self.scores) / len(self.scores)

        if average >= 90:
            return 'O'
        elif average >= 80 and average < 90:
            return 'E'
        elif average >= 70 and average < 80:
            return 'A'
        elif average >= 55 and average < 70:
            return 'P'
        elif average >= 40 and average < 55:
            return 'D'
        else:
            return 'T'
    

