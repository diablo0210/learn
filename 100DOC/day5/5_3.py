# Highest Score

score_list = input("Enter the scores separated by space:\n").split()
print(score_list)

# using list function max() and min()
print(f"The total number of students is {len(score_list)}.")
print(f"The maximum score is {max(score_list)}.")
print(f"The minimum score is {min(score_list)}.")

# using the for loop
for n in range(0, len(score_list)):
    score_list[n] = int(score_list[n])
max = 0
for i in score_list:
    if i > max:
        max = i
print(f"The maximum score using for loop is {max}.")