from random import randint
from time import sleep

PLAYER1 = 'X'

# Create a list with the positions than players can choice
# size is a parameter for make the board bigger
def start_positions(size: int = 3) -> list:
    board = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append("*")
        board.append(row)
    return board

# Print the board with the positions of the players
def print_board(size: int = 3):
    board = ""
    for x in range(size):
        for y in range(size):
            board += f"  {game[x][y]}  "
        board += "\n\n"
    return print(board)

# Take the coordinates to write the player simbol
def play_human(player='O'):
    pos = input("Write the position (e.g. '1 2'): ").split()
    row = int(pos[0]) - 1
    col = int(pos[1]) - 1
    if game[row][col] == '*':
        game[row][col] = player
    else:
        print("This position is already used, choice other place!")
        play_human(player)

# The bot choose a random position
def play_bot():
    row = randint(0, 2)
    col = randint(0, 2)
    if game[row][col] == '*':
        game[row][col] = 'O'
    else:
        play_bot()

# Check if is the same symbol in rows/columns/diagonal
def is_winner(player='O', size: int = 3):
    ########## Comprobar por filas ###########
    for row in game:
        win = True
        for col in row:
            if col != player:
                win = False
                break
        if win:
            return win

    ########### Comprobar por columnas ###########
    for x in range(size):
        win = True
        for y in range(size):
            if game[y][x] != player:
                win = False
                break
        if win:
            return win

    ########### Comprobar en diagonal ###########
    # left-down to right-up -> /
    win = True
    for pos in range(size):
        if game[pos][pos] != player:
            win = False
            break
    if win:
        return win

    # left-up to right-down -> \
    for pos in range(size - 1, 0, -1):
        if game[pos][pos] != player:
            win = False
            break
    if win:
        return win

    return False

# If there isn't any * in the list that means the game is tied
def is_tie():
    over = True
    for row in game:
        if '*' in row:
            over = False
    if over:
        print("Tie!")
        return True

def play(play1, play2, second_player):
    # JUEGA EL JUGADOR 1 (YO :))
    print("Player 1 turn.")
    play1(PLAYER1)
    print_board()
    if is_winner(PLAYER1) or is_tie():
        return True

    # JUEGA EL JUGADOR 2 / BOT
    print(f"{second_player} turn")
    sleep(1)
    play2()
    print_board()
    if is_winner() or is_tie():
        return True


# If user wants to make the board bigger
# size_board = int(input("Size of the board (a.g 3x3, 6x6): ").strip()[0])
mode = input("How do you want to play? ('single'/'versus') ").lower()
print(f"Player 1: 'X'\t\t Player 2: 'O'")
game = start_positions()
print_board()

is_over = False
if mode == 'single':
    while not is_over:
        is_over = play(play_human, play_bot, second_player='Bot')

elif mode == 'versus':
    while not is_over:
        is_over = play(play_human, play_human, second_player="Player 2")
