# implement a program that prompts the user for a vanity plate
# and then output Valid if meets all of the requirements or Invalid if it does not.
# Assume that any letters in the user’s input will be uppercase.
# Structure your program per the below, wherein is_valid returns True if s meets all requirements
# and False if it does not.
# Assume that s will be a str.

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if max_min_chars(s):
        if start_two_letters(s) and other_symbols(s) and numbers_at_end(s):
            return True
        else:
            return False
    else:
        return False

def start_two_letters(plate):
    # “All vanity plates must start with at least two letters.”
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    first_two = plate[:2]
    for char in first_two:
        if char in numbers:
            return False
    return True

def max_min_chars(plate):
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(plate) >= 2 and len(plate) <= 6:
        return True
    else:
        return False

def numbers_at_end(plate):
    # “Numbers cannot be used in the middle of a plate; they must come at the end.
    # The first number used cannot be a ‘0’
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    num = 0
    for char in plate:
        if char in numbers:
            num += 1
            if char == "0" and num == 1:
                return False
        if char not in numbers and num > 0:
            return False
    return True

def other_symbols(plate):
    # “No periods, spaces, or punctuation marks are allowed.”
    invalid_chars = [".", ";", ":", ",", "!", "?", "-", "+", "=", " "]
    for char in plate:
        if char in invalid_chars:
            return False
    return True

main()