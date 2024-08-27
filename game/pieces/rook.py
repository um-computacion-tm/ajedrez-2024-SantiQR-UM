from game.pieces.pieces import Piece
from game.pieces import NON_DIAGONALS

class Rook(Piece):

    # To return the rook symbol.
    __white_str__ = "♖"
    __black_str__ = "♜"
    
    directions = NON_DIAGONALS