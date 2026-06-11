#Question 9: E-Commerce Delivery Qualification (Nested If)

# A customer has:
# purchaseAmount = 6000
# location = "Nairobi"
# Rules:
# Orders above 5,000 qualify for free delivery.
# If qualified:
#   Check location.
#   If customer is in Nairobi:
#       Free Delivery Approved
#   Otherwise:
#       Free Delivery Not Available In Your Area
# If purchase amount is below 5,000:
#   Delivery Charges Apply
# Use nested if statements.

purchaseAmount = 6000
location = "Nairobi"
qualified_purchase_amount = 5000
allowed_location = "Nairobi"

if purchaseAmount > qualified_purchase_amount:
    if location == allowed_location:
        print("Free Delivery Approved")
    else:
        print("Free Delivery Not Available In Your Area")
else:
    print("Delivery Charges Apply")