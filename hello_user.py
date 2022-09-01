"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 00.1 - Hello User
Date: 08/26/2022

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
    Hello_Prompt = input("What is your name? ") #Asks the user for their name

    print(f"Hello {Hello_Prompt}!") #Code prints the phrase as " 'Hello ' Hello_Prompt'!' using a f-string printing format


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
