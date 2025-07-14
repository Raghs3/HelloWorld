entries = []

if entries:  # here it evaluates as false
    print("all: {}".format(all(entries)))  # gives true in empty list, documented behaviour(rem)
else:
    print(False)
    print("any: {}".format(any(entries)))

# result = entries and all(entries)  # gives empty list not false, have to be explicit
result = bool(entries) and all(entries)
print(result)
