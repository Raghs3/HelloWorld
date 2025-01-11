import random


# class Enemy:
class Enemy(object):  # is same, py3 allows shortcut like this, i.e. automatically inherits from object class

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print(f"I {self._name} took {damage} points damage and have {self._hit_points} left")
        else:
            self._lives -= 1
            if self._lives > 0:
                print(f"{self._name} lost a life")
            else:
                print(f"{self._name} is dead")
                self._alive = False

    def __str__(self):
        return f"Name: {self._name}, Lives: {self._lives}, Hit Points: {self._hit_points}"


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)  # best way
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)

    def grunt(self):
        print(f"Me {self._name}. {self._name} stomp you")


class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print(f"***** {self._name} dodges *****")
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)
