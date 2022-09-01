"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 01.2 - Interest
Date: 09/01/2022

Description:
    This program takes an input from the user (such as XXX) and writes a greeting in the form of "Hello XXX!".

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
    P = float(input("Enter the following parameters.\n  The initial deposit? ")) #Get principal
    r = float(input("  The annual interest rate in percent? "))/100 #Get annual interest rate
    t = float(input("  The number of years the account earn interest? ")) #Get specified number of years
    n = float(input("  The number of times interest is compounded each year: ")) #Get  number of times per year that the interest is compounded
    
    FV = (P*(1 + r/n)**(n*t)) #Calculate the future value
    fv_shrunk = limited_float = round(FV, 2) #This limits the FV to 2 decimals
    fv = "{:,}".format(fv_shrunk) #Put truncated FV with comma separated
    print(f"The balance of this account will be ${fv} after {t} years.") #output the cost

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()