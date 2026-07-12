p1_score = 0
p2_score = 0
p1 = "r"
p2 = "s"
valid_answers = [
    "r",
    "p",
    "s",
    "q",
]
win_dict = {
    "r": "s",
    "p": "r",
    "s": "p",
}  # defines 3 ways to win in rock, scissors, paper


def show_scores(score_1, score_2):
    print("Player 1: ", score_1)
    print("Player 2: ", score_2, "\n")


while (p1 != "q") and (p2 != "q"):
    p1 = input("Player 1, enter r, p, or s (or q to quit): ")
    while p1 not in valid_answers:
        p1 = input("Player 1 - r, p, s, or q ONLY: ")

    if p1 == "q":
        p1_score = 0
        p2_score = 0
        break

    p2 = input("Player 2, enter r, p, or s: ")
    while p2 not in valid_answers:
        p2 = input("Player 2 - r, p, s, or q ONLY: ")

    if p2 == "q":
        p1_score = 0
        p2_score = 0
        break

        # Determine outcome
    if p1 == p2:
        print("Match is a draw. Settle with swords!\n")

    elif win_dict[p1] == p2:  # checks if p1 is a winning (key:value) entry in win_dict
        p1_score += 1
        print(f"{p1.upper()} beats {p2.upper()}. Player 1 wins!")
        show_scores(p1_score, p2_score)
    else:  # if p1 doesn't draw or win, p2 wins
        p2_score += 1
        print(f"{p2.upper()} beats {p1.upper()}. Player 2 wins!")
        show_scores(p1_score, p2_score)
