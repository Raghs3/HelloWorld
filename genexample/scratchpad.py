a = 2
b = 3
print("a is {}, b is {}".format(a, b))

a, b = 3, 2  # b, a  # official python way to swap  # relies on fact that right hand side of assgn is evaluated first, then resuls assigned to variable on left
# temp = a
# a = b
# b = temp  # other coding langs
print("a is {}, b is {}".format(a, b))
