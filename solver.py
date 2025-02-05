import numpy as np
from boards import *
from queue import PriorityQueue


move_queue = PriorityQueue()


def _get_horizontal(board, v_index, h_index, v_offset = 1, h_offset = 1):
    result = np.sum(board[v_index:v_index + v_offset, h_index:h_index + h_offset])

    while 0 < result < 10 and h_index + h_offset < board.shape[1]:
        h_offset += 1
        result = np.sum(board[v_index:v_index + v_offset, h_index:h_index + h_offset])

        if result == 10:
            coord_1 = slice(v_index, v_index + v_offset)
            coord_2 = slice(h_index, h_index + h_offset)
            move_queue.put((-np.sum(board[coord_1, coord_2] > 0), (coord_1, coord_2)))
        elif result < 10 and v_offset == 1:
            _get_vertical(board, v_index, h_index, v_offset, h_offset)


def _get_vertical(board, v_index, h_index, v_offset = 1, h_offset = 1):
    result = np.sum(board[v_index:v_index + v_offset, h_index:h_index + h_offset])

    while 0 < result < 10 and v_index + v_offset < board.shape[0]:
        v_offset += 1
        result = np.sum(board[v_index:v_index + v_offset, h_index:h_index + h_offset])

        if result == 10:
            coord_1 = slice(v_index, v_index + v_offset)
            coord_2 = slice(h_index, h_index + h_offset)
            move_queue.put((-np.sum(board[coord_1, coord_2] > 0), (coord_1, coord_2)))
        elif result < 10 and h_index == 1:
            _get_horizontal(board, v_index, h_index, v_offset, h_offset)


# Main function to iterate over each element and check all directions
def _get_moves(board):
    for v_index in range(board.shape[0]):  # Vertical indices
        for h_index in range(board.shape[1]):  # Horizontal indices
            _get_horizontal(board, v_index, h_index)
            _get_vertical(board, v_index, h_index)


def highest_score_first(board, output_board = False):
    """
     * Basic probably just a placeholder for now.
     * Uses priority queue to get highest move first.
     * This and the prio queue declaration/usage need a tidy up
    """
    _get_moves(board)
    score = 0

    if output_board:
        print(board)

    while not(move_queue.empty()):
        move = move_queue.get()

        if np.sum(board[move[1][0], move[1][1]]) == 10:
            board[move[1][0], move[1][1]] = 0
            score -= move[0]

            if output_board:
                board[move[1][0], move[1][1]] = -1
                print(f"Score: {score}\n{board}")
                board[move[1][0], move[1][1]] = 0

        if move_queue.empty():
            if output_board:
                print("REFRESHING MOVE QUEUE")

            _get_moves(board)

    print(f"Final score: {score}")

print("Test board")
highest_score_first(np.array(test_board))

print("\n")

print("Real board (Good score >= 104")
highest_score_first(np.array(board_1), output_board=True)
