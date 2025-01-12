# from player import Player
#
# tim = Player("Tim")  # tim = player.Player("Tim")

from enemy import Enemy, Troll, Vampire

# random_monster = Enemy("Basic enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(8)
# print(random_monster)
#
# random_monster.take_damage(9)
# print(random_monster)

ugly_troll = Troll("Pug")
print(f"Ugly troll - {ugly_troll}")

another_troll = Troll("Ug")
print(f"Another troll - {another_troll}")
another_troll.take_damage(18)
print(another_troll)

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

# monster = Enemy("Basic enemy")
# monster.grunt()  # Enemy object has no attribute grunt

vamp = Vampire("Vlad")
print(vamp)
vamp.take_damage(5)
print(vamp)

print("-" * 40)
another_troll.take_damage(30)
print(another_troll)

# while vamp.alive:
#     vamp.take_damage(1)
#   # print(vamp)

vamp._lives = 0
vamp._hit_points = 1
print(vamp)






# print(tim.name)
# print(tim.lives)
# tim.lives -= 1
# print(tim)  # directly calls the __str__ method
#
# # print(tim.get_name())  # get_name method is called as a getter
# # tim.set_lives(300)  # setter
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives = 9
# print(tim)
#
# tim.level = 2
# print(tim)
#
# tim.level += 5
# print(tim)
#
# tim.level = 3
# print(tim)
#
# tim.score = 500
# print(tim)
