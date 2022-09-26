"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 03.1 - Sum Average
Date: 09/26/2022
Description:
    This program adds all the non-negative values and calcualtes the average. It stops once the user provides a negative number.
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

    count = 0 # init
    sum = 0 # init
    num = 0 # init
    while True: # check
        count = float(input("Enter a non-negative number (negative to quit): ")) #Enter a non-negative number
        if count < 0:
            break
        else:
            sum += count
            num += 1
    
    if num > 0:
        avg = sum/(num) 
        print(f'  You entered {num} numbers.')
        print(f'  Their sum is {sum} and their average is: {avg}.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()