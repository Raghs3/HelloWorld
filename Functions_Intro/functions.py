def multiply(x: float, y: float) -> float:  # x, y are (formal) parameters
    """
    Multiply two numbers.

    Although this function is intended to multiply two numbers,
    you can also use it to multiply a sequence.

    If you pass a string, for example, as the first argument,
    you'll get the string repeated `y` times as the returned value.

    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result  # scope of x, y and result is the fn they are defined in


def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards
    as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome,
        False if `string` is not a palindrome.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation and
    punctuation in the sentence.

    :param sentence: The sentence to check.
    :return: True if 'sentence' is a palindrome,
        False otherwise
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    # print(string)  # for checking if correctly done
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`"""
    if 0 <= n <= 1:
        return n
    
    n_minus1, n_minus2 = 1, 0
    
    result = None
    for f in range(n-1): 
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    
    return result  # if False  # type: ignore


for i in range(36):
    print(i + 1, fibonacci(i))

p = palindrome_sentence("11")


# answer = multiply(10.5, 4)  # these are arguments 
# print(answer)
# 
# forty_two = multiply(6, 7)  # positional arguments assigned to parameter in order
# print(forty_two)
# 
# print()
# 
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)


# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))


# word = input("Please enter sentence to check: ")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))
