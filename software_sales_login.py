"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/17/2022
Description:
    This program asks the number of packages purchased and the amount of discount if any and the total amount of purchase after discount.
Contributors:
    None, Stackflow
My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.
Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""


def main():
    qty = int(input("How many packages will be purchased: ")) #Get the quantity purchased 
    price = 880
    
    #Quantity less than 0
    if qty < 0:
        print("Invalid Input!")

    #Quantity between 1 and 3
    elif qty > 0 and qty < 4:
        fprice = "{:,.2f}".format(qty*price)
        print(f"No discount applied.\nThe total price to purchase {qty} packages is ${fprice}")
    
    #10% disc
    elif qty >= 4 and qty <= 39:
        fprice = "{:,.2f}".format(qty*price*0.9)
        print(f"10% discount applied..\nThe total price to purchase {qty} packages is ${fprice}")
    #15%
    elif qty >= 40 and qty <= 199:
        fprice = "{:,.2f}".format(qty*price*0.85)
        print(f"15% discount applied.\nThe total price to purchase {qty} packages is ${fprice}")
    #30%
    elif qty >= 200 and qty <= 999:
        fprice = "{:,.2f}".format(qty*price*0.7)
        print(f"30% discount applied.\nThe total price to purchase {qty} packages is ${fprice}")
    #42%
    elif qty >= 1000:
        fprice = "{:,.2f}".format(qty*price*0.58)
        print(f"42% discount applied.\nThe total price to purchase {qty} packages is ${fprice}")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()