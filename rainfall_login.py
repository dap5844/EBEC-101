"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 03.3 - Rainfall
Date: 09/26/2022
Description:
    This program calculates the total and average rainfall over a period of years the user assigns.
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

    months = ['Jan.','Feb.','Mar.','Apr.','May.','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.']
    count = 1 #Initiate number of years
    j = 0
    total = 0
    avg = 0
    years = 0
    year = int(input("Enter the number of years: "))
    for years in range(year):
        print(f"  For year No. {years+1}")
        while j <= 11:
            rain = float(input(f"    Enter the rainfall for {months[j]}: "))
            #print(f"The month is {months[j]}.")
            if rain < 0:
                print('    Invalid input; rainfall cannot be negative.')
            else:
                j += 1
                total += rain
    avg = total/(year*j)
    print(f"There are {year*j} months.")
    print(f"The total rainfall was {total:.2f} inches.")
    print(f"The monthly average rainfall was {avg:.2f} inches.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()