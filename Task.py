#University Scholarship and Loan Decision System

#A student is applying for a combined scholarship and education loan package. Create a program that uses variables and nested if / elif / else logic to decide the outcome.

#Input values 
# student_name
# marks (0–100)
# family_income
# completed_community_service_hours
# has_criminal_record (True / False)
# requested_loan_amount

#Rules
#If has_criminal_record is True, print: "{student_name}: Application rejected due to criminal record." No further checks.
#Otherwise, check marks: 90 or above → Excellent || 75 to 89 → Very Good ||  60 to 74 → Good || below 60 → Needs Improvement 
# Scholarship eligibility: If marks >= 75 and family_income < 30000 and completed_community_service_hours >= 20, print: "{student_name}: Scholarship approved." Else if marks >= 75 but family_income >= 30000, print:"{student_name}: Scholarship pending — income too high." Else if marks >= 60 but completed_community_service_hours < 20 , print: "{student_name}: Scholarship denied — insufficient service hours." Else print: "{student_name}: Scholarship denied — academic performance not enough."

#Loan approval:

#Only consider loan if scholarship is approved or pending.
#Loan approved if: requested_loan_amount <= 50000 and family_income >= 20000 If loan denied because amount is too high, print: "{student_name}: Loan denied — requested amount exceeds limit." If denied because income is too low, print: "{student_name}: Loan denied — income below required threshold." Final message: If both scholarship approved and loan approved: "{student_name}: Scholarship and loan approved." If scholarship approved and loan denied: "{student_name}: Scholarship approved, loan denied." If scholarship pending and loan approved: "{student_name}: Scholarship pending, loan approved." Otherwise, print the applicable rejection reason from above.