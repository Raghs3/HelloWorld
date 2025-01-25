# my soln
a = int(input("Enter a number "))
b = int(input("Enter second number "))

try:
    print(a/b)
except (TypeError, ZeroDivisionError):
    print("Are you sure you entered an integer? or the second number is not a zero?")
