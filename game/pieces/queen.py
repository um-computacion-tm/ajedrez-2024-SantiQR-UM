from game.pieces.pieces import Piece
from game.pieces import DIAGONALS, NON_DIAGONALS

class Queen(Piece):
        
    # To return the queen symbol.
    __white_str__ = "♕"
    __black_str__ = "♛"

    directions = DIAGONALS + NON_DIAGONALS