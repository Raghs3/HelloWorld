menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
print(meals)  # same as comprehension

# meals = [meal for meal in menu if "spam" not in meal]  # can't have else when if used (filter)
# meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]  # makes it simpler to read
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meals)

fussy_meals = [meal for meal in menu if "spam" or "eggs" in meal if not
                ("bacon" in meal and "sausage" in meal)]  # two filter
print(fussy_meals)

fussy_meals = [meal for meal in menu if  # single filter
               ("spam" in meal or "eggs" in meal) and not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)
