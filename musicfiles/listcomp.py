print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

squares = [number ** 2 for number in numbers]  # the `[ ]` is the `list` comprehension
# bracket of comprehension gives that comprehension for ex: `{ }` gives set comprehension
print(squares)
