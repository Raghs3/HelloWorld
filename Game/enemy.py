import random


# class Enemy:
class Enemy(object):  # is same, py3 allows shortcut like this, i.e. automatically inherits from object class

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f"{self.name} lost a life")
            else:
                print(f"{self.name} is dead")
                self.alive = False

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Hit Points: {self.hit_points}"


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)  # best way
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)

    def grunt(self):
        print(f"Me {self.name}. {self.name} stomp you")


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print(f"***** {self.name} dodges *****")
            return True
        else:
            return False

    def take_damage(self, damage):
        pass
