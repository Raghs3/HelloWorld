def fizz_buzz(number: int) -> str:
    """
    Play the game of Fizz Buzz.

    :param number: The number to check.
    :return: 'fizz' if divisble by 3.
        'buzz' if divisible by 5.
        'fizz buzz' if divisible by both.
        'number' itself, as a string, otherwise.
    """
    if number % 15 == 0:  # as div by both 5 and 3
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


input("Play Fizz Buzz. Press ENTER to start")
print()

# tim way using while loop
next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    # players_answer = correct_answer
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}"
              .format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))


# my way using for loop
# for i in range (1, 101, 2):
    # print("I say {} for {}, now your turn."
    #       .format(fizz_buzz(i), i))


    # game part
    # user_input = input(": ")
    # if user_input.casefold() != fizz_buzz(i + 1):
    #     print("Oh no, you got it wrong! That's the end.")
    #     break

    # print("{}: {} was correct"
    #       .format(i+1, user_input))


    # testing part
    # for j in range(i, 101):
    #     if fizz_buzz(j) != fizz_buzz(i+1):
    #         print("Oh no, you got it wrong! Try again.")
    #     else:
    #         print("{}: {} was correct"
    #               .format(j, fizz_buzz(j)))
    #         break
