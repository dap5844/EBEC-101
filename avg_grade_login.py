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

def determine_grade(grade): #This code takes the score and returns a letter grade

    if grade >= 92 and grade <= 100:
        letter = "A"
    elif grade >= 82 and grade < 92:
        letter = "B"
    elif grade >= 73 and grade < 82:
        letter = "C"
    elif grade >= 64 and grade < 73:
        letter = "D"
    elif grade >= 0 and grade < 64:
        letter = "F"
    return letter

def get_valid_score(): #This code prompts the user for a score. If it's less than 0 or greater than 100, it'll ask again.
                       #Once a valid score is found, it'll return that score and print it's letter grade
    score = -1
    grade = 0
    while score < 0 or score > 100:
        score = float(input(f"Enter a score: "))
        if score < 0 or score > 100:
            print(f"  Invalid Input. Please try again.")
        else:
            letter = determine_grade(score)
            print(f"  The letter grade for {score:.1f} is {letter}.")
            break
    return score
    
def calc_average(grades):
    sum = 0
    for i in range(0,len(grades)):
        grade = grades[i]
        sum += grade
    avg = sum / (len(grades))
    return avg

def main():

    sum = []
    for i in range(0,5):
        grades = get_valid_score()
        sum += [grades]
        determine_grade(grades)
    
    avg = calc_average(sum)
    letter = determine_grade(avg)
    print(f"\nResults:\nThe average score is {avg:.2f}.")
    print(f"   The letter grade for {avg:.2f} is {letter}")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
