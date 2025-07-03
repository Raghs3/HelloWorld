burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

# meals = [(burger, topping) for burger in burgers for topping in toppings]
for meals in [(burger, topping) for burger in burgers for topping in toppings]:  # product of two lists, exists in standard library
    print(meals)

print()

# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))

for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)
