from game.pieces.pieces import Piece
from game.pieces import DIAGONALS

class Bishop(Piece):

    # To return the bishop symbol.
    __white_str__ = "♗"
    __black_str__ = "♝"

    directions = DIAGONALS