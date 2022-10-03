"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 04.3 - Average Grade
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

def determine_grade(grade):

    if grade >= 92 and grade <= 100:
        print(f"The letter grade for {grade:.1f} is A.")
    elif grade >= 82 and grade < 92:
        print(f"The letter grade for {grade:.1f} is B.")
    elif grade >= 73 and grade < 82:
        print(f"The letter grade for {grade:.1f} is C.")
    elif grade >= 64 and grade < 73:
        print(f"The letter grade for {grade:.1f} is D.")
    elif grade >= 0 and grade < 64:
        print(f"The letter grade for {grade:.1f} is F.")
    return

def get_valid_score():
    score = -1
    grade = 0
    while score < 0 or score >= 100:
        score = int(input(f"Enter a score: "))
        if score < 0 or score >= 100:
            print(f"Invalid Input. Please try again.")
        else:
            break
    return score
    
def calc_average(grades):
    avg = grades / 5
    return avg

def main():

    sum = 0
    for i in range(0,5):
        grades = get_valid_score()
        sum += grades
        determine_grade(grades)
    
    avg = calc_average(sum)
    print(f"\nResults:\nThe average score is {avg:.2f}.")
    determine_grade(avg)

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
