#!usr/bin/env python


# User Information

lastName = input("Enter your Last Name: ")

firstName = input("Enter your First Name: ")

middleInitial = input("Enter your Middle Name: ")[:1]

# Message



msg = "                                              [PLEASE READ CAREFULLY]" + " " + lastName.upper() + ", " + firstName.capitalize() + " " + middleInitial.capitalize() + "." +  """
                             Enter your data according on your pre-grade results to double check the grades assessment. 
                     Please thoroughly input your grades to prevent error or confusion.
                                                                                                              Management
"""



print(msg)



# Quiz 30%

quiz_1 = float(input("Enter your score in Quiz 1: "))
quiz_2 = float(input("Enter your score in Quiz 2: "))
quiz_3 = float(input("Enter your score in Quiz 3: "))
print("------------------------------------------------")
quiz_grade = ((quiz_1 + quiz_2 + quiz_3) / 3) * 0.300
print("Grade in Quiz: ", round(quiz_grade, 2))
print("------------------------------------------------")

# Project 30%

project_1 = float(input("Enter your grade in Project 1: "))
project_2 = float(input("Enter your grade in Project 2: "))
project_3 = float(input("Enter your grade in Project 3: "))
print("------------------------------------------------")
project_grade = ((project_1 + project_2 + project_3) / 3) * 0.300
print("Grade in Project: ", round(project_grade, 2))
print("------------------------------------------------")



# Final Grade 10%

finalExam = float(input("Enter your grade in Final Exam: "))
print("------------------------------------------------")
finalGrade = finalExam * 0.100
print("Final Exam: ", round(finalGrade, 2))
print("------------------------------------------------")


# Assignment 10%

assignment = float(input("Enter your grade in Assignment: "))
print("------------------------------------------------")
assignmentGrade = assignment * 0.100
print("Assignment Grade: ", round(assignmentGrade, 2))
print("------------------------------------------------")

# Evaluation

results = (finalGrade + assignmentGrade + project_grade + quiz_grade) / 4
print("Total Grade: ", round(results, 2))


# Assesment

print("------------------------------------------------")
if results == 8:
    print("Final Grade: 1.0",  "REMARKS: Passed")
elif results > 8:
    print("Final Grade: 1.0", "REMARKS: Passed")
elif results == 7.50:
    print("Final Grade: 1.50", "REMARKS: Passed") 
elif results == 7.25:
    print("Final Grade: 1.25", "REMARKS: Passed")       
elif results > 6:
    print("Final Grade: 2.0 ", "REMARKS: Passed")
elif results > 5:
    print("Final Grade: 3.0", "REMARKS: Passed")
elif results < 4:
    print("Final Grade: 5", "REMARKS: Failed")
 
