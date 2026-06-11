#20. Supermarket Stock Report
"""
Create a list containing stock quantities for 10 products.

Example:

stock = [20, 15, 8, 30, 25, 12, 18, 5, 40, 22]
Display:

Total stock available
Highest stock quantity
Lowest stock quantity
Products with stock less than 10
"""
stock = [20, 15, 8, 30, 25, 12, 18, 5, 40, 22]
total_stock = 0
low_stock = list()

for x in stock :
    if x == min(stock) :
        print("The Lowest stock quantity was :", x)
    if x == max(stock) :
        print("The Highest stock quantity was :", x)
    if x < 10 :
         low_stock.append(f"Product.{stock.index(x) + 1}")
    total_stock += x 
print("The products with stock quantity less than 10 were :", low_stock)
print("The total stock quantity for products was:", total_stock)
        