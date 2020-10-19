#usr/bin/env python

# User Data

lastName = input("Enter your Last Name: ")
firstName = input("Enter your First Name: ")
middleInitial = input("Enter your Middle Name: ")[:1] 

print("---------------------------------------------------------------------------------------------------------------------------------------")


# Message

msg = "[PLEASE READ CAREFULLY]" + " " + lastName.upper() + ", " + firstName.capitalize() + " " + middleInitial.capitalize() + "." +  """
                     Enter your scores according to your assesment results. Please thoroughly
        input your data to prevent error or confusion.

                                                                                                              Management
"""
print(msg)
print("---------------------------------------------------------------------------------------------------------------------------------------")


# Assignmnet 10%
assignment = float(input("Enter your score in Assignment: "))
assignment_ev = assignment * .100
print("Assignmnet Grade: ", assignment_ev)

print("---------------------------------------------------------------------------------------------------------------------------------------")

# Attendance 10%
attendance = float(input("Enter the number of days you are present: "))
attendance_ev = attendance * .100
print("Attendance Grade: ", attendance_ev)

print("---------------------------------------------------------------------------------------------------------------------------------------")

# Long Quiz 20%
longQuiz = float(input("Enter your score in Long Quiz: "))
longQuiz_ev = longQuiz * .200
print("Long Quiz Grade: ", longQuiz)

print("---------------------------------------------------------------------------------------------------------------------------------------")

# Short Quiz 15%
shortQuiz = float(input("Enter you Short Quiz Grade: "))
shortQuiz_ev = shortQuiz * .150
print("Short Quiz Grade: ", shortQuiz)

print("---------------------------------------------------------------------------------------------------------------------------------------")

# Major Exam 30%
majorExam = float(input("Enter your Major Exam score: "))
majorExam_ev = majorExam * .300
print("Major Exam Grade: ", majorExam)

print("---------------------------------------------------------------------------------------------------------------------------------------")

# Assesment

finalGrade = (assignment_ev + attendance_ev + shortQuiz_ev + longQuiz_ev + majorExam_ev)

# Grade Evaluation

if finalGrade > 100:
    print("Final Grade: ", round(finalGrade, 0), "REMARKS: Very Good" )
elif finalGrade == 100:
    print("Final Grade: ", round(finalGrade, 0), "REMARKS: Very Good")
elif finalGrade > 80:
    print("Final Grade: ", round(finalGrade, 0), "REMARKS: Good")
elif finalGrade == 89:
    print("Final Grade: ", round(finalGrade, 0), "REMARKS: Good")
elif finalGrade == 69:
    print("Final Grade: ", round(finalGrade, 0), "REMARKS: Poor")
elif finalGrade > 60:
    print("Final Grade: ", round(finalGrade, 0), "REMARKS: Poor")
elif finalGrade < 60:
    print("Final Grade: ", round(finalGrade, 0), "REMARKS: Needs Improvement")
