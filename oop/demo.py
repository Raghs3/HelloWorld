a_string = "this is\na string split\t\t and tabbed"
print(a_string)

raw_string = r"this is\na string split\t\t and tabbed"
print(raw_string)

b_string = "this is" + chr(10) + "a string split" + chr(9) + "and tabbed"
print(b_string)

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)

backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

error_string = r"this string ends with \\"  # escapes final qoute so need the extra backslash
print(error_string)
