a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a tuple")

data = 1, 2, 76  # data represents a tuple
x, y, z = data  # x, y, z not tuple; data is tuple
print(x)
print(y)
print(z)

print("Unpacking a list")

data_list = [12, 13, 14]
# data_list.append(15)  # error: too many values to unpack

p, q, r = data_list
print(p)
print(q)
print(r)
