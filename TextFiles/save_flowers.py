data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plants_filename = "flowers_print.txt"
#
# with open(plants_filename, 'w') as plants:
#     for plant in data:
#         print(plant, file=plants)  # prints to file
#
# new_list = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())  # removes new line character
#
# print(new_list)

# plants_filename = "flowers_write.txt"
#
# with open(plants_filename, 'w') as plants:
#     for plant in data:
#         plants.write(plant)  # single line of text
#
# print(data)
# string_representation = data.__str__()  # string representation
# print(type(string_representation))

filename = "test_numbers.txt"
with open(filename, 'w') as test:
    for i in range(10):
        print(i, file=test)  # we can print numbers to a file but not write them
                             # print calls __str__ so automatically becomes str representation
with open(filename, 'w') as test:
    for i in range(10):
        test.write(str(i) + "\n")  # arg must be str
