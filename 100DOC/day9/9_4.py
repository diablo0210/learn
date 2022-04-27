#  write a program to add a dictionary within an existing dictionary

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#TODO: Write the function that will allow new countries to be added to the travel_log. 👇

def add_new_country(country_input, visits_input, cities_input):
    temp_dir = {
               "country": country_input,
               "visits": visits_input,
               "cities": cities_input,
                }
    travel_log.append(temp_dir)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



