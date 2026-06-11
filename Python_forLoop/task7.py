
#7. Display Even Numbers
"""
Create a list of numbers from 1 to 20 and print only the even numbers.
"""
number_list = list(range(1,21))
even_numbers_list = list()

for x in number_list :
    if x % 2 == 0 :
        even_numbers_list.append(x)
print("The list of even numbers from the  1 to 20  is ", even_numbers_list)