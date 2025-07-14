import timeit
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

for meal in menu:
    if "spam" not in meal:
        print(meal)

print("-" * 40)


def spamless_comp():
    # meals = [meal for meal in menu if "spam" not in meal]
    meals = [meal for meal in menu if not_spam(meal)]
    return meals


print("-" * 40)


def not_spam(meal_list: list):
    return "spam" not in meal_list


def spamless_filter():
    spamless_meals = list(filter(not_spam, menu))  # need to create a function that does filtering
    return spamless_meals  # filter takes 2 args, fn that does filtering and iterable to iterate over
    # output identical to comp

if __name__ == "__main__":
    print(spamless_comp())
    print(spamless_filter())
    print(timeit.timeit(spamless_comp, number=100000))
    print(timeit.timeit(spamless_filter, number=100000))  # taking nearly twice the time
    # mainly slower coz of overhead of the fn call of not_spam function
    # if comp also uses same fn as filter then filter is faster
