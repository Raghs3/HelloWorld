class Kettle(object):

    def __init__(self, make, price):  # init is constructor
        self.make = make  # self is the reference to instance of the class
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)  # kenwood is an instance of class Kettle
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
# when variable bound to instance of class it is referred to as data attribute
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))  # more readable

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""
# class is like a type in python (every type is a class)
print(hamilton.on)
hamilton.switch_on()  # when you call a method on an instance, py automatically provides ref to the instance as first param
print(hamilton.on)

Kettle.switch_on(kenwood)  # used switch_on as class method this time instead of on an instance
print(kenwood.on)
kenwood.switch_on()
