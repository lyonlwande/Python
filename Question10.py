#Question 10: SACCO Loan Approval System (Advanced Nested If)
#A SACCO member has:

#monthsAsMember = 18
#savings = 120000
#Rules:

#Member must have been in the SACCO for at least 12 months.
#If eligible:
#Check savings.
#If savings are 100,000 or above:
#Loan Approved
#Otherwise:
#Increase Savings Before Applying
#If membership is less than 12 months:
#Membership Period Too Short
#Use nested if statements.

monthsAsMember = 18
savings = 120000

if monthsAsMember >= 12 :
    if savings >= 100000 :
        print(f"Loan Approved")
    elif savings < 100000 :
        print(f"Increase Savings Before Applying")
elif monthsAsMember < 12 :
    print(f"Membership Period Too Short")

    
