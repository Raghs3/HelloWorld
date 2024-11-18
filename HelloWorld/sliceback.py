letters = "abcdefghijklmnopqrstuvwxyz"
#          01234567890123456789012345
#          65432109876543210987654321
backwards = letters[::-1]  # when step is -ve, start value defaults to end of str
print(backwards)           # so we can omit start and end values
                           # end value defaults to start of str
print()                    # [::-1] is an idiom meaning reversing str

# create a slice that produces the characters qpo
print(letters[16:13:-1])

# slice the string to produce edcba
print(letters[4::-1])

# slice the string to produce the last 8 characters, in reverse order
print(letters[:-9:-1])  # upto but not including -9

print(letters[-4:])  # idiom for printing last n letters (here n = 4)
print(letters[-1:])  # last item
print(letters[:1])  # first item, (doesn't give error if empty seq)
print(letters[0])  # not slicing as no {:}, it is indexing, but will return error if str empty
