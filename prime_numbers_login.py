"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 10/3/2022
Description:
    This program asks for the user for 5 grades and outputs the average grade along with it's letter value.
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

def is_prime(num): #This code determines whether a number is prime or not
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0: #check if divisible by each number. if only divisible by itself, set flag to True (prime)
                flag = True
                break

    # check if flag is True
    if flag:
        print(f"  {num} is not a prime.")
    else:
        print(f"  {num} is a prime!")
    return

def main():

    num = 1
    while num != -1:
        num = int(input(f"Enter a positive integer (-1 to quit): "))
        if num == -1:
            break
        elif num == 0:
            print(f"Enter a positive integer. Try again.")
        else:
            is_prime(num)
        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
