# Nesting

# nesting a List within a dictionary
# nesting a dictionary within a dictionary

India = {
    "States": {
        "Rajasthan": [
                      'Ajmer',
                      'Jaipur',
                      'Jodhpur',
                      'Jaisalmer'
                     ],
        "Gujarat": [
                    'Surat',
                    'Ahmedabad',
                    'Vadodara'
                   ],
               },
    "Population": 1.4,
    "info": [
                    {"hindi": "north india", "malayalam": "kerela", "Bengali": "West Bengal"},
                    {"tiger": "ranthambore", "camel": "rajasthan", "Gaur": "goa"},
                    {"UP": "taj mahal", "rajasthan": "hawa mahal", "MP": "Khajurao"}
                  ]
}

print(India)
print("_____________________________________________________________________________________________")

for i in India:
    print(i)
    print(India[i])
print("_____________________________________________________________________________________________")

# printing items from the dictionary "India"
print(India["States"])
print(India["Population"])
print(India["info"])
print("_____________________________________________________________________________________________")


# printing individual item from a list nested within a dictionary
print(India["info"][0])
print(India["info"][1])
print(India["info"][2])
print("_____________________________________________________________________________________________")

# printing individual item from a dictionary nested within a dictionary
print(India["States"]["Gujarat"])