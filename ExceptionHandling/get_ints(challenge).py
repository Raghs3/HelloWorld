# # my soln
# a = int(input("Enter a number "))
# b = int(input("Enter second number "))
# # my error: didn't check if user entered numbers or not
# try:
#     print(a/b)
# except (TypeError, ZeroDivisionError):
#     print("Are you sure you entered an integer? or the second number is not a zero?")


# tim soln
import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(0)


# x = int(input("Enter a number "))  # to check what is the exception thrown
first_num = getint("Please enter first number ")
second_num = getint("Please enter second number ")

try:
    print(f"{first_num} divided by {second_num} is {first_num/second_num}")
except ZeroDivisionError:
    print("You can't divide by zero")
