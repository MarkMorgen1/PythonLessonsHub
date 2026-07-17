# w = int(input("Enter grid width: "))
# h = int(input("Enter grid height: "))
w = 3
h = 3
turns_taken = []  # use to keep track of each turn already taken
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # use this matrix to test for wins later
game_over = False
print("Let's play some TicTacToe!")
# fill and print the grid using zeros
print(" ---" * w)
for i in range(1, h + 1):
    for j in range(1, w + 1):
        print("| 0 ", end="")
    print("|")
    print(" ---" * w)
print("\n")


while not game_over:
    # Get input from player
    if len(turns_taken) % 2 == 0:
        x_pos_str, y_pos_str = input("Enter X position as 'x,y': ").split(",")
    else:
        x_pos_str, y_pos_str = input("Enter Y position as 'x,y': ").split(",")
    x_pos = int(x_pos_str)
    y_pos = int(y_pos_str)

    # cleaner version of getting x and y:
    # x_pos, y_pos = [int(n) for n in input("Enter x and y positions as 'x,y': ").split(",")]
    # x_pos = 2
    # y_pos = 1

    this_turn = [x_pos, y_pos]

    # get new entry if x,y already chosen
    while this_turn in turns_taken or x_pos > w or y_pos > h:
        print("\nThat position is taken or out of bounds, try again.")
        if len(turns_taken) % 2 == 0:
            x_pos_str, y_pos_str = input("Enter X again: ").split(",")
        else:
            x_pos_str, y_pos_str = input("Enter Y again: ").split(",")
        x_pos = int(x_pos_str)
        y_pos = int(y_pos_str)
        this_turn = [x_pos, y_pos]

    turns_taken.append(this_turn)  # append new selection to turns_taken
    print("Your choice is:", this_turn)
    print("Turns taken:", turns_taken)
    print("Total turns taken =", len(turns_taken))
    print("Index of [", x_pos, ",", y_pos, "]:", (turns_taken.index([x_pos, y_pos])))

    # fill and print the grid using elements from turns_taken, and update 'game' matrix, which uses indicies from 0 to 2, not 1 to 3, as the user sees
    print(" ---" * w)
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if [j, i] in turns_taken and ((turns_taken.index([j, i])) % 2 == 0):
                print("| X ", end="")
                game[i - 1][j - 1] = 1  # set position in 'game' to 1 for later win test
            elif [j, i] in turns_taken and ((turns_taken.index([j, i])) % 2 == 1):
                print("| Y ", end="")
                game[i - 1][j - 1] = 2  # set position in 'game' to 2 for later win test
            else:
                print("| 0 ", end="")
        print("|")
        print(" ---" * w)

    #        print("| 0 " + "|") # using '+' eliminates the space created when using the ',' in a print statement

    # check for a vertical win using 'game' matrix
    print("Game Matrix:", game)
    for i in range(3):
        if game[i][0] * game[i][1] * game[i][2] == 1:
            print("Player X wins !!!\n")
            game_over = True
        elif game[i][0] * game[i][1] * game[i][2] == 8:
            print("Player Y wins !!!\n")
            game_over = True

    # check for a horizontal win
    if not game_over:
        for j in range(3):
            if game[0][j] * game[1][j] * game[2][j] == 1:
                print("Player X wins !!!\n")
                game_over = True
            elif game[0][j] * game[1][j] * game[2][j] == 8:
                print("Player Y wins !!!\n")
                game_over = True

    # check for a diagonal win
    if not game_over:
        if (game[0][0] * game[1][1] * game[2][2] == 1) or (
            game[0][2] * game[1][1] * game[2][0] == 1
        ):
            print("Player X wins !!!\n")
            game_over = True

    if not game_over:
        if (game[0][0] * game[1][1] * game[2][2] == 8) or (
            game[0][2] * game[1][1] * game[2][0] == 8
        ):
            print("Player Y wins !!!\n")
            game_over = True

    if not game_over and len(turns_taken) == 9:  # no one has won after 9 tries
        game_over = True
        print("Game is a draw.  Restart to go again.\n")
    elif not game_over and len(turns_taken) < 9:
        print("No winner yet...\n")
