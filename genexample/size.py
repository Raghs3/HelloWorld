import sys


def my_range(n: int):
    start = 0
    while start < n:
        yield start
        start += 1


# big_range = range(5)  # after changing value of range, size of range still same while size of list 10 times
big_range = my_range(5)

print(f"big_range is {sys.getsizeof(big_range)} bytes")

# create a list containing all the values in big_range
big_list = []
for val in big_range:
    big_list.append(val)

print(f"big_list is {sys.getsizeof(big_list)} bytes")

# both are iterators but big_range is a special case called generator
print(big_range)  # generator object
print(big_list)  # list
