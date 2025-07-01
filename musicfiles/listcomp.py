print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

# squares = [number ** 2 for number in numbers]  # the `[ ]` is the `list` comprehension
squares = [number ** 2 for number in range(1, 7)]  # same as above
# bracket of comprehension gives that comprehension for ex: `{ }` gives set comprehension
print(squares)
