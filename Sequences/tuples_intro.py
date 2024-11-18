albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))



# t = ("a", "b", "c")  # or "a", "b", "c" i.e without parantheses
# print(t)

# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])


# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
# 
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])  # calculating area of coffee table but not tht readable
# 
# name, lenght, width, height, price = table  # unpacking to make easy reading
# print(lenght * width)


# metallica[0] = "Master of Puppets"  # does not support item assignment

# metallica2 = list(metallica)
# print(metallica2)
# 
# print()
# 
# metallica2[0] = "Master of Puppets"  # type: ignore
# print(metallica2)


