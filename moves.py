import numpy as np


def _get_horizontal(board, v_index, h_index, move_list, v_offset=1, h_offset=1):
    """
        Get moves from coordinate expanding horizontally.
        Expands vertically when a selection sum < 10.
    Args:
        Args:
        board (ndarray): Board as a numpy 2D array
        v_index (int): Board column index to start from
        h_index (int): Board row index to start from
        move_list (list): List of moves initially empty
        v_offset (int): Board column offset for second index
        h_offset (int): Board row offset for second index
    Returns:
        None
    """
    result = np.sum(board[v_index:v_index + v_offset, h_index:h_index + h_offset])

    while 0 < result < 10 and h_index + h_offset < board.shape[1]:
        h_offset += 1
        result = np.sum(board[v_index:v_index + v_offset, h_index:h_index + h_offset])

        if result == 10:
            coord_1 = slice(v_index, v_index + v_offset)
            coord_2 = slice(h_index, h_index + h_offset)
            move_list.append((-np.sum(board[coord_1, coord_2] > 0), (coord_1, coord_2)))
        elif result < 10 and v_offset == 1:
            _get_vertical(board, v_index, h_index, move_list, v_offset, h_offset)


def _get_vertical(board, v_index, h_index, move_list, v_offset=1, h_offset=1):
    """
    Get moves from coordinate expanding vertically.
    Expands horizontally when a selection sum < 10.
    Args:
        board (ndarray): Board as a numpy 2D array
        v_index (int): Board column index to start from
        h_index (int): Board row index to start from
        move_list (list): List of moves initially empty
        v_offset (int): Board column offset for second index
        h_offset (int): Board row offset for second index
    Returns:
        None
    """
    result = np.sum(board[v_index:v_index + v_offset, h_index:h_index + h_offset])

    while 0 < result < 10 and v_index + v_offset < board.shape[0]:
        v_offset += 1
        result = np.sum(board[v_index:v_index + v_offset, h_index:h_index + h_offset])

        if result == 10:
            coord_1 = slice(v_index, v_index + v_offset)
            coord_2 = slice(h_index, h_index + h_offset)
            move_list.append((-np.sum(board[coord_1, coord_2] > 0), (coord_1, coord_2)))
        elif result < 10 and h_index == 1:
            _get_horizontal(board, v_index, h_index, move_list, v_offset, h_offset)


# Main function to iterate over each element and check all directions
def get_moves(board):
    """
    Get all currently available moves for the given board.
    Args:
        board (ndarray): Board as a numpy 2D array
    Returns:
        list: A list of moves. Moves are tuples containing negated score and move coordinates
    """
    move_list = []
    for v_index in range(board.shape[0]):  # Vertical indices
        for h_index in range(board.shape[1]):  # Horizontal indices
            _get_horizontal(board, v_index, h_index, move_list)
            _get_vertical(board, v_index, h_index, move_list)

    return move_list
