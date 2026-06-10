#Question 6: University Admission Decision 
# A student has: grade = "B" 
# Rules:
# Grade A → Direct Admission
# Grade B → Admission Granted
# Grade C → Diploma Recommended
# Grade D or below → Admission Rejected
# Display the result.

student_grade = "B"

if student_grade == "A" :
    print("Direct Admission")
elif student_grade == "B" :
    print("Admission Granted")
elif student_grade == "C" :
    print("Diploma Recommended")
elif student_grade == "D" :
    print("Admission Rejected")
else :
    print("Admission status not determined")