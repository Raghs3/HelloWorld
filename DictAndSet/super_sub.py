animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Aardvark',
           'Cat',
           }
birds = {'Robin', 'Swallow', 'Wren'}

print(f'birds is a subset of animals: {birds.issubset(animals)}')
print(f'animals is a superset of birds: {animals.issuperset(birds)}')

print(f'birds is a superset of animals: {birds.issuperset(animals)}')

print(birds <= animals)  # subset or not
print(birds < animals)  # proper subset or not

print('*' * 70)

garden_birds = {'Robin', 'Wren', 'Swallow'}
print(garden_birds == birds)
print(garden_birds <= birds)  # subset or not
print(garden_birds < birds)  # proper subset or not

print('*' * 70)

more_birds = {'Wren', 'Swallow', 'Budgie'}
print(garden_birds >= more_birds)  # superset or not
