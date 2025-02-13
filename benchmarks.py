from random import choice
from typing import Callable

from components import Board
from test_boards import *


def benchmarks(board: Board, move_op: Callable) -> int:
    """
    Highest/lowest/random score first method depending on move_op.
    :param board: Board as a regular or numpy 2D array
    :param move_op: min/max/random.choice. Function given a list that returns an item from the list
    :return: Final score for the board
    """
    board.find_all_moves()
    score = 0

    while board.move_list:
        move = move_op(board.move_list)
        score += board.make_move(move)
        board.find_all_moves()

    return score


print(f"= Highest score first =\n"
      f"Test board score: {benchmarks(Board(test_board), max)}\n"
      f"Board 1 score: {benchmarks(Board(board_1), max)}\n")

print(f"= Lowest score first =\n"
      f"Test board score: {benchmarks(Board(test_board), min)}\n"
      f"Board 1 score: {benchmarks(Board(board_1), min)}\n")

print(f"= Random =\n"
      f"Test board score: {benchmarks(Board(test_board), choice)}\n"
      f"Board 1 score: {benchmarks(Board(board_1), choice)}\n")
