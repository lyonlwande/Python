#18. Find Numbers Greater Than 100
"""
Create a list of numbers and display only numbers greater than 100.
"""
numbers = [50, 150, 200, 75, 300, 120, 90, 250]
concidered_numbers = list()

for x in numbers :
    if x > 100 :
        concidered_numbers.append(x)
print("The numbers above 100 include :" , concidered_numbers)
