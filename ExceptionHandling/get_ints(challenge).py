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
        except EOFError:  # order of handling exceptions is important
            sys.exit(1)  # when this was below exception, went into infinite loop when pressing ctrl + D due to order of exceptions
        except:  # <-- for all errors do this  # Exception: (doesn't handle all errors)  # ValueError:
            print("Invalid number entered, please try again")
        finally:  # don't use `Exception`, instead try to catch specific error, to react to diff exception in a diff way
            print("The finally clause always executed")


# x = int(input("Enter a number "))  # to check what is the exception thrown
first_num = getint("Please enter first number ")
second_num = getint("Please enter second number ")

try:
    print(f"{first_num} divided by {second_num} is {first_num / second_num}")
except ZeroDivisionError:  # exceptions are objects
    print("You can't divide by zero")
    sys.exit(2)
else:
    print("Division performed successfully")
