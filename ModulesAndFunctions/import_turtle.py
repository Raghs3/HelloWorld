# import turtle

# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()

import turtle
# import math
from math import radians, cos


def square(length: int) -> None:
    """Draws a square of length `length`"""
    for side in range(4):
        turtle.forward(length)
        turtle.right(90)


def encircled_square(length: int) -> None:
    """Draws a square of length `length`,
    then encloses it in a circle."""

    square(length)
    angle = radians(45)  # math.radians(45)  # math prefix not req as we imported them directly to namespace
    radius = length * cos(angle)  # math.cos(angle)
    turtle.right(135)
    turtle.circle(radius)
    turtle.left(135)  # takes same time, draws pattern differently and leaves turtle in same dirn as it started
    print(f"Inside function, namespace is: {dir()}")  # gives names in a list
    print(f"locals: {locals()}")  # shows the namespace dict, i.e. values too


encircled_square(300)
# turtle.speed('fast')
# for s in range(72):
#     encircled_square(120)
#     turtle.left(5)
#
# turtle.done()

print(dir())  # output is a list containing all the names that exist in our namespace, sorted alphabetically, `__` pronounced as dunder

# namespace is a container for variable names
# score is where that variable exists
# scope of a variable means the places in our code where it can be used
# or, scope is where an object exists or where it can be used
# modules, functions and classes can create a new scope
