"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 10/3/2022
Description:
    This program asks the user for two integers and calculates the sum of all numbers within the two integers after removing values divisible by 3.
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

def lucky_sum(a,b):
    integ_1 = a
    integ_2 = b
    sum = 0
    k = 0
    if integ_2 > integ_1: #this checks if b is greater than a
        i = integ_1
        for i in range(integ_1,integ_2):
            if i%3 != 0: #check if the number in the for loop is not divisible by 3 to add it
                k = i
                sum += k
    elif integ_2 < integ_1:
        i = integ_2
        for i in range(integ_2,integ_1):
            if i%3 != 0: #check if the number in the for loop is not divisible by 3 to add it
                k = i
                sum += k
    if integ_2%3 != 0: #check if the 2nd integer is not divisible by 3 to add it to the sum
        SUM = sum + integ_2
    else:
        SUM = sum
    return SUM
        
def main():

    integ_1 = int(input("Enter the first integer: ")) #ask user for 1st integer
    integ_2 = int(input("Enter the second integer: ")) #ask user for 1st integer
    SUM = lucky_sum(integ_1,integ_2) #run lucky sum function
    print(f"The sum of the lucky numbers is {SUM:,.0f}.") #print summed value
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
