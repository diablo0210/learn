# Python Packages
# PyPi - python package index

from prettytable import PrettyTable
my_table = PrettyTable()
my_table.field_names = ["City", "State", "Tier", "Climate"]
my_table.add_row(["Ajmer", "Rajasthan", "2", "Dry"])
my_table.add_row(["Panaji", "Goa", "2", "Humid"])
my_table.add_row(["Mumbai", "Maharashtra", "1", "Humid"])
my_table.add_rows(
    [
    ["Nashik", "Maharashtra", "2", "Dry"],
    ["Gurgaon", "haryana", "1", "Dry"]
    ]
)
# my_table.add_column("City", ["Jaipur", "Bokaro", "Kolkata"])
# my_table.add_column("State", ["Rajasthan", "Jharkhand", "West Bengal"])
# my_table.add_column("Tier", ["1", "2", "1"])
# my_table.add_column("Climate", ["Dry", "Dry", "Humid"])
my_table.align = "l"
print(my_table)
my_table.align = "r"
print(my_table)
