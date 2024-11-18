parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:  # case sensitive
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")
