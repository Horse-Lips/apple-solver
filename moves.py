import numpy as np


class Move:
    def __init__(self, score: int, coordinate: tuple[slice, slice]):
        """
        Basic class for handling moves.
        :param score: The score of the move
        :param coordinate: Tuple containing index slices from top left to bottom right coordinate
        """
        self.score = score
        self.coordinate = coordinate

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.score == other.score and self.coordinate == other.coordinate
        return False

    def __lt__(self, other):
        if isinstance(other, Move):
            return self.score < other.score
        return False

    def __gt__(self, other):
        if isinstance(other, Move):
            return self.score > other.score
        return False

    def __hash__(self):
        return hash((self.score, self.coordinate))

    def __repr__(self):
        return f"Move: {self.coordinate} - Score: {self.score}"

    def __str__(self):
        return f"Move: {self.coordinate} - Score: {self.score}"


def _get_move(board: np.ndarray, v_index: int, h_index: int,
              move_list: set[Move], v_offset: int = 1, h_offset: int = 1) -> None:
    """
    Get moves recursively expanding horizontally/vertically from a start point.
    :param board: Board as a numpy 2D array
    :param v_index: Board column index to start from
    :param h_index: Board row index to start from
    :param move_list: List of moves initially empty
    :param v_offset: Board column offset for second index
    :param h_offset: Board row offset for second index
    :return: None
    """
    if v_index + v_offset > board.shape[0] or h_index + h_offset > board.shape[1]:
        return

    result = np.sum(board[v_index:v_index + v_offset, h_index:h_index + h_offset])

    if result == 10:
        coord_1 = slice(v_index, v_index + v_offset)
        coord_2 = slice(h_index, h_index + h_offset)
        score = np.sum(board[coord_1, coord_2] > 0)
        move_list.add(Move(score, (coord_1, coord_2)))

    elif result < 10:
        _get_move(board, v_index, h_index, move_list, v_offset + 1, h_offset)
        _get_move(board, v_index, h_index, move_list, v_offset, h_offset + 1)


def get_moves(board: np.ndarray) -> list[Move]:
    """
    Get all currently available moves for the given board.
    :param board: Board as a numpy 2D array
    :return: A list of Moves
    """
    move_list = set()
    for v_index in range(board.shape[0]):  # Vertical indices
        for h_index in range(board.shape[1]):  # Horizontal indices
            _get_move(board, v_index, h_index, move_list)

    return list(move_list)


def make_move(board: np.ndarray, move: Move):
    """
    Make a move and set removed numbers to 0
    :param board: Board as a numpy 2D array
    :param move: A Move object
    :return: Score of the move
    """
    board[move.coordinate[0], move.coordinate[1]] = 0
    return move.score
