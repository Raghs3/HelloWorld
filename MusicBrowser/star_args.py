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


# def print_backwards(*args, **kwargs):  # now the user enters the keyword and value pairs, and it gets unpacked like a dict
# def print_backwards(*args, end=' ', **kwargs):  # method 1 to fix multiple value, add end param to function def
def print_backwards(*args, **kwargs):  # method 2, remove it from kwargs dict
    print(kwargs)
    kwargs.pop('end', None)
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)  # don't have to specify file=file, can use as many kwargs as the user wants

with open("backwards.txt", 'w') as backwards:
    # print_backwards('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', file=backwards, end='\n')  # multiple values for keyword arg end in print, so error
    print_backwards('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end='\n')
    print("Another string")  # appears on same line as above

# ** unpacks a dictionary, dict used as keyword args are specified as keywords and value, like a dict
print()
print('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end='\n', sep='|')
print_backwards('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end='\n', sep='|')
