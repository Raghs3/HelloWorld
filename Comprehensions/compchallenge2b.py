import timeit

setup = """\
gc.enable()
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
"""
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

# print("nested for loops")
# print("----------------")
# nested_loop = """\
def nested_loop():
    result = []
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
        result.append(exits_to_destination_1)
        # print("Locations leading to {}".format(loc), end='\t')
        # print(exits_to_destination_1)
    # print the result before returning
    for x in result:
        pass

    return result

print()

# print("List comprehension inside a for loop")
# print("------------------------------------")
# loop_comp = """\
def loop_comp():
    result = []
    for loc in sorted(locations):
        exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
        result.append(exits_to_destination_2)
        # print("Locations leading to {}".format(loc), end='\t')
        # print(exits_to_destination_2)
        # print the result before returning
    for x in result:
        pass

    return result
# print()

# print("nested comprehension")
# print("--------------------")
# nested_comp = """\
def nested_comp():
    exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                              for loc in sorted(locations)]
    # for index, loc in enumerate(exits_to_destination_3):
    #     print("Locations leading to {}". format(index), end='\t')
    #     print(loc)
    # print the result before returning
    for x in exits_to_destination_3:
        pass

    return exits_to_destination_3


def nested_gen():
    exits_to_destination_3 = ([(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                              for loc in sorted(locations))
    for x in exits_to_destination_3:
        pass
    return exits_to_destination_3


print(nested_loop())
print(loop_comp())
print(nested_comp())

result_1 = timeit.timeit(nested_loop, setup, number=1000)  # only works with functions if they don't require arguments
result_2 = timeit.timeit(loop_comp, setup, number=1000)
result_3 = timeit.timeit(nested_comp, setup, number=1000)
result_4 = timeit.timeit(nested_gen, setup, number=1000)
print("Nested loop:\t{}".format(result_1))
print("Loop and comp:\t{}".format(result_2))
print("Nested comp:\t{}".format(result_3))
print("Nested gen:\t{}".format(result_4))  # 10 times faster, but perf penalty when iterating over the generator

# use setup when possible as it allows to be specific, but we used globals here for namespace
# using setup coz it is easy to do that here
