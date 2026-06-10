#Question 4: Mobile Data Bundle Discount

#A customer is purchasing data bundles worth: amount = 2500 
#Rules: Above 2,000 KES → 10% discount. Otherwise → No discount. Display whether the customer qualifies for a discount.

bundles_discount_threshold_amount = 2000
bundles_discount_rate = 10/100
bundles_amount = 2000 
bundles_discount_amount= bundles_amount * bundles_discount_rate


if bundles_amount > bundles_discount_threshold_amount :
    print(f"Qualified for bundles discount for the purchase worth  {bundles_amount} , discount {bundles_discount_amount} ksh will be rewarded ")
else :
    print(f"Not Qualified for bundles discount .  Concidered bundles amount  is  more than ksh {bundles_discount_threshold_amount} ")