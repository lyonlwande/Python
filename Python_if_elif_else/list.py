# List of employees in a company -- string data type
employees = ["Jimmy" , "Sally" , "Tommy" , "Sara" , "Bob" , "Alice" , "John" , "Emily" , "Michael" , "Jessica"]
# Display the list of employees 
print(f"Employees: {employees}")
print(f"The first employee is: {employees[0]}") # 1st employee
print(f"The last employee is: {employees[-1]}") # last employee

# List of employee salaries -- integer data type
salaries = [50000, 65000, 55000, 40000, 45000, 80000, 75000, 90000, 85000, 95000]
# Display the list of salaries
print(f"Salaries: {salaries}")
# Display the sum of salaries
print(f"Total salaries: {sum(salaries)}")
#Display the maximum salary
print(f"Maximum salary: {max(salaries)}")
# Display the minimum salary
print(f"Minimum salary: {min(salaries)}")
#Display the length of the salaries list
print(f"Number of employees: {len(salaries)}")
total_employees = len(employees)
total_salaries =sum(salaries)
avarage_salary = total_salaries / total_employees
#Display the average salary
print(f"The average salary is: {avarage_salary} KES")
