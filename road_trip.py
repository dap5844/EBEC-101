"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 01.1 - Road Trip
Date: 09/01/2022

Description:
    This asks the user for trip distance, average price of gas and mile per gallong of the vehicle to output the cost.

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
    dist = float(input("How far away is your destination (miles)? ")) #Get distance to travel
    price = float(input("What is the average price of gas (dollars per gallon)? ")) #Get avg price of gas
    mpg = float(input("What is the fuel efficiency of your vehicle (mpg)? ")) #Get mpg of te vehicle
    cost = int((2*dist)*price/mpg) #Calculate cost of trip
    print(f"The fuel cost for this trip is approximately ${cost}.\n") #output the cost

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
