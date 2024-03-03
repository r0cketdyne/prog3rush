# Program 3 -- File: Program3.py
# MATTHEW STEPHENSON 3/02/2024
# This program will compute an invoice based on values entered by the user.
###########################################################
def calculate_invoice(hours, rate, discount_code):
    gross_invoice = hours * rate

    if discount_code == 1:
        discount = 0.10 * gross_invoice
    elif discount_code == 2:
        discount = 0.12 * gross_invoice
    elif discount_code == 3:
        discount = 0.15 * gross_invoice
    else:
        discount = 0.00

    net_invoice = gross_invoice - discount

    result_text = f"------------------- INVOICE -------------------------\n" \
                  f"Hours Invoiced: {hours} Hourly Rate: $ {rate:.2f}\n" \
                  f"Gross Invoice: $ {gross_invoice:.2f}\n" \
                  f"Discount: $ {discount:.2f} (Discount Code {int(discount_code)})\n" \
                  f"Net Invoice: $ {net_invoice:.2f} (Pay This Amount)\n" \
                  f"------------------ END INVOICE ----------------------"
#yay GUI's!
    return result_text

def main():
    print("Welcome to the invoice calculator.")

    while True:
        try:
            hours_invoiced = float(input("Please enter the hours invoiced: "))
            hourly_rate = float(input("Please enter the hourly invoice rate: "))
            discount_code = float(input("Please enter the discount code (1=10%, 2=12%, 3=15%): "))

            result = calculate_invoice(hours_invoiced, hourly_rate, discount_code)
            print(result)

            another_invoice = input("Would you like to compute another Invoice [Y/N]? ").lower()
            if another_invoice != 'y':
                print("End Program 2. Goodbye.")
                break
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()

#needs to be extensively commented
#this is actually functional