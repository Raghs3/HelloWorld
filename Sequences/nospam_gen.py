menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],  # idk pep8 thing
]

# tim soln 1
# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(meal)

# tim soln 2
for meal in menu:
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)

# my tim edited soln
# for meal in menu:
#     top_index = len(meal) - 1
#     for index, item in enumerate(reversed(meal)):
#         if item == "spam":
#             del meal[top_index - index]
#     print(meal)


# my soln
# for meal in menu:
#     if "spam" in meal:
#         count = meal.count("spam")
#         for i in range(count):
#             meal.remove("spam")
#         print(meal)
#     else:
#         print(meal)


# for meal in menu:
#     for item in meal:
#         if item == "spam":
#             continue
#         else:
#             print(item, end=", ")
#     print()