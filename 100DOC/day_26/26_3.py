# Dictionary Comprehension : new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,Value) in dict.items() if test}

import random

names = ["sneha", "vivek", "momo", "rocket", "arya", "amit"]
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)