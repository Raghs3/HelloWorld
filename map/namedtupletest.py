from tkinter.scrolledtext import example

from data import basic_plants_list, plants_list

print(plants_list[0])  # output - P(name=............)  # so avoid having tuple name and typename diff

# for plant in basic_plants_list:
#     print(plant[0])

for plant in plants_list:
    print(plant.name, plant[1])  # makes readable and don't need to rem the posn, but we can still use indexing if we want
# named tuples have three extra features normal tuples don't have and are prefixed with `_`
print()

example = plants_list[0]
print(example)
example = example._replace(lifecycle='Annual')  # changes value at lifecycle field
print(example)
