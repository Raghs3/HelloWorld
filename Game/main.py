# from player import Player
#
# tim = Player("Tim")  # tim = player.Player("Tim")

from enemy import Enemy

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

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
