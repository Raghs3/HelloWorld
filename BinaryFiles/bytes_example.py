# equation = bytes((207, 128, 114, 194, 178))
equation = b'\xcf\x80r\xc2\xb2'  # bytes literal, python lets us create it in this way
            # hex after \x, 114 is ascii for `r`
print(equation)
print(type(equation))
print(len(equation))

for b in equation:
    print(b, end=", ")
print()

print(equation.decode('utf-8'))  # symbol for pi is encoded using CF 80 in utf-8, superscript 2 char is encoded using c2 b2
