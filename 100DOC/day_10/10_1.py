# Functions with Outputs

def format_name(first, last):
    if first == "" or last == "":
        return f"Invalid"
    formated_first = first.title()
    formated_last = last.title()
    return f"Result: {formated_first} {formated_last}"
# return tells the computer that this is the end of the function and you should now exit....hence nothing after return gets executed.

print(format_name(input("Enter first name: "), input("Enter last name: ")))
