#Question 4: Mobile Data Bundle Discount

#A customer is purchasing data bundles worth:
# amount = 2500
# Rules: Above 2,000 KES → 10% discount. Otherwise → No discount.
# Display whether the customer qualifies for a discount.

amount = 2500
threshold = 2000
discount_rate = 0.10
reward = amount * discount_rate

if amount > threshold:
    print(f"Qualified for bundles discount for the purchase worth {amount}; discount {reward} KES will be rewarded")
else:
    print(f"Not Qualified for bundles discount. A minimum purchase above {threshold} KES is required.")