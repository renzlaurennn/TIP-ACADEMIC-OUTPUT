#!usr/bin/env python


# Activity 2 Basic Programming Payroll_CPE12FA4 

# User Information

lastName = input("Enter your Last Name: ")
firstName = input("Enter your First Name: ")
middleInitial = input("Enter your Middle Name: ")[:1] 

print("---------------------------------------------------------------------------------------------------------------------------------------")


# Message

msg = "[PLEASE READ CAREFULLY]" + " " + lastName.upper() + ", " + firstName.capitalize() + " " + middleInitial.capitalize() + "." +  """
                     Enter your data according on the number of days of your work per week. Please thoroughly
        input your data to prevent error or confusion.
                                                                                                              Management
"""
print(msg)
print("---------------------------------------------------------------------------------------------------------------------------------------")

# Evaluation 

numberOfDays = int(input("Please enter days worked: "))
ratePerDay = 285.00


# Process

GrossPay = numberOfDays * ratePerDay
deduction = .100 * GrossPay
print("---------------------------------------------------------------------------------------------------------------------------------------")

# Limiting Integer

if int(numberOfDays) in (1, 2, 3, 4, 5, 6, 7):
    print ("                 ","Number of days of work per week:", numberOfDays)
else:
    print ("Invalid Option, you needed to type a 1, 2, 3, 4, 5, 6, 7")
    print("---------------------------------------------------------------------------------------------------------------------------------------")
    
# Display

print("                      ","Emloyee Name: ", lastName.upper() + ", " + firstName.capitalize() + " " + middleInitial.capitalize())
print("=============================================================================")
print("Gross Pay", "            ", "Deduction wtax", "            ", "Net Pay", "            ")
print("=============================================================================")
print(round(numberOfDays, 0), "day(s)", "                  ", "10%", "                  ", round(deduction, 0), "php")
