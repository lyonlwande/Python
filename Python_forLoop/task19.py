#19. Student Fee Analysis
"""
Create a list containing fees paid by students.

Example:

fees = [15000, 20000, 18000, 22000, 17000]
Calculate:

Total fees collected
Highest fee paid
Lowest fee paid
"""
fees = [15000, 20000, 18000, 22000, 17000]

total_collected_fees = 0
for x in fees :
    if x == max(fees) :
        print("Highest collcted fee was :", x)
    if x == min(fees) :
        print("Lowest collcted fee was :", x)
    total_collected_fees += x
print("Total collected fees was :", total_collected_fees)
 