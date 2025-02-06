from utils import populate_queue
from boards import *
from queue import PriorityQueue
import numpy as np


def highest_score_first(board, print_board=False):
    """
    Highest score first method. Makes moves based
    on priority using the highest score first.
    Args:
        board (list[list[int]]): Board as a regular or numpy 2D array
        print_board (bool): Prints board after each move when True
    Returns:
        int: Final score for the board
    """
    board = np.array(board)
    move_queue = PriorityQueue()
    populate_queue(board, move_queue)

    score = 0

    if print_board:
        print(board)

    while not (move_queue.empty()):
        move = move_queue.get()

        if np.sum(board[move[1][0], move[1][1]]) == 10:
            board[move[1][0], move[1][1]] = 0
            score -= move[0]

            if print_board:
                board[move[1][0], move[1][1]] = -1
                print(f"Score: {score}\n{board}")
                board[move[1][0], move[1][1]] = 0

        if move_queue.empty():
            if print_board:
                print("REFRESHING MOVE QUEUE")

            populate_queue(board, move_queue)

    return score


print(f"Test board score: {highest_score_first(test_board)}\n"
      f"Board 1 score: {highest_score_first(board_1)}")
