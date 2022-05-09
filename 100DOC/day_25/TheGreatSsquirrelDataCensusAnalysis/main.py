# The Great Squirrel Data Census

import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)

# fur_color = data["Primary Fur Color"]
# print(fur_color.count())
# # print(fur_color)

color_count_data = data["Primary Fur Color"].value_counts()
print(color_count_data)
color_count_data.to_csv("squirrel_count.csv")


#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [data["Primary Fur Color"].value_counts()]
# }
#
# print(data_dict)