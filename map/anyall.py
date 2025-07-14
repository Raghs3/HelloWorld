entries = [1, 2, 3, 4, 5]

print("all: {}".format(all(entries)))
print("any: {}".format(any(entries)))  # both return true # because all/any value in entries is true value

print("Iterable with a 'False' value")
entries_with_zero = [1, 2, 0, 4, 5]
print(f"all: {all(entries_with_zero)}")  # now return false
print(f"any: {any(entries_with_zero)}")
