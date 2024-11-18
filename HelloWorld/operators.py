a = 12  # these are also expressions
b = 3   # a and b are not expressions (left of assignment)(right is evaluated and bound to left)

print(a + b)  # 15, this is called expression, a and b also expressions
print(a - b)  # 9, expression is anything that can be calculated to return a value
print(a * b)  # 36
print(a / b)  # 4.0 (produces float result)
print(a // b)  # 4, integer division, rounded down towards minus infinity
print(a % b)  # 0, modulo, the remainder after integer division

print()

# for i in range(1, a//b):  # cant use (/) as it float cannot be interpreted as int, i is not expression
#     print(i)              # parameter of for loop are expressions, range evaluates numbers from 1 to 4, i to be evaluated

# i = 1  # these i are not expressions, hence not expression in line 13 either
# print(i)
# i = 2
# print(i)
# i = 3
# print(i)

print(a + b / 3 - 4 * 12)
print(a + (b/3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a) / b)

