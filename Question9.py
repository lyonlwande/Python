#Question 9: E-Commerce Delivery Qualification (Nested If)

# A customer has:

# purchaseAmount = 6000
# location = "Nairobi"

# Rules:
# Orders above 5,000 qualify for free delivery.
# If qualified:
# Check location.
# If customer is in Nairobi:
# Free Delivery Approved
# Otherwise:
# Free Delivery Not Available In Your Area
# If purchase amount is below 5,000:
# Delivery Charges Apply
# Use nested if statements.


qualified_purchase_amount =5000
alowed_locations="Nairobi"

purchase_amount = 6000
location = "Nairobi"

if purchase_amount >= qualified_purchase_amount :
    if location == alowed_locations :
        print(f"Free Delivery Approved")
    elif location != alowed_locations :
        print(f"Free Delivery Not Available In Your Area")
elif purchase_amount < qualified_purchase_amount :
    print(f"Delivery Charges Apply")