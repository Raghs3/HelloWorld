# for index, character in enumerate("abcdefgh"):  # enumerate create tuple, index and character unpacked from tht tuple
#     print(index, character)

for t in enumerate("abcdefgh"):  # enumerate create tuple
    index, character = t  # unpacking the tuple
    print(index, character)

index, character = (0, 'a')  # this is happening on line one
print(index)
print(character)