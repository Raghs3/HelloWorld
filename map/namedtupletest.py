from data import basic_plants_list, plants_list

print(plants_list[0])  # output - P(name=............)  # so avoid having tuple name and typename diff

for plant in basic_plants_list:
    print(plant[0])
