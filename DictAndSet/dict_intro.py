vehicles = {
    'dream': 'Honda 250T',  # key: value
    # 'roadster': 'BMW R1100',  # in intellij use light bulb to remove entry
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT6505',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple',
}

vehicles["starfighter"] = "Lockheed F-104"  # no append method in dict so use key to assign value
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

# upgrade the virago
vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", "You wish! Sell the Learjet and you might afford a racing car.")
print(result)
plane = vehicles.pop("learjet")  # del better than pop
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()


# my_car = vehicles['Fiesta']  # key is used as index
# print(my_car)  # in indexing we get error if wrong key 
# 
# commuter = vehicles['virago']
# print(commuter)  # indexing faster than get method
# 
# learner = vehicles.get("ER5")  # another way to retrieve values
# print(learner)  # key is case sensitive, returns None


# for key in vehicles:
#     print(key, vehicles[key], sep=": ")  # dict is iterable but over keys

for key, value in vehicles.items():  # better than above method
    print(key, value, sep=": ")
