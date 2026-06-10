#Question 5: Employee Tax Category

#An employee earns: salary = 120,000
#Rules: 
# Below 30,000 → Low Tax 
# 30,000 to 100,000 → Medium Tax 
# Above 100,000 → High Tax Use if-elif-else.
#Display the tax category.

employee_salary = 120000

# tax group  salary lower limit 
medium_tax_salary = 30000
high_tax_salary = 100000

if employee_salary < medium_tax_salary :
    print(f"Your salary is in the Low Tax  category ")
elif  employee_salary < high_tax_salary :
    print(f"Your salary is in the Medium Tax  category ")
else :
    print(f"Your salary is in the High Tax  category ")
