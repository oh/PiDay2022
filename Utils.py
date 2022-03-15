import re


def read_and_tally_digits_up_to_i(i):
    # Open the file and initialize the tally
    f = open("resources/1milpi.txt", "r")
    int_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Read the file up to the number
    digits = f.read(int(i))

    # Count the digits
    for digit in digits:
        # Access the tally via index and increment the tally
        int_count[int(digit)] += 1

    # Close the file
    f.close()

    return int_count


def validate_only_numbers_in_string(s):
    # Check if the string is empty
    if len(s) == 0:
        return False

    # Use Regular Expressions to check if the string only contains numbers
    return re.search("[0-9]", s)
