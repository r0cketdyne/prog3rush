"""
Problem Statement
This program will compute an invoice based on values entered by the user. The invoice computes a
total (Gross) bill amount based on the number of hours invoiced and the hourly rate (the gross amount
is the product of those two values).


The user provides a discount code of 1, 2, or 3. 1 is 10% discount, 2 is 12% discount, 3 is 15% discount.
Any other value results in a discount of 0.0.
An invoice must be printed to the screen.
"""

hr_invoiced = (float(input("Enter hours invoiced")))  # takes string from user and ensures it's a float
hr_rate = (float(input('Enter the hourly rate')))  # takes string from the user; transforms it into a float

product = hr_invoiced * hr_rate

print(f"the actual bill amount, sans discount is {product}")
#we have stored the data. this was ridiculously easy, obviously. Now we need to manipulate it

#for some reason I ran into some syntax errors above. It was bc unmatched parenth. obvious. 