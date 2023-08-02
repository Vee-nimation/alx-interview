#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)
else:
    N = int(sys.argv[1])

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def printBoard(board):
    """Print formated board
    Args:
        board (list): list of list of 0 or 1
    """
    board_vect = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                board_vect.append([i, j])
                break
    print(board_vect)


def valid_pos(board, row=0, col=0):
    """Check valid positions in col
    Args:
        row (int): row number of matrix
        col (int): colum number of matrix
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while j >= 0 and i < N:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


def Solver(board, col=0):
    """Vefify the options
    Args:
        col (int): colum number of matrix
    """
    if col >= N:
        printBoard(board)
        return True
    res = False
    for i in range(N):
        if valid_pos(board, i, col):
            board[i][col] = 1
            res = Solver(board, col + 1) or res

            board[i][col] = 0
    return res


def n_queen():
    """Solves the N queens problem.
    Return: None
    """
    board = []
    for row in range(N):
        board.append([0] * N)
    if not Solver(board, 0):
        print("Not Solution Found")
        return
    return


n_queen()
