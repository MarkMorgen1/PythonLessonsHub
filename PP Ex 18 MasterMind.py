# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

# Define all functions and classes at the top level of the module.
# Use {if __name__ == "__main__"} only for code that should run when the file is executed directly (like testing, command-line execution, or demos).
import random as rm

num_digits = 4  # how many digits in the numbers
guesses = 0
Cows = 0  # initialize Cows to enter while-loop
rand_num = str(rm.randint(10 ** (num_digits - 1), 10**num_digits - 1))
# rand_num = "989"
print(rand_num)
print("enter 0 to quit game")
guess_val = input(f"Cows and Bulls: Provide {num_digits}-Digit number --> ")
# guess_val is a string, not an integer!
# print("guess type is:", type(guess_val))

while guess_val != "0" and Cows < num_digits:
    Cows = 0
    Bulls = 0
    Cows_list = ["a"] * num_digits
    Bulls_list = ["a"] * num_digits
    # Cows_list will hold the locations and string-values of Cows in guess_val.  Initialize with characters not in guess_val
    for i in range(0, num_digits):  # i = 0 to (num_digits-1)
        if guess_val[i] == rand_num[i]:  # test all digits for Cows first
            Cows += 1
            Cows_list[i] = rand_num[i]  # put the Cow into Cows_list in correct position
    print("Cows List =", Cows_list)
    Bulls_list = Cows_list.copy()  # mark cows in Bulls_list, too
    # you must use .copy() to create a new unique list, otherwise it points to the same object and changing one list changes the object, and hence the other list!
    print("Bulls List:", Bulls_list)

    for i in range(0, num_digits):
        for j in range(0, num_digits):
            # test all digits for Bulls after having tested for Cows. Ignore Cows so they aren't counted as Bulls.
            if Cows_list[i] == "a" and Bulls_list[j] == "a":
                if guess_val[i] == rand_num[j]:
                    Cows_list[i] = rand_num[j]
                    Bulls_list[j] = rand_num[j]
                    # put a number into both lists so that digit does not get checked again
                    Bulls += 1
                    print("i, j ", i, " ", j)
                    print("Bulls_list:", Bulls_list)
    print("Cows:", Cows, "\nBulls:", Bulls)
    guesses += 1
    print("Guess number:", guesses)
    print("\n", rand_num)
    if Cows == num_digits:
        print("Congratulations!  You got it!")
    else:
        guess_val = input("Next guess: ")
