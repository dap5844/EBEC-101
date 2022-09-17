"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 09/17/2022
Description:
    This program that asks the user for the velocity of the water flowing through a pipe (V), for the pipe’s diameter (d), and to select the water’s temperature
(T) from 5, 20 and 50 deg C.
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
    t = int(input("Enter the temperature in °C as 5, 20, or 50: ")) #Select the temp
    V = float(input("Enter the velocity of water in the pipe (m/s): ")) #Select the velocity
    d = float(input("Enter the pipe's diameter (m): ")) #Select the diameter

    #Num less than 0 or greater than 36
    if t == 5:
        v = 1.52e-6
        Re = "{:,.2e}".format(V*d / v)
        print(f"At 5.0°C, the Reynolds number for flow at {V} m/s in a {d} m diameter pipe is {Re}.")
    
    elif t == 20:
        v = 1.00e-6
        Re = "{:,.2e}".format(V*d / v)
        print(f"At 20.0°C, the Reynolds number for flow at {V} m/s in a {d} m diameter pipe is {Re}.")
        
    elif t == 50:
        v = 5.54e-7
        Re = "{:,.2e}".format(V*d / v)
        print(f"At 50.0°C, the Reynolds number for flow at {V} m/s in a {d} m diameter pipe is {Re}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()