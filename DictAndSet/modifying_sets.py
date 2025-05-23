# numbers = {}  # This is a dictionary
# numbers = {*""}  # This is a set, but try not to do this
# numbers = {*{}}  # This is a set as well, after `*` anything can be put
numbers = set()

print(numbers, type(numbers))

# numbers.add(1)
# print(numbers)

# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value: "))
#     numbers.add(next_value)
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# Create a set from the list, to remove duplicates.
unique_data = sorted(set(data))
print(unique_data)

# Create a list of unique colours, keeping the order they appeared in.
unique_data = list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data))
