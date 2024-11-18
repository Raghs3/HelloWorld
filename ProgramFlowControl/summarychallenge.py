# tim soln changing the condition

# choice = "-"
# while choice != "0":
#     if choice in "12345":
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose your option from the list below:")
#         print("1:\tLearn Python")
#         print("2:\tLearn Java")
#         print("3:\tLearn Swimming")
#         print("4:\tLearn Cooking")
#         print("5:\tLearn Sleeping")
#         print("0:\tExit")
#     choice = input()


# tim soln with optional 

# choice = "-"
# 
# while True:
#     if choice == "0":
#         break
#     elif choice in "12345":
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose your option from the list below:")
#         print("1:\tLearn Python")
#         print("2:\tLearn Java")
#         print("3:\tLearn Swimming")
#         print("4:\tLearn Cooking")
#         print("5:\tLearn Sleeping")
#         print("0:\tExit")
# 
#     choice = input()


# tim soln

# print("Please choose your option from the list below:")
# print("1:\tLearn Python")
# print("2:\tLearn Java")
# print("3:\tLearn Swimming")
# print("4:\tLearn Cooking")
# print("5:\tLearn Sleeping")
# print("0:\tExit")
# 
# while True:
#     choice = input()
# 
#     if choice == "0":
#         break
#     elif choice in "12345":
#         print("You chose {}".format(choice))


# my soln (wrong kinda)

options = ["Python", "Java", "C++", "HTML", "CSS", "C", "Sleep"]

choice = "-"

valid_choices = []
for i in range(1, len(options) +1):
    valid_choices.append(str(i))

while choice != "0":
    if choice in valid_choices:
        print("You have chosen {}, {}".format(choice, options[int(choice) - 1]))
    else:
        print("Please choose your option from the list below")
        for index, item in enumerate(options):
            print("{}:\t{}".format(index + 1, item))
        print("0:\tExit")
    choice = input()
