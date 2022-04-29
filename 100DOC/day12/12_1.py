# Scope

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}.")

increase_enemies()

print(f"enemies outside function: {enemies}.")

# Local Scope : exists within functions; the variables are local and doesn't exist outside the function

# Global Scope:variables declared outside the functions; defined at the top level and available anywhere in the function.