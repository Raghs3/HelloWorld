# x = 8 - 5  # x = 8 = 5  # syntax error
# y = x / 0  # ZeroDivisionError


def factorial(n):
    # n! can also be defined as n * (n-1)!
    """Calculates n! recursively"""
    if n <= 1:
        return 1
    else:
        # print(n / 0)
        return n * factorial(n-1)


try:
    print(factorial(900))  # error on 1000 and not on 900 (for testing purposes)
except (RecursionError, OverflowError):  # can do multiple exceptions this way as well, but not best as doesn't give specific message (as in case of ZeroDivisionError)
    print("This program cannot calculate factorials that large")
# except ZeroDivisionError:
#     print("What are you doing dividing by zero????")

print("Program terminating")
