from game.pieces.pieces import Piece
from game.pieces import DIAGONALS, NON_DIAGONALS


class King(Piece):

    # To return the king symbol.
    __white_str__ = "♔"
    __black_str__ = "♚"

    directions = DIAGONALS + NON_DIAGONALS
    limit = True

    def possible_movements(self):
        return self.calculate_movements(self.__position__, self.directions, self.limit)