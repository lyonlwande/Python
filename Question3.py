#Question 3: Uber Driver Bonus
# An Uber driver completed 120 trips this month.
# Rules:
# - 100 trips or more → Bonus awarded.
# - Less than 100 trips → No bonus.
# Display the appropriate message.

required_trips = 100
completed_trips = 120

if completed_trips >= required_trips:
    print("Bonus Awarded")
else:
    print("Bonus requirement not achieved")