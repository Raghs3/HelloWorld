numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=";")  # only single value printed so sep char not used
# print(*numbers, sep=";")  # '*' unpacks any seq type
# print(0, 1, 2, 3, 4, 5, sep=";")


def test_star(*args):  # '*' used in reverse i.e. param is unpacked sequence and it packs it
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()  # prints an empty tuple and doesnt crash program
