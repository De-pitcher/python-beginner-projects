#!python3
# main.py - uses a regular expression that can detect dates in the DD/MM/YYYY format.
import re

datePattern = re.compile(r'''^(0[1-9]|[1-2]\d|3[0-1])   # Matches the day (01-31).
                         /(0[1-9]|1[0-2])               # Matches the month (01-12).
                         /([1-2]\d{3})$                 # Matches the year (1000-2999).
                         ''', re.VERBOSE)

def isValidDate(day, month, year):
    # Check if month has 30 days
    if month in [4, 6, 9, 11]:
        return day <= 30
    
    # Check if February (leap year)
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return day <= 29
        else:
            return day <= 28
        
    return day <= 31

print('Enter a date in the format DD/MM/YYY: ')
dateStr = input()
match = datePattern.match(dateStr)
if match:
    day, month, year = map(int, match.groups())
    if isValidDate(day, month, year):
        print("Valid date:", dateStr)
    else:
        print("Invalid date:", dateStr)
else:
    print("Invalid format:", dateStr)