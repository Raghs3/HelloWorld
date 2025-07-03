burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

# meals = [(burger, topping) for burger in burgers for topping in toppings]
for meals in [(burger, topping) for burger in burgers for topping in toppings]:  # product of two lists, exists in standard library
    print(meals)  # iterates over burger and topping (two iteration parts), not a nested comprehension necessarily

print()

# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))

for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:  # nested list of tuples
    print(nested_meals)  # expression is another list comprehension, outer iteration values used first

print()

for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]:
    print(nested_meals)  # changing order of iteration
