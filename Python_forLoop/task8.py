#8. Display Odd Numbers
"""
Create a list of numbers from 1 to 20 and print only the odd numbers.
"""
numbers_list = list(range(1, 21))
odd_numbers_list = list()

for x in numbers_list :
    if x % 2 != 0 :
        odd_numbers_list.append(x)
print("The list of odd numbers from   1 to 20  is ", odd_numbers_list)