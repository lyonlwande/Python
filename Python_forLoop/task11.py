#11. Count Passing Students
"""Create a list of marks and count how many students scored 50 and above."""
marks = [65, 45, 80, 30, 55, 70, 40, 90, 25, 60]
pass_count = 0

for x in marks :
    if x >= 50 :
        pass_count += 1
print("The number of students with 50 marks and above are :", pass_count )
        
