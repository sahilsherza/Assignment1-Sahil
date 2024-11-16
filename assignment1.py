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
    ...
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
def before(date: str) -> str:
    "Returns previous day's date as YYYY-MM-DD"
    ...

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
    ...

def dbda(start_date: str, step: int) -> str:
    "given a start date and a number of days into the past/future, give date"
    # create a loop
    # call before() or after() as appropriate
    # return the date as a string YYYY-MM-DD
    ...

if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    # output the result
    ...
