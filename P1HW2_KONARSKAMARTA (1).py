#Marta Konarska
#03/07/2024
#P1HW2


print("This program calculates and displays travel expenses")
print("")
budget = int(input("Enter Budget: "))
print("")
location = input("Enter your travel destination: ")
print("")
gas = int(input("How much do you think you will spend on gas? "))
print("")
hotel = int(input("Approximately, how much will you need for accomondation/hotel? "))
print("")
food = int(input("Last, how much do you need for food? "))
print("")
print("------------Travel Expenses------------:")
print(f"Location:                       " + str(location) + '.')
##print(Location: ",location)
print(f"Initial Budget:                ",  "${: .2f}". format(budget))
print(f"Fuel:                             ",  "${: .2f}". format(gas))
print(f"Accomodation:              ", "${: .2f}". format(hotel))
print(f"Food:                            ","${: .2f}". format(food))
print("-------------------------------------------")
balance = budget - gas - hotel - food
##print("Remaining Balance: ",balance)
print(f"Remaining Balance:       ", "${: .2f}". format(budget - gas - hotel - food))
