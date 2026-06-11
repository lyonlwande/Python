#9. Calculate Average Marks

"""
Create a list of marks for 10 students and calculate the average mark.
"""
marks = [85, 90, 78, 92, 88, 95, 80, 91, 89, 87]

total_marks = 0
total_students = 0

for x in marks :
    total_marks += x
    total_students +=1
print(f"Total marks : {total_marks}  , Total students : {total_students}")
avarage_marks = total_marks/total_students
print("Avarage marks is " , avarage_marks)