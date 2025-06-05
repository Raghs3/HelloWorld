# print("Hello", "planet", "earth")  # values are wrapped in tuple, *args is unpacked values in tuple


def average(*args):  # gives error if it is only args without star
    print(type(args))
    print(f"args is {args}")
    print("*args is: ", *args)  # represents unpacked tuple, *args tells python to expect unpacked tuple
    mean = 0  # `*` unpacks tuple but when in param, it means args will be unpacked tuple, and will be packed in to args param
    for arg in args:
        mean += arg
    return mean / len(args)  # in python2 it does integer division

print(average(1, 2, 3, 4))


def build_tuple(*args):  # challenge
    return args
