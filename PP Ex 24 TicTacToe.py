# w = int(input("Enter grid width: "))
# h = int(input("Enter grid height: "))
w = 3
h = 3
count = 0
turns_taken = [[1, 1], [2, 2]]  # use to keep track of each turn already taken

# x_pos_str, y_pos_str = input("Enter x and y positions as 'x,y': ").split(",")
# x_pos = int(x_pos_str)
# y_pos = int(y_pos_str)

# cleaner version:
# x_pos, y_pos = [int(n) for n in input("Enter x and y positions as 'x,y': ").split(",")]
x_pos = 2
y_pos = 3
this_turn = [x_pos, y_pos]
print("Your choice is:", this_turn)
print("Turns taken:", turns_taken)
print("Total turns taken =", len(turns_taken))


# get new entry if x,y already chosen
while this_turn in turns_taken or x_pos > w or y_pos > h:
    print("\nThat position is taken or out of bounds, try again.")
    x_pos_str, y_pos_str = input("Enter as 'x,y': ").split(",")
    x_pos = int(x_pos_str)
    y_pos = int(y_pos_str)
    this_turn = [x_pos, y_pos]

turns_taken.append(this_turn)
print("Your choice is:", this_turn)
print("Turns taken:", turns_taken)
print("Total turns taken =", len(turns_taken))

# fill and print the grid using elements in turns_taken
print(" ---" * w)
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if [j, i] in turns_taken and ((turns_taken.index([j, i])) // 2 == 0):
            print("| X ", end="")
        elif [j, i] in turns_taken and ((turns_taken.index([j, i])) // 2 == 1):
            print("| Y ", end="")
        else:
            print("| 0 ", end="")
    print("|")
    print(" ---" * w)


# for i in range(1, h + 1):
#     for j in range(1, w + 1):
#         if [x_pos, y_pos] == [j, i] and (count // 2 == 1):
#             print("| X ", end="")
#         elif [x_pos, y_pos] == [j, i] and (count // 2 == 0):
#             print("| Y ", end="")
#         else:
#             print("| 0 ", end="")
#     print("|")
#     print(" ---" * w)
#     count += 1


#        print("| 0 " + "|")
# using '+' eliminates the space created when using the ',' in a print statement

game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game_over = False

# test cases
winner_is_2 = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
winner_is_1 = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
winner_is_also_1 = [[0, 1, 0], [2, 1, 0], [2, 1, 1]]
no_winner = [[1, 2, 0], [2, 1, 0], [2, 1, 2]]
also_no_winner = [[1, 2, 0], [2, 1, 0], [2, 1, 0]]

# check for a vertical win
for i in range(3):
    if game[i][0] * game[i][1] * game[i][2] == 1:
        print("Player 1 wins !!!")
        game_over = True
    elif game[i][0] * game[i][1] * game[i][2] == 8:
        print("Player 2 wins !!!")
        game_over = True

# check for a horizontal win
if not game_over:
    for j in range(3):
        if game[0][j] * game[1][j] * game[2][j] == 1:
            print("Player 1 wins !!!")
            game_over = True
        elif game[0][j] * game[1][j] * game[2][j] == 8:
            print("Player 2 wins !!!")
            game_over = True

# check for a diagonal win
if not game_over:
    if (game[0][0] * game[1][1] * game[2][2] == 1) or (
        game[0][2] * game[1][1] * game[2][0] == 1
    ):
        print("Player 1 wins !!!")
        game_over = True

if not game_over:
    if (game[0][0] * game[1][1] * game[2][2] == 8) or (
        game[0][2] * game[1][1] * game[2][0] == 8
    ):
        print("Player 2 wins !!!")
        game_over = True

if not game_over:
    print("Game is a draw.  Go again.")
