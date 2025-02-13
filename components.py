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


class Board:
    def __init__(self, board: list[list[int]] | np.ndarray):
        """
        Class for handling board object
        :param board: Board as a python or numpy 2D array
        """
        self.board = np.array(board)
        self.move_list = []

    def _get_move(self, v_index: int, h_index: int, move_list: set[Move],
                  v_offset: int = 1, h_offset: int = 1) -> None:
        """
        Get moves recursively expanding horizontally/vertically from a start point.
        :param v_index: Board column index to start from
        :param h_index: Board row index to start from
        :param move_list: List of moves initially empty
        :param v_offset: Board column offset for second index
        :param h_offset: Board row offset for second index
        :return: None
        """
        if v_index + v_offset > self.board.shape[0] or h_index + h_offset > self.board.shape[1]:
            return

        result = np.sum(self.board[v_index:v_index + v_offset, h_index:h_index + h_offset])

        if result == 10:
            coord_1 = slice(v_index, v_index + v_offset)
            coord_2 = slice(h_index, h_index + h_offset)
            score = np.sum(self.board[coord_1, coord_2] > 0)
            move_list.add(Move(score, (coord_1, coord_2)))

        elif result < 10:
            self._get_move(v_index, h_index, move_list, v_offset + 1, h_offset)
            self._get_move(v_index, h_index, move_list, v_offset, h_offset + 1)


    def find_all_moves(self):
        """
        Get all possible moves for the board. Stored in self.move_list
        :return: None
        """
        move_list = set()
        for v_index in range(self.board.shape[0]):  # Vertical indices
            for h_index in range(self.board.shape[1]):  # Horizontal indices
                self._get_move(v_index, h_index, move_list)

        self.move_list = list(move_list)


    def make_move(self, move: Move):
        """
        Make a move and set removed numbers to 0
        :param move: A Move object
        :return: Score of the move
        """
        self.board[move.coordinate[0], move.coordinate[1]] = 0
        return move.score
