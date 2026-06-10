#Question 5: Employee Tax Category

#An employee earns: salary = 120000
#Rules: 
# Below 30,000 → Low Tax 
# 30,000 to 100,000 → Medium Tax 
# Above 100,000 → High Tax
# Use if-elif-else.
# Display the tax category.

salary = 120000

if salary < 30000:
    print("Your salary is in the Low Tax category")
elif salary <= 100000:
    print("Your salary is in the Medium Tax category")
else:
    print("Your salary is in the High Tax category")
