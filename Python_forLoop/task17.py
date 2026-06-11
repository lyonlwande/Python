#17. Calculate Class Total Marks
"""
Create a list containing marks for 15 students and calculate the class total.
"""
marks = [75, 82, 90, 68, 88, 95, 70, 80, 85, 92, 78, 84, 91, 79, 87]
total_marks =0

for x in marks :
    total_marks += x
print("Total Marks:", total_marks)