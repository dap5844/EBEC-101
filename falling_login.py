"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 04.1 - Falling
Date: 10/3/2022
Description:
    This program calls a distance function to calculate the fallen distance for a given time.
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

def falling_dist(t):
    g = 8.87
    d = 0.5*(g*(t**2)) #This function calculates the distance per given falling time
    return d

def main():

    time = [5,10,15,20,25,30,35,40,45,50] #Split input time
    i = 0
    print(f"Time (s)  Distance (m)")
    print('─ ' * 15)
    for i in range(len(time)):
        d=falling_dist(time[i]) #call falling_dist function and calculate distance for given time
        D = "{:.1f}".format(d) #format with 1 decimal point
        print(f"{time[i]:>4}\t\t{D:>4}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()