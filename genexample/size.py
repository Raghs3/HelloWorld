import sys

big_range = range(10000)  # after changing value of range, size of range still same while size of list 10 times

print(f"big_range is {sys.getsizeof(big_range)} bytes")

# create a list containing all the values in big_range
big_list = []
for val in big_range:
    big_list.append(val)

print(f"big_list is {sys.getsizeof(big_list)} bytes")
