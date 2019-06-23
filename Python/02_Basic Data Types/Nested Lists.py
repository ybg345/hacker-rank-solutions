# Problem Link: https://www.hackerrank.com/challenges/nested-list/problem
# -----------------------------------------------------------------------


# Took help from "sheethalgowda191": https://www.hackerrank.com/challenges/nested-list/forum/comments/511889

if __name__ == '__main__':
    students = []
    n = int(input())
    for i in range(n): 
        name = input() 
        grade = float(input()) 
        students += [[name,grade]]       
      # Students nested list contains name and grade pair. 

#   Next three line will find second highest grade. 
    non_duplicate_grade = list(set([grade for name,grade in students]))
    non_duplicate_grade.sort()
    second_highest = non_duplicate_grade[1]
    
    for name, grade in sorted(students):
        if grade == second_highest:
            second_highest_names = name 
            print(*second_highest_names, sep='')