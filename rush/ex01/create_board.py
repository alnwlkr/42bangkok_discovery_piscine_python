import random

def create_chess_board(size):
    if size < 2:
        print("Size must be at least 2.")
        return

    board = [['.' for _ in range(size)] for _ in range(size)]
    # print(board)
    pieces = {
        'K': 1,
        'Q': 1,
        'B': 2,
        'R': 2,
        'P': 8
    }

    positions = [(i, j) for i in range(size) for j in range(size)]
    random.shuffle(positions)
    # print(positions)

    for piece, limit in pieces.items():
        for _ in range(limit):
            if positions:
                x, y = positions.pop()
                board[x][y] = piece

    for row in board:
        print(''.join(row))
    # print(board)

try:
    size = int(input("Enter the size of the board: "))
    create_chess_board(size)
except ValueError:
    print("Invalid input. Please enter an integer.")
