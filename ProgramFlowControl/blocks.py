# for i in range(1, 13):
#     print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
#     print("*" * 80)  # prints all * in one line

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))  # input fn returns str datatype
print(age)  # using int() we make input fn return int datatype instead of str

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:  # clause? idk english lol
#     print("Please come back in {0} years".format(18 - age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
