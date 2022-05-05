#Tresure Island

print("Welcome to the Treasure Island!!!\nYour mission is to find the hidden treasure.")
lr = input("In which direction would you like to proceed first? Left or Right :\n").lower()
if lr == "right":
    print("Game Over!")
elif lr == "left":
    sw = input("There is a river with a strong current. Would you like to swim or wait?\n").lower()
    if sw == "swim":
        print("Game Over!")
    elif sw == "wait":
        color = input("There are three doors of different colors. Which color do you choose? Red, Blue or Yellow?\n").lower()
        if color == "red":
            print("Game Over!")
        elif color == "blue":
            print("Game Over!")
        elif color == "yellow":
            print("You won!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")