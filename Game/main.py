from player import Player

tim = Player("Tim")  # tim = player.Player("Tim")

print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim)

# print(tim.get_name())  # get_name method is called as a getter
# tim.set_lives(300)  # setter
tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)
