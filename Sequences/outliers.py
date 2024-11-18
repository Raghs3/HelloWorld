# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 
#         160, 170, 183, 185, 187, 188, 191, 350, 360]  #len(data) == 18

# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 
#         160, 170, 183, 185, 187, 188, 191,]

# data = [104, 105, 110, 120, 130, 130, 150, 
#         160, 170, 183, 185, 187, 188, 191, 350, 360]

# data = [104, 105, 110, 120, 130, 130, 150, 
#         160, 170, 183, 185, 187, 188, 191]

# data = [4, 5, 350, 360]

data = []

# del data[0:2]
# print(data)
# del data[14:]  # as we deleted 2 items in line 4 so index of 350 changes
# print(data)

min_valid = 100
max_valid = 200

# for index, value in enumerate(data):  # doesnt work skips, over elements
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
# 
# print(data)

# THIS WORKS ONLY FOR SORTED DATA
# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging
del data[:stop]
print(data)

# stop = 0
# for index, value in enumerate(data):  # if we have billions going through all time consuming
#     if value >= max_valid:
#         stop = index
#         break
# 
# print(stop)  # for debugging
# del data[stop:]
# print(data)


# process the high values in the list
start = 0  # where to start deleting from
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # We have the index of the last item to keep
        # Set 'start' to the position of the first
        # item to delete, which is 1 after 'index'
        start = index + 1
        break

print(start)  # for debugging
del data[start:]
print(data)
