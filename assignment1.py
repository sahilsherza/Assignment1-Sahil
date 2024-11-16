#!/usr/bin/env python3

'''
OPS445 Assignment 1 
Program: assignment1.py 
The python code in this file is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Author: Sahil Sherzai
Semester: Fall 2024
Description: This script implements date manipulation functions such as leap year check,
# calculating next and previous days, and computing the maximum days in a given month, 
# while handling command-line input.

'''

import sys
from datetime import datetime, timedelta



# Function to check if a year is a leap year
def leap_year(year: int) -> bool:
    """
    Returns True if the given year is a leap year.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
    
# Function to get the maximum number of days in a month, considering leap years for February
def mon_max(month: int, year: int) -> int:
    """
    Returns the maximum number of days in the given month and year, considering leap years for February.
    """
    # Days in each month (Non-leap year)
    mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    if month == 2 and leap_year(year):  # February in a leap year
        return 29
    
    return mon_dict.get(month, 31)  # Default to 31 if month is invalid
# Function to calculate the next day based on a given date in 'YYYY-MM-DD' format
def after(date: str) -> str:
    """
    Returns the date for the next day given a starting date in 'YYYY-MM-DD' format.
    """
    year, month, day = (int(x) for x in date.split('-'))
    day += 1  # Move to the next day
    
    if day > mon_max(month, year):  # If the day exceeds the month's max, reset to the next month
        day = 1
        month += 1
    
    if month > 12:  # If the month exceeds December, reset to January of the next year
        month = 1
        year += 1
    
    return f"{year}-{month:02}-{day:02}"  # Format date as 'YYYY-MM-DD'

# Function to calculate the previous day based on a given date in 'YYYY-MM-DD' format
def before(date: str) -> str:
    """
    Returns the previous day's date in 'YYYY-MM-DD' format.
    """
    year, month, day = (int(x) for x in date.split('-'))
    day -= 1  # Move to the previous day
    
    if day == 0:  # If the day is 0, reset to the last day of the previous month
        month -= 1
        if month == 0:
            month = 12
            year -= 1
        day = mon_max(month, year)
    
    return f"{year}-{month:02}-{day:02}"  # Format date as 'YYYY-MM-DD'

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD NN")
    sys.exit()

# Function to validate if the given date is in the correct format (YYYY-MM-DD)
def valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
   
def dbda(date, days):

    """

    Returns a new date by moving a specified number of days before or after a starting date.

    """

    current_date = datetime.strptime(date, '%Y-%m-%d')  # Convert string to datetime

    if days >= 0:

        return after(date)  # Use after() to move forward in time

    else:

        return before(date)  # Use before() to move backward in time



# Main function to handle command-line input and output the result
def main():
    if len(sys.argv) != 3:
        usage()  # Ensure the correct number of arguments are provided
    
    date = sys.argv[1]
    divisor = int(sys.argv[2])

    if not valid_date(date):
        usage()  # Ensure the provided date is valid
    
    if divisor <= 0:
        usage()  # Prevent division by zero errors
    
    days_in_year = 365
    divided_days = round(days_in_year / divisor)  # Divide the days in a year by the divisor

    print(f"A year divided by {divisor} is {divided_days} days.")
    
    # Call dbda() to get the new dates after moving forward and backward by 'divided_days'
    before_date = dbda(date, -divided_days)
    after_date = dbda(date, divided_days)

    print(f"The date {divided_days} days ago was {before_date}.")
    print(f"The date {divided_days} days from now will be {after_date}.")

if __name__ == "__main__":
    main()
