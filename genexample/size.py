import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))  # function is called 5 times
        yield start  # function finishes after returning so have to use yield instead so further lines can be executed
        start += 1  # yielding puts function in suspended state, doesn't actually end it

# _ = input("line 12")
# big_range = range(5)  # after changing value of range, size of range still same while size of list 10 times
big_range = my_range(5)  # function isn't actually executed here
# _ = input("line 15")
# don't need line 14, directly use my_range(5) in for loop, doing line 14 in some cases might even be a bad idea
print(next(big_range))  # call to my_range fn # now the for loop only goes from 1 to 4 instead of 0 to 4
print(f"big_range is {sys.getsizeof(big_range)} bytes")

# create a list containing all the values in big_range
big_list = []

# _ = input("line 22")
for val in big_range:  # for loop effectively calls next function
    # _ = input("line 24 - inside loop")
    big_list.append(val)  # function executed here, while running notice the start value continues on instead of restarting

print(f"big_list is {sys.getsizeof(big_list)} bytes")

# both are iterators but big_range is a special case called generator which works like a generator
print(big_range)  # generator object
print(big_list)  # list
