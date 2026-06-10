# Question 8: Scholarship Eligibility (Nested If)
 # A student has:

#marks = 85
#familyIncome = 25000
#Rules:

#Student must score at least 80 marks.
# If they qualify:
# Check family income.
# If income is below 30,000:
# Scholarship Approved
# Otherwise:
# Scholarship Not Approved Due To Income
# If marks are below 80:
# Scholarship Not Approved Due To Marks
# Use nested if statements.

qualified_mark = 80
family_Income_threshold = 30000

student_marks = 85
students_family_Income = 25000
     

if student_marks >= qualified_mark :
    print(f"Marks status eligible for Scholarship ")
    if students_family_Income < family_Income_threshold :
        print(f"Scholarship Approved")
    elif students_family_Income >= family_Income_threshold :
        print(f" Scholarship Not Approved Due To Income")
if student_marks < qualified_mark :
     print(f" Scholarship Not Approved Due To Marks")


