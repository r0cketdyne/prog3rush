#cleaned everything up.

while True:
    hr_invoiced = float(input("Please enter hours invoiced: "))
    hr_rate = float(input('Please enter the hourly rate: '))
    discount = float(input("Please enter your discount code (1, 2, 3): "))

    product = hr_invoiced * hr_rate

    if discount == 1:
        product *= 0.10  # 10% discount
    elif discount == 2:
        product *= 0.12  # 12% discount
    elif discount == 3:
        product *= 0.15  # 15% discount
    elif discount == 0:
        print("The gross bill amount is ", product)
    else:
        print("Invalid discount code")

    # Calculate and print the gross bill amount
    gross_amount = (hr_invoiced * hr_rate) - product
    print(f"The gross bill amount is {gross_amount}")

    # Ask the user if they want to continue
    user_input = input("Do you want to enter another set of data? (Y/N): ")
    if user_input.lower() != 'y':
        break  # Exit the loop if the user enters anything other than 'Y' or 'y'


