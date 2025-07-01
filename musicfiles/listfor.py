print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a number, and I'll tell you it's square: "))
# whtever number u input always returns 36 as same var also used in for loop
squares = []
for number in numbers:
    squares.append(number ** 2)

index_pos = numbers.index(number)
print(squares[index_pos])
