#16. Count Fruits
"""
Create a list containing different fruits. Count how many times the fruit "Mango" appears in the list.

Example:

fruits = ["Mango", "Apple", "Mango", "Orange", "Mango"]
"""
fruits = ["Mango", "Apple", "Mango", "Orange", "Mango"]

count = 0 
for x  in fruits :
    if x == "Mango" :
        count += 1 
print("The Counter for the number of appearances  for  Mango , in the fruits list  is ", count)