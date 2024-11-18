# in -ve  43210987654321
#         01234567890123
parrot = "Norwegian Blue"

print(parrot[0:6:2])  # Nre
print(parrot[0:6:3])  # Nw

number = "9,223;372:036 854,775;807"
# print(number[1::4])  # prints the seperators
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators
                  else " " for char in number).split()
print(values)
print([int(val) for val in values])


# print(parrot[0:6])  # Norweg, last character is not incl (upto but not incl)
# print(parrot[-14:-8])

# print(parrot[-4:-2])  # Bl
# print(parrot[-4:12])  # Bl


# print(parrot[3:5]) 
# print(parrot[0:9])
# print(parrot[:9])  # default start is 0 i.e start of str
# 
# print(parrot[10:14])  # : is necessary otherwise it is not slicing
# print(parrot[10:])  # default end is end of str
# 
# print(parrot[:6])
# print(parrot[6:])
# 
# print(parrot[:6] + parrot[6:])
# 
# print(parrot[:])  # == print(parrot)
# 
# letters = "abcdefghijklmnopqrstuvwxyz"


# print(parrot)
# 
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])
# 
# print()
# 
# print(parrot[-1])
# print(parrot[-14])
# 
# print()
# 
# print(parrot[-11])
# print(parrot[-1])  # or [-10]
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])
# 
# print()
# 
# print(parrot[3 - 14])  # -ve index value can be obtained by subtracting str len
# print(parrot[4 - 14])
# print(parrot[9 - 14])
# print(parrot[3 - 14])
# print(parrot[6 - 14])
# print(parrot[8 - 14])
