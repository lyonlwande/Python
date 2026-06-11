#Question 7: ATM Withdrawal (Nested If)

#A customer wants to withdraw money.

#balance = 15000
#withdrawAmount = 5000

#Rules:
# First check if balance is greater than 0.
# If yes: Check if withdrawal amount is less than or equal to balance.
# If true, print: "Withdrawal Successful"
# Otherwise print: "Insufficient Funds"
# If balance is 0 or below:
# Print: "Account Empty"
# Use nested if statements.

balance = 1500
withdrawAmount = 5000

if balance > 0:
    if withdrawAmount <= balance:
        print("Withdrawal Successful")
    else:
        print("Insufficient Funds")
else:
    print("Account Empty")