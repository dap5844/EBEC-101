"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/17/2022
Description:
    This program asks the user for a year and tells the user if the year is a leap year or not.
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
    year = int(input("Enter a year: ")) #Get the year from the user
    
    #Check if it's divisible by 100 and 400 
    if (year % 400 == 0) and (year % 100 == 0):
 
        print("The year {0} is a leap year.\nFebruary of {0} has 29 days.".format(year))

    #Check if it's divisible by 4 and it's not a century
    elif (year % 4 ==0) and (year % 100 != 0):
        print("The year {0} is a leap year.\nFebruary of {0} has 29 days.".format(year))
    
    #If it's neither of the two options above, it's not a leap year
    else:
        print("The year {0} is not a leap year.\nFebruary of {0} has 28 days.".format(year))


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()