#   **kwargs - Many keyword arguments

def calculator(n, **kwargs):
    # print(kwargs)
    # print(type(kwargs))
    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculator(3, add=4, multiply=5)