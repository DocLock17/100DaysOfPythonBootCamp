#!/bin/python3
"""
Tip Calculator
"""

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15, or more? "))
people = int(input("How many people to split the bill?"))

bill_with_tip = bill * (1 + (tip / 100))
print(f"The total bill was ${bill_with_tip:.2f}")

bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay ${final_amount:.2f}")
