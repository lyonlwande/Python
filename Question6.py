#Question 6: University Admission Decision 
# A student has: grade = "B" 
# Rules:
# Grade A → Direct Admission
# Grade B → Admission Granted
# Grade C → Diploma Recommended
# Grade D or below → Admission Rejected
# Display the result.

grade = "B"

if grade == "A":
    print("Direct Admission")
elif grade == "B":
    print("Admission Granted")
elif grade == "C":
    print("Diploma Recommended")
elif grade == "D":
    print("Admission Rejected")
else:
    print("Admission status not determined")