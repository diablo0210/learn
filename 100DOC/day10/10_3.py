# Docstrings
# """_""" can also be used for multi line comments
"""A Python docstring is a string used to document a Python module, class, function or method, so programmers can understand what it does without having to read the details of the implementation.
"""

# eg: Leap Year Function

def is_leap(year):
    """this function is used to identify any year as a leap year or not."""
    x = int(year)
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                print(f"{x} is a Leap Year.")
            else:
                print(f"{x} is NOT a Leap Year.")
        else:
            print(f"{x} is a Leap Year.")
    else:
        print(f"{x} is NOT a Leap Year.")

is_leap(1997)
