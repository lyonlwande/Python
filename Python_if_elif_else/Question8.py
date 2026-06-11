# Question 8: Scholarship Eligibility (Nested If)
# A student has:
# marks = 85
# familyIncome = 25000
# Rules:
# Student must score at least 80 marks.
# If they qualify:
#   Check family income.
#   If income is below 30,000:
#       Scholarship Approved
#   Otherwise:
#       Scholarship Not Approved Due To Income
# If marks are below 80:
#   Scholarship Not Approved Due To Marks
# Use nested if statements.

marks = 85
familyIncome = 25000
income_threshold = 30000

if marks >= 80:
    if familyIncome < income_threshold:
        print("Scholarship Approved")
    else:
        print("Scholarship Not Approved Due To Income")
else:
    print("Scholarship Not Approved Due To Marks")


