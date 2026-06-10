#Question 2: Bank Loan Qualification

# A bank only gives loans to people earning at least 50,000 KES per month.Create a program using:salary = 70000
#Requirements: If salary is 50,000 or above, print: "Loan Approved" Otherwise print: "Loan Rejected"

minimum_salary = 50000
applicant_salary = 70000

if applicant_salary >= minimum_salary :
    print(f"Loan Approved") 
else :
    print(f"Loan Rejected")