"""
Problem Statement
This program will compute an invoice based on values entered by the user. The invoice computes a
total (Gross) bill amount based on the number of hours invoiced and the hourly rate (the gross amount
is the product of those two values).


The user provides a discount code of 1, 2, or 3. 1 is 10% discount, 2 is 12% discount, 3 is 15% discount.
Any other value results in a discount of 0.0.
An invoice must be printed to the screen.
"""

hr_invoiced = (float(input("Enter hours invoiced\n")))  # takes string from user and ensures it's a float
hr_rate = (float(input('Enter the hourly rate\n')))  # takes string from the user; transforms it into a float
discount = (float(input("Enter your discount code\n")))

product = hr_invoiced * hr_rate

if discount == 1:
    product *= .10
elif discount == 2:
    product *= .12
elif discount == 3:
    product *= .15
else:
    print(f"the discount is {(hr_invoiced * hr_rate) - product}") #for some reason this is just giving me gross? tf?
    
print(f"the discount is {(hr_invoiced * hr_rate) - product}")


"""
cont = input("Do you want to continue? Enter Y for yes or N for no")


if cont == "Y":
    #execute control struct
else: #terminate program
"""

#we have stored the data. this was ridiculously easy, obviously. Now we need to manipulate it

#for some reason I ran into some syntax errors above. It was bc unmatched parenth. obvious. 

#ok I have NOT ran this. but I'm guessing that maths can be done within {} constraints so lets cross
#our fingers. this should run flawlessly in principle!
# =============================================================================
# #JESUS CHRIST IT WORKED FIRST TIME! CODED FROM SCRATCH!!
# =============================================================================
#^right before I pushed this... I created something above with a hotkey. I don't remember how I did it?^
#I still need to implement this 
"""
After printing an invoice, ask the user if they want to continue and enter another set of data (Y or N).
Your program should loop as long as the response is a Y or a y.
Sample Execution
Below is shown a screen capture of what the program would look like if I ran it with two sets of input
data. The values in YELLOW are what were entered by the user in this example execution.

"""