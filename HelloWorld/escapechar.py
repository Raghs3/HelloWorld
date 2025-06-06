splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5\t6"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")  # escape char '\' used to escape quote marks

# if we use escape char then we can write print statements in multiple lines but output will be in one line
print("""The pet shop owner said "No, no, \
'e's uh,...he's resting".""")  # triple quotes so no escape char needed for quotation marks

anotherSplitString = """This string has been \
split over \
several \
lines"""  # another use for triple quotation marks, when (\) used, output in one line otherwise split

print(anotherSplitString)  # if escape char not used it will be outputted in multiple lines

print("C:\\Users\\tom\\notes.txt")  # preferred method
print(r"C:\Users\tom\notes.txt")  # r for raw
# print("C:\Users\tom\notes.txt")
