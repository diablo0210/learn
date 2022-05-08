# How to iterate over a Pandas Dataframe

student_dict = {
    "student": ["Vivek", "Sneha", "Momo"],
    "score": [89, 98, 55]
}

# looping through a dictionary
for (key, value) in student_dict.items():
    print(key)
    print(value)

import pandas

student_df = pandas.DataFrame(student_dict)
print(student_df)

# looping through a dataframe
for (key, value) in student_df.items():
    # print(key)
    print(value)

# iterrows : inbuilt loop in pandas : allows to loop through each of the rows in a dataframe
for(index, row) in student_df.iterrows():
    print(row.student)
    # print(row.score)
    # print(index)
    # print(row)