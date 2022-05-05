# painting the wall: Calculate the number of paint cans required to paint a wall

# Define a function called paint_calc()
# height = height of the wall to be painted
# width = width of the wall to be painted
# coverage = coverage area by one can of paint
# num_cans = number of cans required to paint the wall
import math

def paint_calc(height, width, coverage):
    num_cans = (height * width) / coverage
    print(f"You will need {math.ceil(num_cans)} number of cans.")
#     instead of using round(), we are using math.ceil() so as to round of to the nearest largest whole num.
#       round(2.3) = 2; math.ceil(2.3) = 3

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
test_c = 5
paint_calc(height=test_h, width=test_w, coverage=test_c)
