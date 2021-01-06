"""
Tic Tac Toe Player
"""

import math, random

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
    count = 0
    for i in board:
        for j in i:
            if j == EMPTY:
                count += 1

    if count == 0:
        return None
    elif count % 2 == 1:
        return X
    elif count % 2 == 0:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # if terminal(board):
    #     return []
    # else:

    possible_actions = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardcopy = []
    for i in board:
        row = []
        for j in i:
            row.append(j)
        boardcopy.append(row)

    x = action[0]
    y = action[1]

    if (x > 2) or (y > 2) or (boardcopy[x][y] != EMPTY):
        raise Exception("INVALID MOVE!")

    boardcopy[x][y] = player(board)
    return boardcopy

def winner_x(board):
    """
    Return True iff X has won the game.
    """
    x = [X, X, X]
    # CHECKING FOR ROWS
    for i in board:
        if i == x:
            return True

    # CHECKING FOR COLUMNS
    for i in range(len(board)):
        if [board[0][i], board[1][i], board[2][i]] == x:
            return True

    # CHECKING FOR DIAGONALS
    if ([board[0][0], board[1][1], board[2][2]] == x) or \
        ([board[0][2], board[1][1], board[2][0]] == x):
        return  True

    return False


def winner_o(board):
    """
    Return True iff X has won the game.
    """
    x = [O, O, O]
    # CHECKING FOR ROWS
    for i in board:
        if i == x:
            return True

    # CHECKING FOR COLUMNS
    for i in range(len(board)):
        if [board[0][i], board[1][i], board[2][i]] == x:
            return True

    # CHECKING FOR DIAGONALS
    if ([board[0][0], board[1][1], board[2][2]] == x) or \
            ([board[0][2], board[1][1], board[2][0]] == x):
        return  True

    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if winner_x(board):
        return X
    elif winner_o(board):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (player(board) is None) or (winner(board) is not None):
        return True
    else:
        return False


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


def max_value(board):
    """A helper for minimax() that return that best move for X."""
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    """A helper for minimax() that return that best move for X."""

    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # We assume that O is minimising utility while X is maximising it.

    score_to_action = {}

    if terminal(board):
        return None

    if player(board) == X:
        score = max_value(board)
        for action in actions(board):
            # score = max_value(board)
            # if score not in score_to_action:
            #     score_to_action[score] = []
            # score_to_action[score].append(action)
            if min_value(result(board, action)) == score:
                return action
        # return random.choice(score_to_action[max(score_to_action.keys())])

    else:
        score = min_value(board)
        for action in actions(board):
            # score = min_value(board)
            # if score not in score_to_action:
            #     score_to_action[score] = []
            # score_to_action[score].append(action)
            if max_value(result(board, action)) == score:
                return action
        # return random.choice(score_to_action[min(score_to_action.keys())])

    return None
