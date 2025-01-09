from player import Player

tim = Player("Tim")  # tim = player.Player("Tim")

print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim)  # directly calls the __str__ method

# print(tim.get_name())  # get_name method is called as a getter
# tim.set_lives(300)  # setter
tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives = 9
print(tim)

tim.level = 2
print(tim)

tim.level += 5
print(tim)

tim.level = 3
print(tim)

tim.score = 500
print(tim)
