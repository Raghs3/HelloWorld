entries = []

if entries:  # here it evaluates as false
    print("all: {}".format(all(entries)))  # gives true in empty list, documented behaviour(rem)
else:
    print(False)
    print("any: {}".format(any(entries)))
