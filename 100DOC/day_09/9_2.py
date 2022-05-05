# Grading Program Exercise

student_scores = {
    "Vivek": 99,
    "Sneha": 100,
    "Momo": 53,
    "Rocket": 12,
    "Amit": 86,
    "Diablo": 66
}

# create a new empty dictionary for grades
student_grades = {}

for i in student_scores:
    score = student_scores[i]
    if score > 90:
        student_grades[i] = "Outstanding"
    elif score > 80:
        student_grades[i] = "Exceeds Expectations"
    elif score > 70:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"

print(student_grades)



