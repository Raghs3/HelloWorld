# import turtle

# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()

# import turtle
from turtle import *  # every name that doesn't begin with one or more underscore will be imported into namespace
# import math
from math import radians, cos


def square(length: int) -> None:
    """Draws a square of length `length`"""
    inner_forward = forward  # don't use this method, use as last resort
    inner_right = right
    for side in range(4):
        inner_forward(length)  # turtle.forward(length)
        inner_right(90)  # turtle.right(90)


def encircled_square(length: int) -> None:
    """Draws a square of length `length`,
    then encloses it in a circle."""

    square(length)  # doesn't find in local namespace, then looks in enclosing scope which is global scope in this case
    angle = radians(45)  # math.radians(45)  # math prefix not req as we imported them directly to namespace
    radius = length * cos(angle)  # math.cos(angle)
    right(135)  # turtle.right(135)
    circle(radius)  # turtle.circle(radius)
    left(135)  # turtle.left(135)  # takes same time, draws pattern differently and leaves turtle in same dirn as it started
    print(f"Inside function, namespace is: {dir()}")  # gives names in a list
    print(f"locals: {locals()}")  # shows the namespace dict, i.e. values too


# encircled_square(300)
speed('fast')  # turtle.speed('fast')
Screen().tracer(0)  # disable turtle animation
for s in range(72):
    encircled_square(120)
    left(5)  # turtle.left(5)
# improve the way the code works, before resorting to quick fixes
Screen().update()  # update the screen
done()  # turtle.done()

print(dir())  # output is a list containing all the names that exist in our namespace, sorted alphabetically, `__` pronounced as dunder

# namespace is a container for variable names
# score is where that variable exists
# scope of a variable means the places in our code where it can be used
# or, scope is where an object exists or where it can be used
# modules, functions and classes can create a new scope

g = globals()
print(g['square'])

print(dir(__builtins__))

# LEGB, order Python searches for names
