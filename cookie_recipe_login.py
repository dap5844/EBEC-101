"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 01.3 - Cookie Recipe 
Date: 09/01/2022

Description:
    This program gives the required amount of ingredients to generate a desired quantity of cookies.

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
    quant = int(input("How many cookies do you want to make? ")) #Get amount of cookies
    #Below the quantity of that's required for each ingredient is divided by what it makes
    #Then it's multiplied by the quantity of desired cookies to get the partitions
    Butter = "{:,.2f}".format(quant*1.25/48)
    Sugar = "{:,.2f}".format(quant*1.50/48)
    Flour = "{:,.2f}".format(quant*2.50/48)
    Quant = "{:,}".format(quant)
    print(f"To make {Quant} cookies, you will need: ")
    print("%10s"%(Butter)," cups of butter")    
    print("%10s"%(Sugar)," cups of sugar")
    print("%10s"%(Flour)," cups of flour")
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
