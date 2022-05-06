# Creating a Dataframe from scratch
import pandas

data_dict = {
    "students": ["Neha", "Kanika", "Momo", "Arya"],
    "scores": [56, 78, 98, 90]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")