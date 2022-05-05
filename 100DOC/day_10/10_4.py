# Calculator

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for i in operations:
        print(i)
symbol = input("Which operation do you want to perform: ")

function = operations[symbol]
answer = function(num1, num2)

print(f"{num1} {symbol} {num2} = {answer}.")