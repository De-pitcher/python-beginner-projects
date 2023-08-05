#!python3
# main.py - Uses regular expression to make sure the password string it is passed is strong.
import re

def isStrongPassword(password):
    # Check if password is at least eight characters long
    if not re.search(r'.{8,}', password):
        return False

    # Check if password contains both uppercase and lowercase characters
    if not re.search(r'(?=.*[A-Z])(?=.*[a-z])', password):
        return False

    # Check if password has at least one digit
    if not re.search(r'(?=.*\d)', password):
        return False

    return True

print('Enter a password that is at least eight characters long, contains both uppercase and lowercase characters and has at least one digit: \n>', end='')
password = input()
if isStrongPassword(password):
    print(password + ': is a strong password')
else:
    print(password + ': is not a strong password')