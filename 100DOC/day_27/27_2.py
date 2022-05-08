#  *args - Many positional arguments/Unlimited arguments

def add(*args):
    # print(args)
    # print(type(args))
    sum = 0
    for n in args:
        sum += n
        # print(n)
    print(sum)


add(2, 5, 6, 9, 4)

add(1, 2, 3, 4, 5, 6, 7, 8, 9)
