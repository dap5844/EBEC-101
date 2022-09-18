"""
Author: Daniel Perez, perez294@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 09/17/2022
Description:
    This program asks the user to enter a number of seconds and displays the total time entered in days, hours, minutes and seconds.
Contributors:
    Exercise tip video
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
    num = int(input("Please enter a time in seconds: ")) #Get the amount of seconds 
    time =  "{:,}".format(num)

    if num > 0 and num < 60:
        print(f"  {time} seconds is less than one minute.")

    elif num >= 60 and num < 3600:
        mins = num // 60
        num = num - mins*60
        secs = num % 60
        if mins != 0 and secs != 0:
            print(f"  {time} seconds equals {mins} minute(s) and {secs} second(s).")
        elif mins !=0 and secs == 0:
            print(f"  {time} seconds equals {mins} minute(s).")
        
    elif num >= 3600 and num < 86400:

        hours = num // 3600
        num = num - hours*3600
        mins = num % 3600 // 60
        num = num - mins*60
        secs = num % 60
        if mins != 0 and secs != 0:
            print(f"  {time} seconds equals {hours} hour(s), {mins} minute(s) and {secs} second(s).")
        elif mins == 0 and secs != 0:
            print(f"  {time} seconds equals {hours} hour(s) and {secs} second(s).")
        elif mins != 0  and secs == 0:
            print(f"  {time} seconds equals {hours} hour(s) and {mins} minute(s).")
        elif mins == 0  and secs == 0:
            print(f"  {time} seconds equals {hours} hour(s).")

    elif num >= 86400:
        days = num // 86400
        num = num - days*86400
        hours = num % 86400 // 3600
        num = num - hours*3600
        mins = num % 3600 // 60
        num = num - mins*60
        secs = num % 60
        if hours !=0 and mins != 0 and secs != 0:
            print(f"  {time} seconds equals {days} day(s), {hours} hour(s), {mins} minute(s) and {secs} second(s).")
        elif hours != 0 and mins != 0 and secs == 0:
            print(f"  {time} seconds equals {days} day(s), {hours} hour(s) and {mins} minute(s).")
        elif hours != 0 and mins == 0 and secs == 0:
            print(f"  {time} seconds equals {days} day(s) and {hours} hour(s).")    
        elif hours != 0 and mins == 0 and secs != 0:  
            print(f"  {time} seconds equals {days} day(s), {hours} hour(s)  and {secs} second(s).")
        elif hours == 0 and mins != 0 and secs != 0:
            print(f"  {time} seconds equals {days} day(s), {mins} minute(s) and {secs} second(s).")
        elif hours == 0 and mins == 0 and secs != 0:  
            print(f"  {time} seconds equals {days} day(s) and {secs} second(s).")
        elif hours == 0 and mins != 0 and secs == 0:
            print(f"  {time} seconds equals {days} day(s) and {mins} minute(s).")
        elif hours == 0  and mins == 0  and secs == 0:
            print(f"  {time} seconds equals {days} day(s).")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()