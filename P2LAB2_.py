# Your Name
# Date
# Assignment Name
# Assignment tests student's knowledge
# of how to write code that uses a dictionary to store user input and
# displays output to the user

car_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
    }
car_list = car_dict
print("The keys in the dictionary are: ")
print(*car_list, sep=", ")
print()
vehicle = input("Enter a vehicle to see it mpg: ")
print()
#mpg = car_dict[vehicle]
mpg = car_dict.get(vehicle)
print("The " + vehicle + " gets",mpg,"mpg.")
print()
miles = float(input("How many miles will drive the " + vehicle + "? "))
print()
gallons = miles/mpg
print(f'{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.')
