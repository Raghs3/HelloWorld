empty_list = []  # list created
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]  # list of lists
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)
        




# numbers = even + odd  # list created


# sorted_numbers = sorted(numbers)  # list created 
# print(sorted_numbers)
# print(numbers)
# 
# digits = list("432985617")
# print(digits)
# 
# # more_numbers = list(numbers)
# # more_numbers = numbers[:]  # slicing, another way to copy list
# more_numbers = numbers.copy()
# print(more_numbers)
# print(numbers is more_numbers)
# print(numbers == more_numbers)


# even.extend(odd)
# print(even)
# another_even = even
# print(another_even)
# 
# even.sort(reverse=True)
# print(even)
# print(another_even)


# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
# 
# print()
# print(len(even))
# print(len(odd))
# 
# print()
# print("mississippi".count("issi"))  # each char is counted only once
# 
