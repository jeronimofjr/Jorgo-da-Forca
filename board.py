
def board(i):
    board = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']
    return board[i]