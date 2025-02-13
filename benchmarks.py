import time
from random import choice
from typing import Callable

from moves import get_moves, make_move
from boards import *
import numpy as np


def benchmarks(board: list[list[int]] | np.ndarray, move_op: Callable) -> int:
    """
    Highest/lowest/random score first method depending on move_op.
    :param board: Board as a regular or numpy 2D array
    :param move_op: min/max/random.choice. Function given a list that returns an item from the list
    :return: Final score for the board
    """
    board = np.array(board)
    move_list = get_moves(board)
    score = 0

    while move_list:
        move = move_op(move_list)
        score += make_move(board, move)
        move_list = get_moves(board)

    return score


print(f"= Highest score first =\n"
      f"Test board score: {benchmarks(test_board, max)}\n"
      f"Board 1 score: {benchmarks(board_1, max)}\n")

print(f"= Lowest score first =\n"
      f"Test board score: {benchmarks(test_board, min)}\n"
      f"Board 1 score: {benchmarks(board_1, min)}\n")

print(f"= Random =\n"
      f"Test board score: {benchmarks(test_board, choice)}\n"
      f"Board 1 score: {benchmarks(board_1, choice)}\n")
