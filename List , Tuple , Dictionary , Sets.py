##python lists using various methods
#creating a list 
bikes = ["Trek", "Cannondale", "Specialized", "Giant", "Scott"]
#append
bikes.append("Bianchi")
print(bikes)  
#insert
bikes.insert(2, "Merida")
print(bikes) 
#remove
bikes.remove("Giant")
print(bikes)  
#copy
bikes_copy = bikes.copy()
print(bikes_copy)  
#count
num_specialized = bikes.count("Specialized")
print(num_specialized)  
#extend
more_bikes = ["Kona", "Santa Cruz"]
bikes.extend(more_bikes)
print(bikes)  
#index
index_specialized = bikes.index("Specialized")
print(index_specialized)  
#sort
bikes.sort()
print(bikes)  
#reverse
bikes.reverse()
print(bikes) 
#clear
bikes.clear()
print(bikes) 
#pop
bikes = ["Trek", "Cannondale", "Specialized", "Giant", "Scott"]
last_bike = bikes.pop()
print(last_bike)  
print(bikes) 

#bike brands in uppercase
bike_brands = ["Trek", "Cannondale", "Specialized", "Giant", "Scott"]
uppercased_bike_brands = [brand.upper() for brand in bike_brands]
print("Uppercased bike brands:", uppercased_bike_brands)
#lengths of each bike
brand_lengths = [len(brand) for brand in bike_brands]
print("Lengths of bike brand names:", brand_lengths)
#bike brands that contain with letter 'a'
brands_with_a = [brand for brand in bike_brands if 'a' in brand]
print("Bike brands containing 'a':", brands_with_a)
#list of tuples and bike brands and their lengths
brand_length_pairs = [(brand, len(brand)) for brand in bike_brands]
print("Bike brand-length pairs:", brand_length_pairs)
#bike models
bike_models = [["Domane", "Émonda", "Madone"], ["Synapse", "SuperSix"], ["Allez", "Tarmac", "Roubaix"]]
flattened_models = [model for sublist in bike_models for model in sublist]
print("Flattened list of bike models:", flattened_models)
#bike brands with models in uppercase
bike_brands = ["Trek", "Cannondale", "Specialized"]
bike_models = [
    ["Domane", "Émonda", "Madone"],  
    ["Synapse", "SuperSix"],         
    ["Allez", "Tarmac", "Roubaix"]   
]
print("Bike brands with models in uppercase:", bike_models)
#indexing

#positive indexing

first_bike = bike_brands[0]  
second_bike = bike_brands[1]  

print("First bike brand:", first_bike)  
print("Second bike brand:", second_bike)  

#negative indexing

last_bike = bike_brands[-1]  
second_last_bike = bike_brands[-2]  

print("Last bike brand:", last_bike)  
print("Second last bike brand:", second_last_bike) 

#retrieve
third_bike = bike_brands[2]  

print("Third bike brand:", third_bike)  
#update 
# Update the fourth bike brand from 'Giant' to 'Bianchi'
bike_brands[3] = "Bianchi"

print("Updated bike brands:", bike_brands)

#retreve and update
# Retrieve the second bike brand
second_bike = bike_brands[1]
print("Retrieved second bike brand:", second_bike)  

# Update the first bike brand to 'Merida'
bike_brands[0] = "Merida"
print("Updated bike brands:", bike_brands)

##slicing 
bike_brands = ["Trek", "Cannondale", "Specialized", "Giant", "Scott"]

# Positive Slicing
# Retrieve a portion of the list from index 1 to 3 (excluding 3)
subset_positive = bike_brands[1:3]
print("Subset (positive slicing):", subset_positive)  

# Negative Slicing
# Retrieve a portion of the list from index -4 to -2 (excluding -2)
subset_negative = bike_brands[-4:-2]
print("Subset (negative slicing):", subset_negative)  

# Retrieve a Portion of the List
# Retrieve bikes from the start up to (but not including) index 3
first_three_bikes = bike_brands[:3]
print("First three bikes:", first_three_bikes)  

# Retrieve bikes from index 2 to the end
bikes_from_third = bike_brands[2:]
print("Bikes from third to end:", bikes_from_third)  

# Update Elements Within a Slice
# Update bikes from index 1 to 3
bike_brands[1:3] = ["Merida", "Bianchi"]
print("Updated bike brands:", bike_brands)

# Delete Elements from a Slice
# Delete bikes from index 2 to 4
del bike_brands[2:4]
print("Bike brands after deletion:", bike_brands)

# Insert Elements into a Specific Position
bike_brands[1:2] = ["Cervelo", "Pinarello"]
print("Bike brands after insertion:", bike_brands)

bike_brands = ["Trek", "Cannondale", "Specialized", "Giant", "Scott"]
bike_prices = [1000, 1200, 1500, 1100, 1300]

# reduce Example
total_cost = reduce(lambda x, y: x + y, bike_prices)
print("Total cost of all bikes:", total_cost)

# map Example
uppercased_brands = list(map(lambda brand: brand.upper(), bike_brands))
print("Uppercased bike brands:", uppercased_brands)

# filter Example
long_brands = list(filter(lambda brand: len(brand) > 6, bike_brands))
print("Bike brands with more than 6 characters:", long_brands)

#zip 
brand_price_pairs = list(zip(bike_brands, bike_prices))
print("Bike brand-price pairs:", brand_price_pairs)


###tuples

# Basic Bike Information
bike_info = ("Road Bike", "23", "Shimano")  

# Bike Parts Tuple (with Nesting)
bike_parts = (
    ("Frame", "Aluminum"),  
    ("Fork", "Carbon Fiber"),
    ("Wheels", (27.5, 2.1)),  
    ("Drivetrain", ("Shifters", "Derailleurs", "Cassette")),  
)

# Bike Inventory (List of Tuples)
inventory = [
    ("Mountain Bike", "M", 1200),
    ("Hybrid Bike", "L", 800),
    ("Cruiser Bike", "S", 500),
]  

# Using a Namedtuple for Bike Specs
from collections import namedtuple

BikeSpecs = namedtuple("BikeSpecs", ["model", "frame_size", "price"])

###Dictionary

 # Using a dictionary to represent bike short codes and their corresponding meanings
bike_short_codes = {
    'MTB': 'Mountain Bike',
    'RB': 'Road Bike',
    'BMX': 'BMX Bike',
    'CTY': 'City Bike',
    'EL': 'Electric Bike'
}

# Accessing the meaning of a bike short code
print(bike_short_codes['MTB'])  
# Adding a new bike short code
bike_short_codes['CR'] = 'Cruiser Bike'
# Removing a bike short code
removed_meaning = bike_short_codes.pop('BMX')
# Updating the meaning of a bike short code
bike_short_codes['CTY'] = 'City Commuter Bike'
# Dictionary comprehension to create a subset of bike short codes
urban_bikes = {code: meaning for code, meaning in bike_short_codes.items() if 'City' in meaning}
print(urban_bikes)  

##sets

# Define sets of bike short codes
bike_short_codes = {'MTB', 'RB', 'BMX', 'CTY', 'EL'}
# Checking membership
print('MTB' in bike_short_codes)  
print('CR' in bike_short_codes)   
# Adding new bike short codes
bike_short_codes.add('CR')
bike_short_codes.update({'RR', 'BMX'})  
# Removing bike short codes
bike_short_codes.remove('BMX')
bike_short_codes.discard('RR')  
# Set operations
other_bike_short_codes = {'RB', 'CTY', 'TT'}
common_codes = bike_short_codes.intersection(other_bike_short_codes)
all_codes = bike_short_codes.union(other_bike_short_codes)
unique_codes = bike_short_codes.difference(other_bike_short_codes)
print(common_codes)  
print(all_codes)     
print(unique_codes)  

#-----



