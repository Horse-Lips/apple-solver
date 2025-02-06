from moves import get_moves


def populate_queue(board, queue, negate=False):
    """
    Populate a priority queue with moves
    Args:
        board (ndarray): Board as a numpy 2D array
        queue (PriorityQueue): Priority queue
        negate (bool): Whether to negate the score
    """
    move_list = get_moves(board)

    for move in move_list:
        if negate:
            queue.put((-move.score, move.coordinate))
        else:
            queue.put((-move.score, move.coordinate))
