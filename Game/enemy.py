class Enemy:  # class Enemy(object) is same, py3 allows shortcut like this, i.e. automatically inherits from object class

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1

    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Hit Points: {self.hit_points}"


class Troll(Enemy):
    pass
