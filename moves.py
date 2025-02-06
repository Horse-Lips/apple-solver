import numpy as np


class Move:
    def __init__(self, score: int, coordinate: tuple[slice, slice]):
        """
        Basic class for handling moves.
        Args:
            score: The score of the move
            coordinate: Tuple containing index slices from top left to bottom right coordinate
        """
        self.score = score
        self.coordinate = coordinate

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score


def _get_horizontal(board: np.ndarray, v_index: int, h_index: int, move_list: list[Move], v_offset: int = 1,
                    h_offset: int = 1) -> None:
    """
        Get moves from coordinate expanding horizontally.
        Expands vertically when a selection sum < 10.
    Args:
        Args:
        board: Board as a numpy 2D array
        v_index: Board column index to start from
        h_index: Board row index to start from
        move_list: List of moves initially empty
        v_offset: Board column offset for second index
        h_offset: Board row offset for second index
    Returns:
        None
    """
    while h_index + h_offset < board.shape[1]:
        h_offset += 1
        result = np.sum(board[v_index:v_index + v_offset, h_index:h_index + h_offset])

        if result == 10:
            coord_1 = slice(v_index, v_index + v_offset)
            coord_2 = slice(h_index, h_index + h_offset)
            score = np.sum(board[coord_1, coord_2] > 0)

            move_list.append(Move(score, (coord_1, coord_2)))
        elif result < 10 and v_offset == 1:
            _get_vertical(board, v_index, h_index, move_list, v_offset, h_offset)
        else:
            return


def _get_vertical(board: np.ndarray, v_index: int, h_index: int, move_list: list[Move], v_offset: int = 1,
                  h_offset: int = 1) -> None:
    """
    Get moves from coordinate expanding vertically.
    Expands horizontally when a selection sum < 10.
    Args:
        board: Board as a numpy 2D array
        v_index: Board column index to start from
        h_index: Board row index to start from
        move_list: List of moves initially empty
        v_offset: Board column offset for second index
        h_offset: Board row offset for second index
    Returns:
        None
    """
    while v_index + v_offset < board.shape[0]:
        v_offset += 1
        result = np.sum(board[v_index:v_index + v_offset, h_index:h_index + h_offset])

        if result == 10:
            coord_1 = slice(v_index, v_index + v_offset)
            coord_2 = slice(h_index, h_index + h_offset)
            score = np.sum(board[coord_1, coord_2] > 0)

            move_list.append(Move(score, (coord_1, coord_2)))
        elif result < 10 and h_index == 1:
            _get_horizontal(board, v_index, h_index, move_list, v_offset, h_offset)
        else:
            return


# Main function to iterate over each element and check all directions
def get_moves(board: np.ndarray) -> list[Move]:
    """
    Get all currently available moves for the given board.
    Args:
        board: Board as a numpy 2D array
    Returns:
        A list of Moves
    """
    move_list = []
    for v_index in range(board.shape[0]):  # Vertical indices
        for h_index in range(board.shape[1]):  # Horizontal indices
            _get_horizontal(board, v_index, h_index, move_list)
            _get_vertical(board, v_index, h_index, move_list)

    return move_list
