# Pandas Library - a python data analysis library for tabular data

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# # avg_temp = sum(temp_list) / len(temp_list)
# # print(avg_temp)

# avg_temp = data["temp"].mean()
# print(avg_temp)

# # max in a series
# max_temp = data["temp"].max()
# print(f"max temp is {max_temp}\n")

# # get data in columns
# print(data["condition"])
# # or
# print(data.condition)
# print(data.day)

# # get data in a row
# print(data[data.day == "Tuesday"])

# # getting the row with max temp
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])

