#given the following properties with the following observations and features

"""  
House 1. price: $115910
         rooms: 4
         Area: 128 m^2

House 2. price: $48718
        rooms: 3
            Area: 210 m^2
            
House 3. price: 28977
        rooms:2
        Area:58 m^2

House 4: price: 83,903
        ROOMS: 3
        Area: 111 m^2
"""

####Organizing the data into lists

house_0_list = [115910.26, 128, 4]
house_1_list = [48718, 210, 3]
house_2_list = [28977, 58, 2]
house_3_list = [83903, 111, 3]

# To determine price per square meter for house 1

price = house_0_list[0]
area = house_0_list[1]

house_0_price_m2 = price/area
print("price per square meter for house 0 is:", house_0_price_m2, "m^2")

house_0_list.append(house_0_price_m2)
print(house_0_list)

house_nested_list =[[115910.26, 128, 4],
                    [48718, 210, 3],
                    [28977, 58, 2],
                    [83903, 111, 3]]


###Organizing Data into Dictionaries

#declaring dictionary variables for the above properties

house_0_dict = {"price_approx_usd":115910.26, "area_in_m2":128, "rooms": 4}
house_1_dict = {"price_approx_usd":48718, "area_in_m2":210, "rooms":3}
house_2_dict = {"price_approx_usd":28977,"area_in_m2":58, "rooms":2}
house_3_dict = {"price_approx_usd":83903, "area_in_m2":111, "rooms":3}

#calculating price per meters squared using dictionaries

price_house_0 = house_0_dict['price_approx_usd']
area_house_0 = house_0_dict["area_in_m2"]

price_house_0_per_m2 = price_house_0/area_house_0

print(price_house_0_per_m2)

# to add the value/feature in to the dictionary

house_0_dict["price_m2"] = price_house_0_per_m2

print(house_0_dict)

# to combine them all, it would be best to put them in a list

# Declare variable `houses_rowwise`
houses = [
    {
        "price_approx_usd": 115910.26,
        "area_in_m2": 128,
        "rooms": 4,
    },
    {
        "price_approx_usd": 48718.17,
        "area_in_m2": 210,
        "rooms": 3,
    },
    {
        "price_approx_usd": 28977.56,
        "area_in_m2": 58,
        "rooms": 2,
    },
    {
        "price_approx_usd": 36932.27,
        "area_in_m2": 79,
        "rooms": 3,
    },
    {
        "price_approx_usd": 83903.51,
        "area_in_m2": 111,
        "rooms": 3,
    },
]

# To calculate the price per square meter in the house list

for house in houses:
    price_per_m2 = house["price_approx_usd"] / house["area_in_m2"]
    house["price_per_m2"] = price_per_m2
    
print(houses)

###calculating the mean price for the houses

house_prices =[]
for house in houses:
    house_prices.append(house['price_approx_usd'])
    
mean_price = sum(house_prices)/len(house_prices)

print("mean price =",mean_price)


#### Using Pandas dataframe to organize the data

price_apro_usd = []
surface_covered_m2 = []
rooms = []

for house in houses:
    price_apro_usd.append(house["price_approx_usd"])
    surface_covered_m2.append(house["area_in_m2"])
    rooms.append(house["rooms"])

import pandas as pd