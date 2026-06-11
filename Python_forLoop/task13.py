#13. Find Students Who Scored Above 80
"""
Create a list of  marks and display only marks greater than 80.
"""
marks = [75, 82, 90, 68, 88, 95, 70, 80, 85, 92, 78, 84, 91, 79, 87] 
concidered_marks = list()
for x in  marks :
    if x > 80 :
        concidered_marks.append(x)
print("Marks greater than 80 , include :", concidered_marks)