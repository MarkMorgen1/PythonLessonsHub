# w = int(input("Enter grid width: "))
# h = int(input("Enter grid height: "))
w = 3
h = 3

# print the grid
for _ in range(1, h + 1):
    print(" ---" * w)
    print("|   " * (w + 1))
print(" ---" * w)

game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game_over = False

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
