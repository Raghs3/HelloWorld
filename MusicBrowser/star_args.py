# # print("Hello", "planet", "earth")  # values are wrapped in tuple, *args is unpacked values in tuple
#
#
# def average(*args):  # gives error if it is only args without star
#     print(type(args))
#     print(f"args is {args}")
#     print("*args is: ", *args)  # represents unpacked tuple, *args tells python to expect unpacked tuple
#     mean = 0  # `*` unpacks tuple but when in param, it means args will be unpacked tuple, and will be packed in to args param
#     for arg in args:
#         mean += arg
#     return mean / len(args)  # in python2 it does integer division
#
# print(average(1, 2, 3, 4))
#
#
# def build_tuple(*args):  # challenge
#     return args
#
#
# #test
# message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
# print(type(message_tuple))
# print(message_tuple)
#
# number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
# print(type(number_tuple))
# print(number_tuple)


def print_backwards(*args, file=None):
    for word in args[::-1]:
        print(word[::-1], end=' ', file=file)

with open("backwards.txt", 'w') as backwards:
    print_backwards('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', file=backwards)

# ** unpacks a dictionary, dict used as keyword args are specified as keywords and value, like a dict
