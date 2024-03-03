# Program 3 -- File: Program3.py
# MATTHEW STEPHENSON 3/02/2024
# This program will compute an invoice based on values entered by the user.
###########################################################

# Func to calculate the invoice based on hours, rate, and discount code
def calculate_invoice(hours, rate, discount_code):
    # Calculate the gross invoice by multiplying hours and rate
    gross_invoice = hours * rate

    # Determine discount based on the provided discount code
    if discount_code == 1:
        discount = 0.10 * gross_invoice
    elif discount_code == 2:
        discount = 0.12 * gross_invoice
    elif discount_code == 3:
        discount = 0.15 * gross_invoice
    else:
        discount = 0.00

    # Calculate the net invoice by subtracting the discount from the gross invoice
    net_invoice = gross_invoice - discount

    # Generate a formatted invoice text
    result_text = f"------------------- INVOICE -------------------------\n" \
                  f"Hours Invoiced: {hours} Hourly Rate: $ {rate:.2f}\n" \
                  f"Gross Invoice: $ {gross_invoice:.2f}\n" \
                  f"Discount: $ {discount:.2f} (Discount Code {int(discount_code)})\n" \
                  f"Net Invoice: $ {net_invoice:.2f} (Pay This Amount)\n" \
                  f"------------------ END INVOICE ----------------------"

    # Return the formatted invoice text
    return result_text

# Main function to interact with the user and call the calculate_invoice func above
def main():
    print("Welcome to the invoice calculator.")
    # Welcoming the user with text logged to standard i/o

    while True:
        try:
            # Get input values from the user
            hours_invoiced = float(input("Please enter the hours invoiced: "))
            hourly_rate = float(input("Please enter the hourly invoice rate: "))
            discount_code = float(input("Please enter the discount code (1=10%, 2=12%, 3=15%): "))

            # Call the calculate_invoice function and print the result
            result = calculate_invoice(hours_invoiced, hourly_rate, discount_code)
            print(result)

            # Ask the user if they want to compute another invoice
            another_invoice = input("Would you like to compute another Invoice [Y/N]? ").lower()
            
            # If the input is not 'y', end the program
            if another_invoice != 'y':
                print("End Program. Au Revoir ")
                break
        except ValueError:
            # Handle invalid input by catching ValueError and prompting the user to enter valid numeric values
            print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    # Execute the main function at line 36 if this script is run as the main module
    main()

