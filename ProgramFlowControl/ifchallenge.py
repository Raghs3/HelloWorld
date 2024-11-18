name = input("What is your name?: ")
age = int(input("Hello, {}, how old are you?: ".format(name)))

if 18 <= age < 31:
    print("Welcome to the Holiday, {}".format(name))
else:
    print("We are sorry, but you cannot come to the Holiday :(")
