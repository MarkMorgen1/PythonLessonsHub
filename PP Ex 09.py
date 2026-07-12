import random

rand_num = random.randint(1, 10)
num_guesses = 0
user_guess = int(input("Guess a number between 1 and 10, or '0' to exit... "))

while user_guess != rand_num and user_guess != 0:
    if user_guess > rand_num:
        num_guesses += 1
        user_guess = int(input("Guess lower..."))
    else:
        num_guesses += 1
        user_guess = int(input("Guess higher..."))

    if user_guess == rand_num:
        num_guesses += 1
        print("That took you ", num_guesses, "guesses")
        num_guesses = 0
        user_guess = int(input("Guess a number between 1 and 10, or '0' to exit... "))
        rand_num = random.randint(1, 10)
