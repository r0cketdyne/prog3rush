# Program 3 -- File: Program3.py
# MATTHEW STEPHENSON 3/02/2024
# This program will compute an invoice based on values entered by the user.
###########################################################

while True:
#we will implement a while loop to keep prompting the usr for input until they choose not to continue.
    hr_invoiced = float(input("Please enter hours invoiced: "))
    hr_rate = float(input('Please enter the hourly rate: '))
    discount = float(input("Please enter your discount code (1, 2, 3): "))

    product = hr_invoiced * hr_rate

    if discount == 1:
        product *= 0.10
# 10% discount
    elif discount == 2:
        product *= 0.12
 # 12% discount
    elif discount == 3:
        product *= 0.15
# 15% discount
    elif discount == 0:
        print("The gross bill amount is ", product)
    else:
        print("Invalid discount code")

    gross_amount = (hr_invoiced * hr_rate) - product
# Calculate and print the gross bill amount to the terminal emulator at the standard i/o
    print(f"The gross bill amount is {gross_amount}")

    user_input = input("Do you want to enter another set of data? (Y/N): ")
# Ask the user if they want to continue. log this output to standard i/o
    if user_input.lower() != 'y':
#I implemented the use of the .lower method here. which takes Y, which is transformed into y and checks if it is indeed y.
        break
# Exit the loop if the user enters anything other than 'Y' or 'y'

#ps: I will still probably implement a kind of GUI, just wanted something
#functional uploaded to canvas just in case...
#well, I don't want to use a library not native to python so I guess we're hard coding it...LMAO

