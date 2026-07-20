import random
import string


# choose a random word from SOWPODS file
def getword():
    with open("SOWPODS_words.txt", "r", encoding="utf-8") as f:
        # Read all words into a list
        words_list = [line.strip() for line in f]  # removes trailing \n
        # print(words_list)
        # print("# of words in SOWPODS is", len(words_list))
        random_word = random.choice(words_list)
        del words_list
    return random_word


gameword = getword()
print(gameword, "\n")
while len(gameword) > 8:
    gameword = getword()
    print(gameword, "\n")

alphabet = string.ascii_uppercase  # aceept 'A' to 'Z' caps only
gameover = False
word_length = len(gameword)
guesses_right = list("_" * word_length)  # initiate list of guesses with '_'s
guesses_wrong = []  # store wrong guesses here
print("the gameword is:", gameword)  # " ".join(gameword))
print("# of letters =", str(word_length), "\n")

# invite player to start the game
print("Welcome to Hangman")
print("Your game word contains " + str(word_length) + " letters")
print("ENTER LETTERS IN CAPS ONLY")
print(" _" * word_length, "\n")

while not gameover and "_" in guesses_right:
    # take a guess and convert to UPPERCASE
    letter_guess = input("Guess a letter >>> ").strip().upper()
    if letter_guess in gameword and letter_guess in guesses_right:
        print("You already got that letter.")

    # if format of guess is wrong:
    while len(letter_guess) != 1 or letter_guess not in alphabet:
        letter_guess = input("Wrong format.  Try again > ").strip().upper()
    if letter_guess in gameword:
        for index, letter in enumerate(gameword):  # check each letter
            if letter_guess == letter:  # if your guess is in the gameword,
                guesses_right[index] = (
                    letter_guess  # then update 'guesses_right' list at correct index
                )
    else:
        # put the wrong guess into 'guesses_wrong' list
        if letter_guess in guesses_wrong:
            print("You already tried that letter.")
        else:
            guesses_wrong.append(letter_guess)
            print("Nope")

    print(" ".join(guesses_right), "\n")  # print what's right
    print("Wrong guesses so far: ", guesses_wrong)  # print what's wrong

if "".join(guesses_right) == gameword:
    print(
        "\nYou got " + gameword + " in",
        len(set(guesses_right)) + len(set(guesses_wrong)),
        "guesses !!!\n",
    )  # using sets eliminates duplicate letters in 'guesses_right' which matches the gameword
