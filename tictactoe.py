"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    Xnum = sum(row.count("X") for row in board)
    Onum = sum(row.count("O") for row in board)

    if Xnum == Onum:
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acts = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                acts.add((i, j))

    return acts

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Move!!!")

    board_copy = copy.deepcopy(board)
    s = player(board_copy)
    (row, col) = action
    board_copy[row][col] = s

    return board_copy

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if (((board[0][0] == board[1][1] == board[2][2] == 'X') or (board[0][2] == board[1][1] == board[2][0] == 'X') or (
            board[0][0] == board[1][0] == board[2][0] == 'X') or (board[0][0] == board[0][1] == board[0][2] == 'X') or (
                 board[0][1] == board[1][1] == board[2][1] == 'X') or (
                 board[1][0] == board[1][1] == board[1][2] == 'X') or (
                 board[0][2] == board[1][2] == board[2][2] == 'X') or (
                 board[2][0] == board[2][1] == board[2][2] == 'X'))):
        return X
    if (((board[0][0] == board[1][1] == board[2][2] == 'O') or (board[0][2] == board[1][1] == board[2][0] == 'O') or (
            board[0][0] == board[1][0] == board[2][0] == 'O') or (board[0][0] == board[0][1] == board[0][2] == 'O') or (
                 board[0][1] == board[1][1] == board[2][1] == 'O') or (
                 board[1][0] == board[1][1] == board[1][2] == 'O') or (
                 board[0][2] == board[1][2] == board[2][2] == 'O') or (
                 board[2][0] == board[2][1] == board[2][2] == 'O'))):
        return O
    else:
        return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    Tie = False
    if not (any(None in sublist for sublist in board)):
        Tie = True

    if winner(board) == X or winner(board) == O or Tie == True:
        return True
    else:
        return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for a in actions(board):
            v = max(v, min_value(result(board, a)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for a in actions(board):
            v = min(v, max_value(result(board, a)))
        return v

    if player(board) == X:
        MAX = - math.inf
        if not (any('X' in sublist for sublist in board)):
            return (1, 1)
        for a in actions(board):
            if MAX < min_value(result(board, a)):
                MAX = min_value(result(board, a))
                act = a
        return act

    elif player(board) == O:
        MIN = math.inf
        for a in actions(board):
            if MIN > max_value(result(board, a)):
                MIN = max_value(result(board, a))
                act = a
        return act

    raise NotImplementedError
