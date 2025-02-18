class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a but chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!")


class Mallard(Duck):  # example of why if type is type is wrong
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:  # adding annotation so the intellij checker, checks and warns
        # if isinstance(duck, Duck):  # if necessary use this method instead  # if type(duck) is Duck:  # never do this, just wrong, and not pythonic
        #     self.flock.append(duck)  # no need to annotate self, auto annotates
        fly_method = getattr(duck, 'fly', None)  # checks if attribute exists or not, checks dict of object to see if it contains specified attr
        if callable(fly_method):  # callable to check if fly method is callable  # getattr like dict get method
            self.flock.append(duck)  # data attr aren't callable, functions and methods are
# this is the pythonic way, testing if it flies rather than if it is a duck

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:  # reference to exception is stored in a variable
                print("One duck down")
                # raise  # raising errors makes it so only 4 birds fly as loop is terminated
                problem = e
        if problem:
            raise problem  # all birds fly, and problem is raised as well
# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == '__main__':
    donald = Duck()
    # test_duck(donald)
    donald.fly()

    # percy = Penguin()
    # test_duck(percy)
