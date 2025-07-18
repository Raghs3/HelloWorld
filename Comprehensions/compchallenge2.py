# Create a comprehension that returns a list of all the locations that have an exit to the forest.
# The list should contain the description of each location, if it's possible to get to the forest from there.
#
# The forest is location 5 in the locations dictionary
# The exits for each location are represented by the exits dictionary.
#
# Remember that a dictionary has a .values() method, to return a list of the values.
#
# The forest can be reached from the road, and the hill; so those should be the descriptions that appear in your list.
#
# Test your program with different destinations (such as 1 for the road) to make sure it works.
#
# Once it's working, modify the program so that the comprehension returns a list of tuples.
# Each tuple consists of the location number and the description.
#
# Finally, wrap your comprehension in a for loop, and print the lists of all the locations that lead to each of the
# other locations in turn.
# In other words, use a for loop to run the comprehension for each of the keys in the locations dictionary.


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

# soln
loc = 5
forest = [locations[xit] for xit in exits if loc in exits[xit].values()]  # refactoring exit here doesn't change in 2nd comp as scope limited to comp only
print(forest)
# soln
forest = []
for xit in exits:  # here important to use diff variable unlike comprehension as in global scope here
    if loc in exits[xit].values():
        forest.append(locations[xit])
print(forest)

print()
# soln challenge 3
for loc in sorted(locations):  # no need to sort in 3.6 but it is not reliable so better to sort
    forest = []
    for xit in exits:  # here important to use diff variable unlike comprehension as in global scope here
        if loc in exits[xit].values():
            forest.append((xit, locations[xit]))
    print("Locations leading to {}".format(loc), end='\t')
    print(forest)


# soln challenge 2
# for loc in sorted(locations):  # no need to sort in 3.6 but it is not reliable so better to sort
#     forest = [(exit, locations[exit]) for exit in exits if loc in exits[exit].values()]
#     print("Locations leading to {}".format(loc), end='\t')
#     print(forest)




# # challenge 2  # I failed
# results = [(locations[x], "yes") if x == 1 or x == 2 else (locations[x], "no") for x in locations]
# print(results)
#
#
# # challenge 3  # I failed
# result = []
# for x in locations:
#     if x in exits:
#         result.append("yes")
#     else:
#         result.append("no")
# print(result)
