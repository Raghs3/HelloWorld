import random
# we can use fn in random module using dot notation (.)
highest = 1000
answer = random.randint(1, highest)  # highest is inclusive, dot notation, randint fn is in random module
print(answer)  # TODO: Remove after testing
guess = 0   # initialise to any number that doesn't equal the answer
print("Please guess a number between 1 and {0}: ".format(highest))

# tim soln
while guess != answer:
    guess = int(input())
    if guess == 0:
        break

    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")




# my solution with no of guesses

# print("Please guess a number between 1 and {0}: ".format(highest))
# guess = int(input())
# attempts = 0
# 
# while True:
#     if guess == answer:
#         if attempts == 0:
#             print("You got it first time")
#         else:
#             print("Well done, you got it in {} guesses".format(attempts))
#         break
#     elif guess == 0:
#         print("I see you have given up in {} tries".format(attempts))
#         break
#     else:
#         if guess < answer:
#             print("Please guess higher")
#         else:  # guess must be greater than answer
#             print("Please guess lower")
#         guess = int(input())
#     attempts += 1


# answer = 5
# 
# print("Please guess a number between 1 and 10: ")
# guess = int(input())
# 
# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")


# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer: 
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")
